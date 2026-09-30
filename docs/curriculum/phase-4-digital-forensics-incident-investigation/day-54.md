# Day 54: Memory forensics, network connections and injected code

Phase 4, digital forensics and incident investigation. Track goal: link processes to the network endpoints they held and to memory regions that look like injected code, and separate real hits from the false positives these plugins are known for.

## Concept

Yesterday's tree tells you what ran. Today's plugins tell you what those processes were doing.

`windows.netscan` scans memory for TCP and UDP endpoint structures and prints local and remote address, state, owning PID and creation time. Because it scans rather than walks a live list, it also finds closed connections whose structures have not been overwritten yet. That is useful (a `CLOSED` entry shows an earlier connection) and a trap (a stale structure can carry a PID that has since been reused by another process). Treat a netscan row as "this process held this endpoint at some point before capture".

`windows.malfind` looks for memory regions that are private (not backed by a file on disk), marked executable, and usually writable too (`PAGE_EXECUTE_READWRITE`). That combination is what classic code injection leaves behind: a process allocates memory, writes code into it, and runs it. If the region starts with `MZ`, a whole PE file was likely written there. Malfind is noisy by design. Just-in-time compilers (.NET, which PowerShell uses, and the JavaScript engines in browsers) legitimately create private executable memory. A hit is a question: what is in this region, and does it fit the process?

Two more plugins answer follow-up questions. `windows.dlllist --pid N` lists modules loaded from disk, so you can see whether `rundll32.exe` actually loaded any DLL. `windows.handles --pid N` lists open files, registry keys, mutexes and other objects, which often shows the file or key a suspicious process was working with.

Volatility 3 moved malfind and several other detection plugins under a `windows.malware.` prefix. In v2.28.2 (the current release as of September 2026) the canonical name is `windows.malware.malfind`; the old `windows.malfind` still runs but is a deprecated alias whose source marks it for removal, so expect it to disappear in a later release. Run `vol -h` and use whatever your installed version lists.

## Resources

- Volatility 3 [plugin reference](https://volatility3.readthedocs.io/en/latest/volatility3.plugins.html).
- *The Art of Memory Forensics* (Ligh, Case, Levy, Walters; Wiley, 2014): chapters on process memory and networking. Written for Volatility 2 but the concepts carry over.
- Microsoft documentation on [memory protection constants](https://learn.microsoft.com/en-us/windows/win32/memory/memory-protection-constants).
- [Gephi](https://gephi.org/) or Graphviz for the graph.

## Practical: netscan and malfind to a process-network graph

Data: [`windows.netscan.txt`](resources/case-lab-p4/memory/windows.netscan.txt) and [`windows.malfind.txt`](resources/case-lab-p4/memory/windows.malfind.txt), synthetic output for WS-FIN-07 (10.10.40.57). Against a real image the commands are:

```bash
vol -f ws-fin-07.mem windows.netscan            > netscan.txt
vol -f ws-fin-07.mem windows.malware.malfind    > malfind.txt
vol -f ws-fin-07.mem -o ./malfind_dump/ windows.malware.malfind --pid 7704 --dump
vol -f ws-fin-07.mem windows.dlllist --pid 7704
vol -f ws-fin-07.mem windows.handles --pid 7488
```

`--dump` writes each flagged region to a file in the `-o` directory so you can hash it and run `strings` on it (day 61). Do that inside an analysis VM.

1. Filter netscan to connections with a remote endpoint and sort by owner.

   ```bash
   N=resources/case-lab-p4/memory/windows.netscan.txt
   awk -F'\t' '$1 ~ /^0x/ && $5!="0.0.0.0" && $5!="*" {print $9" ("$8")", $3":"$4, "->", $5":"$6, $7, $10}' "$N" | sort
   ```

   You should get five rows. Classify each remote address: 192.0.2.30 and 192.0.2.31 are the mail and web services the fictional company uses (treat them as expected); 198.51.100.23 and 203.0.113.80 are not.

2. Note the timing detail on `synchelper.exe` (7488): one `CLOSED` connection to 198.51.100.23:443 created at 05:02:30 and one `ESTABLISHED` at 05:07:31. Five minutes apart. One interval is not a pattern; it is a question to test on day 59 against network data.

3. Record the cross-host link. 198.51.100.23 is also the destination of the roughly 48 MB outbound transfer from `fs01` in `firewall.log` (you will line these up on day 56). That shared address connects two hosts in the case. Write it down as "same remote IP", which is what you observed, and not "same attacker", which you have not shown.

4. Read malfind. Three regions are flagged. Judge each:

   | PID | Process | Protection | First bytes | Your call |
   |---|---|---|---|---|
   | 7704 | rundll32.exe | PAGE_EXECUTE_READWRITE, private | `4d 5a 90 00` (MZ) | ? |
   | 7316 | powershell.exe | PAGE_EXECUTE_READWRITE, private | `49 ba ... 41 ff e3` stubs | ? |
   | 6208 | msedge.exe | PAGE_EXECUTE_READWRITE, private | all zeros | ? |

   Guidance: an MZ header in private RWX memory of a process with no DLL argument is a strong injection indicator. Repeated `mov r10, imm64; jmp r11` stubs (`49 ba` ... `41 ff e3`) padded with `cc` are typical of .NET JIT thunks, which PowerShell produces; weak on its own. An all-zero RWX region in a browser is almost always JIT allocation not yet filled. Write your call and one sentence of reasoning per row.

5. Build the graph. Nodes: processes (boxes), remote IPs (ellipses), malfind regions (diamonds). Edges: process to remote IP labelled `state, created time`; process to region labelled `protection`; and parent-child edges from day 53 for the suspicious chain only. Colour by your call from step 4. A Graphviz start:

   ```dot
   digraph net {
     rankdir=LR;
     p7316 [shape=box, label="powershell.exe (7316)"];
     p7488 [shape=box, label="synchelper.exe (7488)", style=filled, fillcolor="#f4b6b6"];
     p7704 [shape=box, label="rundll32.exe (7704)", style=filled, fillcolor="#f4b6b6"];
     ip23  [shape=ellipse, label="198.51.100.23:443\nalso fs01 egress (firewall.log)"];
     r7704 [shape=diamond, label="0x1c0000 RWX\nMZ header"];
     p7316 -> p7488 -> p7704 [color=gray];
     p7488 -> ip23 [label="ESTABLISHED 05:07:31Z"];
     p7488 -> ip23 [label="CLOSED 05:02:30Z", style=dashed];
     p7704 -> r7704 [label="PAGE_EXECUTE_READWRITE"];
   }
   ```

   Finish it with `svchost.exe` (5124) and 203.0.113.80:8443 (`SYN_SENT`, meaning the connection attempt had not completed), the PowerShell JIT region marked as likely benign, and the Outlook and Edge connections in grey.

Artifact: `ws-fin-07-process-network.png` plus the filled-in malfind judgement table.

## Checkpoint

- The graph has every non-listening netscan row and every malfind region, each with a label taken from the text file.
- Your malfind table calls the Edge region benign or likely benign, and gives a reason for the PowerShell one either way.
- You wrote down what `SYN_SENT` means for 5124 and did not describe it as "connected to".
- You can say what you would run next against a real image to confirm the rundll32 region is a PE file, and where the output goes.

## Note

As on day 53, the memory data is synthetic text and there is no raw image. The `--dump` and `dlllist` steps need a real image, such as one from MemLabs.
