# Day 1: What an investigator does, and the line you don't cross

Phase: 1. Foundations · Track goal: Know what the investigator's job is, where the legal and ethical boundary sits, and set up the tracking you will use for the next 89 days.

## Concept
A cyber investigator establishes what happened, how it happened, and what was involved, and does it carefully enough that the conclusion survives someone trying to prove it wrong. A penetration tester looks for weaknesses before an attacker finds them. An incident responder contains an active incident and restores service. Investigators overlap with both, but their product is different: a finding that another person can check, step by step, from raw evidence to conclusion.

That product depends on evidence discipline. "I'm pretty sure the login came from abroad" is an opinion. "The sign-in log exported at 14:02 UTC shows a successful login from 203.0.113.45, which the provider's own geolocation field lists as outside the country, and here is the SHA-256 of the export" is a finding. Day 2 turns this into a routine.

Authorization decides whether any of the work is lawful. Pulling DNS records, reading a log, or searching a username across platforms can be routine casework in one context and an offence or a privacy violation in another. The technique is the same in both. The difference is whether someone with the right to grant access gave you a legitimate reason to look, and whether what you are doing stays inside that reason.

In most jurisdictions the law turns on authorization. In the United States, the Computer Fraud and Abuse Act at 18 U.S.C. § 1030(a)(2) makes it a crime to intentionally access a computer "without authorization" or to "exceed authorized access" and thereby obtain information. In *Van Buren v. United States* (2021), the Supreme Court read "exceeds authorized access" narrowly: it covers entering parts of a system (files, folders, databases) that are off limits to you, not misusing data you were entitled to see. That narrowing does not help an investigator who logs into a system they were never given access to. The UK Computer Misuse Act 1990, section 1, and Canada's Criminal Code, section 342.1, draw the same basic line.

Fraud and abuse work adds one more rule: hunt patterns, not people. Good investigative output describes a tactic (a recruitment-scam script, a phishing kit, the infrastructure a scam campaign reuses) that protects many people at once. Building a profile of one private person because you are curious, with no sanctioned case behind it, is where investigation turns into stalking. If you notice you are researching a person instead of a pattern or an assigned case, stop and ask why.

## Resources
- [18 U.S.C. § 1030, full text (Cornell LII)](https://www.law.cornell.edu/uscode/text/18/1030). Read subsection (a)(2) and the definitions in (e)(6).
- [Van Buren v. United States, opinion (PDF)](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf). The syllabus on the first pages is enough.
- [UK Computer Misuse Act 1990, section 1](https://www.legislation.gov.uk/ukpga/1990/18/section/1) and [Criminal Code of Canada, section 342.1](https://laws-lois.justice.gc.ca/eng/acts/c-46/section-342.1.html). Pick whichever applies where you live, or find your own country's equivalent.
- [EC-Council Code of Ethics](https://www.eccouncil.org/code-of-ethics/): a short statement of professional conduct that applies whether or not you hold the certification.
- [OSINT Framework](https://osintframework.com/): browse it to see the scope of Phase 2. Do not run any of the tools yet.

## Practical: GitHub Projects board and a completed authorization record

### Part 1: the progress board
1. Fork this repository (or create a private repo of your own).
2. In your fork, open the Projects tab, choose New project, and pick the Board template.
3. Rename the default columns to `Not started`, `In progress`, and `Artifact built`.
4. Add one draft item per day (`Day 01` through `Day 90`) using the "Add item" box at the bottom of the `Not started` column. If typing 90 items is tedious, add the 18 Phase 1 days now and the rest at the start of each phase.
5. Add a custom field named `Artifact` (type: Text). When you finish a day, paste the path or link to the artifact there before moving the card.

A card only moves to `Artifact built` when the Artifact field points at something that exists. Reading a day does not complete it.

### Part 2: worked example of authorized and unauthorized actions
Read this scenario and the verdict on each action before you fill in your own record.

A credit union (fictional, using the reserved domain `creditunion.example`) hires you under a signed engagement letter. Members are receiving text messages linking to `creditunion-login.example`, a lookalike page that collects online-banking passwords. Your written scope says: "Identify and document the phishing infrastructure impersonating the credit union, and prepare takedown requests. Do not contact suspects. Do not access any system not owned by the credit union."

| Action | Verdict | Why |
|---|---|---|
| Load the phishing page from an isolated analysis browser and save the HTML and a screenshot | Authorized | The page is publicly served, and documenting it is the core of the scope. |
| Run `dig creditunion-login.example` and look up the domain's registration record | Authorized | These are public records about the infrastructure, which is exactly what the scope names. |
| Search Certificate Transparency logs for other lookalike domains | Authorized | Public data, and it serves the stated purpose of finding related infrastructure. |
| Find a config file the kit left exposed, read the admin password in it, and log into the kit's admin panel to see how many victims there are | Not authorized | The panel belongs to someone else, and nobody with the right to grant access gave you permission. Criminal ownership does not change that. Under § 1030 this is access "without authorization." Document that the file is exposed and hand it to law enforcement. |
| Try the stolen member credentials the kit logged against the real banking site to see which ones work | Not authorized | You would be logging into accounts that belong to members, who never consented. The credit union's fraud team resets those accounts through its own process. |
| Look up the suspected kit operator's family members on social media | Not authorized | This is outside scope, and it targets private people rather than the pattern. |
| Write up the kit's page structure, lure text, and hosting pattern so the fraud team can spot the next campaign | Authorized, and the most useful thing you produce | This is the pattern, and it protects every member rather than one. |

Most of the unauthorized rows would feel helpful at the moment you are tempted. Because of that, write the scope down before you start.

### Part 3: your authorization record
Create `notes/authorization-record.md` in your fork using this structure, and fill it in for the scenario above as if you were the investigator:

```markdown
# Authorization record

Engagement / case ID:
Authorized by (name, role, organization):
Their authority to grant access (why this person can say yes):
Date authorized (UTC):
Written evidence of authorization (file name + SHA-256):

## In scope
- Systems / data I may examine:
- Techniques I may use:

## Out of scope
- Systems / data I may not touch:
- Techniques I may not use:
- People I may not research:

## Stop conditions
- If I encounter ______, I stop and escalate to ______.

## Data handling
- Where evidence is stored:
- Who may see it:
- When it is deleted:
```

Then write your own answer, in 3 to 5 sentences, to this question: *what would make me stop, even though I technically could keep going?* Save it as `notes/my-line.md`. You will revisit it at the Phase 5 checkpoint.

## Checkpoint
- Your board has at least the 18 Phase 1 items across three columns, with Day 01 in `Artifact built` and its Artifact field pointing at `notes/authorization-record.md`.
- Every field in your authorization record is filled for the credit union scenario, and the stop conditions name at least two concrete triggers (for example, "I find credentials" or "I find material involving a minor").
- Without notes, you can explain the difference between "capable of" and "authorized to," give one example from your own life (a shared family computer, a partner's phone, a coworker's account) where they differ, and name the statute section that applies where you live.
