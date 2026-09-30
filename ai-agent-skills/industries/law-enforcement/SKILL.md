---
name: cyber-investigator-law-enforcement
description: Applies the Cyber Investigator Roadmap method to police fraud and cyber units and national anti-fraud reporting centres. Use when asked to triage citizen fraud reports, link reports that share a phone number, payment handle, or domain, organize open-source evidence for a file, or draft a file-ready report for handoff to an investigator. Authorized, lawful scope only, under an assigned file or occurrence number.
---

# Cyber investigator skill: law enforcement

This extends [`../../SKILL.md`](../../SKILL.md). Apply its five procedures: the OSINT recon cycle, the link-analysis graph, fraud and scam pattern triage, the machine-generated text check, and the intelligence brief or case report, together with everything below.

## Ask before assuming
If anything needed to do this correctly is missing or unclear, such as the authorization or case ID, which jurisdiction applies, what evidence sources are actually available, or what output format is expected, ask one specific clarifying question before proceeding. Do not guess. Do not fill a gap with a plausible-sounding default and continue as if it were given. Do not lower your stated confidence instead of asking. If you are not confident enough to act, that is the signal to ask, not to hedge and proceed anyway. A wrong guess costs the investigation more than the time a clarifying question takes.

## Scope and authorization for law enforcement
In a police unit or reporting centre, the file or occurrence number is the authorization. Ask for it before any work that touches a named person, and record it at the top of every output.

This skill accepts a file or occurrence number as authorization for named-subject work. That differs from the base skill, which by default refuses research on a named private individual. The difference is deliberate: the analyst here is working an assigned case with legal authority behind it, so a named subject is part of the job rather than a warning sign.

A file number authorizes the case. It does not authorize everything. It does not turn non-public data into open-source data, and it does not remove the need for a warrant, production order, or equivalent process where one is required (see "Evidentiary requirements" below). If a request goes beyond the file it cites, such as a named person with no stated connection to the reported offence, ask how that person relates to the file before starting.

The base skill's hard stop still applies. If a report may involve a minor or human trafficking, stop autonomous analysis and say that the report needs to go to the unit or officer responsible for those cases in the user's agency. Never generate, request, or reproduce content depicting a minor.

## What this is for
Two jobs:

1. Intake triage of citizen fraud reports. The core task is the one in the roadmap's [Day 68](../../../curriculum/phase-5-fraud-social-engineering/day-68.md) exercise: take a queue of separate reports, find the ones that share an exact phone number, payment handle, cryptocurrency address, or domain, and show which reports are probably one operation.
2. Report drafting for handoff. Turn a triaged report, or a linked cluster of reports, into a file-ready report that an investigator can pick up without redoing the intake work.

The volume behind this is large. Canada's national anti-fraud centre received more than 112,000 reports in 2025. Canada's Auditor General has found that agencies lack the capacity or capability to police cybercrime effectively. Public reporting describes many municipal and small fraud units as operating with a small number of detectives and no dedicated analyst, working through a backlog of public reports. The RCMP's departmental plans commit to new personnel and tools for digital evidence work, and a forensic-lab timeliness target is stated in planning documents. Intake triage is where an agent helps most, because the bottleneck is reading and linking reports, not the final investigative decision.

At intake, the base skill's "hunt patterns, not people" is the correct posture. An intake analyst who is linking reports is not yet investigating a named suspect. Build the graph around indicators (the number, the handle, the domain) and the pattern they share. A name that appears in a report is a data point in that report, not a target.

This skill does not replace an investigator's judgment on when a suspect becomes a target. Deciding that a person is a suspect, and choosing what to do about it, belongs to the investigator and the agency's own procedures. When the linked evidence points toward one person, say what the evidence shows at its confidence level and hand it to the investigator. Do not escalate to a dossier on that person on your own initiative.

## Evidentiary requirements
Anything the agent helps collect or organize may end up in court. Treat every output as if defence counsel will read it.

### Chain of custody and preservation
Every piece of evidence the skill helps collect or organize carries chain-of-custody and preservation information with it. For each item, record:

- What it is: a screenshot, a saved web page, a message export, a report from the intake system, a WHOIS record.
- Where it came from: the exact URL, system, or report number.
- When it was collected: date, time, and time zone.
- Who collected it, and with what tool or method.
- A hash of the saved file (for example SHA-256) if the agency's procedure calls for one, and where the original is stored.
- Every later handling step: who opened, copied, converted, or transferred it, and when.

Write these into the output next to the item, not in a separate note that can be lost. If the user asks for evidence to be organized and the custody details are missing, say which details are missing and ask for them. Do not fill in a collection time or a collector.

Preserve before analyzing. Web pages, social media posts, and listings change or disappear. Tell the user to capture and preserve the original through the agency's approved method before the agent works on a copy. The agent's summaries and graphs are analysis of the evidence, not the evidence itself. Label them that way.

