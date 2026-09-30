# Day 90: Portfolio, resume and where to apply

Phase: 7. Capstone and career · Track goal: Package the artifacts from 90 days into a portfolio a hiring manager can check in five minutes, write a resume that points to them, and build a target list for investigator-track roles.

## Concept

Hiring for investigative roles has a trust problem. Anyone can list "OSINT", "threat intelligence" and "log analysis" on a resume, and an interviewer has about 30 minutes to find out whether you can actually do the work. A portfolio shortens that. If the interviewer can open your capstone graph, read the edge labels, and see that each one cites evidence and carries a confidence, they have seen your method before asking a question. The capstone matters most because it is end to end: intake, collection, forensics, fraud analysis, a graph and a calibrated report on one case.

The roadmap's artifacts map onto five common entry points. A SOC analyst triages alerts and escalates incidents, so the timelines and session attribution show the core skill. A CTI analyst tracks adversary infrastructure and behaviour, so the pivot graphs and ATT&CK layers matter. An OSINT analyst answers questions from open sources under legal and ethical limits, so the recon logs and the rules-of-engagement work show judgment as well as technique. A digital forensics examiner reconstructs events from artifacts in a way that holds up to challenge, so evidence handling and hash verification matter as much as findings. A fraud investigator recognizes schemes and follows money and messages, so the triage sheets, swimlane and pattern card are the lead exhibits.

Two rules apply to everything you publish. Nothing from real work goes in: not a sanitized log, not a "lightly edited" report, not a screenshot with the names blurred. Only synthetic, public or your own lab data. And every synthetic artifact is labelled as synthetic, so nobody who finds it later mistakes a training case for a real one.

## Resources

