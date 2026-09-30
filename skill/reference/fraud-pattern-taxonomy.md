# Fraud and scam pattern taxonomy (starter set)

These are the mechanisms the fraud and scam triage procedure in [`../SKILL.md`](../SKILL.md) checks for. [Day 67](../../curriculum/phase-5-fraud-social-engineering/day-67.md) covers the recruitment-fraud entries in depth; [Day 68](../../curriculum/phase-5-fraud-social-engineering/day-68.md) builds the cross-case relationship graph from them. Add an entry only when a documented case supports it, through the [contribution process](../../CONTRIBUTING.md).

A pattern name alone cannot score a case. Each entry below gives the mechanism and the evidence that shows it is present in a specific case.

## Recruitment and job fraud

| Mechanism | Evidence that it is present |
|---|---|
| Upfront-payment lure | A fee for equipment, training, or visa processing is required before the job starts |
| Overpayment and check cashing | The "employer" sends a check larger than owed and asks for the difference back before it clears |
| Identity-harvesting application | SIN or SSN, bank details, or a photo ID scan requested before any real interview, for a role that doesn't need them yet |
| Reshipping or money-mule role | Duties involve forwarding packages or moving money for others, under a title like "logistics coordinator" or "payment processor" |
| Urgency and platform hopping | Pressure to move from a job board to personal email or a messaging app before the candidate can verify the employer |

## Romance and relationship fraud

| Mechanism | Evidence that it is present |
|---|---|
| Rapid escalation | Declarations of love before any verified in-person meeting |
| Video-call avoidance | Repeated refusals or excuses when asked to video call |
| Escalating emergencies | A sequence of financial "emergencies," each asking for more than the last |
| Inconsistent details | Personal facts (job, location, family) that change between conversations |

## Business email compromise (BEC)

| Mechanism | Evidence that it is present |
|---|---|
| Spoofed or lookalike domain | The sender domain differs from the real one by a character, a TLD, or a display-name trick |
| Authority and urgency | A payment or wire request that invokes an executive or deadline |
| Process bypass | A request to skip normal approval "just this once" |
| Secrecy | An instruction not to discuss the request with colleagues |

## Phishing (general)

| Mechanism | Evidence that it is present |
|---|---|
| Sender mismatch | The sending domain doesn't belong to the organization the message claims to be from |
| Generic greeting with fear or urgency | No name, plus a subject line threatening suspension, a charge, or a deadline |
| Link mismatch | The visible link text and the actual URL destination differ |
| Wrong channel for the request | Credentials or MFA codes requested through a channel the real organization doesn't use for that |

## Machine-generated text (supporting signal only)
Scam scripts are increasingly written with LLMs. Text that shows several of the tell categories in the "Procedure: machine-generated text check" section of [`../SKILL.md`](../SKILL.md) is a supporting signal. It never counts as a mechanism on its own, because legitimate senders also use these tools.