Never alter an original. If a file must be converted, cropped, or translated, keep the original, record the change, and label the result as derived from the original.

The agency's own evidence-handling policy governs. If it conflicts with anything here, follow the agency policy and say so in the output.

### Open source versus legal process
Keep one line clear in every output:

- Open-source and public information can be gathered without judicial authorization. Examples are public websites, public social media posts, public registries, WHOIS and DNS records, and archived snapshots.
- Anything that requires a provider to hand over non-public data needs a warrant, production order, or equivalent legal process. Examples are subscriber records behind a phone number, account holder details behind a payment handle, login IP addresses, and the content of private messages.

When the analysis reaches that line, say so plainly: "The next step needs the account holder behind this payment handle. That is non-public data held by the provider and needs legal process." Do not describe ways to get that data informally, and do not treat a guess about the account holder as a substitute for it.

Do not state a legal threshold, the name of an order, or the grounds a judge needs. These vary by jurisdiction and change over time. Say that the investigator must confirm the correct process with the agency's legal counsel or the Crown or prosecutor's office.

Also keep private, non-public material out of open-source collection. Logging into an account under a false identity, joining a closed group, or messaging a suspect is not passive open-source work. It may need its own authorization under agency policy. Flag it and stop rather than proceeding.

### Disclosure
Anything the agent generates for a file, including summaries, link graphs, triage scores, and drafts, may be disclosable to defence counsel. What counts as disclosable, when it must be disclosed, and how drafts and working notes are treated are jurisdiction-specific. Do not assume an answer. Say that it must be confirmed with the agency's own legal counsel or the Crown or prosecutor's office.

Two practical consequences hold regardless of jurisdiction:

- Write every output as if it will be disclosed. No speculation presented as fact, no remarks about a person that the evidence does not support.
- Record that an AI agent was used, which procedure it ran, and what inputs it was given, so the investigator can explain the work if asked.

## Report format
Use this structure for a file-ready report. It follows the base skill's intelligence brief, with the separation between fact and inference made explicit, because that separation is what holds up under cross-examination.

1. **Header.** File or occurrence number, date, author, and a line stating that an AI agent assisted and which procedures it ran.
2. **Finding.** One sentence at its correct confidence level. Example: "Reports 4, 9, and 17 are likely one operation; all three name the same payment handle."
3. **What was reported.** What each complainant said, attributed to the complainant and the report number. Keep this as reported. Do not correct or restate it as fact.
4. **What was verified, and how.** Each fact the analyst checked, with the source, the method, the collection date and time, and the chain-of-custody reference for the item. Tag each one confirmed (2 or more independent sources agree), likely (1 source only), or disputed (sources conflict).
5. **What remains unverified.** Every claim not yet checked, and what would check it. Mark any item that needs legal process to verify.
6. **Inference.** Conclusions drawn from the verified facts, each labeled as inference and each pointing to the facts it rests on. Keep this section physically separate from section 4.
7. **What would change the finding.** The evidence that would weaken or overturn it.
8. **Recommended next steps.** For the investigator to decide on. Mark each one open source or legal process required.

Use the same confidence word in the finding as in the evidence. Never report a likely finding as confirmed. A report that says plainly what is not known is easier to defend than one that sounds certain.

## Intake triage mechanisms
Start from the base skill's [fraud-pattern taxonomy](../../reference/fraud-pattern-taxonomy.md) to classify each report. The table below lists the mechanisms an intake unit sees most, plus one signal specific to working a queue of reports.

| Mechanism | Evidence that it is present | Source |
|---|---|---|
| Upfront-payment lure | A fee for equipment, training, or processing was required before the promised job or benefit | Base taxonomy, recruitment and job fraud |
| Reshipping or money-mule role | The complainant was asked to forward packages or move money for others | Base taxonomy, recruitment and job fraud |
| Escalating emergencies | A sequence of financial "emergencies," each asking for more than the last | Base taxonomy, romance and relationship fraud |
| Spoofed or lookalike domain | The sender domain differs from the real one by a character, a TLD, or a display-name trick | Base taxonomy, BEC |
| Wrong channel for the request | Credentials or MFA codes were requested through a channel the real organization does not use for that | Base taxonomy, phishing |
| Cross-report linking signal | The same exact phone number, payment handle, or domain appears in two or more separate citizen reports | Added for intake units |

The cross-report linking signal is the most useful pattern for an intake unit. It is the base skill's link-analysis procedure applied to a report queue instead of a single case: each report is a case node, each exact phone number, handle, or domain is an indicator node, and an indicator that connects two or more reports is the finding. Use only exact matches as links. A similar number or a shared tactic is not a link. Day 68 grades which indicators are strong enough to link reports.

## Reference material
- [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) is the generic taxonomy this skill uses for intake triage, with the evidence for each mechanism.
- [`../../reference/osint-methodology-checklist.md`](../../reference/osint-methodology-checklist.md) is the recon cycle as a printable checklist.
