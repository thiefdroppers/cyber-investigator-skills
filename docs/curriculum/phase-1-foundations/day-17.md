# Day 17: From threat model to evidence map, which record proves what

Phase: 1. Foundations · Track goal: For every threat in a model, name the exact record that would show it happened, check whether that record exists today, and turn the gaps into a short evidence-readiness plan.

## Concept
Yesterday's threat model answered "what can go wrong?" Today's work answers the investigator's follow-up: "if it did go wrong, could anyone prove it?" For many small organizations the honest answer is no. Nobody failed to look; the record that would settle the question was never created, or was deleted after seven days.

Evidence readiness (sometimes called forensic readiness) is the practice of deciding in advance which evidence you will need and making sure it is collected and kept. For each threat you need four facts. The source is the system that would record it. The specific record is the event, field, or line that would show the threat happening; "the logs" is not an answer. The retention is how long that record survives before rotation or deletion. The custodian is who can hand it over and how fast. A threat whose record does not exist cannot be investigated, however skilled the investigator.

Each threat goes through the same four checks, and a "no" at any of them is a gap for the readiness plan:

```mermaid
flowchart LR
    T["Threat from the<br/>Day 16 model"] --> S["Source<br/>which system would record it"]
    S --> R["Specific record<br/>event, field, or log line"]
    R --> E{"Exists today?"}
    E -- No --> GAP["Gap: not investigable.<br/>Create the record"]
    E -- "Yes or partial" --> RT{"Kept long enough?<br/>(retention)"}
    RT -- No --> GAP2["Gap: extend retention"]
    RT -- Yes --> TR{"Off-host or<br/>append-only?"}
    TR -- No --> GAP3["Gap: root on the server can erase it.<br/>Forward it off the host"]
    TR -- Yes --> CU{"Custodian known,<br/>and how fast they can hand it over?"}
    CU -- No --> GAP4["Gap: find out who holds it<br/>(often a third party)"]
    CU -- Yes --> OK["Investigable"]
```

The first of the three patterns below, seen as a request passing through the system:

```mermaid
sequenceDiagram
    participant C as Coordinator (or anyone with a stolen login)
    participant N as nginx
    participant A as Python app
    participant L as nginx access log
    participant AU as App audit log (does not exist)
    C->>N: GET /admin/export?file=...
    N->>L: source IP, time, path, status, bytes
    N->>A: forwards the request
    Note over A: Only the app knows which account is logged in
    A--xAU: account, file, time (never written)
    A-->>C: CSV export
```

Three patterns show up in almost every readiness review. First, the web server logs the request but not the identity: nginx sees `GET /admin/export?file=...` from an IP address, while only the application knows which account made it. If the application does not write that down, every admin action is anonymous. Second, logs live on the machine they describe. An attacker with root on the server can edit or delete `/var/log/auth.log`, so logs that matter should also be sent somewhere the attacker cannot reach, such as a separate syslog server or a cloud log service. Third, third parties hold some of the most useful records (the email service's delivery logs, the identity provider's sign-in logs), and their retention and export rules are set by contract and licence tier, not by you.

The output of this work is short and concrete: a table mapping threats to records, and a list of the few changes that would close the biggest gaps. It is also a document you will reuse in every later phase, because in a real case the first hour often goes to finding out which of these records exist.

