# Curriculum

| Phase | Days | Directory |
|---|---|---|
| 1. Foundations | 01-18 | [`phase-1-foundations/`](phase-1-foundations/) |
| 2. OSINT & Digital Footprint | 19-34 | [`phase-2-osint-digital-footprint/`](phase-2-osint-digital-footprint/) |
| 3. Cyber Threat Intelligence | 35-48 | [`phase-3-cyber-threat-intelligence/`](phase-3-cyber-threat-intelligence/) |
| 4. Digital Forensics & Incident Investigation | 49-64 | [`phase-4-digital-forensics-incident-investigation/`](phase-4-digital-forensics-incident-investigation/) |
| 5. Fraud, Scam & Social-Engineering Investigation | 65-76 | [`phase-5-fraud-social-engineering/`](phase-5-fraud-social-engineering/) |
| 6. Cloud & AI-System Investigation | 77-82 | [`phase-6-cloud-ai-system-investigation/`](phase-6-cloud-ai-system-investigation/) |
| 7. Capstone & Career | 83-90 | [`phase-7-capstone-career/`](phase-7-capstone-career/) (includes the case packet) |

Every day follows [`_template.md`](_template.md): Concept, Resources, Practical (named tool, built artifact), Checkpoint.

## Known open items
- Legal citations, hotline and contact numbers, trafficking statistics, MITRE ATT&CK technique IDs, and cloud-provider CLI syntax were checked against primary or live sources on 2026-09-30; corrections from that check are reflected in the current text. The Action Fraud to Report Fraud rebrand date (Day 76) rests on secondary news sources, since the relevant UK police sites blocked automated access.
- MITRE ATT&CK v19.0 restructured Defense Evasion (split into Stealth and Defense Impairment) and revoked some technique IDs after part of this curriculum was written. On 2026-09-30 every technique ID in `curriculum/` was checked against attack.mitre.org (v19.2): the only revoked IDs found were T1656 (now T1684.001, fixed in Day 15 and the capstone instructor key) and T1070.001 (now T1685.005, cited on Day 35 deliberately as the example of a revoked ID). Re-check on each new ATT&CK release.
- Phase 4's lab data does not yet include a real packet capture or a real memory image; days 53, 54, 59, and 60 currently work from synthetic text output and point learners to public practice images instead.
