# Day 89: The final report at calibrated confidence

Phase: 7. Capstone and career · Track goal: Write the report a client, an insurer and the police could each act on, where every judgment carries the confidence its evidence supports and points to the case graph.

## Concept

The report is where the work becomes useful to someone else, and it is also where most of the damage from a weak investigation happens. An overclaimed finding ("Castellan's email was hacked") can start a dispute between two companies. An underclaimed one ("we could not determine anything about the source") leaves the client without advice it could have had. Calibration means each sentence claims exactly what the evidence supports, in words the reader will interpret the way you intend.

Two kinds of statement belong in the report, and they need different language. Facts you observed directly are stated plainly with their source: "The attacker created an inbox rule at 14:36:50 UTC on 10 March (audit log)." Judgments, which are conclusions you reached by reasoning from facts, carry an explicit likelihood: "It is likely that the attacker obtained the invoice from Castellan's side." Mixing the two is the most common calibration failure. Either a judgment gets written as if it were observed, or an observed fact gets hedged until it reads like a guess.

For likelihood words, use a fixed scale and put it in the report, so that "likely" means the same thing to you and to the insurer. The US intelligence community's analytic standard (ICD 203) publishes one:

| Term | Probability |
|---|---|
| Almost no chance | 1 to 5% |
| Very unlikely | 5 to 20% |
| Unlikely | 20 to 45% |
| Roughly even chance | 45 to 55% |
| Likely | 55 to 80% |
| Very likely | 80 to 95% |
| Almost certain | 95 to 99% |

The roadmap's tags map onto this. "Confirmed" (two or more independent sources agree) is for observed facts and needs no probability word. "Likely" findings from a single source, and anything you reasoned to, get a term from the scale. "Disputed" findings are reported as disputed, with both sides.

Structure follows the reader. The client and the insurer read the first page and maybe nothing else, so the first page gives the answers. Everything after it is the evidence for those answers, arranged so a skeptical reader can check any claim.

## Resources

