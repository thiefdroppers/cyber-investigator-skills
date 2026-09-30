# Day 87: Fraud and social-engineering analysis

Phase: 7. Capstone and career · Track goal: Apply the Phase 5 triage method to the case's messages, show how each message was built to get past a specific control, and turn the case into a reusable fraud pattern.

## Concept

The forensics told you what the attacker did with Jordan's mailbox. It does not explain why two careful employees moved $48,612.50 to a stranger. That part of the case is social engineering, and it has its own evidence: the wording of each message, what it asks for, what it discourages, and which business control stood between the attacker and the money at each step.

Business email compromise (BEC) against accounts payable usually follows one pattern: persuade the payer that a real supplier has new bank details, and make sure the change is approved before anyone checks with the real supplier. The variant in this case adds two refinements. The first message arrived inside a real invoice thread, which borrows all the trust built up by earlier genuine emails. The bank change then reached the approver from a colleague's real mailbox. The controller never saw an external message at all, only an internal one from someone she works with every day.

Reading the messages as a set of countermeasures makes the analysis concrete. Orrin Valley had controls, even if they were informal: the controller approves vendor changes, staff can call a supplier, the supplier emails reminders, Jordan would notice replies from Castellan. Each attacker message or action lines up against one of those. The "phones are being migrated" line exists because a phone call would have ended the fraud. The inbox rule exists because Castellan's real reminder, which said the banking details had not changed, would have ended it too. Castellan's own website told customers to call before acting on any banking change by email. The attacker's clone of that website removed that paragraph.

Two disciplines from Phase 5 apply. Score each mechanism with the exact words that show it, and record the ones that are absent, since absence tells you about targeting. Then write up the pattern: a description of the technique general enough to recognize in the next case, with no names or identifiers from this one. Write about Jordan and Maren as people a control failed, which is what the evidence shows.

## Resources

