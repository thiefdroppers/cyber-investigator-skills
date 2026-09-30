#!/usr/bin/env python3
"""Generate the SYNTHETIC log set for Phase 4 case LAB-P4.

Everything this script writes is invented training data. The organization
("Example Fabrication Co."), hosts, accounts and events are fictional. Public
IPs come only from the documentation ranges in RFC 5737 (192.0.2.0/24,
198.51.100.0/24, 203.0.113.0/24); internal IPs are RFC 1918.

Deliberate traps for learners (documented in ../README.md):
  * firewall.log is written in America/New_York local time (EDT, UTC-4 on
    2026-03-14), with no offset in the line.
  * fs01's clock runs 83 seconds fast, so fs01-auth.log and
    docportal-app.jsonl are 83 s ahead of true UTC.

Run:  python3 generate_synthetic.py   (writes into this directory)
The output is deterministic (fixed random seed).
"""
import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

random.seed(4049)
HERE = Path(__file__).resolve().parent
UTC = timezone.utc
EDT = timezone(timedelta(hours=-4))
FS01_SKEW = timedelta(seconds=83)

ATTACKER = "203.0.113.45"
EXFIL_DEST = "198.51.100.23"
BASTION = "10.10.20.5"
FS01 = "10.10.30.17"
WS = "10.10.40.57"


def t(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)


def syslog_ts(dt):
    # classic syslog: no year, no zone
    return dt.strftime("%b %d %H:%M:%S").replace(" 0", "  ", 1) if dt.day < 10 else dt.strftime("%b %d %H:%M:%S")


# ---------------------------------------------------------------- bastion01
bastion = []
sshd_pid = 21800
# normal admin activity the previous afternoon
for ts, user, ip, port in [
    ("2026-03-13 14:02:11", "ops.admin", "10.10.50.12", 51544),
    ("2026-03-13 16:47:39", "ops.admin", "10.10.50.12", 52010),
]:
    sshd_pid += 7
    dt = t(ts)
    bastion.append((dt, f"bastion01 sshd[{sshd_pid}]: Accepted publickey for {user} from {ip} port {port} ssh2: ED25519 SHA256:q8m1Xx0lab0synthetic0key0fingerprint0AAAA"))
    bastion.append((dt + timedelta(seconds=1), f"bastion01 sshd[{sshd_pid}]: pam_unix(sshd:session): session opened for user {user}(uid=1001) by (uid=0)"))

# password spray 02:51:03 -> 03:13:40
dt = t("2026-03-14 02:51:03")
users = ["admin", "root", "backup", "oracle", "svc_backup", "test", "ubuntu", "ftpuser"]
port = 49200
while dt < t("2026-03-14 03:13:41"):
    for u in users:
        sshd_pid += 1
        port += random.randint(1, 9)
        valid = u in ("root", "svc_backup")
        if valid:
            msg = f"bastion01 sshd[{sshd_pid}]: Failed password for {u} from {ATTACKER} port {port} ssh2"
        else:
            msg = f"bastion01 sshd[{sshd_pid}]: Failed password for invalid user {u} from {ATTACKER} port {port} ssh2"
        bastion.append((dt, msg))
        dt += timedelta(seconds=random.randint(9, 15))
        if dt >= t("2026-03-14 03:13:41"):
            break

success = t("2026-03-14 03:14:07")
sshd_pid += 1
bastion.append((success, f"bastion01 sshd[{sshd_pid}]: Accepted password for svc_backup from {ATTACKER} port 50122 ssh2"))
bastion.append((success + timedelta(seconds=1), f"bastion01 sshd[{sshd_pid}]: pam_unix(sshd:session): session opened for user svc_backup(uid=1107) by (uid=0)"))
bastion.append((success + timedelta(seconds=1), f"bastion01 systemd-logind[642]: New session 318 of user svc_backup."))
bastion.append((t("2026-03-14 03:52:44"), f"bastion01 sshd[{sshd_pid}]: pam_unix(sshd:session): session closed for user svc_backup"))
bastion.sort(key=lambda x: x[0])
with open(HERE / "logs/bastion01-auth.log", "w") as f:
    for dt, msg in bastion:
        f.write(f"{syslog_ts(dt)} {msg}\n")

