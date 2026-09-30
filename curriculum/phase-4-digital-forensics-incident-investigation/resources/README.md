# Phase 4 lab data (synthetic)

Every file under this folder is synthetic training data. The organization (Example Fabrication Co.), its hosts, accounts, files and events are invented. Public IP addresses come only from the RFC 5737 documentation ranges (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24), and internal addresses are RFC 1918. Nothing here describes a real breach, company or person. Do not load any of it into a production SIEM without the `labels.synthetic` field intact.

## Case LAB-P4 in one paragraph

On the night of 13 to 14 March 2026 (UTC), someone at 203.0.113.45 ran an SSH password spray against the bastion host `bastion01` (10.10.20.5) and logged in as `svc_backup`. The same account then reached the file server `fs01` (10.10.30.17), where the document portal logged a bulk export of 412 finance files, and the firewall logged about 48 MB leaving `fs01` for 198.51.100.23. Separately, the finance workstation `WS-FIN-07` (10.10.40.57) shows an unfamiliar process talking to the same 198.51.100.23 address. Days 49 to 64 work this case from evidence intake to the final report. How the attacker got the `svc_backup` password is not shown by any file here, and your report should say so.

## Files

| Path | What it is | Used on |
|---|---|---|
| `chain-of-custody-form.md` | Blank chain-of-custody form | 49, 50, 64 |
| `case-lab-p4/disk/make-evid-004.sh` | Builds a 16 MiB FAT16 USB image with one deleted file | 50, 51 |
| `case-lab-p4/filesystem/ws-fin-07-mft-excerpt.csv` | MFTECmd-style excerpt for WS-FIN-07 | 52 |
| `case-lab-p4/memory/windows.*.txt` | Volatility 3 style plugin output for WS-FIN-07 (no image behind it) | 53, 54 |
| `case-lab-p4/windows/ws-fin-07-security.csv` | Security log logon events, one week | 55 |
| `case-lab-p4/logs/bastion01-auth.log` | Linux sshd/PAM log, true UTC | 55 to 58 |
| `case-lab-p4/logs/fs01-auth.log` | Linux sshd/sudo log, clock runs 83 s fast | 56 to 58 |
| `case-lab-p4/logs/docportal-app.jsonl` | Document portal app log on fs01, same 83 s skew | 56 to 58 |
| `case-lab-p4/logs/firewall.log` | Firewall log in America/New_York local time with no offset printed | 56 to 60 |
| `case-lab-p4/siem/lab-events.ndjson` | ECS-style export of all of the above, corrected to UTC | 63 |
| `case-lab-p4/generate_synthetic.py` | Regenerates the logs, CSV and NDJSON deterministically | any |

## Instructor key

`INSTRUCTOR-KEY.md` in this folder states the case's built-in traps directly. Do not read it before finishing day 58; working the timing and the loose end out from the evidence is the point of days 49 through 58.

## Still missing

There is no packet capture and no raw memory image in this folder. Days 53, 54, 59 and 60 say where to get a lawful public practice file and what the synthetic text files stand in for.
