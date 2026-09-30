# Day 13: Bash scripting to automate one recon step

Phase: 1. Foundations · Track goal: Turn a lookup you have been typing by hand into a script that collects the same data the same way every time, stamps it with UTC time, hashes it, and shows what changed between runs.

## Concept
Investigators script for consistency more than for speed. A lookup typed by hand on Monday and again on Thursday will differ in small ways: a record type forgotten, a different resolver, the time not written down. A script makes every collection identical, so when two results differ, the difference is in the world and not in how you collected it. A script is also documentation. Handing a colleague `dns-snapshot.sh` and its output tells them exactly how the data was produced.

A few bash habits make scripts trustworthy enough for evidence work:

- Start with `set -euo pipefail`. `-e` stops the script at the first failed command instead of carrying on with bad data, `-u` treats a misspelled variable as an error instead of an empty string, and `pipefail` makes a pipeline fail when any stage fails, not only the last one.
- Quote every variable (`"$domain"`, not `$domain`). Unquoted variables split on spaces and expand wildcards, which turns odd input into odd behaviour.
- Read input files line by line with `while IFS= read -r line`. The `|| [[ -n "$line" ]]` addition catches a final line with no newline at the end, which hand-edited files often have.
- Stamp output with `date -u` in ISO 8601 form, and write to a new timestamped folder on every run so you never overwrite an earlier collection.
- Hash the output at the end, as on Day 2, so the snapshot can be verified later.
- Keep a machine-comparable copy of the output with volatile fields removed. DNS TTLs count down continuously, so two snapshots taken a minute apart always differ in TTL; comparing only domain, type, and value shows real changes.

