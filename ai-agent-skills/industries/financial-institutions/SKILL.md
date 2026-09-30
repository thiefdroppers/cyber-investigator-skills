---
name: cyber-investigator-financial-institutions
description: Applies the Cyber Investigator Roadmap method to fraud operations and AML/FIU work at banks, credit unions, fintech risk teams, money-services businesses, and financial intelligence units. Use when asked to triage a fraud or AML alert, check a case against a known financial-fraud pattern, review a customer's transaction activity for mule or scam indicators, or draft a SAR or STR narrative. Authorized, defensive, lawful scope only.
---

# Cyber investigator skill: financial institutions

This extends [`../../SKILL.md`](../../SKILL.md). Apply its five procedures: OSINT recon cycle, link-analysis graph, fraud and scam pattern triage, machine-generated text check, and intelligence brief or case report. Apply them together with everything below.

## Ask before assuming
If anything needed to do this correctly is missing or unclear, such as the authorization or case ID, which jurisdiction applies, what evidence sources are actually available, or what output format is expected, ask one specific clarifying question before proceeding. Do not guess. Do not fill a gap with a plausible-sounding default and continue as if it were given. Do not lower your stated confidence instead of asking. If you are not confident enough to act, that is the signal to ask, not to hedge and proceed anyway. A wrong guess costs the investigation more than the time a clarifying question takes.

## Scope and authorization for financial institutions
This section replaces the generic skill's "ask for case context" step. Everything else in the generic "Scope and ethics" section still applies, including the hard stop for cases that may involve a minor or human trafficking.

1. The case or alert ID is the authorization. Do not start work without one. If the user has not given it, ask for it.
2. Log the case or alert ID at the top of every output, so the work can be traced back to the case that justified it.
3. Research the named subject only within the institution's own data (the KYC file, transaction history, and prior alerts) and public sources. Do not go beyond those.
4. Never contact the subject directly, and never draft a message to the subject. Contact with a customer under review can tip them off and is a decision for the institution's staff, not for this skill.
5. This analysis does not replace human review. A qualified person at the institution must review the finding before any account action (a hold, a freeze, a closure, a reversal) and before any regulatory filing. Say this plainly in every case output.
6. Before this skill is used against live customer data, the institution's model-risk function will likely need validation evidence for it. The US and Canada both have formal model-risk-management frameworks. Confirm with the model-risk function which requirements apply. Do not assume the skill is approved for production use.

## Fraud and scam pattern triage for this industry
Run the generic triage procedure, then check the case against the financial-institution patterns in [`reference/fraud-taxonomy.md`](reference/fraud-taxonomy.md): investment and pig-butchering scams, authorized push payment (APP) scams, mule-account indicators, first-party and check fraud, and elder financial exploitation. The same evidence rule applies. Quote the transaction, field, or record that shows each mechanism, or mark it absent.

Most transaction-monitoring alerts are not fraud. Vendor and practitioner sources cite false-positive rates of 85-95%. That range is an industry folk figure, not an audited number, but the direction is not in dispute. Treat an alert as a question to answer, not as a finding.

## Evidence sources
Use these sources, and record for each data point the source, the record or field, and the date and time it was pulled.

| Source | What it shows |
|---|---|
| KYC file | Stated identity, occupation, income, expected account activity, account opening date, and any EDD notes. Compare actual activity against what the customer said to expect. |
| Device and IP history | Logins, new devices, device changes just before a large payment, and several customers sharing one device or IP. |
| Transaction velocity | Volume and frequency over time, especially sudden change on a new or dormant account, and the gap between money coming in and going out. |
| Interac, Zelle, and e-transfer recipient history | Whether the payee is new, how many other customers have paid the same recipient, and whether the recipient's details match the stated purpose of the payment. |
| Prior alerts on the counterparty | Earlier alerts, cases, or filings involving the same recipient, originator, device, or account. A counterparty that recurs across unrelated customers is a candidate hub in a link-analysis graph. |
| FINTRAC and FinCEN typology bulletins | The "confirmed pattern" source category. A mechanism described in a current bulletin counts as a documented pattern. Cite the bulletin by the title and date you actually read, and do not cite one from memory. |

Only the first five are about the subject. The typology bulletins tell you what a pattern looks like. They are not evidence that this customer is part of it.

## Report format
Use the generic "intelligence brief or case report" procedure for internal case notes. For a SAR or STR, structure the narrative around six questions:

1. Who. The subject, other parties, and their relationship to the institution, identified by the fields in the institution's records.
2. What. The activity and why it is suspicious, tied to the specific pattern and mechanisms from the taxonomy.
3. When. Dates and times of each transaction or event, and the period the activity covers.
4. Where. Accounts, branches, channels, and jurisdictions involved.
5. Why. The facts that made the activity suspicious, stated as facts with their source, not as conclusions.
6. How. How the money moved, in order, from origin to final destination as far as the records show.

Filing deadlines, the tipping-off prohibition, and record-retention rules differ by jurisdiction and change over time. Confirm each one with the institution's compliance team before relying on it. Do not state a deadline, threshold, or retention period from memory, and do not assume the rules of one country apply in another.

The draft narrative is a draft. A human investigator reviews and owns the filing.

## Terminology

| Term | Meaning |
|---|---|
| APP fraud | Authorized push payment fraud. The customer sends the payment themselves, after being deceived about who they are paying or why. The customer's credentials were not stolen. |
| Mule | A person whose account is used to receive and move the proceeds of crime. Some know what they are doing. Others are recruited under a pretext, such as a "payment processor" job. |
| Layering | Moving funds through several accounts, products, or jurisdictions to separate them from their source. |
| Structuring | Splitting cash transactions to stay below a reporting threshold. It is a reportable pattern whether or not the underlying funds are illicit. |
| CTR threshold | The amount at which a currency transaction report must be filed. The amount and the report name vary by jurisdiction. Confirm the current figure with compliance rather than stating one. |
| KYC and EDD | Know your customer: the identity and profile checks done at onboarding and kept current. Enhanced due diligence: the additional checks applied to higher-risk customers. |
| Beneficiary and originator | The originator sends the payment. The beneficiary receives it. In APP fraud the institution's customer is usually the originator and the victim. In a mule case the institution's customer is usually the beneficiary. |

## Reference material
- [`reference/fraud-taxonomy.md`](reference/fraud-taxonomy.md) lists the mechanisms for each financial-institution fraud type with the evidence that shows each one in the institution's own records.
- [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) is the generic taxonomy. Its recruitment and job fraud section covers how mule-account holders are often recruited.
