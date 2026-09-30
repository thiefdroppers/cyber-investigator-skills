---
name: cyber-investigator-crypto-vasp
description: Applies the Cyber Investigator Roadmap method to fraud and compliance work at crypto exchanges, virtual asset service providers (VASPs), and money-services businesses that handle crypto. Use when asked to triage an exchange fraud or compliance alert, check whether a customer's deposits match an investment or pig-butchering pattern, assess a suspected fake exchange site, or add on-chain relationships to a link-analysis graph. Authorized, defensive, lawful scope only.
---

# Cyber investigator skill: crypto exchanges and VASPs

This extends [`../../SKILL.md`](../../SKILL.md). Apply its five procedures: OSINT recon cycle, link-analysis graph, fraud and scam pattern triage, machine-generated text check, and intelligence brief or case report. Apply them together with everything below.

It also builds on the [financial-institutions skill](../financial-institutions/SKILL.md). This skill adds only the on-chain and exchange-specific layer. It does not restate the investment-fraud pattern.

## Ask before assuming
If anything needed to do this correctly is missing or unclear, such as the authorization or case ID, which jurisdiction applies, what evidence sources are actually available, or what output format is expected, ask one specific clarifying question before proceeding. Do not guess. Do not fill a gap with a plausible-sounding default and continue as if it were given. Do not lower your stated confidence instead of asking. If you are not confident enough to act, that is the signal to ask, not to hedge and proceed anyway. A wrong guess costs the investigation more than the time a clarifying question takes.

## Scope and authorization for crypto exchanges and VASPs
This section replaces the generic skill's "ask for case context" step. Everything else in the generic "Scope and ethics" section still applies, including the hard stop for cases that may involve a minor or human trafficking.

1. The case or alert ID from the exchange's compliance or fraud system is the authorization. Do not start work without one. If the user has not given it, ask for it.
2. Log the case or alert ID at the top of every output.
3. Research only the exchange's own account, transaction, and KYC data, plus public on-chain data and public sources. Do not go beyond those.
4. Never contact the customer or any counterparty, and never draft a message to them. That decision belongs to the exchange's staff.
5. A qualified person at the exchange must review the finding before any account action (a hold, a freeze, an offboarding) and before any regulatory filing. Say this plainly in every case output.

## The exchange's position in the fraud
In an investment scam, the exchange is often where the victim's fiat becomes crypto. That makes it a choke point: the compliance team can see the pattern in deposit and withdrawal activity before the victim knows they are being scammed. A US Congressional Research Service product describes "Operation Level Up," under which 5,831 crypto-investment-fraud victims had been notified by April 2025. Of those contacted, 77% did not know they were being scammed at the time.

The losses are large. Pig-butchering losses were $7.228 billion in the FBI IC3 2025 report.

Use the mechanisms in the financial-institutions taxonomy's [investment and pig-butchering scams](../financial-institutions/reference/fraud-taxonomy.md#investment-and-pig-butchering-scams) section. Read them from the exchange's side. The bank sees fiat leaving for an exchange. The exchange sees that fiat arrive, get converted, and leave again as a crypto withdrawal to an external address. The same evidence rule applies: quote the deposit, withdrawal, address, or record that shows each mechanism, or mark it absent.

## On-chain and exchange-specific additions
Check these alongside the investment-fraud mechanisms.

| Mechanism | Evidence that it is present |
|---|---|
| Fake exchange or trading site | The customer withdraws to an address they say belongs to a "platform," and that platform's site copies a real exchange's interface, claims licenses or registrations that cannot be found in the regulator's public register, or blocks every withdrawal until a fee is paid |
| Withdrawal-fee gate | The customer makes a new withdrawal, or asks about one, described as a "tax," "unlock fee," or "verification deposit" the platform requires before releasing funds |
| Recovery-scam second wave | After a reported loss, the customer is approached by someone offering to recover the funds for a fee, often after the victim appears in a public report or complaint list, and a new withdrawal follows |
| Shared deposit address | Withdrawals from several unrelated customers go to the same external address |
| Shared chain-analytics cluster | Different destination addresses fall in the same cluster under a chain-analytics provider's label |

Add the last two as edge types in the base skill's link-analysis procedure. Label each edge with its source: "same deposit address (on-chain, tx hash)" or "same cluster (provider name, label, date pulled)." A cluster label is a vendor's inference, not an on-chain fact. Record it as "likely," not "confirmed," unless a second independent source agrees.

## Compliance layer
Travel Rule requirements (which originator and beneficiary fields must travel with a transfer, and at what amount) and MSB or VASP registration obligations are jurisdiction-specific and change over time. Confirm each one with the VASP's own compliance function. Do not state a threshold, field list, or registration requirement from memory, and do not assume one country's rules apply in another. This is the same compliance boundary the financial-institutions skill draws for filing deadlines and thresholds.

The Travel Rule is relevant to fraud work, not only to AML. FATF's June 2025 Travel Rule best-practices update expanded its stated objectives to explicitly include fraud prevention. Where originator and beneficiary data exist for a transfer, use them as evidence in the triage.

## Reporting routes
For on-chain fraud in the US, two public reporting routes are Chainabuse (for the addresses involved) and the FBI's IC3 (for the victim's complaint). For other jurisdictions, confirm the local equivalent with the exchange's compliance team. Do not assume IC3 applies. These routes sit alongside the exchange's own regulatory filing, which a human at the exchange owns.

## Reference material
- [`../financial-institutions/reference/fraud-taxonomy.md`](../financial-institutions/reference/fraud-taxonomy.md) has the investment and pig-butchering mechanisms this skill builds on, plus the mule-account indicators that often show up on the fiat side of the same case.
- [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) is the generic taxonomy.
