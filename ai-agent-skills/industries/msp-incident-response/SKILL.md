---
name: cyber-investigator-msp-incident-response
description: Applies the Cyber Investigator Roadmap method to incident response that managed service providers (MSPs) and small incident-response consultancies run for small and mid-sized business (SMB) clients. Use when asked to triage a suspected business email compromise or mailbox takeover in Microsoft 365 or Google Workspace, review a client tenant's audit logs for signs of compromise, lay out what data was accessed and when, or draft an insurer-facing incident summary. Authorized, defensive, lawful scope only.
---

# Cyber investigator skill: MSP and SMB incident response

This extends [`../../SKILL.md`](../../SKILL.md). Apply its five procedures: OSINT recon cycle, link-analysis graph, fraud and scam pattern triage, machine-generated text check, and intelligence brief or case report. Apply them together with everything below.

Business email compromise (BEC) is one of the most common engagements an MSP or small IR consultancy runs for SMB clients: a mailbox is taken over, inbox rules forward or hide mail, and the client has to decide whether to notify anyone and what to tell their insurer. Industry summaries of Verizon's 2025 Data Breach Investigations Report put BEC losses at $6.3B across about 19,000 reports, with a median loss of roughly $50,000. The same summaries report that among small-business cyber-insurance claims with a loss, BEC accounted for 19% of claims, with a median impact of roughly $38,000. Treat those exact figures as secondary-sourced. The shape is consistent across sources: BEC is a leading SMB loss category, and a typical loss is five figures.

## Ask before assuming
If anything needed to do this correctly is missing or unclear, such as the authorization or case ID, which jurisdiction applies, what evidence sources are actually available, or what output format is expected, ask one specific clarifying question before proceeding. Do not guess. Do not fill a gap with a plausible-sounding default and continue as if it were given. Do not lower your stated confidence instead of asking. If you are not confident enough to act, that is the signal to ask, not to hedge and proceed anyway. A wrong guess costs the investigation more than the time a clarifying question takes.

## Scope and authorization for MSP and SMB incident response
This section replaces the generic skill's "ask for case context" step. Everything else in the generic "Scope and ethics" section still applies, including the hard stop for cases that may involve a minor or human trafficking.

1. The client's signed engagement letter or incident-response retainer is the authorization. Do not start work without one. If the user has not confirmed it, ask.
2. Record the client name and the engagement or ticket reference at the top of every output, so the work can be traced back to the engagement that justified it.
3. In scope: the client's own tenant, the client's own mailboxes and user accounts, and the logs the client's tenant produces (audit logs, sign-in logs, message traces, and admin activity).
4. Never in scope:
   - any system the client does not own, including the attacker's infrastructure, a vendor's systems, or a customer's systems
   - any third party's account, even one that received mail from the compromised mailbox
   - logging into the compromised account, or any other account, as the user. Investigate the account through its logs and the admin tools. Do not sign in as the user to look around.
5. Containment actions (password resets, session revocation, rule removal, app consent removal) change the evidence. Preserve first, as step 1 of the triage procedure says, then contain. Who approves each containment action is set by the engagement, not by this skill.
6. This analysis does not replace a qualified person's review. The MSP or consultant running the engagement reviews every finding before it goes to the client.

## Email-compromise triage
Run the procedure in [`reference/email-compromise-triage.md`](reference/email-compromise-triage.md) for any suspected mailbox takeover in Microsoft 365 or Google Workspace. It is a numbered checklist that starts with preserving the audit log and message trace, then checks inbox rules, OAuth app consents, MFA state, sign-in geography and timing, and mailbox delegation.

If the case also involves a fraudulent payment request or invoice sent from or to the client, run the generic fraud and scam pattern triage as well, and check it against the BEC section of [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md).

## Notification and reporting decision
Whether the client must notify affected people, a regulator, or anyone else depends on the breach-notification law of the client's jurisdiction and on the nature of the data that was accessed. That determination is made by the client, with their legal counsel if they have one. It is not made by this skill.

1. Lay out the facts the decision depends on: which accounts were compromised, which mailboxes, files, or records were accessed or could have been accessed, what kinds of personal or financial information they held, and the time window of access.
2. State plainly where the logs do not answer a question. "The logs show the attacker signed in, but do not show which messages were read" is a finding. Do not fill that gap with a guess in either direction.
3. Do not state whether notification is required. Do not cite a specific statute, section, or threshold as settled. Say that the requirement must be confirmed for the client's jurisdiction, and leave the decision to the client.
4. Record the client's decision and their stated rationale in the report, attributed to the client.

A cyber-insurer will typically want specific documentation: the timeline, the scope, the containment actions taken, the data accessed, and the notification decision with its rationale. The report format below covers each of those.

If money was lost or a fraudulent payment was requested, a report to a national fraud-reporting body may also be appropriate, such as the Canadian Anti-Fraud Centre (CAFC) in Canada or the FBI's Internet Crime Complaint Center (IC3) in the US. Structure that report with the generic "intelligence brief or case report" procedure. Whether and when to file is the client's decision.

## Report format
Use the generic "intelligence brief or case report" procedure for internal notes. For the insurer-facing incident summary, use these sections in this order:

1. Timeline. Each event with its date, time, time zone, and the log source it came from, from the first sign of compromise to the end of containment.
2. Scope. The accounts, mailboxes, and systems involved, and the ones checked and found not involved.
3. Containment actions taken. Each action, who took it, and when.
4. Data accessed. What the logs show was accessed, with its source. If the logs cannot establish it, write "not determined" and say which log or retention gap prevents it. Do not estimate.
5. Notification decision and rationale. Record it as the client's decision, in the client's words where possible, with the date it was made and who made it. If the client has not decided yet, write "pending client decision."

The summary is a draft. The MSP or consultant running the engagement reviews it and owns what goes to the client and the insurer.

## Reference material
- [`reference/email-compromise-triage.md`](reference/email-compromise-triage.md) is the email-compromise triage procedure for Microsoft 365 and Google Workspace, as a numbered checklist.
- [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) is the generic taxonomy. Its business email compromise section covers the payment-request side of a BEC case.
