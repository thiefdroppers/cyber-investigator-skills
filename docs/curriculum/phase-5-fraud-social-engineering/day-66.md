# Day 66: Business email compromise and how spoofed domains are detected

Phase: 5. Fraud, scam, and social-engineering investigation · Track goal: Read an email header well enough to tell a spoofed sender, a lookalike domain, and a genuinely compromised mailbox apart, and write down which one you are looking at and why.

## Concept
Business email compromise (BEC) is a payment fraud. The attacker gets a business to send money to the wrong account by impersonating someone the business already pays or obeys: a supplier with a "new bank account", a CEO who needs a wire sent quietly, a lawyer or title company closing a property sale. IC3's 2025 report lists 24,768 BEC complaints and $3.05 billion in reported losses, second only to investment fraud by dollar amount.

BEC often involves no malware and no link. The weapon is one convincing email, so the investigator's job comes down to one question: did this message really come from the account it claims to come from? There are three different answers, and each leads to a different response.

1. Spoofed sender. The From address shows the real domain (`ap@acme-supplies.example`), but the message was sent from a server that domain never authorized. Email authentication (SPF, DKIM, DMARC) exists to catch this, and it shows up in the headers.
2. Lookalike domain. The attacker registered a similar domain (`acme-suppIies.example` with a capital I, or `acme-supplies-billing.example`). The message passes SPF, DKIM, and DMARC, because the attacker controls that domain and set up authentication for it. Header checks pass; only a careful comparison of the domain catches it.
3. Compromised mailbox. The attacker logged in to the real supplier's real account. Every technical check passes, the domain is correct, and the message may even sit in an existing email thread. Only the request itself (new bank details, secrecy, urgency) and an out-of-band call to a known phone number catch this.

### How authentication shows up in a header
Receiving mail servers record their verdicts in the `Authentication-Results` header. A spoofed message typically looks like this (fictional):

```
Authentication-Results: mx.receiver.example;
  spf=fail (sender IP 203.0.113.55 not permitted by domain of acme-supplies.example)
  dkim=none;
  dmarc=fail (p=REJECT) header.from=acme-supplies.example
```

SPF checks whether the sending server's IP address is on the list the domain published in DNS. DKIM checks a cryptographic signature the sending domain adds to the message. DMARC checks that at least one of those passed and that the passing domain matches (is "aligned" with) the domain in the visible From line, then applies the domain owner's published policy: `none`, `quarantine`, or `reject`. A domain with `p=none`, or no DMARC record at all, can be spoofed and the message may still land in the inbox, marked only by a failing result in a header nobody reads.

### Red-flag checklist
1. A change to payment details (new bank, new account, "our bank is being audited") arriving by email.
2. Urgency tied to a deadline ("the wire must go out before 3 PM or we lose the deal").
3. A request to skip the usual approval step "just this once".
4. A request for secrecy ("don't mention this to anyone until the acquisition is announced").
5. The sender is traveling, in a meeting, or otherwise unreachable by phone.
6. The Reply-To address differs from the From address, or replies go to a free-mail account.
7. `Authentication-Results` shows `spf=fail`, `dkim=fail`, or `dmarc=fail`.
8. The domain differs from the one in previous genuine correspondence by a character, a hyphen, a word, or a top-level domain.
9. The domain was registered days or weeks ago (check WHOIS or RDAP).
10. The message joins an existing thread but the thread history quoted below it has small differences from the original messages.

## Resources
- [FBI IC3 2025 Internet Crime Report (PDF)](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf): BEC figures and the Recovery Asset Team's Financial Fraud Kill Chain results. In 2025 the team froze about $679 million of roughly $1.16 billion in attempted theft across 3,900 incidents. The report's advice: contact the bank immediately to request a recall, then file at ic3.gov with full transaction details.
- [Google Admin Toolbox Messageheader](https://toolbox.googleapps.com/apps/messageheader/): paste a raw header and get the hop-by-hop path, delays, and SPF/DKIM/DMARC results in a table.
- [MXToolbox Email Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx) and [MXToolbox DMARC lookup](https://mxtoolbox.com/DMARC.aspx): a second parser, and a quick way to read a domain's published DMARC policy.
- [dnstwist](https://github.com/elceef/dnstwist): an open-source tool that generates lookalike permutations of a domain (typos, homoglyphs, added words, other TLDs) and checks which ones are registered. `pip install dnstwist`.
- [ICANN Lookup](https://lookup.icann.org/): registration data (RDAP) including creation date.
- [dmarcian DMARC overview](https://dmarcian.com/what-is-dmarc/): how policy and alignment work, with examples.

## Practical: Google Admin Toolbox and dnstwist, an annotated header and a lookalike-domain table

### Part 1: read your own headers
Use two messages from your own mailbox: one genuine message from a large company, and one from your spam folder. In Gmail, open "Show original"; in Outlook, open "View message details" or "Properties".

For each message:
1. Paste the full header into Google Admin Toolbox Messageheader.
2. Record the SPF, DKIM, and DMARC results, the domain each one checked, and whether the DKIM `d=` domain matches the From domain.
3. Read the `Received:` lines from the bottom up. The lowest one is closest to the sender. Record the first external server name and IP address.
4. Compare From, Reply-To, and Return-Path. Note any that differ.
5. Look up the From domain's DMARC policy with MXToolbox and record it (`p=none`, `quarantine`, or `reject`).

### Part 2: lookalike domains for a fictional supplier
Run dnstwist against a large, well-known brand's domain (a bank or retailer; any public domain works, since you are only reading registration data):

```
dnstwist --registered --format csv <brand-domain> > lookalikes.csv
```

From the output, pick five registered lookalikes. For each, record the permutation type dnstwist reports (addition, homoglyph, hyphenation, tld-swap, and so on), whether it has MX records (it can receive mail), and its creation date from ICANN Lookup. Do not visit the domains in your browser. If you need to see what one hosts, use a private urlscan.io scan as on Day 65.

### Part 3: classify three fictional cases
For each case, state whether it is a spoofed sender, a lookalike domain, or a compromised mailbox, and which evidence decided it.

- Case A: From `ceo@harborline.example`. `spf=fail`, `dkim=none`, `dmarc=fail (p=none)`. Delivered to inbox. Asks the controller to buy gift cards "before my 2 PM board meeting".
- Case B: From `billing@harborIine.example` (capital I). `spf=pass`, `dkim=pass (d=harborIine.example)`, `dmarc=pass`. Domain created 9 days before the email. Asks to update the remittance account.
- Case C: From `billing@harborline.example`. All checks pass, `d=harborline.example`. Arrives inside a real three-week-old invoice thread. Asks to update the remittance account. The supplier later confirms someone logged in to their mailbox from an unfamiliar country.

(Answers: A is spoofed and shows why `p=none` matters. B is a lookalike, where authentication passes for the wrong domain. C is a compromised mailbox, and the only reliable control would have been calling the supplier on a number already on file.)

### The artifact
A single document with three parts: two annotated headers (each with the authentication table, the bottom-most external `Received:` hop, the From/Reply-To/Return-Path comparison, and the domain's DMARC policy); the five-row lookalike table from dnstwist with permutation type, MX presence, and creation date; and the three case classifications with the deciding evidence quoted.

## Checkpoint
Without notes, explain why case B passed DMARC and why that does not make it legitimate. In your annotated headers, every authentication result must name the domain it evaluated, not just "pass". If you cannot say which `Received:` line is the first external hop, redo step 3 until you can point to it and explain which lines above it belong to your own mail provider.
