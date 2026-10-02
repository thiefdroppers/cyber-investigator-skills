# Financial institution fraud taxonomy

These are the mechanisms the fraud and scam triage step in [`../SKILL.md`](../SKILL.md) checks for at banks, credit unions, fintechs, money-services businesses, and FIUs. They extend the generic [`../../../reference/fraud-pattern-taxonomy.md`](../../../reference/fraud-pattern-taxonomy.md). Add an entry only when a documented case supports it, through the [contribution process](../../../../CONTRIBUTING.md).

A pattern name alone cannot score a case. Each entry below gives the mechanism and the evidence in the institution's own records that shows it is present in a specific case.

For scale: US filers submitted more than 4.105 million SARs in 2025, up 7.99% over 2024, and banks and credit unions alone filed 2.193 million. Suspicious wires (8.15%) and check fraud (7.46%) were among the top bank SAR categories (Forvis Mazars, March 2026). In Canada, FINTRAC's 2024-25 disclosures contained 511,480 financial transaction reports (FINTRAC Annual Report 2024-25).

## Investment and pig-butchering scams
The largest single loss category in both the FBI IC3 2025 report ($7.228 billion across 61,559 complaints) and Canada's CAFC 2025 data ($351 million).

| Mechanism | Evidence that it is present |
|---|---|
| Unsolicited contact | The customer reports, or case notes record, that the relationship began with a message from a stranger, often described as a wrong number or a social media contact |
| "Mentor" relationship | The customer describes a person guiding their investment decisions whom they have not met and cannot identify |
| Small early withdrawal succeeds | A small inbound credit from the platform or counterparty shortly after the first deposit, followed by larger outbound deposits |
| Deposits routed to crypto or a third party | Outbound payments go to a crypto exchange or to an individual's account rather than to a registered investment firm |
| Fee to withdraw | The customer says they must pay a "tax," "unlock fee," or similar charge before they can take money out, and a new outbound payment follows |
| Recovery-scam second wave | After the loss, the customer is contacted by someone offering to recover the funds for a fee, and makes another payment |

## Authorized push payment (APP) and payer social-engineering scams
The customer sends the money themselves. The FTC reports $900 million lost to government-impersonation scams in 2025 (via WBIW coverage, September 2026).

| Mechanism | Evidence that it is present |
|---|---|
| Safe-account scam | The customer moves funds to a new payee after a caller claiming to be from the institution's fraud team or another authority says their account is compromised |
| Government impersonation | A payment described as a fine, tax debt, or fee to avoid arrest or deportation, often by gift card, crypto, or e-transfer to an individual |
| Utility disconnection | An urgent payment to an individual or unfamiliar payee described as a utility bill, under threat of immediate shutoff |
| Grandparent or bail scam | An urgent cash withdrawal or payment, often by an older customer, for a relative said to be in jail, hospital, or trouble, with instructions not to tell anyone |
| Coaching | The customer gives a scripted or inconsistent reason for the payment, refuses to discuss it, or is on the phone with someone during the transaction |
| New payee, first large payment | The payee has no history with this customer and the amount is out of pattern for the account |

## Mule-account indicators
The account holder is often recruited through a "payment processor" or similar job. See the reshipping or money-mule role in the generic taxonomy's recruitment and job fraud section.

| Mechanism | Evidence that it is present |
|---|---|
| New account | The account was opened recently, relative to when the suspicious flow began |
| Rapid inbound transfers | Several e-transfers or EFTs arrive, often from unrelated senders |
| Immediate outbound | Funds leave soon after arriving, to crypto, to cash withdrawals, or to another account, leaving a low balance |
| Activity does not fit the KYC profile | Volume or counterparties inconsistent with the occupation and expected activity on file |
| Shared infrastructure | The same device, IP, phone number, or address appears on other accounts under review |
| Inbound from known victims | Senders include customers flagged in APP or investment-scam cases |

## First-party and check fraud
Check fraud is among the top five bank SAR categories (Forvis Mazars, March 2026).

| Mechanism | Evidence that it is present |
|---|---|
| Bust-out | A period of normal use that builds credit limits or trust, followed by a sharp run-up of balances or withdrawals and then no further payments |
| Altered or washed check | The payee name or amount on the image does not match the issuer's records, or shows signs of alteration |
| Mobile-deposit duplicate | The same check is deposited more than once, by mobile capture and again at a branch, ATM, or another institution |
| Funds withdrawn before the check clears | Withdrawals against a deposit before the deposit has finally cleared |

## Elder financial exploitation red flags
Consult your institution's current FinCEN or FINTRAC elder-exploitation advisory for the authoritative list of red flags. The rows below are general and need a documented case or the current advisory behind each one before they are treated as settled.

| Mechanism | Evidence that it is present |
|---|---|
| Sudden change in activity | Large or frequent withdrawals, or new payment types, on an account with a long, stable history |
| New person directing the account | A new joint holder, power of attorney, authorized user, or companion who speaks for the customer or accompanies them to transactions |
| Customer cannot explain the transaction | The customer seems confused about the purpose of a payment, or gives an account that differs from what the other person says |
| Changes to beneficiaries or contact details | Address, phone, or email changed so statements and alerts no longer reach the customer |
| Overlap with scam patterns | The activity also matches a grandparent, government-impersonation, or investment-scam row above |

## Machine-generated text (supporting signal only)
Scam scripts sent to customers may be written with LLMs. Text that shows several of the tell categories in the "Procedure: machine-generated text check" section of [`../../../SKILL.md`](../../../SKILL.md) is a supporting signal. It never counts as a mechanism on its own.

## Further reading: fraud slang
[The Fraudster Glossary](https://www.fraudsterglossary.com/) by Eric Huber decodes criminal fraud slang and jargon — useful when a customer's own words or a scam script contain terms not defined above. We mirror a fork, unmodified, at [`thiefdroppers/tfg-tools`](https://github.com/thiefdroppers/tfg-tools); it carries its own CC BY-NC-SA 4.0 license, separate from this repository's MIT license.
