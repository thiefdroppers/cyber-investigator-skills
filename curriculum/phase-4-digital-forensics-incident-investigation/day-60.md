# Day 60: Detection rules with Suricata

Phase 4, digital forensics and incident investigation. Track goal: turn what you learned about LAB-P4's traffic into Suricata rules, test each rule against a capture where you know the right answer, and read the alerts from `eve.json`.

## Concept

An investigation produces indicators and behaviours. Writing them as detection rules does two jobs: it lets you sweep other captures and sensors for the same activity (scoping), and it hands the defenders something that fires next time. Suricata is an open-source IDS/IPS and network security monitor that reads live traffic or pcap files, applies rules, and logs alerts and protocol metadata as JSON.

A Suricata rule has a header and options:

```text
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"..."; flow:established,to_server; http.method; content:"POST"; sid:9000001; rev:1;)
|     |    |         |   |  |             |    |
action proto source  port dir destination port options in parentheses, each ending with ;
```

Actions are `alert`, `pass`, `drop` and `reject` (the last two only matter inline). The protocol can be a transport (`tcp`, `udp`, `ip`) or an application protocol Suricata parses (`http`, `dns`, `tls`, `ssh`, `smb` and others), which unlocks protocol keywords. `$HOME_NET` and `$EXTERNAL_NET` are variables set in `suricata.yaml`.

The options you will use most:

| Option | Purpose |
|---|---|
| `msg:"..."` | Alert text; start with a project prefix so your alerts are easy to find |
| `flow:established,to_server` | Only packets in an established session, client to server |
| `http.method; content:"POST";` | Sticky buffer: the `content` match applies to the HTTP method only |
| `http.host`, `http.uri`, `dns.query`, `tls.sni` | Other sticky buffers for common fields |
| `content:"..."; nocase;` | Byte or string match, case-insensitive |
| `flags:S,12;` | TCP SYN set (ignoring the two ECN bits) |
| `threshold: type threshold, track by_src, count 10, seconds 60;` | Alert only when a source hits the rule 10 times in 60 s |
| `sid:9000001; rev:1;` | Unique rule ID (use 9,000,000 and up for local rules) and revision |

Write rules for behaviour where you can, and for single indicators when you must. A rule for "any traffic to 198.51.100.23" stops being useful the day the address changes; a rule for "one internal host sends more than 20 MB to an external address in one HTTPS session" does not.

## Resources

