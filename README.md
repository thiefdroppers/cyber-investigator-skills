# Cyber investigator roadmap

A 90-day, hands-on path into cyber investigation: OSINT, threat intelligence, digital forensics, and fraud and scam investigation. A companion agent skill in [`skill/`](skill/SKILL.md) runs the same procedures.

Status: all 90 days are drafted. An accuracy and depth audit is in progress before this is treated as final; see [`curriculum/README.md`](curriculum/README.md) for what that covers.

## Contents
- [What the roadmap teaches](#what-the-roadmap-teaches)
- [Who it is for](#who-it-is-for)
- [Ethics and ground rules](#ethics-and-ground-rules)
- [Start here](#start-here)
- [The roadmap](#the-roadmap)
- [Templates](#templates)
- [Companion skill](#companion-skill)
- [Contributing](#contributing)
- [License](#license)

## What the roadmap teaches
Most security study plans prepare you for an exam. This one prepares you to work a case: a suspicious message, a compromised account, a scam report, or a log file. You collect evidence, record where each piece came from, and write conclusions that still hold when someone asks how you know.

Each phase ends in something you build. On Day 22 you build a link-analysis graph in Maltego Community Edition. On Day 40 you pivot from one known indicator through certificate transparency logs (crt.sh), Shodan or Censys, and urlscan.io to map an actor's infrastructure, then produce a MITRE ATT&CK Navigator heatmap. The capstone (Days 83 to 90) produces a mock case file with a relationship graph, a timeline, and a written report.

## Who it is for
- People aiming for SOC analyst, OSINT analyst, CTI analyst, digital forensics examiner, or fraud investigator roles
- IT and security staff moving into investigative work
- Anyone who wants to recognize and document scams, fraud, and abuse, at work or in their own community

Phase 1 assumes only basic computer literacy.

## Ethics and ground rules
Read this section before starting. Everything in the roadmap is for authorized, defensive, lawful use: securing systems, investigating incidents you are authorized to investigate, researching threats and scam patterns, and protecting people. It does not cover stalking, harassment, doxxing, or targeting a private individual outside a legitimate, authorized engagement.

The rule that runs through every phase is to hunt patterns, not people. Fraud and abuse investigation works by recognizing tactics and indicators that recur across many cases. Building a dossier on one private person out of curiosity is not investigation. [Day 1](curriculum/phase-1-foundations/day-01.md) covers this in depth, including why "I could technically access this" and "am I authorized to" are different questions.

If you are unsure whether something you want to practice is authorized, treat it as unauthorized and use a sanctioned lab, a CTF, or your own accounts.

## Start here
- Day numbers are a guide. Some days are a 45-minute read and others are a multi-hour lab.
- Fork the repo or copy the roadmap into your own notes, and check off each day as you finish its practical.
- Do the labs. A day counts as done when you have built its artifact, not when you have read its page.
- Every tool the roadmap uses is free or has a no-cost tier that covers the labs: Maltego Community Edition, Gephi, SpiderFoot, Wireshark, Timesketch, and MITRE ATT&CK Navigator.
- Report content errors and propose additions through issues. [CONTRIBUTING.md](CONTRIBUTING.md) has the process.

## The roadmap

| Phase | Days | Core topics | Practical output |
|---|---|---|---|
| 1. Foundations | 1 to 18 | Networking, Linux, security fundamentals, investigator ethics | Topology map of your home or lab network; first pcap captured and read in Wireshark |
| 2. OSINT and digital footprint | 19 to 34 | OSINT cycle, metadata, social media recon, OSINT law | Maltego CE link-analysis graph of a public entity; 5 images geolocated and plotted on a map |
| 3. Cyber threat intelligence | 35 to 48 | MITRE ATT&CK, actor TTPs, IOC enrichment | Infrastructure pivot graph (domain to IP to certificate to related domains); ATT&CK Navigator heatmap for a publicly reported actor |
| 4. Digital forensics and incident investigation | 49 to 64 | Disk and memory forensics, log analysis, network forensics | Incident timeline built from cross-referenced logs in Timesketch; Wireshark IO and conversation graphs from a pcap |
| 5. Fraud, scam, and social-engineering investigation | 65 to 76 | Scam taxonomy, grooming and trafficking indicators, AI-enabled fraud | Fraud-ring graph linking shared indicators (phone numbers, payment handles, domains) across separate scam reports |
| 6. Cloud and AI-system investigation | 77 to 82 | Cloud audit logs, IAM abuse, AI and LLM abuse | Cloud IAM access graph; attack-path graph across misconfigured resources |
| 7. Capstone and career | 83 to 90 | One full mock investigation from intake to report | Case graph connecting every entity and piece of evidence, plus the written case report |

Day-by-day status is in [`curriculum/README.md`](curriculum/README.md).

## Templates
[`templates/`](templates/README.md) has the working documents the labs use. The first is the OSINT recon log, used from Day 22 on.

## Companion skill
[`skill/SKILL.md`](skill/SKILL.md) is the roadmap's method written in the packaged agent skill format, for agent frameworks that load skill files. For any other LLM, [`skill/PORTABLE_PROMPT.md`](skill/PORTABLE_PROMPT.md) is a self-contained system prompt with the same content. Both cover the OSINT recon cycle, link-analysis graphs, fraud and scam triage, and report drafting, written as numbered steps so that a weaker model can follow them literally. The authorization rules and the patterns-not-people rule are part of the skill's instructions, and the skill refuses requests that break them.

## Contributing
Corrections, new labs, new days, and translations are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License
Everything in this repository, including the curriculum text, is under the [MIT License](LICENSE).

Maintained by [ThiefDroppers](https://thiefdroppers.com).