## Resources
- [NIST SP 800-92: Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final), sections 2 and 4 on log sources and retention.
- [UK NCSC: Introduction to logging for security purposes](https://www.ncsc.gov.uk/guidance/introduction-logging-security-purposes).
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html): which application events to record and which fields each record needs.
- [rsyslog documentation: forwarding logs](https://www.rsyslog.com/doc/), for sending logs off the host.

## Practical: OWASP Threat Dragon and a spreadsheet, producing an evidence-readiness map and an annotated DFD

### Step 1: build the evidence map
Open your Day 16 model. Create a spreadsheet `day17-evidence-map` with one row per threat and these columns:

| Threat ID | STRIDE | Threat title | Evidence source | Specific record / field | Exists today? (Y / N / Partial) | Retention today | Tamper-resistant? (off-host, append-only) | Custodian | Gap and fix |

Worked rows, using the three threats from Day 16:

| Field | Admin login by credential stuffing | Export file name is guessable | No application audit log |
|---|---|---|---|
| Evidence source | nginx access log; app login handler | nginx access log | App (none exists) |
| Specific record | `POST /admin/login` lines with status codes per source IP (Day 11's pattern: many `200` then a `302`) | `GET /admin/export?file=...` lines, with status, bytes sent, and source IP | Would be: `event=export account=<name> file=<name> src_ip=<ip> ts=<UTC>` |
| Exists today? | Partial: shows attempts and success by IP, not which username was tried | Y for the request; N for which account (if any) was logged in | N |
| Retention today | nginx default rotation on Ubuntu is 14 daily files; confirm in `/etc/logrotate.d/nginx` | Same | n/a |
| Tamper-resistant? | N (on the same server) | N | n/a |
| Custodian | Food bank's volunteer IT helper | Same | Same |
| Gap and fix | Log username and outcome from the app; forward logs off the server | Log account with every export | Add audit log for all admin actions; forward off the server; keep 12 months |

Check the retention claim for yourself on any Ubuntu machine with nginx installed:
```bash
cat /etc/logrotate.d/nginx
```
Look for the `daily` or `weekly` directive and the `rotate N` count; together they give the retention. Record what you find rather than trusting the table above.

Fill a row for every threat in your model, including the five or more you added yourself. Two rows need special handling:

- The API-key disclosure threat. The most useful record is at the email service (API calls per key, with source IP), not on the server. Look up what your chosen provider's documentation says about API activity logs and their retention, and record the answer and the documentation link. If you cannot find it, write "unknown, ask provider," which is itself a finding.
- The denial-of-service threat. nginx logs show volume, but the record that proves impact is the application or database error log during the flood, and possibly the server's resource metrics. Name both.

### Step 2: annotate the DFD
In Threat Dragon, open the Day 16 diagram and save a copy as `day17-foodbank-evidence.json`. On the copy:

1. Add a store for each evidence source that is missing today, named with a `(PROPOSED)` suffix: `App audit log (PROPOSED)`, `Off-host log collector (PROPOSED)`.
2. Draw flows from the web app to these stores, labelled with what would be sent.
3. Add a third trust boundary around the off-host collector, to show it sits outside the server an attacker might control.
4. In the description of each existing store (`nginx access log`), write its retention and whether it is tamper-resistant.

Export the diagram as `day17-evidence-dfd.png`.

The annotated copy should look like this reference: the Day 16 diagram plus dashed proposed stores and flows, and a third boundary around the collector. The retention shown for the nginx log is the Ubuntu default from the worked rows and stays unverified until you have read `/etc/logrotate.d/nginx`.

```mermaid
flowchart LR
    VOL["Volunteer (browser)"]
    COORD["Coordinator (browser)"]
    subgraph SERVER["Trust boundary: food bank server"]
        APP(("Web app<br/>nginx + Python"))
        DB[("Sign-up database<br/>PostgreSQL")]
        LOG[("nginx access log<br/>retention: 14 daily files (unverified)<br/>tamper-resistant: no")]
        CFG[("App config file<br/>API key")]
        AUD[("App audit log (PROPOSED)")]
    end
    subgraph EMAIL["Trust boundary: third-party email service"]
        ES["Email service<br/>API activity log: retention unknown, ask provider"]
    end
    subgraph COLLECT["Trust boundary: off-host collector (PROPOSED)"]
        OHC[("Off-host log collector (PROPOSED)")]
    end
    VOL -->|"Sign-up form, HTTPS"| APP
    APP -->|"INSERT sign-up"| DB
    APP -->|"Confirmation email request + API key"| ES
    ES -->|"Confirmation email"| VOL
    COORD -->|"Admin login"| APP
    APP -->|"Sign-up list / CSV export"| COORD
    APP -->|"Request records"| LOG
    CFG -->|"API key, DB credentials"| APP
    APP -.->|"event, account, file, src_ip, UTC time"| AUD
    APP -.->|"nginx, auth, and audit log lines"| OHC
    style SERVER stroke-dasharray: 6 4
    style EMAIL stroke-dasharray: 6 4
    style COLLECT stroke-dasharray: 6 4
    style AUD stroke-dasharray: 4 3
    style OHC stroke-dasharray: 4 3
```

### Step 3: write the readiness plan
Create `day17-readiness-plan.md` with no more than five actions, ranked by how many threats each closes. For each action, state:

- which threats it makes investigable (by Threat ID),
- the specific record it creates or preserves,
- the retention it needs and why that period (for example, "12 months, because volunteers often report misuse of their details months later"),
- rough effort (hours, not budget).

Close with a one-paragraph "if we are breached tomorrow" statement: which threats you could investigate today, which you could not, and what you would ask the email provider for first.

## Checkpoint
Your artifacts are `day17-evidence-map`, `day17-evidence-dfd.png`, and `day17-readiness-plan.md`. They pass when:

- Every threat from Day 16 has a row.
- Every "specific record" cell names an event, a field, or a log line pattern. No cell says just "logs."
- Retention values come from something you checked (a config file you read or a documentation page you link), or are marked "unverified."
- The annotated DFD shows the proposed stores.
- The annotated DFD shows the off-host boundary.
- Every proposed store and the off-host boundary carry the `(PROPOSED)` suffix.
- The readiness plan has at most five actions.
- Each action is tied to Threat IDs.
- The top action closes the repudiation gap from Day 16.
- Without notes, you can name the four facts each threat needs for evidence readiness.