- [Suricata documentation](https://docs.suricata.io/), chapters "Rules" (format, HTTP/DNS/TLS keywords, thresholding) and "Output" (`eve.json`).
- [Emerging Threats Open ruleset](https://rules.emergingthreats.net/) for real-world examples of rule style.
- `jq` manual for reading `eve.json`.

## Practical: Suricata rules tested against your day 59 capture, with an alert table

Install on Debian/Ubuntu: `sudo apt install suricata jq`. Record `suricata -V`.

1. Write `~/lab-p4/work/local.rules`. The first four rules are tested against your own capture, so you know exactly when each should fire. The last two carry LAB-P4's lessons and cannot be tested until a LAB-P4 pcap exists (see Note).

   ```text
   alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"LAB own-capture HTTP POST to example.com"; flow:established,to_server; http.method; content:"POST"; http.host; content:"example.com"; sid:9000001; rev:1;)
   alert dns $HOME_NET any -> any any (msg:"LAB own-capture DNS query for lab NXDOMAIN name"; dns.query; content:"nonexistent-lab-name"; nocase; sid:9000002; rev:1;)
   alert tls $HOME_NET any -> $EXTERNAL_NET any (msg:"LAB own-capture TLS SNI example.org"; tls.sni; content:"example.org"; sid:9000003; rev:1;)
   alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"LAB own-capture repeated GET to example.com"; flow:established,to_server; http.method; content:"GET"; http.host; content:"example.com"; threshold: type threshold, track by_src, count 3, seconds 180; sid:9000004; rev:1;)
   alert tcp $EXTERNAL_NET any -> $HOME_NET 22 (msg:"LAB-P4 SSH connection burst from one source"; flow:to_server; flags:S,12; threshold: type threshold, track by_src, count 20, seconds 300; sid:9000010; rev:1;)
   alert ip $HOME_NET any -> 198.51.100.23 any (msg:"LAB-P4 traffic to case indicator 198.51.100.23"; sid:9000011; rev:1;)
   ```

2. Test the syntax before running.

   ```bash
   sudo suricata -T -c /etc/suricata/suricata.yaml -S ~/lab-p4/work/local.rules -v
   ```

   `-S` loads only this file (the installed ruleset is ignored), which keeps today's alerts to your own rules. Fix any error it reports; the usual causes are a missing `;` or a keyword your version does not support.

3. Run against the capture.

   ```bash
   mkdir -p ~/lab-p4/work/suri-out
   sudo suricata -c /etc/suricata/suricata.yaml -S ~/lab-p4/work/local.rules \
     -r ~/lab-p4/work/own-lab.pcapng -l ~/lab-p4/work/suri-out -k none \
     --set vars.address-groups.HOME_NET="[10.0.0.0/8,172.16.0.0/12,192.168.0.0/16]"
   ```

   `-k none` turns off checksum validation. Captures taken on the same host that sent the traffic often have wrong checksums because the network card computes them after capture; without `-k none` Suricata may ignore those packets and your rules will silently miss.

4. Read the alerts.

   ```bash
   cd ~/lab-p4/work/suri-out
   cat fast.log
   jq -c 'select(.event_type=="alert") | {ts:.timestamp, sid:.alert.signature_id, sig:.alert.signature, src:.src_ip, dst:.dest_ip, dport:.dest_port}' eve.json
   jq -r 'select(.event_type=="alert") | .alert.signature' eve.json | sort | uniq -c
   ```

   Expected: 9000001 once (your POST), 9000002 once (plus possibly once more if your resolver retried), 9000003 once, and 9000004 once your third GET within 180 seconds arrives. 9000010 and 9000011 should not fire on your capture. If an expected rule did not fire, check `jq 'select(.event_type=="http")' eve.json` to see whether Suricata parsed the session at all.

5. Look at the non-alert records too. `eve.json` also logs `dns`, `http`, `tls` and `flow` events. These metadata records are often more useful to an investigator than the alerts:

   ```bash
   jq -c 'select(.event_type=="tls") | {ts:.timestamp, dst:.dest_ip, sni:.tls.sni, version:.tls.version}' eve.json
   jq -c 'select(.event_type=="flow") | {src:.src_ip, dst:.dest_ip, proto:.proto, app:.app_proto, bytes_out:.flow.bytes_toserver, bytes_in:.flow.bytes_toclient}' eve.json | head
   ```

6. Replay the case logic on flow data. Rule 9000010 describes the LAB-P4 spray. Check whether its threshold would have fired, using the firewall log instead of packets: count connections from 203.0.113.45 to port 22 in each 5-minute bucket.

   ```bash
   grep '203.0.113.45' ~/lab-p4/work/EVID-001/firewall.log \
     | awk '{split($2,t,":"); b=$1" "t[1]":"sprintf("%02d", int(t[2]/5)*5); c[b]++} END {for (k in c) print k, c[k]}' | sort
   ```

   The buckets are in the firewall's local time (22:50 local is 02:50 UTC). The three full buckets hold 23 to 27 connections, and the partial first and last buckets hold 20 and 19. A threshold of 20 in 300 seconds would have fired within the first five minutes, but only just; a spray paced slightly slower would stay under it. Write down the threshold you would recommend and what it would cost in false positives from legitimate admins.

Artifact: `local.rules` (six rules, each with a comment line above it saying what it detects and how it was tested), and an alert table: sid, expected to fire (yes/no), fired (yes/no), count, and notes.

## Checkpoint

- `suricata -T` passes on your rules file.
- Your table has a row for every rule, and every "expected yes" rule either fired or has a written reason why not.
- Rules 9000010 and 9000011 are marked "untested on packets" with the date you will test them.
- You can explain why rule 9000011 is weaker than a volume-based rule for the same activity, and sketch that behaviour-based rule in words.

## Note

A synthetic LAB-P4 pcap is still needed to test rules 9000010 and 9000011 on packets. It is not in `resources/`. The flow-log check in step 6 is the substitute until then.
