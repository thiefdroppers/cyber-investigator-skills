---
name: cyber-investigator-trust-and-safety
description: Applies the Cyber Investigator Roadmap method to platform trust and safety work on job boards, marketplaces, dating apps, rental platforms, social media, and gig platforms. Use when asked to review a reported account, listing, message, or ad against a known scam pattern, triage a moderation ticket or queue item, write an enforcement note, or route a case that may involve a minor or trafficking to the right escalation queue. Authorized, defensive, lawful scope only.
---

# Cyber investigator skill: platform trust and safety

This extends [`../../SKILL.md`](../../SKILL.md). Apply its five procedures: OSINT recon cycle, link-analysis graph, fraud and scam pattern triage, machine-generated text check, and intelligence brief or case report. Apply them together with everything below.

## Ask before assuming
If anything needed to do this correctly is missing or unclear, such as the authorization or case ID, which jurisdiction applies, what evidence sources are actually available, or what output format is expected, ask one specific clarifying question before proceeding. Do not guess. Do not fill a gap with a plausible-sounding default and continue as if it were given. Do not lower your stated confidence instead of asking. If you are not confident enough to act, that is the signal to ask, not to hedge and proceed anyway. A wrong guess costs the investigation more than the time a clarifying question takes.

## Scope and authorization for platform trust and safety
This section replaces the generic skill's "ask for case context" step. Everything else in the generic "Scope and ethics" section still applies.

1. The ticket, report, or queue ID is the authorization. Do not start work without one. If the user has not given it, ask for it.
2. Log that ID at the top of every output, so the work can be traced back to the report that justified it.
3. The subject is a platform account or listing, not a private individual outside the platform. The generic refusal for "a named private individual with no authorized case" does not apply to routine review of a reported account, listing, message, or ad.
4. That refusal still applies to the person behind the account. Review what the account did on the platform and what the reported content shows. Do not research the user's off-platform life (their employer, home address, family, or other social accounts) beyond what the reported content itself shows.
5. Never contact the account, and never draft a message to it. Contact can warn a scammer before enforcement or evidence preservation, and it is a decision for the platform's staff.
6. This skill is meant to move fast on ordinary tickets. That does not change the hard stop: a case that may involve a minor, or may involve trafficking, still ends autonomous analysis. Preserve the evidence and route it to the platform's named escalation queue, such as its CSAM or NCMEC reporting pipeline. See "Escalation routing" below.
7. A human reviewer owns every enforcement action. Platforms have moved moderation work toward automation (TikTok restructured and laid off global trust and safety staff in February 2025, betting on automated moderation), which makes a clear, reviewable note more important, not less. Say plainly in every output that the finding needs human review before action.

## Fraud and scam pattern triage for this industry
Run the generic triage procedure, then check the case against the mechanisms for its vertical in [`reference/vertical-taxonomy.md`](reference/vertical-taxonomy.md): job boards and professional networks, marketplaces and classifieds, dating, and social media and ads. Gig platforms use the job-board table. Rental platforms use the marketplace table.

The same evidence rule applies. Quote the message, listing field, or account record that shows each mechanism, or mark it absent. Each vertical also lists platform signals, such as account age or payout method changes. A signal can raise a ticket's priority. It is not a mechanism, and it never supports a verdict alone.

A pattern seen across several reports belongs in a link-analysis graph. Shared payout accounts, reused listing photos, repeated message templates, and a common IP or ASN are all labeled edges. A cluster of accounts joined by those edges is usually worth more to the platform than a verdict on any one of them.


## Enforcement note format
This replaces the generic intelligence brief for enforcement decisions. Use the generic brief only for pattern reports that go to a policy or intelligence team rather than to an enforcement queue.

1. Ticket ID and subject. The ticket, report, or queue ID, and the account, listing, or ad ID under review.
2. Policy clause violated. Name the platform policy and the specific clause, as written in the platform's policy. Do not paraphrase a clause from memory. If you do not have the policy text, ask for it.
3. Evidence quotes. Quote each message, listing field, or record that shows a mechanism, with its item ID and timestamp. Tie each quote to the mechanism it shows and the clause it breaks.
4. Action taken. The action the reviewer took or recommends (warning, listing removal, feature restriction, suspension, or referral), and who approved it.
5. Appeal-relevant facts. What the account holder could reasonably contest, any fact that points the other way (an established account history, a verified employer, a plausible innocent reading of a quote), and what new evidence would reverse the action.

State the verdict's confidence in the note, using the generic skill's wording. A note that claims more than its quotes support will fail on appeal.

## Escalation routing
The base skill's hard stop is a routing rule here, not a dead end. The red line is no autonomous analysis of a case that may involve a minor. It is not a refusal to help the platform escalate that case.

When a case may involve a minor or trafficking:

1. Stop analysis. Do not score mechanisms, build a graph, or summarize the content. Never generate, request, or reproduce content depicting a minor.
2. Say which queue to route it to. Name the platform's internal escalation queue for child safety or trafficking. If you do not know the queue's name, ask the reviewer for it rather than guessing.
3. Name the external body where one applies. For child sexual exploitation that is NCMEC's CyberTipline in the US, or the equivalent child-protection hotline in the platform's jurisdiction. For trafficking it is the national anti-trafficking body. The platform's escalation or legal team decides whether and how the external report is made.
4. Say what to preserve before escalating. Do not delete the account, listing, or content. Do not contact the account. Record the ticket ID, the account and content IDs, URLs, and timestamps, and leave the content in place for the escalation team. Follow that team's procedure on whether to restrict visibility in the meantime.
5. Hand over only identifiers. The routing note lists IDs, the reason for escalation in one sentence, and what was preserved. It does not describe or quote the content.

## Reference material
- [`reference/vertical-taxonomy.md`](reference/vertical-taxonomy.md) lists the mechanisms and platform signals for each vertical, with the evidence that shows each one.
- [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) is the generic taxonomy. Its recruitment and romance sections apply to job boards and dating apps.