- [ODNI Intelligence Community Directive 203, Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf). Two pages of standards and the probability table above.
- Sherman Kent, [Words of Estimative Probability](https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf), the 1964 essay on why these words need fixed meanings.
- [Pandoc](https://pandoc.org/) for converting the Markdown report into a Word document or PDF.
- Your case graph, graph memo, session table, triage sheet, ACH matrix and evidence register.

## Practical: Pandoc, the final case report

Write `report/report.md`, export it with Pandoc, and then score it against the instructor key.

### Step 1: draft the report in this structure

```markdown
# Investigation report: diverted payment to Castellan Hardwood Supply
Prepared for: Orrin Valley Millworks · Date: · Investigator: · Classification: Confidential, client and insurer
SYNTHETIC TRAINING CASE. All organizations, people and indicators are fictional.

## 1. Summary
## 2. Key judgments
## 3. What happened: condensed timeline (UTC)
## 4. Findings by client question
## 5. Indicators to block
## 6. Limits of this investigation
## 7. Recommendations
## Appendix A: case graph and legend
## Appendix B: ATT&CK technique layer
## Appendix C: evidence register and hash verification
## Appendix D: probability scale used in this report
```

Section guidance:

1. Summary: at most 150 words. Answer all five client questions in order, each in one or two sentences, with the confidence word. Somebody who reads only this section should know what happened, whether it is over, and the two most important things to change.
2. Key judgments: numbered. Each has the judgment in one sentence, the basis (evidence IDs and case graph node IDs), and what would change it. Aim for six to nine.
3. Timeline: 15 to 25 rows, UTC, with the source for each row. Condense Day 86 to the events that carry the story.
4. Findings by client question: one subsection per question, a few paragraphs each, citing evidence and pointing to the graph.
5. Indicators: a defanged table of domains, IPs, email addresses, hashes and the phone number, with type, first seen, confidence and a recommended action for each. Include the related infrastructure you judged to belong to the same operator, labelled with its confidence.
6. Limits: log coverage (dates, accounts), what happened before collection, hearsay you relied on, the data requests the client could not fulfil, and anything you were not authorized to examine.
7. Recommendations: ranked by how much of the fraud chain each would have broken, tied to your Day 87 break points. Put the ones the client can do this week first.

### Step 2: write the key judgments

Worked example of a confirmed judgment:

> KJ2. An attacker took over Jordan Pike's email account at 14:31 UTC on 10 March 2026, using the password Jordan entered on a phishing page about ten minutes earlier. (Confirmed.)
> Basis: Jordan's workstation posted to `cstl-docshare[.]example/view/auth` at 14:20:41 UTC (P9, converted from UTC-4 using two anchor events); a sign-in to `jpike` succeeded from 198.51.100[.]23 at 14:31:12 UTC with no MFA (P8); the same IP submitted the phishing email (P2); Jordan's statement describes entering the password (P1). Graph paths: `msg_M2` → `d_phish`, and `ip_023` → `sess_7f3a61` → `acct_jpike`.
> What would change it: evidence that the password was exposed earlier by another route. None appears in the audit data from 9 March, and every password-spray attempt against the account failed.

Now three sentences a first draft often contains, with the problem and the rewrite:

> Draft: "The attackers are based in Europe."
> Problem: server location stands in for operator location. P6 L8 reports datacenter locations only.
> Rewrite: "Two of the attacker's servers were hosted by a VPS provider in an EU-West datacenter. Server location does not indicate where the operator is, and this report makes no judgment about the attacker's location or identity."

> Draft: "Jordan fell for the phishing email, and Maren approved the change without checking."
> Problem: it blames people for control gaps, and it will be read by their employer and insurer.
> Rewrite: "The phishing email reached an account without MFA, and the vendor-change approval process did not require a call-back to the vendor on a number already on file. The fraudulent request was written to discourage exactly that call-back ('their phones are down this week')."

> Draft: "The invoice details were stolen from Castellan's email system."
> Problem: this states as fact something the evidence can only make more or less likely, about an organization you did not examine.
> Rewrite: state the judgment at the confidence your final ACH matrix supports, using a term from the scale; name the evidence that points each way; list the data that would settle it (the client's older audit logs, the `ap@` mailbox audit, and Castellan's own review). Then recommend what the client should share with Castellan so Castellan can check its side.

### Step 3: run the overclaim sweep

When the draft is complete, search it for words that often signal more certainty than the evidence allows:

```bash
grep -n -i -E "prove|clearly|definitely|obviously|certainly|undoubtedly|must have|hacker|confirmed" report/report.md
```

For each hit, check that the sentence is either a confirmed fact with two independent sources cited, or rewrite it. Then check that every confidence word in section 2 matches the confidence colour of the corresponding edges on your case graph. If the report says "likely" and the graph edge says "confirmed", one of them is wrong.

### Step 4: verify the evidence and export

Rerun your Day 83 hash check. Put the result in Appendix C.

```bash
cd ~/capstone/originals/case-packet && shasum -a 256 -c ~/capstone/notes/evidence.sha256
```

Then export:

```bash
pandoc report/report.md -o report/report.docx
pandoc report/report.md -o report/report.pdf    # needs a LaTeX engine installed; the .docx does not
```

Insert the case graph image in Appendix A before exporting (`![Case graph](../notes/graph/case-graph.png)` in the Markdown).

### Step 5: score yourself against the instructor key

Only now open [`case-packet/07-instructor-key.md`](case-packet/07-instructor-key.md). Score your report and graph:

| Criterion | Points |
|---|---|
| Each of the eight judgments in the key reached at a matching confidence (one point each, half a point if one step off on the scale) | 8 |
| Planted traps you identified and handled correctly (one point per two traps, up to 6) | 6 |
| Case graph meets the minimum node set (2) and has evidence and confidence on every edge (2) | 4 |
| No out-of-scope action taken or proposed; no person blamed or named as a suspect | 2 |

A score of 16 or more out of 20 means the report is ready to show in your portfolio tomorrow. For every point you lost, add a line to your decisions log saying what you missed and which step in Days 84 to 88 would have caught it. That list is more useful than the score.

## Checkpoint

1. The summary answers all five client questions in 150 words or fewer, each with a confidence word or marked as confirmed.
2. Every key judgment has a basis citing packet evidence and case graph nodes, and a "what would change it" line.
3. The limits section states log coverage, remediation before collection, and each unfulfilled data request.
4. The overclaim sweep has been run, and every remaining hit is a confirmed fact with two cited sources.
5. The hash check in Appendix C shows every original packet file unchanged.
6. You have scored the report against the instructor key and logged what you missed.
