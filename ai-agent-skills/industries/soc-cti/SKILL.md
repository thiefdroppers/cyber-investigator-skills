---
name: cyber-investigator-soc-cti
description: Applies one narrow part of the Cyber Investigator Roadmap method for SOC and cyber threat intelligence (CTI) teams at security vendors and enterprises. Use when asked to check whether phishing-kit lure text, a ransomware note, or an extortion message was machine-generated, or to use shared generated phrasing as a supporting signal when clustering separate incidents. Does not replace existing threat-intelligence platforms or ATT&CK playbooks. Authorized, defensive scope only, under a ticket, case, or investigation ID.
---

# Cyber investigator skill: SOC and CTI teams

This extends [`../../SKILL.md`](../../SKILL.md). Most of what a SOC or CTI team needs, infrastructure pivoting, ATT&CK mapping, and IOC handling, is already covered by mature commercial tooling and the curriculum's own Phase 3 material. This file names the one place the base skill adds something distinctive, and says plainly where it does not.

## Ask before assuming
If anything needed to do this correctly is missing or unclear, such as the authorization or case ID, which jurisdiction applies, what evidence sources are actually available, or what output format is expected, ask one specific clarifying question before proceeding. Do not guess. Do not fill a gap with a plausible-sounding default and continue as if it were given. Do not lower your stated confidence instead of asking. If you are not confident enough to act, that is the signal to ask, not to hedge and proceed anyway. A wrong guess costs the investigation more than the time a clarifying question takes.

## Where this does not add much
Infrastructure pivoting, ATT&CK technique mapping, and IOC enrichment are already well served by commercial threat-intelligence platforms and established playbooks. This skill does not try to replace them. A SOC or CTI team should keep using its existing tooling for that work.

The base skill's OSINT recon cycle and link-analysis graph procedures describe the same method those tools already run, at a lower level of automation. For a team with that tooling in place, they are mostly redundant. If a request is only about pivoting, mapping, or enrichment, say so and point the user back to their own tooling rather than repeating the work by hand.

## Scope and authorization
A ticket, case, or investigation ID from the team's own case-management system is the authorization. Ask for it if it is missing, and record it at the top of every output.

The base skill's rule on named private individuals still applies. Any work that moves from clustering incidents to naming a person behind them needs a stated reason tied to the ticket. A ticket ID for an incident does not on its own authorize research on a named individual. If a request names a person, ask how that person relates to the case before starting.

The base skill's hard stop also applies. If a case may involve a minor or human trafficking, stop autonomous analysis and say that it needs a qualified human and a report to the appropriate authority.

## The one distinctive addition: machine-generated-text attribution
Apply the base skill's machine-generated text check, step by step and without changes, to phishing-kit lure text, ransomware notes, or extortion messages. Record each tell with its quoted text and category, per incident.

Then compare across incidents:
1. For each pair of incidents, list the tells they share: matching chatbot residue (the same leftover placeholder or assistant phrasing), matching generated phrasing, or the same set of tell categories.
2. Quote the matching text from both incidents side by side. A match you cannot quote is not a finding.
3. Add each match as a labeled edge between the two incidents, such as "same unfilled placeholder in lure text" or "near-identical generated closing paragraph."
4. Report the result as a supporting signal for clustering, with its confidence.

This is a supporting signal for clustering incidents. It is never proof of common authorship on its own. The base skill's own caveat applies: legitimate senders use the same tools, so generated phrasing shows how text was written, not who wrote it. Two more limits matter here:
- Phishing kits and ransomware note templates are sold, shared, and copied. Matching text can mean a shared kit or template rather than a shared operator. Day 47 of the curriculum covers this shared-tooling trap.
- Two operators who give a model a similar prompt can get similar output. Matching generated phrasing is weaker evidence than matching residue, such as the same unfilled placeholder.

Combine this signal with the team's other clustering evidence, such as infrastructure, tooling, and behavior. Do not let it carry a cluster by itself.

## Reference material
- [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) is the base mechanism list. Its phishing and BEC entries apply to lure text, and its machine-generated text entry states the same supporting-signal limit used here.
- ATT&CK-specific material is not part of this skill family. It lives in the curriculum's [Phase 3 (threat intelligence)](../../../curriculum/phase-3-cyber-threat-intelligence/), including [Day 35](../../../curriculum/phase-3-cyber-threat-intelligence/day-35.md) on how ATT&CK is built and [Day 47](../../../curriculum/phase-3-cyber-threat-intelligence/day-47.md) on attribution and the shared-tooling trap.