Scripting also multiplies whatever the script does. Point it only at domains you are authorized to monitor (your own, a client's under a written scope, or public organizations for practice), keep request rates low, and never loop an active tool against third-party systems. DNS lookups through a public resolver are lightweight, which makes them a good first automation target.

## Resources
- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html), sections 3.2 (pipelines) and 4.3.1 (the `set` builtin).
- [ShellCheck](https://www.shellcheck.net/): paste a script in the browser or install it locally; it catches quoting bugs and other common mistakes.
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html).
- [BashFAQ/001: How can I read a file line by line?](https://mywiki.wooledge.org/BashFAQ/001)

## Practical: bash and dig, producing a DNS snapshot tool, two dated snapshots, and a change report

### Step 1: write the domain list
In `~/lab/day13/`, create `domains.txt`. Use the public organizations from Days 5 to 8, plus `example.com`:
```
wikipedia.org
example.com   # IANA reserved example domain
```

### Step 2: write the script
Save as `~/lab/day13/dns-snapshot.sh`:
```bash
#!/usr/bin/env bash
# dns-snapshot.sh: record the public DNS state of domains you are authorized to monitor.
# Usage: ./dns-snapshot.sh domains.txt [resolver]
set -euo pipefail

infile="${1:?usage: $0 domains.txt [resolver]}"
resolver="${2:-1.1.1.1}"
run_ts="$(date -u +%Y%m%dT%H%M%SZ)"
outdir="snapshots/${run_ts}"
mkdir -p "$outdir"
csv="${outdir}/dns.csv"
stable="${outdir}/dns.stable.txt"

hash256() {
  if command -v sha256sum >/dev/null 2>&1; then sha256sum "$@"; else shasum -a 256 "$@"; fi
}

echo "collected_utc,domain,rtype,ttl,value,resolver" > "$csv"
: > "${stable}.tmp"

while IFS= read -r line || [[ -n "$line" ]]; do
  domain="${line%%#*}"                          # drop comments
  domain="$(printf '%s' "$domain" | tr -d '[:space:]')"
  [[ -z "$domain" ]] && continue

  for rtype in A AAAA NS MX TXT CAA; do
    now="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    dig @"$resolver" +noall +answer "$domain" "$rtype" \
      | awk -v ts="$now" -v d="$domain" -v rt="$rtype" -v r="$resolver" -v st="${stable}.tmp" '
          $4 == rt {
            val = ""
            for (i = 5; i <= NF; i++) val = val (i > 5 ? " " : "") $i
            print d "\t" rt "\t" val >> st      # plain copy for diffing
            gsub(/"/, "\"\"", val)                 # CSV-escape quotes
            printf "%s,%s,%s,%s,\"%s\",%s\n", ts, d, rt, $2, val, r
          }' >> "$csv"
  done
  sleep 1                                       # stay polite to the resolver
done < "$infile"

# TTLs and timestamps change on every run, so diff on domain + type + value only.
sort -u "${stable}.tmp" > "$stable" && rm -f "${stable}.tmp"

( cd "$outdir" && hash256 dns.csv dns.stable.txt > SHA256SUMS )
echo "wrote $(( $(wc -l < "$csv") - 1 )) records to $csv"
```
How it works, section by section:
- `${1:?usage...}` stops with a usage message if you forget the input file. `${2:-1.1.1.1}` defaults the resolver.
- The `awk` block keeps only answer lines whose type matches the one asked for (`$4 == rt`). A name that is a CNAME returns the CNAME line first, and this filter drops it so a CNAME is not recorded as an A record. It rebuilds the record value from field 5 onward, because TXT and MX values contain spaces.
- The CSV escapes embedded double quotes by doubling them, which is the CSV rule, so TXT records open cleanly in a spreadsheet.
- If `dig` cannot reach the resolver it exits non-zero, and `set -e` with `pipefail` stops the script instead of writing a half-empty snapshot.

Make it executable and check it:
```bash
chmod +x dns-snapshot.sh
shellcheck dns-snapshot.sh     # install with: sudo apt install shellcheck / brew install shellcheck
```

### Step 3: run it and read the output
```bash
./dns-snapshot.sh domains.txt
```
Trimmed output based on test runs in 2026 (your counts and values will differ):
```
wrote 22 records to snapshots/20260930T051836Z/dns.csv
```
```
collected_utc,domain,rtype,ttl,value,resolver
2026-09-30T05:18:36Z,wikipedia.org,A,296,"208.80.154.224",1.1.1.1
2026-09-30T05:18:36Z,wikipedia.org,AAAA,296,"2620:0:861:ed1a::1",1.1.1.1
2026-09-30T05:18:37Z,wikipedia.org,MX,223,"10 mx-in1001.wikimedia.org.",1.1.1.1
2026-09-30T05:18:37Z,wikipedia.org,TXT,600,"""v=spf1 include:_cidrs.wikimedia.org ~all""",1.1.1.1
2026-09-30T05:18:38Z,example.com,MX,241,"0 .",1.1.1.1
2026-09-30T05:18:38Z,example.com,TXT,300,"""v=spf1 -all""",1.1.1.1
```
Verify the snapshot as you would any evidence:
```bash
cd snapshots/<run folder> && sha256sum -c SHA256SUMS && cd -
# macOS: shasum -a 256 -c SHA256SUMS
```

### Step 4: take a second snapshot and compare
Run the script again later (an hour, or the next day), then compare the stable files:
```bash
a=$(ls -d snapshots/* | head -1); b=$(ls -d snapshots/* | tail -1)
diff "$a/dns.stable.txt" "$b/dns.stable.txt" > day13-changes.diff && echo "no changes between $a and $b"
```
`diff` prints nothing and exits 0 when the files match. Lines starting with `<` exist only in the first snapshot and lines starting with `>` only in the second. For a busy CDN-hosted domain you may see A records rotate between runs; for a domain whose NS or MX records change, investigate why.

To see the tool detect a change without waiting, add a third domain to `domains.txt` and run it again. The diff should show only that domain's records as new.

### Step 5: schedule it (optional)
To run daily at 06:00 UTC on a machine that stays on, add this with `crontab -e` (cron uses the machine's local time, so adjust the hour if your system clock is not UTC):
```
0 6 * * * cd "$HOME/lab/day13" && ./dns-snapshot.sh domains.txt >> run.log 2>&1
```

### Step 6: write the change report
Create `day13-change-report.md`:
```markdown
# DNS change report
Domains monitored: (list, with why you are authorized or why they are public practice targets)
Snapshot A: folder, SHA-256 of dns.csv
Snapshot B: folder, SHA-256 of dns.csv
Resolver:

| Domain | Record type | Value in A | Value in B | Change type (added / removed / modified) | Likely cause |
|---|---|---|---|---|---|
```
If nothing changed, say so explicitly and include the third-domain test as the demonstration row.

## Checkpoint
Your artifacts are `dns-snapshot.sh`, at least two snapshot folders, and `day13-change-report.md`. They pass when:
- ShellCheck reports no warnings, or you can explain each remaining one.
- Each snapshot folder holds `dns.csv`, `dns.stable.txt`, and `SHA256SUMS`, and `sha256sum -c SHA256SUMS` passes in both.
- The change report cites both snapshot hashes and lists every line from `day13-changes.diff`, or states that it was empty and shows the third-domain test.
- You can explain what `set -euo pipefail` would do if the resolver were unreachable halfway through, and why the script diffs `dns.stable.txt` instead of `dns.csv`.
