# Day 32: Investigator OPSEC: VPN, Tor, isolation, and leak testing

Phase: 2. OSINT and digital footprint · Track goal: Measure what your browser and network reveal about you under four configurations, choose the right one for a given task, and learn the everyday mistakes that expose investigators.

## Concept
Every request you make leaves traces on the other side: your IP address and the network it belongs to, your browser's fingerprint (user agent, screen size, fonts, canvas and WebGL rendering, time zone, language), and behavioral signals such as the page you came from and the time of day you work. A scam operator who runs their own website sees all of it in their server logs. If an investigation site suddenly shows visits from your employer's network during business hours, you have told the subject they are being looked at.

Each common tool hides some of these traces and hands trust to a new party.

A VPN hides your IP from the site and hides your traffic from your local network, and replaces them with the VPN provider, who sees both. VPN exit IPs are listed in commercial databases, so sophisticated sites know a VPN is in use. It does nothing about browser fingerprint or cookies.

Tor Browser routes traffic through three relays so no single relay knows both who you are and what you visit, and it tries to make every Tor Browser user's fingerprint look the same. Exit IPs are public, so many sites block Tor or add CAPTCHAs, and the use of Tor is itself a signal to a suspicious subject. Logging into any account over Tor ties that session to the account.

Isolation (a separate VM, or at least a separate browser profile) prevents cross-contamination: cookies, logged-in sessions, extensions, and history from your real life never touch the investigation. It does not hide your IP; that is the network layer's job.

The mistakes that expose investigators are usually mundane: clicking a link in a scam email from your work mailbox (tracking pixels and unique links fire), opening a suspect's shortened URL that logs every visitor, uploading evidence to a public scanner whose results anyone can search, a WebRTC leak revealing your real IP through the VPN, or searching a subject's name while logged into your personal search account.

## Resources
- [EFF Cover Your Tracks](https://coveryourtracks.eff.org/) tests tracker blocking and how unique your fingerprint is.
- [BrowserLeaks](https://browserleaks.com/) has separate pages for IP, WebRTC, canvas, WebGL, fonts, and more.
- [Tor Browser](https://www.torproject.org/download/) and [check.torproject.org](https://check.torproject.org/) to confirm you exit through Tor.
- [urlscan.io](https://urlscan.io/) scans a suspicious URL from its own infrastructure; set visibility to Private or Unlisted (Public scans are searchable by anyone, including the subject).

## Practical: Cover Your Tracks, BrowserLeaks, and Tor Browser: an OPSEC leak heatmap
You will test four configurations against the same set of checks and record the results in a grid.

The configurations:

- A: your everyday browser, home or office network.
- B: your `persona-P1` Firefox profile from Day 31, through a VPN.
- C: Tor Browser at its default security level.
- D: the `persona-P1` profile inside a VM (Trace Labs OSINT VM or other), through a VPN.

If you do not have a VPN, run B and D without one and note it; the network columns will show why a VPN or Tor matters.

Step 1: IP and network. In each configuration, open `https://ipleak.net/` or `https://browserleaks.com/ip`. Record the IP, the ISP or ASN shown, and the country. From a terminal on the same machine you can also check:

```bash
curl -s https://ipinfo.io/json
curl -s https://check.torproject.org/api/ip
```

The Tor Project endpoint returns JSON such as `{"IsTor":false,"IP":"..."}` (real format, from a live call). Run it through Tor to see `"IsTor":true`; with Tor Browser running, the local SOCKS port is usually 9150:

```bash
curl -s --socks5-hostname 127.0.0.1:9150 https://check.torproject.org/api/ip
```

`--socks5-hostname` makes DNS resolution happen through Tor too; plain `--socks5` would resolve names locally and leak the lookups.

Step 2: WebRTC. Open `https://browserleaks.com/webrtc`. If any listed address is your real public IP or your home network's local address while the VPN is on, WebRTC is leaking. In Firefox you can disable it in `about:config` by setting `media.peerconnection.enabled` to `false`, at the cost of breaking video calls in that profile.

Step 3: DNS. Run the extended test on `https://www.dnsleaktest.com/`. If the resolvers listed belong to your ISP while the VPN is on, DNS is leaking outside the tunnel.

Step 4: fingerprint. Run Cover Your Tracks ("Test your browser"). Record whether it says your browser has a unique fingerprint, and the bits of identifying information. Then look at `https://browserleaks.com/canvas` and note the canvas signature. Compare configurations: Tor Browser should report the same values as most other Tor users; your everyday browser will usually be unique.

Step 5: time zone and language. BrowserLeaks' JavaScript page shows your browser's time zone and languages. A VPN exit in one country with a browser time zone in another is an inconsistency a careful site operator notices.

Step 6: build the heatmap. In a spreadsheet, configurations as rows, checks as columns. Cell value: 0 = no leak or consistent, 1 = partial, 2 = leaks real identity. Apply a green-to-red color scale. Illustrative:

| Config | Real IP hidden | WebRTC | DNS | Fingerprint unique | TZ matches exit | Logged-in sessions |
|---|---|---|---|---|---|---|
| A everyday | 2 | 2 | 2 | 2 | 0 | 2 |
| B profile + VPN | 0 | 2 | 0 | 2 | 2 | 0 |
| C Tor Browser | 0 | 0 | 0 | 0 | 0 | 0 |
| D VM + profile + VPN | 0 | 0 | 0 | 1 | 0 | 0 |

In this example, config B still leaks the real IP through WebRTC and has a time-zone mismatch, both fixable settings.

Step 7: write a one-page OPSEC standard. For each kind of task (passive browsing of a public org's site, visiting a suspected scam site, viewing a login-only platform with a persona, handling a suspicious link from a victim's email) state which configuration you use and why, plus these standing rules:

- Suspicious links go to urlscan.io with visibility Private, or open in config C or D, never in config A.
- Never click links or load images in a suspect email from your real mailbox; save the `.eml` and analyze it offline.
- Never log into a personal account in configs B, C, or D.
- Hashes, not files, go to public malware scanners unless your policy allows uploads; an upload makes the file available to others.

The artifact is the leak heatmap (PNG or PDF) and the one-page OPSEC standard.

## Checkpoint
Every red or amber cell in the heatmap must have a mitigation written beside it (a setting changed, or a configuration you will not use for that task) and a re-test result. Your OPSEC standard must name a configuration for all four task types. Finally, take the most sensitive task in your standard and explain in two sentences what the subject could still learn about you even in the recommended configuration.
