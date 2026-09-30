# Capstone case packet: the Castellan remittance diversion

> **SYNTHETIC TRAINING MATERIAL. EVERYTHING IN THIS FOLDER IS FICTION.**
> Orrin Valley Millworks, Castellan Hardwood Supply, Marrowline Freight Services, Brightquay Legal, Quennmarsh, and every person, bank, registrar, hosting company and carrier named in this packet were invented for this exercise. They are not based on any real organization, person, case or client, and any resemblance is coincidental. Domains use the reserved `.example` top-level name (RFC 2606), IP addresses come from the RFC 5737 documentation ranges, AS numbers come from the RFC 5398 documentation range, and phone numbers use the 555-01XX block reserved for fiction.

This packet is the evidence for the Phase 7 capstone (Days 83 to 89). It describes one business email compromise: a lookalike vendor domain, a credential-phishing page, a taken-over mailbox, a hidden inbox rule, and a $48,612.50 payment sent to the wrong bank account. It is built so that OSINT, threat intelligence, log forensics and fraud analysis each answer part of the case and none of them answers all of it.

## What is in the packet

| ID | File | What it is | First used |
|---|---|---|---|
| P1 | [`01-engagement-letter.md`](01-engagement-letter.md) | The client's request, your authorization and scope, IT environment notes, two staff statements, and what the vendor said by phone | Day 83 |
| P2 | [`02-suspicious-email.eml`](02-suspicious-email.eml) | The phishing email as a raw message with full headers | Day 84 |
| P3 | [`03-related-messages.md`](03-related-messages.md) | Six related messages (M1 to M7, with M2 being P2), including the fraudulent bank-change letter and its document metadata | Day 84 |
| P4 | [`04-vendor-site-archived.md`](04-vendor-site-archived.md) | Public artifact A: the real vendor's About page, archived November 2025 | Day 84 |
| P5 | [`05-lookalike-site-capture.md`](05-lookalike-site-capture.md) | Public artifact B: the lookalike site's About and Privacy pages, captured 17 March 2026 | Day 84 |
| P6 | [`06-lookup-results.md`](06-lookup-results.md) | Pre-collected WHOIS, DNS, passive DNS, certificate transparency, URL scan, favicon hash and IP enrichment results (L1 to L9) | Day 84 |
| P7 | [`logs/mail-trace.csv`](logs/mail-trace.csv) | Mail gateway message trace, 1 to 17 March, UTC | Day 86 |
| P8 | [`logs/mailbox-audit.csv`](logs/mailbox-audit.csv) | Sign-in and mailbox audit events for two users, 9 to 17 March, UTC | Day 86 |
| P9 | [`logs/web-proxy.log`](logs/web-proxy.log) | Web proxy log for the AP specialist's workstation, 10 and 11 March, local time with no offset recorded | Day 86 |
| P10 | [`07-instructor-key.md`](07-instructor-key.md) | Ground truth, planted traps and a marking guide. Do not open it until your Day 89 report is finished. | After Day 89 |

Cite evidence by these IDs in your notes, on your case graph, and in your report: `P8 row 2026-03-10T14:36:50Z`, `P6 L3`, `P3 M4`. If a reviewer cannot find the thing you cited in under a minute, the citation is not good enough.

## Rules for working the packet

1. Read [`01-engagement-letter.md`](01-engagement-letter.md) before anything else. Its scope section is binding for the whole capstone.
2. Do not run live lookups on anything here. The domains and IPs are reserved and will return nothing, or something unrelated. [`06-lookup-results.md`](06-lookup-results.md) stands in for those lookups.
3. Work on copies. Hash the original packet files on Day 83 and check the hashes again before you submit on Day 89.
4. Defang indicators whenever you write them outside the packet: `castellan-hardwood[.]example`, `hxxps://cstl-docshare[.]example/view/r`, `198.51.100[.]23`.
5. Some evidence in this packet is wrong, misleading or irrelevant on purpose, just as in a real case file. Part of the exercise is deciding which is which and saying how you decided.

## How the capstone uses the packet

| Day | Work | Main files |
|---|---|---|
| 83 | Briefing, rules of engagement, evidence register | P1, all files for hashing |
| 84 | OSINT and threat-intel recon on the external entities | P2 to P6 |
| 85 | Intake: the case question, scope, hypotheses, plan | P1 plus your Day 84 output |
| 86 | Log forensics and a merged UTC timeline | P7 to P9, P2 headers |
| 87 | Fraud and social-engineering analysis of the messages | P2, P3, P4, P5 |
| 88 | The final case graph | Everything from Days 84 to 87 |
| 89 | The final report at calibrated confidence | The case graph and your notes |
