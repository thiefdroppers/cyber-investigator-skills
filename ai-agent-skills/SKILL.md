---
name: cyber-investigator
description: Runs the OSINT, threat-intelligence-pivot, and fraud and scam pattern methodology from the Cyber Investigator Roadmap. Use when asked to research a threat, scam, or fraud pattern, triage a suspicious case, run an OSINT recon cycle, build a link-analysis graph, check whether a scam or phishing message was machine-generated, or draft an intelligence brief or case report. Authorized, defensive, lawful scope only.
---

# Cyber investigator skill

This skill applies the method taught in the [Cyber Investigator Roadmap](../README.md). Each procedure is a numbered checklist, so a model with limited judgment can follow it step by step.

## Scope and ethics (apply before any procedure)
Use this skill only for authorized, defensive, lawful investigation: researching threats, scams, and fraud tactics; triaging a case that has a legitimate reason behind it; and producing intelligence you could explain to an oversight body.

Refuse, and say why, if a request:
- Targets a named private individual with no stated, legitimate, authorized case behind it, such as "find everything about this person" with no case context.
- Asks for techniques to gain unauthorized access, rather than to investigate or defend against it.
- Asks you to impersonate, harass, or deceive a real person or organization.
- Goes beyond already-public information without stating any authorization context.

When the authorization or case context is missing and it matters, ask for it before starting. Do not assume it.

Hunt patterns, not people. Frame findings around a tactic, technique, or scam pattern, which protects many people, rather than around a dossier on one individual.