- [FBI Internet Crime Complaint Center (IC3)](https://www.ic3.gov/). Its public service announcements on business email compromise describe the vendor-impersonation and bank-change variants, and its annual report gives the reported losses.
- The roadmap's [fraud pattern taxonomy](../../skill/reference/fraud-pattern-taxonomy.md) (BEC and phishing sections) and the triage procedure in [`skill/SKILL.md`](../../skill/SKILL.md).
- [Day 68](../phase-5-fraud-social-engineering/day-68.md) for mechanism scoring with quoted evidence.
- [diagrams.net (draw.io)](https://app.diagrams.net/), free, for the swimlane diagram.

## Practical: diagrams.net, a scored triage sheet, a swimlane diagram with break points, and a pattern card

Artifacts: `notes/triage.md`, `notes/swimlane.drawio` plus a PNG export, and `notes/pattern-card.md`.

### Part 1: score each attacker message

Triage four items: the phishing email (P2), the internal email to the controller (M3), the attacker's follow-up (M6), and the bank letter attached to M3. Use the BEC and phishing mechanisms from the taxonomy. For each mechanism, mark present or absent and quote the exact evidence. Worked example for P2:

| Mechanism | Present? | Evidence (quoted) |
|---|---|---|
| BEC: spoofed or lookalike domain | Yes | `From: ... <dana.whitlock@castellan-hardwood.example>`; real domain is `castellanhardwood.example` (P3 M1) |
| BEC: authority and urgency | Yes | "We would appreciate it if CHS-20417 could go out in Friday's payment run, as the old account closes on the 16th." |
| BEC: process bypass | Yes | "Our office phones are being migrated to a new system this week, so email is the quickest way to reach me." It closes off the phone call, the one check that would have caught the fraud. |
| BEC: secrecy | No | Nothing asks Jordan to keep it quiet. In a vendor-impersonation scheme secrecy would look odd, since bank changes are routine paperwork. |
| Phishing: sender mismatch | Yes | Same evidence as the lookalike domain row |
| Phishing: link mismatch | Yes | Text `https://castellanhardwood.example/remittance`; `href` to `cstl-docshare.example/view/r?...` |
| Phishing: generic greeting with fear or urgency | No | "Hi Jordan," and the link parameters encode Jordan's username, which fits a targeted message. |
| Phishing: wrong channel for the request | Yes (on the linked page) | P6 L6 S1: "Sign in with your work email to view Remittance_Form.pdf", email field prefilled |

Verdict line, in the form the taxonomy procedure asks for: "Matches BEC vendor impersonation (3 of 4 BEC mechanisms present) combined with a targeted credential-phishing link (3 of 4 phishing mechanisms present). Evidence as quoted above."

Do the same for M3, M6 and the letter. M3 is the interesting one: it comes from a genuine internal mailbox, so the sender-domain mechanisms are absent. Record which mechanisms the internal relay made unnecessary.

### Part 2: examine the bank letter as a document

Compare the letter (P3 M3) with everything you know about the real Castellan: the invoice details in M1, the archived About page (P4), and the phone listings (P6 L9). List every inconsistency with its source. One to start:

> The letter is dated 9 March 2026, but its metadata shows it was created on 26 February 2026 at 19:12 -05:00 and last modified on 9 March at 22:41 -04:00, with the title `vendor_letter_v3`. The letter was drafted before Castellan issued the invoice it was used against (3 March), and the "v3" suggests earlier versions. Inference: the letter was prepared as a general template for Castellan's customers, not written in response to CHS-20417.

Find at least four more, covering the company name, the officers named, the contact details and the salutation. For each, say whether a careful approver could have spotted it without special tools. That answer feeds the recommendations on Day 89.

### Part 3: map each message to the control it defeated

Build a table in `notes/triage.md`:

| Step | Message or action | Persuasion lever | Control it was built to get past | Evidence |
|---|---|---|---|---|
| 1 | P2 phishing email | Continuity: sits in the real invoice thread with the real quoted text | Jordan's familiarity with the vendor, and the "[EXTERNAL]" tag | `In-Reply-To` matches M1; quoted text identical to M1 |
| 2 | Inbox rule | (none, a technical step) | Castellan's reminder emails, and Jordan noticing replies | P8 `New-InboxRule` keywords; M4, M5, M6 found in RSS Subscriptions |

Continue for M3, M6 and the ERP remittance email (M7). For M3, name the two levers it relies on (look at who it appears to come from, and at its last paragraph).

### Part 4: draw the swimlane in diagrams.net

Create a diagram with one horizontal lane each for: attacker infrastructure, Jordan's mailbox under attacker control, Jordan, Maren, the ERP, and the real Castellan. Draw each message or action as an arrow between lanes, labeled with its ID and UTC time from your Day 86 timeline, for example `M3 · 11 Mar 13:52`. Start with the real invoice (M1) and end with the remittance advice (M7) and Castellan's call on 16 March.

Then add break points. A break point is a red marker on the arrow where one control, had it existed and been used, would have stopped the fraud. For each, add a note with two parts: the control, and the evidence that it was missing or bypassed. Worked example:

> Break point at the sign-in of 10 Mar 14:31 UTC. Control: MFA on Jordan's account. Evidence it was missing: P8 `MFA=NotRegistered` on every `jpike` sign-in until 17 March; P1 notes MFA rollout at 70%. Maren's account had MFA and shows no attacker sign-in.

Mark at least four break points. At least one must be a process control rather than a technical one. The controller calling Castellan on a number from the vendor file, not from the email, is one such control.

Export the diagram as PNG and keep the `.drawio` file.

### Part 5: write the pattern card

Write `notes/pattern-card.md` for the taxonomy, in a form you could propose through the roadmap's contribution process. It must describe the technique with no names, domains, IPs, amounts or dates from this case. Use this structure:

```markdown
## Vendor thread hijack with internal relay (BEC)
Mechanism: (two or three sentences on how the scheme works)
Stages: (numbered, from infrastructure setup to payment)
Evidence that confirms it in a new case: (what to look for, per stage, and in which log or message)
Detection opportunities: (for each stage, what a defender could alert on)
Controls that break it: (ranked by where in the chain they act)
Common false leads: (what looks connected but usually is not)
```

Test the card by rereading it as if you had never seen this case. If any line only makes sense with the case packet open, rewrite it.

## Checkpoint

1. Every mechanism marked present in your triage sheet has quoted evidence, and every item has at least one mechanism marked absent with a reason.
2. Your letter analysis lists at least five inconsistencies, each with its source.
3. The swimlane runs from M1 to Castellan's call, every arrow carries an ID and a UTC time, and there are at least four break points, each with the missing control and the evidence that it was missing.
4. The pattern card contains no identifier from this case, and a colleague could use its "Evidence that confirms it" section to check a different case.
5. Nothing in your notes describes Jordan or Maren as careless or at fault. Where a person acted, the note names the control that should have supported them.
