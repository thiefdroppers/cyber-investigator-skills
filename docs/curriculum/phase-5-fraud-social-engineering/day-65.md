# Day 65: Phishing red flags and inspecting a link without clicking it

Phase: 5. Fraud, scam, and social-engineering investigation · Track goal: Take a suspicious message apart safely, record every red flag with the evidence behind it, and find out where its link goes without ever loading the page in your own browser.

## Concept
Phishing is the entry point for most of what this phase covers. A fake job offer, a romance contact, and a spoofed invoice all usually arrive as a message that wants you to click, reply, or pay. In the FBI IC3 2025 annual report, phishing and spoofing was the most-reported crime type by a wide margin, with 191,561 complaints out of 1,008,597 total. Reported losses in that category rose from about $70 million in 2024 to about $216 million in 2025, while the complaint count stayed almost flat.

An investigator handles a phishing sample the way a forensic examiner handles a disk. You preserve the original first, you work on a copy, and you never "just check" the link by clicking it. Opening a phishing page can confirm to the sender that your address is live, trigger a drive-by download, or log your IP address against a tracking token in the URL. Each of those changes the evidence and can put you at risk.

The red flags below repeat across almost every phishing campaign. None of them proves a message is malicious. Three or four together, each backed by a specific line from the message, make a strong case.

### Red-flag checklist
1. The display name says one organization, and the actual sending address or domain belongs to someone else ("PayPal Support" from `notice@secure-acct-update.example`).
2. The link text and the link destination differ. The visible text reads `www.yourbank.com` and the underlying `href` points somewhere else.
3. The domain is a lookalike: swapped characters (`rn` for `m`), an extra word (`yourbank-verify.example`), a different top-level domain, or punycode (`xn--`) that renders as familiar letters.
4. The link goes through a URL shortener or open redirect, so the real destination is hidden until something expands it.
5. The message sets a deadline or threat ("account suspended in 24 hours", "final notice") that leaves no time to verify.
6. It asks for credentials, an MFA code, or payment details through a channel the real organization says it never uses for that purpose.
7. The greeting is generic ("Dear Customer") when the real sender would know your name, or the message uses your name and nothing else it should know.
8. An unexpected attachment arrives, especially an archive, an HTML file, a disk image, or an Office document that asks you to "enable content".
9. The reply-to address differs from the from address.
10. The message references a transaction, delivery, or account you have no record of.

## Resources
- [FBI IC3 2025 Internet Crime Report (PDF)](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf): the complaint and loss tables quoted above, by crime type.
- [FTC: How to recognize and avoid phishing scams](https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams): plain-language red flags you can compare against the checklist.
- [CISA: Avoiding social engineering and phishing attacks](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks).
- [urlscan.io](https://urlscan.io/): loads a URL in its own sandboxed browser and returns a screenshot, the redirect chain, contacted domains, and page resources. Free account; set scans to Private or Unlisted.
- [VirusTotal URL scan](https://www.virustotal.com/gui/home/url): checks a URL against dozens of reputation engines. Anything you submit publicly becomes visible to other users, so read "Before you submit anything" below first.
- Shortener previews: add `+` to the end of a bit.ly link (`bit.ly/abc123+`) to see Bitly's own preview page, and put `preview.` in front of a TinyURL link (`preview.tinyurl.com/abc123`).
- [Google Phishing Quiz](https://phishingquiz.withgoogle.com/): a short self-test to calibrate before the lab.

## Practical: urlscan.io, a link-inspection worksheet for three samples

You need three phishing samples. Use messages from your own spam folder, the examples in the FTC and CISA pages above, or the fictional sample below. Do not ask friends to forward you theirs; a forwarded message loses its original headers.

### Before you submit anything
A URL can carry data about the target. Tokens like `?id=8f3a...` or `?email=jane%40company.example` often identify the specific recipient. Submitting that URL to a public scanner tells the attacker (who can watch public feeds) that someone investigated, and it publishes the recipient's identifier. Strip or replace personal identifiers before submitting, and set urlscan.io scans to Private. If the sample came from a real case, check whether your organization's policy allows external submission at all.

### Worked example (fictional)
This message is invented for training. The domains use the reserved `.example` top-level domain and do not resolve.

```
From: "Northwind Bank Security" <alerts@nw-secure-login.example>
Reply-To: helpdesk.nwbank@freemail.example
Subject: Unusual sign-in blocked: verify within 24 hours

Dear Customer,
We blocked a sign-in attempt from a new device. To keep your account
open, confirm your identity at https://www.northwindbank.example/verify
before 5:00 PM today.
```

In the raw HTML (in most mail clients: "View source" or "Show original"), the link reads:

```
<a href="https://bit.ly/3xFICTN?u=c3RhZmYxMg">https://www.northwindbank.example/verify</a>
```

Worksheet row for this sample:

| Check | Finding | Evidence |
|---|---|---|
| Display name vs. address | Mismatch | Display "Northwind Bank Security", domain `nw-secure-login.example` |
| Reply-To | Differs from From | `helpdesk.nwbank@freemail.example` |
| Link text vs. href | Mismatch | Text shows `northwindbank.example/verify`, href is `bit.ly/3xFICTN` |
| Tracking token | Present | `?u=c3RhZmYxMg` is base64 for `staff12`, a per-recipient ID |
| Shortener expansion | (Real sample: result of `+` preview) | Final domain recorded here |
| Deadline | Present | "within 24 hours", "before 5:00 PM today" |
| Greeting | Generic | "Dear Customer" |

### Steps for each of your three samples
1. Save the original. In Gmail, "Show original" then "Download original" gives an `.eml` file. In Outlook, drag the message to a folder or use "Save as". Record the file name and the date you saved it.
2. Extract every link from the source, not from the rendered message. Copy the `href` value exactly. Write it in the worksheet "defanged" so nobody clicks it by accident: `hxxps://bit[.]ly/3xFICTN`.
3. Compare link text with the `href` and record the result.
4. If the link is shortened, expand it with the provider's preview (`+` for Bitly, `preview.` for TinyURL). For other shorteners, submit it to urlscan.io, which follows redirects and lists every hop.
5. Remove recipient tokens, then submit the final URL to urlscan.io with visibility set to Private. From the result page, record the final landing domain, the page screenshot (is it a fake login form?), the IP address and hosting country, and the domain's age if shown.
6. Check the same URL on VirusTotal and note how many engines flag it. A score of 0 is common for a phishing page that went live in the last few hours, so zero detections does not mean the link is safe.
7. Score the message against the ten-item checklist, quoting the exact line for each item you mark present.

### The artifact
A worksheet (spreadsheet or markdown table) with one section per sample. Each section has the defanged links, the link-text vs. `href` comparison, the full redirect chain, the final landing domain with its urlscan.io result link, the VirusTotal detection count, and the checklist score with quoted evidence per item. End each section with one sentence: "Phishing / likely phishing / not enough evidence, because ...".

## Checkpoint
Hand the worksheet to someone else and ask them to find one link you wrote in clickable form; there should be none. Every checklist item marked present must have a quoted line next to it. For at least one sample, your redirect chain should show more than one hop, and you should be able to say which hop hid the real destination. If any scan you submitted was set to Public, note it and the identifiers it exposed, then delete the scan if the service allows it.