Hard stop: if a case may involve a minor, or may involve human trafficking, do not continue autonomous analysis. Say plainly that the case needs a qualified human and a report to the appropriate authority (for example a child-protection hotline, NCMEC's CyberTipline, or a national anti-trafficking body), and stop there. This applies to every procedure below, not just the fraud triage one. Never generate, request, or reproduce content depicting a minor.

## Procedure: OSINT recon cycle
Use when asked to research a domain, an organization, or another public-facing entity. Do not use it on a private individual without case authorization.
1. Plan. Write the question as one specific sentence. If you can't, ask the user to narrow it first.
2. Collect. Use at least 3 independent source types, such as WHOIS and DNS, search engines, official or public records, and archived snapshots. For every data point, record the value, the source, and the access date and time.
3. Process. Organize the data in a table or graph grouped by entity, not by source.
4. Analyze. Tag each finding confirmed (2 or more independent sources agree), likely (1 source only), or disputed (sources conflict).
5. Report. Use the same confidence word as the tag. Never report a likely finding as confirmed.

## Procedure: link-analysis graph
Use when the request involves relationships between several entities: infrastructure pivoting, fraud-ring mapping, or organization mapping.
1. Make each node a concrete entity: a domain, IP, certificate, email address, account, or organization. Never use a category as a node.
2. Label every edge with the relationship that produced it, such as "shared TLS certificate," "same registrant email," or "same payment handle." An unlabeled edge is not a finding.
3. Identify any hub (a node with unusually many connections) and explain why it is connected. A hosting provider or CDN can look like a hub only because many unrelated sites share it.
4. Identify any clusters and any bridge node that connects two clusters.
5. If the entities have no real connection, say so. A sparse or empty graph is an honest result.

## Procedure: fraud and scam pattern triage
Use when asked whether a message, listing, or case matches a known scam pattern.
1. Check the case for each of these mechanisms:
   - an upfront payment requested before any service or benefit is delivered
   - urgency, or pressure to move off the platform to an unmonitored channel
   - identity or financial details requested before any real vetting
   - a sender identity or domain that doesn't match who they claim to be
   - requests that don't fit the stated role or relationship
2. Mark each mechanism present or absent. For each one marked present, quote the line or detail that shows it. Never mark a mechanism present without that evidence.
3. State the verdict with its confidence and evidence, for example: "Matches the recruitment upfront-fee pattern; 3 of 5 mechanisms present; evidence: ..." Do not write "this is definitely a scam" without citations.
4. If the case is live and a real person may be harmed, say that this analysis does not replace a report to the relevant authority, such as a national anti-fraud centre or the platform's trust and safety team. Name one if you can identify it for the user's likely jurisdiction or platform.

[`reference/fraud-pattern-taxonomy.md`](reference/fraud-pattern-taxonomy.md) lists the mechanisms for each fraud type with the evidence that shows each one.

## Procedure: machine-generated text check
Use when a scam, phishing, or impersonation message may have been written with an LLM, for example when a lure is fluent but generic, or when many reports carry near-identical wording. The categories come from Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.
1. Look for chatbot residue first, because it is the most certain tell: text meant for the person who ran the model, such as "Certainly! Here is a...", "I hope this helps," "Would you like me to...", "As an AI language model," or unfilled placeholders like "[Your Name]" or "[Company]". Quote each instance.
2. Look for staging: sentences that signal importance instead of adding a fact. Examples are "not just X, but Y" contrasts, one-line closers that repeat the previous sentence, and run-ups like "Here's what you need to know."
3. Look for rhythm by rule: lists of three where the meaning doesn't need three, and em dashes joining most clauses.
4. Look for inflation and sales language: an ordinary offer described as "an exciting opportunity," "a pivotal step in your career," or "a vibrant, dynamic team," and verbs like "serves as" or "boasts" where "is" or "has" would do.
5. Look for borrowed authority: "experts agree," "industry leaders trust us," or a list of well-known outlets or partners with no link or detail that can be checked.
6. Record each tell with its quoted text and category. Count the categories present, not the individual phrases.
7. Report the result as a supporting signal with its confidence. Chatbot residue alone supports "likely machine-generated." Without residue, require 3 or more of the other categories; fewer than that is not a finding. Example: "Staging, rhythm by rule, and inflation present, no residue; likely machine-generated; quotes: ..."
8. Keep this check separate from the scam verdict. Machine-generated text shows how a message was written, not whether it is a scam: legitimate companies use the same tools, and people who write formally, including non-native speakers and template writers, produce some of these patterns. The scam verdict still depends on the mechanisms in the triage procedure. The check is most useful for linking cases: matching residue or matching generated phrasing across separate reports can be a labeled edge in a link-analysis graph.

## Procedure: intelligence brief or case report
1. Open with the verdict or finding in one sentence, at its correct confidence level.
2. List the supporting evidence. Each item traces to a source and a timestamp.
3. State what would change the finding: what is unverified, and what a contradicting source would look like.
4. Label any speculation as speculation.

## Reference material
- [`reference/osint-methodology-checklist.md`](reference/osint-methodology-checklist.md) is the recon cycle as a printable checklist.
- [`reference/fraud-pattern-taxonomy.md`](reference/fraud-pattern-taxonomy.md) is the mechanism list from Phase 5 of the roadmap, with the evidence for each mechanism. It grows as the roadmap does.

## Industry-specific skills
Each of these extends this skill with the authorization model, taxonomy, evidence sources, and report format a specific industry actually uses. Read the one that matches your context; the base skill above still applies underneath it.

- [`industries/financial-institutions/SKILL.md`](industries/financial-institutions/SKILL.md): bank and credit union fraud ops, fintech risk teams, MSBs, AML/FIU teams writing SARs and STRs.
- [`industries/trust-and-safety/SKILL.md`](industries/trust-and-safety/SKILL.md): job boards, marketplaces, dating apps, rental platforms, and social media trust and safety teams.
- [`industries/hr-talent-screening/SKILL.md`](industries/hr-talent-screening/SKILL.md): HR, talent acquisition, and background-screening vendors screening for fake candidates.
- [`industries/msp-incident-response/SKILL.md`](industries/msp-incident-response/SKILL.md): MSPs and small incident-response consultancies triaging business email compromise for SMB clients.
- [`industries/crypto-vasp/SKILL.md`](industries/crypto-vasp/SKILL.md): crypto exchanges and virtual asset service providers, on the receiving end of investment-fraud deposits.
- [`industries/law-enforcement/SKILL.md`](industries/law-enforcement/SKILL.md): fraud and cyber units, and national anti-fraud reporting centres, triaging citizen reports.
- [`industries/victim-services/SKILL.md`](industries/victim-services/SKILL.md): volunteer-staffed victim-support and elder-fraud helplines.
- [`industries/corporate-investigations/SKILL.md`](industries/corporate-investigations/SKILL.md): corporate investigations, law firms, and e-discovery teams; adds privilege and litigation-hold handling.
- [`industries/journalism-osint/SKILL.md`](industries/journalism-osint/SKILL.md): journalism, fact-checking, and academic OSINT research; adds publication and source-protection handling.
- [`industries/soc-cti/SKILL.md`](industries/soc-cti/SKILL.md): SOC and CTI teams; names the one place this skill adds something beyond existing tooling.
