# Instructor key: ground truth and marking guide

> SYNTHETIC TRAINING MATERIAL. Fictional case; see the packet [README](README.md).
>
> Learners: stop here until your Day 89 report is finished and saved. Reading this first turns the capstone into a reading exercise and leaves you with nothing to compare your judgment against.

## What happened (the scenario as designed)

One operator ran a vendor-impersonation campaign against the customers of at least two suppliers. The Castellan leg went like this. All times are UTC.

| When | Event | Where a learner can see it |
|---|---|---|
| 19 Feb 22:05 | `marrowline-docs.example` registered (earlier campaign against Marrowline Freight's customers) | P6 L1 |
| 20 Feb | Certificates issued for `marrowline-docs.example`; `mail.marrowline-docs.example` starts resolving to 198.51.100.23 | P6 L3, L4 |
| 24 Feb 21:14 | Lookalike `castellan-hardwood.example` registered | P6 L1 |
| 26 Feb 03:40 | Phishing domain `cstl-docshare.example` registered | P6 L1 |
| 27 Feb 00:12 | Bank-change letter PDF created (metadata shows 26 Feb 19:12 -05:00) | P3 M3 metadata |
| 3 Mar 14:47 | Real invoice CHS-20417 sent by Castellan to `ap@` with Jordan in cc | P3 M1, P7 |
| 9 Mar | Passive DNS for `mail.marrowline-docs.example` ends | P6 L3 |
| 10 Mar 02:41 | Letter PDF last modified (9 Mar 22:41 -04:00) | P3 M3 metadata |
| 10 Mar 03:11 to 03:13 | Password spray from 203.0.113.200, all failed. Unrelated to the BEC as far as the evidence shows | P8 |
| 10 Mar 14:02:37 | Phishing email delivered to Jordan only; submitted from 198.51.100.23 through the lookalike's mail server 203.0.113.47 | P2 headers, P7 |
| 10 Mar 14:19:07 | Jordan opens the phishing link (10:19:07 local, EDT) | P9 |
| 10 Mar 14:20:41 | Jordan submits credentials; the page redirects to the real vendor site | P9 |
| 10 Mar 14:31:12 | Attacker signs in as Jordan from 198.51.100.23, Linux Firefox, no MFA | P8 |
| 10 Mar 14:36:50 | Hiding rule created: keywords Castellan, remittance, banking, CHS- go to RSS Subscriptions, marked read | P8 |
| 10 Mar 14:38 to 14:44 | Attacker syncs Inbox (212 items) and Sent Items (388 items) | P8 |
| 11 Mar 13:21:05 | Jordan's genuine email from the office (baseline for comparison) | P8, P9, P7 |
| 11 Mar 13:52:44 | Attacker sends the fake bank letter from Jordan's mailbox to the controller, then deletes it from Sent and Deleted Items | P8, P7, P3 M3; absent from P9 |
| 11 Mar 15:06:12 | Controller approves and updates the vendor record; the rule hides her reply from Jordan and the attacker reads it at 15:20 | P3 M4, P8 |
| 12 Mar 16:05 | Castellan's real reminder ("banking details are unchanged") is hidden by the rule | P3 M5, P7, P8 |
| 12 Mar 16:40 | Attacker's follow-up asking for the remittance advice is hidden by the rule; attacker reads both at 16:45 | P3 M6, P7, P8 |
| 13 Mar 19:02 | ERP sends the remittance advice to the attacker's address. Payment released | P3 M7, P7 |
| 14 Mar 02:51 | `quennmarsh-accounts.example` registered and later hosted on the same VPS as the Marrowline infrastructure | P6 L1, L3, L5 |
| 16 Mar about 14:15 | Castellan phones the client (10:15 local) and emails at 14:20 | P1, P7 |
| 16 Mar 19:32 to 19:40 | IT resets the password, revokes sessions, deletes the rule (before exporting logs) | P8, P1 |
| 16 Mar 23:14 | Attacker tries Jordan's old password from 198.51.100.23 and fails | P8 |

## Expected key judgments and the confidence they support

A strong report reaches roughly these judgments. The confidence words follow the roadmap's tags (confirmed, likely, disputed) and the probability language from Day 89. Accept different wording at the same confidence. Mark down any judgment stated at a higher confidence than the evidence here supports.

1. Jordan's account was taken over on 10 March at 14:31 UTC using a password captured by `cstl-docshare.example` about ten minutes earlier. Confirmed. Three sources agree (P9 POST, P8 sign-in, Jordan's statement), and the phishing URL's parameters decode to Jordan's address and username.
2. The attacker created the hiding rule, sent the fake bank letter internally, deleted the sent copy, and read the controller's approval, Castellan's real reminder and the attacker's own follow-up. Confirmed from P8, corroborated by P7 and P3. The absence of any send in P9 at 13:52 UTC supports the conclusion that Jordan did not send M3.
3. The attacker had copies of the Inbox and Sent Items from 10 March. Confirmed that the sync happened (P8). Which items the attacker actually read beyond the Bind events is unknown.
4. The source of the invoice details. The phishing email carried the real Message-ID of M1 in `In-Reply-To`, so the attacker had the original message before 14:02 on 10 March, and nothing in P8 shows attacker access to Jordan's mailbox before 14:31 that day. Vendor-side exposure is likely (about 55 to 80%), supported by the generic "to our valued customers" letter created on 26 February, the lookalike registered before the invoice existed, and Castellan's hearsay about other customers. Client-side exposure cannot be excluded because P8 starts on 9 March and does not cover `ap@`. A report that states "Castellan was breached" as fact has overclaimed. A report that says the question cannot be answered at all has underclaimed.
5. The Marrowline infrastructure and the Castellan infrastructure belong to the same operator or a closely shared toolkit. Highly likely, and supported by independent pivots that converge: the identical JavaScript hash and form path (P6 L6), the Marrowline sentence left on the lookalike's privacy page (P5 B2), 198.51.100.23 serving as `mail.marrowline-docs.example` until 9 March and then submitting the phish and logging in to Jordan's mailbox (P6 L3, P2, P8), and the matching registrar and name server pattern (weak alone). Neither the favicon match nor the IP alone would support this.
6. `quennmarsh-accounts.example` is probably part of the same infrastructure (likely: same single-tenant VPS, same registrar and DNS host, registered after the Castellan leg). Its purpose is unknown. Recommend blocking it and asking the client whether it does business with anyone called Quennmarsh. Stating it as the next confirmed target is overclaiming.
7. The password spray from 203.0.113.200 has no demonstrated connection to this case. It failed, it hit six accounts, and the IP is on a public blocklist for spraying many tenants. The compromise is fully explained without it.
8. Attribution to a person, group or country is not supported. The VPS locations, the PDF's time zone offset (which matches the victim's region and may be a setting or a choice), and the Linux user agent are not attribution evidence.

