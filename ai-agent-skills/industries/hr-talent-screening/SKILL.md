---
name: cyber-investigator-hr-talent-screening
description: Applies the Cyber Investigator Roadmap method to candidate-fraud screening for HR teams, talent acquisition, and background-screening vendors. Use when asked to check whether a job applicant or new hire shows signs of identity fraud, a proxy or face-swapped interview, a manufactured work history, generated application text, or post-hire signals of a fraudulent remote worker. Produces screening signals for human review, never hiring decisions. Authorized, defensive, lawful scope only.
---

# Cyber investigator skill: HR and talent screening

This extends [`../../SKILL.md`](../../SKILL.md). Apply its five procedures: OSINT recon cycle, link-analysis graph, fraud and scam pattern triage, machine-generated text check, and intelligence brief or case report. Apply them together with everything below.

## Important: this is the inverse taxonomy
The base skill's [`fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) covers fake employers. Its recruitment and job fraud section protects job seekers from employers who are not real.

This skill covers the opposite direction: fake candidates. It protects employers from applicants and hires who are not who they say they are. Do not mix the two. A case about a suspicious job posting belongs to the base taxonomy. A case about a suspicious applicant belongs here.

## Ask before assuming
If anything needed to do this correctly is missing or unclear, such as the authorization or case ID, which jurisdiction applies, what evidence sources are actually available, or what output format is expected, ask one specific clarifying question before proceeding. Do not guess. Do not fill a gap with a plausible-sounding default and continue as if it were given. Do not lower your stated confidence instead of asking. If you are not confident enough to act, that is the signal to ask, not to hedge and proceed anyway. A wrong guess costs the investigation more than the time a clarifying question takes.

## Scope and authorization for HR and talent screening
This section replaces the generic skill's "ask for case context" step. Everything else in the generic "Scope and ethics" section still applies, including the hard stop for cases that may involve a minor or human trafficking.

1. The case context is an open requisition ID plus the candidate's consent on file. Consent is required for any lookup that is part of a background check. If the user has not given both, ask for them. Do not start without them.
2. Log the requisition ID at the top of every output, so the work can be traced back to the hiring process that justified it.
3. Research the candidate only within what they submitted (application, resume, portfolio, interview records), the checks they consented to, and public sources. Do not go beyond those.
4. Post-hire signals concern an employee, not a candidate. Checking them needs the employer's own authorization for that review, such as a security or insider-risk case ID. Ask for it. The hiring requisition does not cover it.
5. Never contact the candidate or their references directly, and never draft a message to them. Contact is a decision for the employer's staff.
6. This skill is a screening signal generator. It is not an adverse-action decision-maker. It does not decide whether to reject a candidate, withdraw an offer, or end employment. Every output must say so.

## Why a records check is not enough
In June 2025 the US Department of Justice announced coordinated nationwide actions against facilitators who helped North Korean IT workers get remote jobs at more than 100 US companies. They used the stolen identities of more than 80 Americans and generated more than $5M for the regime. In January 2025 the FBI issued an advisory on North Korean IT-worker threats, including extortion after hiring. Reporting from August 2026 indicates the scheme has spread beyond IT roles into healthcare and sales roles, and documents face-swap software used in video interviews, with the camera switched off partway through.

These operatives pass standard record checks by design. A background-check vendor verifies records, and the scheme is built around identity documents that check out. That is why a behavioral and investigative layer is needed in addition to records verification. A clean records check does not clear a candidate on its own, and a flagged signal here does not override a clean records check on its own either. Both go to a human.

## Candidate-fraud triage
Run the generic triage procedure, then check the case against the patterns in [`reference/candidate-fraud-taxonomy.md`](reference/candidate-fraud-taxonomy.md): identity discontinuity, interview evasion, manufactured history, generated application text, and post-hire signals. The same evidence rule applies. Quote the record, field, log line, or observation that shows each mechanism, or mark it absent.

1. For each mechanism marked present, give the source and the date and time it was observed.
2. Check the innocent explanation before recording a finding. A person may use a different name on GitHub than on their ID, have a broken camera, live in one timezone and keep another's hours, or have worked at a company that has since closed. Record the innocent explanation you checked and what you found.
3. Use the link-analysis graph when several applicants or hires may be connected. Useful labeled edges include "same equipment shipping address," "same bank account for payroll," "same reference email," and "identical application phrasing." A shared address or account across unrelated hires is a candidate hub.
4. Report the result as a count of mechanisms present with their evidence, for example: "Identity discontinuity and interview evasion present; 2 of 5 categories; evidence: ...; this is a screening signal, not a decision; route to HR and legal."

## Compliance guard
Any adverse decision made from these signals triggers background-check and employment-law obligations. Those obligations vary by jurisdiction. They typically cover consent for background checks, notice to the candidate before and after an adverse action, and a bar on any decision or inference based on a protected characteristic.

1. End every finding with this sentence: "This is a screening signal, not a decision; route to HR and legal." It plays the same role as the base skill's rule that a machine-generated text result is a supporting signal, not a verdict.
2. Do not name a specific statute, section, notice period, or retention rule as settled. The applicable law must be confirmed with legal or compliance for the jurisdiction in question. Do not assume the rules of one country or province apply in another.
3. Never use a protected characteristic, or a proxy for one, as a signal. Nationality, national origin, ethnicity, accent, name origin, religion, age, and disability are not evidence. The North Korean IT-worker scheme makes this easy to get wrong: the scheme is the pattern to hunt, not people of any national origin. A mechanism counts only through the behavior or record mismatch the taxonomy names.
4. Do not treat a disability-related reason for declining a camera, or any request for an accommodation, as interview evasion. Record it, exclude it from the count, and route it to HR.
5. If the candidate has not consented to a background check, limit the work to what they submitted and public sources, and say so in the output.

## Reference material
- [`reference/candidate-fraud-taxonomy.md`](reference/candidate-fraud-taxonomy.md) lists the candidate-fraud mechanisms with the evidence that shows each one, and marks which rows still need a documented case.
- [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) is the generic taxonomy. Its recruitment and job fraud section covers the opposite direction: fake employers targeting job seekers.
