# Engagement letter and intake notes

> SYNTHETIC TRAINING MATERIAL. Orrin Valley Millworks, Castellan Hardwood Supply, Marrowline Freight Services and every person named here are fictional. Any resemblance to a real organization or person is coincidental.

## Part A: engagement letter (from the client)

From: Owen Tran, Operations Director, Orrin Valley Millworks
To: You, contract investigator
Date: Tuesday 17 March 2026
Re: Diverted vendor payment, request for investigation

Owen writes:

We are a 64-person custom millwork and cabinetry manufacturer. On Friday 13 March our weekly payment run sent $48,612.50 for invoice CHS-20417 to a bank account that our long-standing lumber supplier, Castellan Hardwood Supply, says is not theirs. We found out on Monday 16 March at about 10:15 our time, when Castellan's accounts receivable manager, Dana Whitlock, phoned to ask why the invoice was unpaid.

What we have done so far:

1. Our bank has opened a recall request on the payment. We have filed a police report (reference OV-2026-03-0412) and notified our cyber insurer.
2. Our IT contractor reset Jordan Pike's password, signed out all of Jordan's sessions, and deleted an inbox rule they found on Jordan's mailbox. They did this on 16 March before exporting any logs. They have since exported what we are sending you.
3. We have not contacted anyone else about this.

We would like you to answer these questions:

1. How did this happen, step by step?
2. Was Jordan's email account taken over? If so, when, from where, and what did the attacker do with it?
3. The fraudulent email quoted Castellan's real invoice, word for word. Did that information leak from us or from Castellan?
4. Is the same group targeting other suppliers or other staff here? Is there anything else we should block?
5. What should we change so this does not happen again?

Our insurer has asked for a written report. Please treat anything you tell us as something the insurer and possibly the police will read.

## Part B: authorization and scope

Orrin Valley Millworks authorizes you to:

- Review every file in this case packet, including the three log exports under `logs/`.
- Run passive research on the domains, IP addresses, email addresses and phone numbers that appear in the packet, using the pre-collected lookup results in `06-lookup-results.md`. Because every domain and IP here is a reserved documentation value, live lookups return nothing useful. The lookup file stands in for what WHOIS, passive DNS, certificate transparency and a URL scanner returned when the client's IT contractor ran them on 17 March.
- Treat the two staff statements in Part C as your interview evidence. You cannot interview the staff again before the report is due.
- Produce a case graph and a written report for the client, its insurer and, if the client chooses, the police.

The following are out of scope. The client did not authorize them, and several would be unlawful or unsafe in a real case:

- Visiting, logging in to, or submitting anything to `cstl-docshare.example` or any other attacker-controlled site, even "just to see the page."
- Contacting the attacker by email (including the freemail Reply-To address), by phone (555-0148) or any other channel, or replying to the fraudulent thread.
- Investigating Castellan Hardwood Supply's systems, mailboxes or staff. Castellan is a separate organization and has not engaged you. You may record what Castellan told the client and recommend that the client share indicators with Castellan.
- Researching Dana Whitlock, Jordan Pike, Maren Beaulieu or any other named person's personal social media, home address, relatives or other personal life. You are investigating what happened to accounts and money, not the private lives of the people involved.
- Researching Marrowline Freight Services, the real business whose brand appears on the attacker's infrastructure, beyond noting that its brand was used.
- Attempting to identify the attacker as a named individual. Attribution to a person is a police matter. You may describe infrastructure, tactics and patterns.
- Tracing, freezing or recovering the funds. The bank and police are handling that.
- Any active scanning of any IP address or domain.

## Part C: intake notes (taken by you on the intake call, 17 March 2026)

Environment facts from the client's IT contractor (Priya Anand, contractor):

- Email is a cloud-hosted mailbox service with a webmail interface at `mail.orrinvalley.example`. All sign-ins go through the same cloud identity service.
- MFA rollout is 70% complete. Jordan Pike's account (`jpike`) was not yet enrolled. The controller, Maren Beaulieu (`mbeaulieu`), was enrolled in February.
- The inbound mail gateway tags outside mail with `[EXTERNAL]` in the subject. It does not rewrite links and does not flag lookalike domains.
- The web proxy logs in the appliance's local time. Priya is "pretty sure" it is set to the office time zone (US/Canada Eastern, IANA zone `America/Toronto`) but has not checked.
- The mailbox audit export covers all events for `jpike` and `mbeaulieu` from 9 March 2026 00:00 UTC to 17 March 2026 12:00 UTC, plus failed sign-ins tenant-wide from one IP that Priya noticed. It does not cover the shared `ap@` mailbox or any other staff. Audit data before 9 March was not exported.
- The mail gateway trace covers 1 to 17 March, filtered to messages involving `castellan`, `jpike` or `mbeaulieu`.
- Vendor master changes are made in the ERP by the controller. ERP logs were not provided. According to Maren, she changed Castellan's bank account and remittance email address on 11 March after an email from Jordan.

Statement from Jordan Pike, AP specialist (summarized):

> "I got the email from Dana on Tuesday morning, the 10th. It was in the same thread as the invoice, so I didn't think twice. I clicked the link, it asked me to sign in to see the document, and I did. Then it just went to Castellan's normal website. I figured the document had moved or something. I never sent Maren anything about banking. I didn't see any more emails from Castellan that week, which I thought was a bit odd because Dana usually sends a reminder before the due date."

Statement from Maren Beaulieu, controller (summarized):

> "On Wednesday the 11th Jordan emailed me Castellan's bank letter and asked me to update the vendor record before Friday's run. The email said Castellan's phones were down that week, so I didn't call. The letter looked right. I made the change and replied to Jordan."

What Castellan told Owen by phone on 16 March (hearsay, one call, not verified):

> Dana Whitlock said she never sent a banking-change email. Castellan's IT "checked and found nothing." Dana also mentioned that "a couple of other customers" had asked about a banking change in the past two weeks.