# ---------------------------------------------------------------- fs01 (clock +83 s)
fs = []
lat = t("2026-03-14 03:19:22")  # true UTC of the lateral SSH
fs.append((t("2026-03-13 09:15:02"), "fs01 sshd[1188]: Accepted publickey for ops.admin from 10.10.50.12 port 50912 ssh2: ED25519 SHA256:q8m1Xx0lab0synthetic0key0fingerprint0AAAA"))
fs.append((lat, "fs01 sshd[30411]: Accepted publickey for svc_backup from 10.10.20.5 port 41766 ssh2: RSA SHA256:Zb7synthetic0lab0svcbackup0key0BBBBBBBBBB"))
fs.append((lat + timedelta(seconds=1), "fs01 sshd[30411]: pam_unix(sshd:session): session opened for user svc_backup(uid=1107) by (uid=0)"))
fs.append((t("2026-03-14 03:31:40"), "fs01 sudo[30502]: svc_backup : TTY=pts/1 ; PWD=/home/svc_backup ; USER=root ; COMMAND=/usr/bin/tar -czf /var/tmp/.q1.tgz /srv/docportal/finance/2026-Q1"))
fs.append((t("2026-03-14 03:31:40"), "fs01 sudo[30502]: pam_unix(sudo:session): session opened for user root(uid=0) by svc_backup(uid=1107)"))
fs.append((t("2026-03-14 03:33:05"), "fs01 sudo[30502]: pam_unix(sudo:session): session closed for user root"))
fs.append((t("2026-03-14 03:49:58"), "fs01 sshd[30411]: pam_unix(sshd:session): session closed for user svc_backup"))
fs.sort(key=lambda x: x[0])
with open(HERE / "logs/fs01-auth.log", "w") as f:
    for dt, msg in fs:
        f.write(f"{syslog_ts(dt + FS01_SKEW)} {msg}\n")

# ---------------------------------------------------------------- docportal (JSON lines, fs01 clock)
app = []
for i in range(14):
    d = t("2026-03-13 13:00:00") + timedelta(minutes=random.randint(0, 240))
    app.append({"ts": d, "level": "INFO", "event": "document.view", "user": random.choice(["acct.clerk01", "acct.lead02", "fin.mgr01"]), "src_ip": random.choice(["10.10.40.57", "10.10.40.61", "10.10.40.63"]), "path": f"/finance/2026-Q1/inv-{random.randint(1000, 1999)}.pdf", "count": 1})
app.append({"ts": t("2026-03-14 03:23:10"), "level": "INFO", "event": "auth.login", "user": "svc_backup", "src_ip": "127.0.0.1", "method": "local-token", "count": 1})
app.append({"ts": t("2026-03-14 03:23:48"), "level": "WARN", "event": "document.bulk_export", "user": "svc_backup", "src_ip": "127.0.0.1", "path": "/finance/2026-Q1", "count": 412, "bytes": 48006112})
app.append({"ts": t("2026-03-14 03:24:02"), "level": "INFO", "event": "export.complete", "user": "svc_backup", "path": "/srv/docportal/finance/2026-Q1", "count": 412})
app.sort(key=lambda r: r["ts"])
with open(HERE / "logs/docportal-app.jsonl", "w") as f:
    for r in app:
        r = dict(r)
        r["ts"] = (r["ts"] + FS01_SKEW).strftime("%Y-%m-%dT%H:%M:%SZ")
        f.write(json.dumps(r) + "\n")

# ---------------------------------------------------------------- firewall (local EDT, no offset printed)
fw = []
for dt, msg in bastion:
    if ATTACKER in msg and ("Failed" in msg or "Accepted" in msg):
        p = int(msg.split(" port ")[1].split()[0])
        fw.append((dt - timedelta(seconds=1), f"ACCEPT TCP {ATTACKER}:{p} -> {BASTION}:22 rule=allow-ssh-bastion bytes=4120"))
fw.append((lat - timedelta(seconds=1), f"ACCEPT TCP {BASTION}:41766 -> {FS01}:22 rule=allow-ssh-internal bytes=18844"))
fw.append((t("2026-03-14 03:41:02"), f"ACCEPT TCP {FS01}:39514 -> {EXFIL_DEST}:443 rule=allow-https-out bytes=48213904"))
fw.append((t("2026-03-14 03:41:00"), f"ACCEPT UDP {FS01}:53422 -> 10.10.0.2:53 rule=allow-dns-internal bytes=92"))
for i in range(30):
    d = t("2026-03-13 20:00:00") + timedelta(minutes=random.randint(0, 480))
    fw.append((d, f"ACCEPT TCP {random.choice(['10.10.40.57','10.10.40.61','10.10.50.12'])}:{random.randint(40000,60000)} -> 192.0.2.{random.randint(10,40)}:443 rule=allow-https-out bytes={random.randint(2000,90000)}"))
for i in range(6):
    d = t("2026-03-14 01:00:00") + timedelta(minutes=random.randint(0, 170))
    fw.append((d, f"DROP TCP 198.51.100.{random.randint(60,90)}:{random.randint(40000,60000)} -> {BASTION}:3389 rule=default-deny bytes=60"))