## Planted traps

| Trap | Where | What a careful learner does |
|---|---|---|
| Time zone change | P3 M1 is -0500, later messages are -0400, because Eastern daylight time began on 8 March 2026 | Converts each timestamp with its own offset. A learner who applies -4 everywhere finds a false one-hour mismatch between M1 and the quote in P2. |
| Proxy log in local time with no offset | P9 | Anchors the offset with a cross-source event: P9 `POST /login` at 09:05:13 matches P8 sign-in at 13:05:14 UTC, so the proxy is UTC-4 on that date. Does not take the IT contractor's "pretty sure" as proof. |
| SPF pass on the lookalike | P2 `Authentication-Results` | Notes that SPF passed for the attacker's own domain, which says nothing about whether the sender is Castellan. DKIM none and DMARC none are the informative results, compared against M1's triple pass. |
| Same /24, different owners | 198.51.100.23 (attacker VPS), .77 (mobile carrier), .170 and .180 (Castellan's mail) | Links IPs by ASN and context from P6 L8, never by prefix. |
| Shared hosting | 203.0.113.88 hosts 1,412 domains | Does not pull co-hosted domains onto the graph as suspects. |
| Favicon from a public template | P6 L6 S3, L7 | Recognizes that Brightquay Legal shares the favicon because it uses the same open-source template (different JS hash, certificates since 2021). Excludes it from the operator cluster. |
| Favicon matching the real vendor | P6 L7 hash 884215106 | Reads this as the clone copying the vendor, not as evidence against the vendor. |
| Castellan's mail server moved in January | P6 L3 | Checks whether the move explains anything. It does not: M1, M5 and the 16 March email all pass SPF, DKIM and DMARC from the new server. |
| VPS IP reuse | 198.51.100.23 pDNS ends 9 March, attacker use starts 10 March | Raises IP reassignment as the rival explanation and shows that the other pivots carry the link without it. |
| Password spray | P8, 10 March 03:11 | Treats it as a separate event unless evidence connects it. |
| Jordan's phone | 198.51.100.77, iOS, mobile carrier | Classifies as benign with a stated reason (present on 9 March, before the phish; mobile carrier; matches Jordan's device) and recommends confirming with Jordan. |
| Remediation before collection | P1 Part A, P8 16 March 19:40 | Notes that IT deleted the rule before exporting logs, records it as an evidence-handling gap, and relies on the `New-InboxRule` audit event for the rule's content. |
| Company name | M1 invoice says "Inc.", fake letter and ERP payee say "Ltd."; letter's CFO is "G. Castellan", real CFO is Ines Castellan-Rowe | Uses both as fraud indicators in the Day 87 analysis. |

