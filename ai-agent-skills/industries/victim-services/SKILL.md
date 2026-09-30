---
name: cyber-investigator-victim-services
description: Applies the Cyber Investigator Roadmap's scam triage to live calls at victim-services nonprofits and elder-fraud helplines. Use when a helpline volunteer or victim advocate needs to recognize which scam a caller is describing, explain it in plain language, and route the caller to the right help. Not for investigating anyone. Authorized, defensive, lawful scope only.
---

# Cyber investigator skill: victim-services nonprofits and elder-fraud helplines

This extends [`../../SKILL.md`](../../SKILL.md). Apply its report-writing procedure, together with everything below. The OSINT recon cycle and link-analysis graph procedures are deliberately not used here; see the removal note below.

This skill is short on purpose. Helplines like AARP's Fraud Watch Network take a large number of calls every day, answered mostly by trained volunteers whose training takes about a workday, not weeks. A volunteer needs to be able to follow this during a live, emotional call. The need is large: the US Department of Justice's 2025 annual elder-fraud report states that VOCA-funded organizations served close to 200,000 older victims in 2025.

## Ask before assuming
If anything needed to do this correctly is missing or unclear, such as the authorization or case ID, which jurisdiction applies, what evidence sources are actually available, or what output format is expected, ask one specific clarifying question before proceeding. Do not guess. Do not fill a gap with a plausible-sounding default and continue as if it were given. Do not lower your stated confidence instead of asking. If you are not confident enough to act, that is the signal to ask, not to hedge and proceed anyway. A wrong guess costs the investigation more than the time a clarifying question takes.

On a live call, the question that matters most is usually which country the caller is in, because that decides where they report.

## Removal note: no investigation
Helpline volunteers should not be investigating anyone. This skill removes the base skill's OSINT recon cycle and link-analysis graph procedures entirely. Do not look up the scammer's phone number, website, payment handle, or name. Do not build a graph of accounts or domains. The job here is to triage what the caller describes and route them, not to research the scammer.

If a volunteer asks for research on a scammer, say that this is work for law enforcement or the agency the caller reports to, and go back to helping the caller.

## Scope and authorization for victim-services helplines
The caller's own account of what happened to them is the case. No separate authorization step is needed to help the person in front of you.

1. Work only from what the caller tells you. Do not research any third party, whether a suspected scammer or a family member, beyond what the caller volunteers.
2. If the caller suspects a relative or caregiver, write down what the caller said and follow the organization's own procedure for suspected elder abuse. Do not look into that person.
3. The base skill's hard stop still applies. If the case may involve a minor or human trafficking, stop the analysis and say it needs a qualified human and a report to the appropriate authority.
4. If the caller is in danger or money is leaving their account right now, the first step is the organization's urgent procedure (for example, telling them to call their bank), not triage.

## How to use fraud and scam pattern triage on a live call
Apply the base skill's triage procedure to what the caller describes. Do it gently, in plain language a distressed person can follow.

1. Let the caller tell the story first. Do not run through the mechanism list as questions.
2. Match what they describe against the base skill's five mechanisms and the lure table below.
3. The quote-the-evidence rule still applies, in a softer form. For each mechanism you mark present, note which part of what they told you shows it. For example: "They were told to buy gift cards and read out the numbers." This is a note for the volunteer, not an interrogation of the caller.
4. Tell the caller what it sounds like in one or two plain sentences. For example: "What you're describing matches a common scam where someone pretends to be a government agency." Say "matches" or "sounds like," not "you were definitely scammed," unless the evidence is clear.
5. Move to next steps: protecting their money and accounts now, then reporting.

### Common lures aimed at older adults

| Mechanism | What the caller might describe |
|---|---|
| Grandparent or bail scam | A call from someone claiming a grandchild is in jail or in the hospital and needs money urgently |
| Tech-support pop-up | A browser pop-up saying the computer is infected, with a phone number to call for help |
| Government impersonation | A caller claiming to be from the tax agency, Social Security, or the police, demanding immediate payment to avoid arrest or a penalty |
| Gift-card or crypto-ATM payment demand | Being told to pay in gift cards or at a crypto ATM. This is a strong scam indicator, because legitimate agencies never ask for payment this way |
| Refund scam through remote access | Being talked into installing remote-access software so someone can "process a refund" |

## Reporting table
Where the caller should report depends on the country they are in. Examples are the FTC or IC3 in the US, and the Canadian Anti-Fraud Centre in Canada.

Use the organization's own current reporting reference for the agency, website, and phone number. Do not let the model supply an agency name or phone number from memory. These details change, and a wrong number given to a distressed caller does real harm. If the organization's reference does not cover the caller's country, say so and ask a supervisor. Do not guess.

This overrides step 4 of the base skill's triage procedure, which allows naming an authority when one can be identified.

## A note on tone
The roadmap's Day 74 material, "Interviewing fraud victims without re-harming them," applies to every call. Never call the caller naive, greedy, or foolish, and do not imply it either, for example with "Why didn't you check first?" The scam worked because it was designed to work, not because the person was careless. Many callers feel ashamed. A caller who feels blamed may hang up and not report at all.

## Reference material
- [`../../reference/fraud-pattern-taxonomy.md`](../../reference/fraud-pattern-taxonomy.md) is the base skill's fraud-pattern taxonomy, with the evidence for each mechanism.
- [Day 74 of the curriculum](../../../curriculum/phase-5-fraud-social-engineering/day-74.md) is companion material for interview technique.
