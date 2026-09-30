# OSINT recon checklist

The recon cycle from [`SKILL.md`](../SKILL.md) as a checklist you can print. The cycle starts on [Day 19](../../curriculum/phase-2-osint-digital-footprint/day-19.md); [Day 22](../../curriculum/phase-2-osint-digital-footprint/day-22.md) applies it in a Maltego link-analysis lab.  [`templates/osint-recon-log.md`](../../templates/osint-recon-log.md) is the matching log.

## Plan
- [ ] Question written as one specific sentence
- [ ] Authorization or case context confirmed
- [ ] Out-of-scope people, accounts, and systems named

## Collect
- [ ] At least 3 independent source types used (for example WHOIS and DNS, search engines, official records, archived snapshots)
- [ ] Every data point logged with its value, source, and access date and time
- [ ] Historical state checked in the Wayback Machine or a similar archive for anything that looks recently changed

## Process and graph
- [ ] Nodes are concrete entities (domain, IP, certificate, email address, account, organization), never categories
- [ ] Every edge labeled with the relationship that produced it, such as "same registrant email" or "shared TLS certificate"
- [ ] Hubs, clusters, and bridges identified, with the reason each one is connected
- [ ] Shared infrastructure checked before treating a hub as significant (a hosting provider or CDN connects thousands of unrelated sites)

## Analyze
- [ ] Each finding tagged confirmed (2 or more independent sources agree), likely (1 source), or disputed (sources conflict)
- [ ] Contradictions recorded, not dropped

## Report
- [ ] Confidence words match the analysis tags exactly
- [ ] Every claim traces to an entry in the collection log
- [ ] Unverified items labeled as unverified
