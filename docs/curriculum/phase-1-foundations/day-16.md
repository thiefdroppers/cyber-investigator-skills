# Day 16: Threat modeling with STRIDE

Phase: 1. Foundations · Track goal: Draw a small system as a data flow diagram, find its threats with STRIDE, and produce a threat model another person can review.

## Concept
Threat modeling asks four questions, in the wording of the Threat Modeling Manifesto: what are we working on, what can go wrong, what are we going to do about it, and did we do a good enough job? Developers use it before building. Investigators use the same method in reverse: given a system that was attacked, which paths were open, and which one fits the evidence? A threat model also tells you, before any incident, which logs would be needed to investigate each threat. Day 17 builds that second use on top of today's model.

The model starts with a data flow diagram (DFD) using four element types and one boundary. External entities are people or systems outside your control (a volunteer's browser, an email provider). Processes are code that handles data (a web application). Data stores hold data (a database, a log file, a storage bucket). Data flows are the arrows between them, labelled with what moves. Trust boundaries are dashed lines where the level of trust changes, such as between the internet and your server, or between your server and a third-party service. Most threats sit on flows that cross a boundary.

STRIDE, developed at Microsoft, is a checklist of six threat types, each the opposite of a security property:

| Threat | Violates | Question to ask | Investigator's view |
|---|---|---|---|
| Spoofing | Authentication | Can someone pretend to be a user or a system? | Sign-in and session logs |
| Tampering | Integrity | Can data be changed in transit or at rest? | Hashes, change and audit logs |
| Repudiation | Non-repudiation | Can someone deny doing something because nothing recorded it? | Whether an audit trail exists at all |
| Information disclosure | Confidentiality | Can data reach someone it should not? | Access logs, data-transfer volumes |
| Denial of service | Availability | Can the service be made unusable? | Error rates, resource metrics |
| Elevation of privilege | Authorization | Can someone do more than their role allows? | Role changes, access to admin functions by non-admins |

Not every threat applies to every element. The usual rule of thumb, from the "STRIDE per element" method: external entities can be spoofed and can repudiate; processes are exposed to all six; data stores to tampering, information disclosure, denial of service, and repudiation when the store is a log; data flows to tampering, information disclosure, and denial of service.

Keep models small. A model with five elements that you actually finish and review is worth more than a fifty-element diagram abandoned halfway.

## Resources
- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/), a one-page statement of the four questions and the values behind them.
- [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/), the free tool used today, with [downloads on GitHub](https://github.com/OWASP/threat-dragon/releases) and [documentation](https://www.threatdragon.com/docs/).
- [Microsoft: Threat Modeling Tool threats (STRIDE categories)](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats).
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html).
- Adam Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014), if you want the full book. His free [Elevation of Privilege card game](https://github.com/adamshostack/eop) teaches STRIDE by play.

## Practical: OWASP Threat Dragon, producing a STRIDE data flow diagram with at least eight documented threats

### The system
A fictional neighbourhood food bank runs a small volunteer sign-up site, described here in full so you do not need to invent anything:

- Volunteers use a public web form to submit their name, email, phone number, and available shifts.
- The web application (one Linux server, nginx plus a Python app) stores sign-ups in a PostgreSQL database on the same server.
- It sends a confirmation email to each volunteer through a third-party transactional email service, using an API key stored in the app's configuration file.
- Two coordinators log in to an admin page (username and password, no second factor) to view sign-ups and export them as a CSV file.
- The export link has the form `/admin/export?file=signups-2026-03-10.csv`.
- nginx writes access logs. The application writes no audit log of its own.

### Step 1: install and create the model
1. Download the desktop build for your OS from the Threat Dragon releases page on GitHub and install it. A web version also exists; the desktop build keeps your model as a local file.
2. Create a new, empty threat model. Title: "Food bank volunteer sign-up (fictional)". Owner: your name. Description: paste the system description above.
3. Add a diagram and choose the STRIDE diagram type.

### Step 2: draw the DFD
Using the element palette, place:

- Actors (external entities): `Volunteer (browser)`, `Coordinator (browser)`, `Email service (third party)`
- Processes: `Web app (nginx + Python)`
- Stores: `Sign-up database (PostgreSQL)`, `nginx access log`, `App config file (API key)`
- Trust boundaries: one around the server (separating it from the internet) and one around the email service

Then connect them with data flows, and label each flow with what it carries:

| From | To | Label |
|---|---|---|
| Volunteer | Web app | Sign-up form (name, email, phone, shifts), HTTPS |
| Web app | Sign-up database | INSERT sign-up |
| Web app | Email service | Confirmation email request + API key, HTTPS |
| Email service | Volunteer | Confirmation email |
| Coordinator | Web app | Admin login (username, password) |
| Web app | Coordinator | Sign-up list / CSV export |
| Web app | nginx access log | Request records |
| App config file | Web app | API key, DB credentials |

Check that every flow from an actor to the web app crosses the server's trust boundary.

### Step 3: find threats with STRIDE
Select each element and flow in turn and use the threat panel to add threats. For each one record the STRIDE category, a title, a description specific to this system, a status (Open for all of them today), a severity (Low, Medium, or High), and a mitigation.

Worked examples for three of them:

- Spoofing, on the Coordinator actor and the admin login flow. Title: "Admin login by credential stuffing." Description: "The admin page accepts a username and password with no second factor or rate limit. An attacker using passwords leaked from other sites could log in as a coordinator and read or export every volunteer's contact details." Severity: High. Mitigation: "Add a second factor for coordinator accounts, rate-limit and log failed logins, alert on logins from new networks."
- Information disclosure, on the web app process (the export). Title: "Export file name is guessable." Description: "Export files are named by date. If the `file` parameter is not checked against the logged-in session, or accepts paths, anyone who guesses a date may download a list, or read other files on the server through path traversal." Severity: High. Mitigation: "Generate exports on demand behind an authenticated session, reject any `file` value that is not an expected name, and never pass the parameter to the filesystem."
- Repudiation, on the web app process. Title: "No application audit log." Description: "The app does not record which coordinator viewed, exported, or deleted records. nginx logs show a request to `/admin/export` and an IP address, but not which account made it. A coordinator could deny an export, and an attacker using a stolen login would be indistinguishable from the real coordinator." Severity: Medium. Mitigation: "Write an audit record for every admin action with account, time, source IP, and object affected, and ship it off the server."

Add at least five more of your own. Every STRIDE letter must appear at least once across the model. Ideas to check: tampering with the sign-up form (HTML or script injected into a name field and later shown in the admin page), information disclosure of the API key from the config file (and what someone could do with it: send email that looks like it comes from the food bank), denial of service through thousands of automated sign-ups, and elevation of privilege if the admin pages rely on a hidden link rather than checking the session role.

### Step 4: export the artifacts
1. Save the model; Threat Dragon stores it as a JSON file. Name it `day16-foodbank-threat-model.json`.
2. Open the report view, which lists every element with its threats and mitigations, and print it to PDF as `day16-foodbank-report.pdf`.
3. Take a screenshot of the diagram itself as `day16-foodbank-dfd.png`.

## Checkpoint
Your artifacts are the model JSON, the PDF report, and the diagram image. They pass when:
- The DFD has every element and flow from the tables above, each flow is labelled with its content, and both trust boundaries are drawn.
- There are at least eight threats, covering all six STRIDE categories, each with a system-specific description (it names this system's fields, pages, or components) and a mitigation.
- At least one threat is a repudiation threat that points out a missing log, because tomorrow's work depends on it.
- You can point to the single flow you consider highest risk and say why in one sentence that names the boundary it crosses.