- [NICE Workforce Framework for Cybersecurity](https://niccs.cisa.gov/workforce-development/nice-framework), the US government's catalogue of cyber work roles with the tasks and knowledge for each. Useful for vocabulary on your resume and for reading job postings.
- [CyberSeek career pathway](https://www.cyberseek.org/pathway.html), which shows entry, mid and advanced cyber roles and common transitions between them (US data).
- [Trace Labs](https://www.tracelabs.org/), which runs OSINT competitions that generate leads on missing-person cases for law enforcement. Taking part gives you supervised, ethical OSINT experience you can describe in an interview.
- Certification bodies you will see in postings: [CompTIA](https://www.comptia.org/) (Security+, CySA+), [GIAC](https://www.giac.org/) (GCIH, GCTI, GCFE, GCFA, GOSI), [ACFE](https://www.acfe.com/) (Certified Fraud Examiner), [ACAMS](https://www.acams.org/) (CAMS, anti-money laundering).
- Government job portals: [USAJOBS](https://www.usajobs.gov/) (US), [GC Jobs](https://www.canada.ca/en/services/jobs/opportunities/government.html) (Canada), [Civil Service Jobs](https://www.civilservicejobs.service.gov.uk/) (UK).

## Practical: GitHub and a spreadsheet, a public portfolio, a one-page resume and a target tracker

Artifacts: a public GitHub repository, a one-page resume as PDF, and `career/targets.ods` (or a Google Sheet).

### Part 1: build the portfolio repository

Create a new public repository, for example `investigation-portfolio`. Suggested layout:

```
investigation-portfolio/
├── README.md                     # who you are, what's here, how to read it
├── capstone-castellan-bec/       # the synthetic Phase 7 case
│   ├── README.md                 # case study write-up (see below)
│   ├── report.pdf
│   ├── case-graph.png
│   ├── case-graph.gephi
│   ├── swimlane.png
│   ├── pattern-card.md
│   └── layer-day86.json          # ATT&CK Navigator layer
├── infrastructure-pivot/         # Day 40
├── incident-timeline/            # Day 58
├── fraud-ring-graph/             # Day 68
└── cloud-iam-graph/              # Phase 6
```

Before you push anything, run each artifact through this check:

1. The data is synthetic, public, or from your own lab. Nothing came from an employer, a client or a real victim.
2. Synthetic material says so at the top of the file or in the image caption.
3. Indicators in text are defanged.
4. No real private individual is named or profiled anywhere, including in the Day 22 and Day 68 work that used public sources. If a public-source lab named a person, cut it to the organization and the pattern.
5. Metadata is clean. Run `exiftool` on every image and PDF and remove author names and paths you do not want public.

Each project folder gets a README written as a short case study. Worked example for the capstone:

```markdown
# Capstone: diverted vendor payment (synthetic BEC case)

Synthetic training case from the Cyber Investigator Roadmap. All organizations,
people and indicators are fictional.

Question: How did a $48,612.50 vendor payment reach an attacker's account,
was an employee's mailbox taken over, and is related infrastructure still active?

What I did:
- Hashed and registered 11 evidence files; wrote rules of engagement before collection.
- Parsed the phishing email's headers and link; pivoted through WHOIS, passive DNS,
  certificate transparency and URL-scan data to a second campaign sharing a phishing kit.
- Anchored an unlabelled proxy clock against the mailbox audit log (UTC-4), merged three
  log sources into one UTC timeline in Timesketch, and attributed 17 sign-in sessions.
- Scored the messages against BEC and phishing mechanisms and mapped each to the control
  it was written to defeat.
- Built a 40-node case graph in Gephi with evidence and confidence on every edge.

Result: account takeover confirmed with timing to the second; source of the leaked invoice
assessed as [your conclusion and confidence]; related infrastructure listed for blocking.

What I would do differently: [one honest paragraph]
```

Replace the bracketed parts and the numbers with your own. The "what I would do differently" paragraph is the part interviewers ask about most, so make it specific. Your Day 89 scoring log is where to find it.

The top-level README should say in three or four sentences who you are, which roles you are aiming for, and which folder to open first for each role.

### Part 2: write the resume

One page. Sections: header with a link to the portfolio, a two-line summary naming the role you want, experience, projects (the portfolio), certifications if any, and relevant skills. Education goes last unless you are a recent graduate.

Write project bullets as action, tool and result, with a link. Before and after:

> Before: "Completed a 90-day cyber investigation program covering OSINT, CTI, forensics and fraud."
> After: "Investigated a synthetic business email compromise end to end: merged mail gateway, mailbox audit and proxy logs into a UTC timeline (Timesketch), attributed 17 sign-in sessions, and delivered a report with probability-scaled judgments and a 40-node evidence graph (Gephi). [link]"

> Before: "Experienced with Maltego and threat intelligence."
> After: "Pivoted from a phishing domain through passive DNS, certificate transparency and page-resource hashes to a second campaign sharing a phishing kit; documented and rejected three false links from shared hosting and a public website template. [link]"

Keep two or three versions of the resume, each leading with different projects:

| Target role | Lead with | Words from postings to use where true |
|---|---|---|
| SOC analyst | Day 58 and Day 86 timelines, session attribution | triage, escalation, SIEM, log analysis, incident timeline |
| CTI analyst | Day 40 and Day 84 pivot graphs, ATT&CK layers, the report's key judgments | infrastructure pivoting, ATT&CK, intelligence requirements, estimative language |
| OSINT analyst | Day 22 graph and map, recon logs, rules of engagement | collection planning, source evaluation, legal and ethical limits |
| Digital forensics examiner | Day 83 evidence register, Day 86 timeline, hash verification | chain of custody, timeline analysis, evidence integrity |
| Fraud investigator | Day 68 fraud-ring graph, Day 87 triage and swimlane, pattern card | scheme typology, BEC, payment diversion, controls |

### Part 3: know the pathways

Entry roles and the employers that hire for them:

| Role | Typical employers | Certifications that often appear in postings |
|---|---|---|
| SOC analyst | Managed security and MDR providers, in-house security teams at banks, retailers, hospitals and universities | CompTIA Security+, CySA+, GCIH |
| CTI analyst | Threat intelligence vendors, large banks and enterprises, national CERTs and CSIRTs | GCTI |
| OSINT analyst | Due-diligence and risk consultancies, corporate security teams, journalism and human-rights research groups, government | GOSI |
| Digital forensics examiner | Incident response and breach-response firms (many work through cyber insurers' panels), e-discovery providers, law enforcement civilian examiner roles | GCFE, GCFA |
| Fraud investigator | Bank and payments fraud teams, insurers' special investigation units, marketplace and platform trust and safety teams | CFE, CAMS |

Many employers use certifications as a screening filter, and they say little about whether you can do the work. If postings you want keep listing one, plan for it. If they do not, your portfolio is a better use of the time.

Common moves after the first role: SOC analyst to incident responder or CTI analyst; OSINT analyst to CTI or fraud intelligence; fraud investigator to financial crime intelligence or AML; forensics examiner to incident response lead. The CyberSeek pathway tool shows more.

### Part 4: build the target tracker

Find ten real postings across at least two of the role families above, using LinkedIn, Indeed, the government portals, and the careers pages of employers from Part 3. For each, record in `career/targets.ods`:

| Column | What goes in it |
|---|---|
| Employer, role, link, date found | The basics |
| Required skills | Copied from the posting |
| Portfolio item that shows each skill | Folder name, or "gap" |
| Required certification | As listed, or "none" |
| Resume version to send | From Part 2 |
| Status | Not applied, applied, interview, closed |

When all ten rows are filled, count the gaps. Write down the three that appear most often and a concrete plan for each: a lab you will build, a certification with a target date, or a community you will join (a local BSides conference, an OWASP chapter, a Trace Labs event). Put the plan at the top of the sheet.

## Checkpoint

1. A reviewer who opens your portfolio README can reach the capstone graph in two clicks, and every synthetic artifact is labelled as such.
2. Every item passed the five-point publishing check, including `exiftool` on images and PDFs.
3. Every project bullet on your resume links to a portfolio folder, and each names a tool and a result.
4. Your tracker has ten real postings across at least two role families, every required skill is mapped to a portfolio item or marked as a gap, and the top three gaps have dated plans.
5. Look back at your Day 1 board. Every day you marked "Artifact built" should now have that artifact either in the portfolio or deliberately left out for a reason you can state, such as a public-source lab that named a person.