fw.sort(key=lambda x: x[0])
with open(HERE / "logs/firewall.log", "w") as f:
    for dt, msg in fw:
        f.write(f"{dt.astimezone(EDT).strftime('%Y-%m-%d %H:%M:%S')} fw01 {msg}\n")

# ---------------------------------------------------------------- WS-FIN-07 Security events (CSV, UTC)
rows = []
start = t("2026-03-09 00:00:00")
for day in range(6):  # Mon 9 -> Sat 14
    base = start + timedelta(days=day)
    if base.weekday() < 5:
        for user in ["acct.clerk01", "acct.clerk01", "acct.clerk01", "acct.lead02"]:
            for _ in range(random.randint(3, 6)):
                d = base + timedelta(hours=random.randint(13, 21), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
                rows.append((d, 4624, user, random.choice([2, 7, 11]), "-" , "WS-FIN-07"))
    for _ in range(2):
        d = base + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        rows.append((d, 4624, "SYSTEM", 5, "-", "WS-FIN-07"))
    if base.weekday() < 5:
        d = base + timedelta(hours=random.randint(14, 20), minutes=random.randint(0, 59))
        rows.append((d, 4625, "acct.clerk01", 2, "-", "WS-FIN-07"))
# anomalies on the night of 13 -> 14
for i in range(23):
    d = t("2026-03-14 02:10:00") + timedelta(seconds=i * 17)
    rows.append((d, 4625, random.choice(["administrator", "acct.clerk01", "svc_backup"]), 3, BASTION, "-"))
rows.append((t("2026-03-14 03:27:41"), 4624, "svc_backup", 3, FS01, "-"))
rows.append((t("2026-03-14 03:27:41"), 4672, "svc_backup", "", "", ""))
rows.sort(key=lambda r: r[0])
with open(HERE / "windows/ws-fin-07-security.csv", "w") as f:
    f.write("TimeCreatedUtc,EventID,TargetUserName,LogonType,IpAddress,WorkstationName\n")
    for d, eid, user, lt, ip, wn in rows:
        f.write(f"{d.strftime('%Y-%m-%dT%H:%M:%SZ')},{eid},{user},{lt},{ip},{wn}\n")

# ---------------------------------------------------------------- SIEM export (ECS-style NDJSON, all true UTC)
ecs = []
for dt, msg in bastion:
    if "Failed password" in msg or "Accepted" in msg:
        user = msg.split(" for ")[1].split(" from ")[0].replace("invalid user ", "")
        ip = msg.split(" from ")[1].split()[0]
        ecs.append({"@timestamp": dt, "host.name": "bastion01", "event.dataset": "system.auth", "event.category": "authentication",
                    "event.outcome": "success" if "Accepted" in msg else "failure", "user.name": user, "source.ip": ip, "message": msg})
for dt, msg in fs:
    if "Accepted" in msg:
        ecs.append({"@timestamp": dt, "host.name": "fs01", "event.dataset": "system.auth", "event.category": "authentication",
                    "event.outcome": "success", "user.name": "svc_backup" if "svc_backup" in msg else "ops.admin",
                    "source.ip": msg.split(" from ")[1].split()[0], "message": msg})
for dt, msg in fw:
    parts = msg.split()
    s_ip, s_port = parts[2].rsplit(":", 1)
    d_ip, d_port = parts[4].rsplit(":", 1)
    ecs.append({"@timestamp": dt, "host.name": "fw01", "event.dataset": "firewall", "event.category": "network",
                "event.action": parts[0].lower(), "network.transport": parts[1].lower(), "source.ip": s_ip,
                "source.port": int(s_port), "destination.ip": d_ip, "destination.port": int(d_port),
                "network.bytes": int(parts[6].split("=")[1]), "rule.name": parts[5].split("=")[1]})
for d, eid, user, lt, ip, wn in rows:
    rec = {"@timestamp": d, "host.name": "WS-FIN-07", "event.dataset": "windows.security", "event.code": str(eid), "user.name": user}
    if eid in (4624, 4625):
        rec.update({"event.category": "authentication", "event.outcome": "success" if eid == 4624 else "failure", "winlog.logon.type": lt})
        if ip and ip != "-":
            rec["source.ip"] = ip
    ecs.append(rec)
ecs.sort(key=lambda r: r["@timestamp"])
with open(HERE / "siem/lab-events.ndjson", "w") as f:
    for r in ecs:
        r = dict(r)
        r["@timestamp"] = r["@timestamp"].strftime("%Y-%m-%dT%H:%M:%S.000Z")
        r["labels.synthetic"] = True
        f.write(json.dumps(r) + "\n")

print("bastion01-auth.log", len(bastion), "| fs01-auth.log", len(fs), "| docportal", len(app),
      "| firewall", len(fw), "| ws-fin-07", len(rows), "| siem", len(ecs))