## Out-of-scope temptations

The Day 85 checkpoint asks learners to name these before starting. Any report or notes that show one being acted on should fail the ethics criterion regardless of analytic quality.

- Looking up Dana Whitlock, Jordan Pike or Maren Beaulieu on social media or people-search sites.
- Visiting the phishing page to see it live, or "testing" it with fake credentials.
- Emailing the freemail Reply-To address or calling 555-0148 to confirm who answers.
- Investigating Castellan's systems, or Marrowline Freight or Quennmarsh beyond noting the brand use.
- Naming a suspect person or country.

## Minimum case graph (Day 88)

A passing graph has at least these nodes: the three attacker domains in the Castellan leg (`castellan-hardwood.example`, `cstl-docshare.example`, `mail.castellan-hardwood.example`), `marrowline-docs.example` and `portal.marrowline-docs.example`, `quennmarsh-accounts.example`, IPs 198.51.100.23, 203.0.113.47, 203.0.113.88 and 203.0.113.91, the Reply-To address, phone 555-0148, the JS hash, the kit favicon hash, Jordan's account, the controller's account, the inbox rule, messages M1, M2, M3, M4, M5, M6 and M7, the payee account ending 8830, and the payment. Every edge carries a relationship label, an evidence citation and a confidence style. The graph shows the Castellan cluster, the Marrowline cluster, and 198.51.100.23 and the kit JavaScript hash as the bridges between them. The spray IP, Brightquay and the shared-hosting neighbours are either absent or explicitly marked as excluded.

## ATT&CK mapping a reviewer would accept

Check each ID against the current ATT&CK release before marking; technique IDs and names change between versions.

| Technique | Evidence |
|---|---|
| T1583.001 Acquire Infrastructure: Domains | P6 L1 registrations |
| T1585.002 Establish Accounts: Email Accounts | Freemail Reply-To address (P2, M6) |
| T1608.005 Stage Capabilities: Link Target | Credential page staged on `cstl-docshare.example` before the phish |
| T1566.002 Phishing: Spearphishing Link, or T1598.003 Phishing for Information: Spearphishing Link | P2. Accept either with a stated reason: the link harvested credentials, which ATT&CK files under T1598.003 in Reconnaissance, and it was also the initial access route. |
| T1078.004 Valid Accounts: Cloud Accounts | P8 14:31:12 sign-in |
| T1564.008 Hide Artifacts: Email Hiding Rules | P8 `New-InboxRule` |
| T1114.002 Email Collection: Remote Email Collection | P8 `MailItemsAccessed` sync events |
| T1534 Internal Spearphishing | P8 and P3 M3 |
| T1070.008 Indicator Removal: Clear Mailbox Data | P8 `MoveToDeletedItems` and `SoftDelete` |
| T1684.001 Social Engineering: Impersonation (was T1656 before ATT&CK v19; accept either if the student notes the version) | P2, P3 M3, M6, the letter |
| T1657 Financial Theft | P3 M7, P1 |

Do not accept T1586.002 (Compromise Accounts: Email Accounts) for Castellan's mailbox as observed. It is a hypothesis in this case, and at most belongs in a hypothesis layer marked as such.
