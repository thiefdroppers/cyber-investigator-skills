# Lab setup resources

Free tools, practice targets and datasets for growing the Day 18 lab past two machines. The curriculum already names Maltego Community Edition, Gephi, SpiderFoot, Wireshark, Timesketch, MITRE ATT&CK Navigator, Autopsy, Volatility 3, MemLabs and the Wireshark sample captures, so none of those are repeated here. Each entry below was checked against the project's own site or repository on 2026-09-30: that it still exists, what it costs, what license it carries, and which release was current. Free tiers and licenses change, so re-check the linked page before you depend on a detail.

Two rules carry over from the rest of the roadmap. Anything deliberately vulnerable runs only on your isolated lab network (the `invlab` internal network from Day 18, or its equivalent), never bridged to your home LAN and never exposed to the internet. Recon tools get pointed at your own domains, a sanctioned target, or the public organizations the Phase 2 days describe, and at no private person.

## Virtualization

### VirtualBox
Day 18 is written for VirtualBox, and it remains the default here. Version 7.2.20 was current on 2026-09-30, with host builds for Windows, Linux, Intel Macs and Apple Silicon Macs. The platform packages are GPL version 3. The separate Extension Pack is under Oracle's Personal Use and Educational License, which excludes commercial use, so leave it off a work laptop unless your employer holds a license. Download from [virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads).

### VMware Workstation Pro and Fusion Pro
Broadcom made both free for commercial, educational and personal use on 11 November 2024, with no license key required. Workstation Player and Fusion Player reached end of sale on 30 April 2024 and are no longer offered for download; the Pro editions replace them. Workstation Pro runs on x86-64 Windows and Linux hosts, and Fusion Pro runs on macOS on both Intel and Apple Silicon. The download sits behind a free Broadcom Support Portal account rather than a public link, and Broadcom no longer sells support contracts for these products, so help comes from the community forums. Useful if you already know VMware, or if a practice image you want ships as a VMware-only appliance. Download instructions: [Broadcom KB 368667](https://knowledge.broadcom.com/external/article/368667/download-and-license-vmware-desktop-hype.html).

### UTM
The option Day 18 mentions for Apple Silicon Macs. UTM uses Apple's Hypervisor framework to run ARM64 guests at near-native speed, and falls back to much slower QEMU emulation for x86-64 guests. That speed gap matters for this curriculum: some practice images below (REMnux, Metasploitable, most VulnHub machines, Windows evaluation images) are x86-64 only, and running them emulated on an M-series Mac is slow. UTM is Apache 2.0 with some GPL and LGPL components. The download from [mac.getutm.app](https://mac.getutm.app/) or [GitHub](https://github.com/utmapp/UTM/releases) is free; the Mac App Store copy is paid, identical in features, and only adds automatic updates. The latest GitHub release on 2026-09-30 was v4.7.5 (January 2026).

### Proxmox VE
Worth considering if you have a spare x86-64 machine (with Intel VT or AMD-V) or a 64-bit Arm board at Armv9-A or newer, and want the lab off your daily laptop entirely. It is an open-source virtualization server that you install from an ISO and manage through a web interface. You do not need a subscription: the no-subscription package repository needs no key, and Proxmox says it is for testing and non-production use, which is what a learning lab is. Proxmox lists 2 GB of RAM as the minimum for the host itself, plus whatever your VMs need. See [proxmox.com](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) and the [package repositories page](https://pve.proxmox.com/wiki/Package_Repositories).

## Practice targets you can legally attack

Every image in this section is built to be compromised. Attach it to your lab's internal network only. Day 18's `inv-target` is a clean Ubuntu server; these give the analyst VM something with real weaknesses to scan, exploit, and then investigate from the logs it leaves behind.

### Metasploitable 2 and Metasploitable3
Rapid7's intentionally vulnerable Linux VM. Metasploitable 2 is still distributed as `metasploitable-linux-2.0.0.zip` from [SourceForge](https://sourceforge.net/projects/metasploitable/files/Metasploitable2/), logs in as `msfadmin`/`msfadmin`, and imports into VirtualBox or VMware. Rapid7's [setup page](https://docs.rapid7.com/metasploit/metasploitable-2/) gives the details. [Metasploitable3](https://github.com/rapid7/metasploitable3) has a BSD-style license and comes in two builds, Ubuntu 14.04 and Windows Server 2008 R2. Prebuilt Vagrant boxes (`rapid7/metasploitable3-ub1404` and `rapid7/metasploitable3-win2k8`, last updated October 2024) are available for VirtualBox and VMware; building your own with Packer needs about 65 GB of free disk and 4.5 GB of RAM. The repository's last commit was February 2025, so treat both as stable old targets rather than current software. Both are x86-64.

### OWASP Juice Shop
A deliberately insecure modern web shop (Node.js, Express, Angular) with a large set of graded hacking challenges covering the OWASP Top Ten. It is an OWASP Flagship project, MIT licensed, and at v20.2.0 on 2026-09-30, with commits landing the day before. It runs as a single container:

```bash
docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```

Binding to `127.0.0.1` keeps it reachable only from the machine it runs on. Run it inside your analyst VM, or on a lab target VM with the port bound to the lab interface, and read its web server logs afterwards the way Day 11 reads nginx logs. Source and documentation: [github.com/juice-shop/juice-shop](https://github.com/juice-shop/juice-shop) and [owasp.org/www-project-juice-shop](https://owasp.org/www-project-juice-shop/).

### DVWA (Damn Vulnerable Web Application)
An older, simpler PHP and MySQL web application with adjustable security levels, which makes it easier than Juice Shop for seeing one vulnerability class at a time. GPL-3.0, actively maintained (last commit September 2026). From a clone of the repository, `docker compose up -d` starts it on `http://localhost:4280`. The maintainers' own warning: "Do not upload it to your hosting provider's public html folder or any Internet facing servers, as they will be compromised." Source: [github.com/digininja/DVWA](https://github.com/digininja/DVWA).

### VulnHub
A library of free, downloadable vulnerable VMs contributed by the community, usually as OVA files for VirtualBox or VMware. The site is still up and downloads still work (a test download on 2026-09-30 returned the full 843 MB image), but the newest machine listed was added on 11 July 2022. Use it as an archive of varied targets, not a current one. Read each machine's page for its expected network setup before attaching it to your lab, and check whether it expects DHCP, since your `invlab` network has none. [vulnhub.com](https://www.vulnhub.com/).

### GOAD (Game of Active Directory)
Orange Cyberdefense's vulnerable Active Directory lab, GPL-3.0 and maintained. It is the most useful target here for Phase 4, because a Windows domain you attack yourself produces real Security log events (logons, failures, Kerberos activity) to compare with the synthetic `ws-fin-07-security.csv` from Day 55. It comes in several sizes: the full GOAD lab (5 VMs, 2 forests, 3 domains), GOAD-Light (3 VMs), and MINILAB (2 VMs, 1 domain), plus SCCM and challenge variants. Providers include VirtualBox, VMware, VMware ESXi, Proxmox, Ludus, AWS and Azure. The Windows VMs use 180-day evaluation images, so the lab expires and has to be rebuilt or licensed. Even MINILAB is much heavier than anything else on this page, so check the documentation's resource notes before starting. The project's warning: "This lab is extremely vulnerable, do not reuse recipe to build your environment and do not deploy this environment on internet without isolation." [github.com/Orange-Cyberdefense/GOAD](https://github.com/Orange-Cyberdefense/GOAD), documentation at [orange-cyberdefense.github.io/GOAD](https://orange-cyberdefense.github.io/GOAD/).

### TryHackMe and Hack The Box (hosted, with free tiers)
These platforms host the vulnerable machines themselves and you reach them over their VPN or an in-browser attack box. They do not replace your own lab, since you cannot capture the target's disk or logs, but their guided rooms are a lawful way to practice the attacker side you will later investigate. The platform's terms are your authorization, and they cover only the machines the platform assigns you.

[TryHackMe's free tier](https://tryhackme.com/pricing) gives free rooms only, limited access to learning paths, and one hour a day of the in-browser AttackBox. Premium was listed at €10.50 a month billed annually.

[Hack The Box Labs](https://help.hackthebox.com/en/articles/7257535-htb-labs-subscriptions) free accounts get 20 active machines, more than 80 active challenges, active Fortresses, unlimited machine resets, and a one-time two-hour Pwnbox trial that does not reset. Retired machines and unlimited Pwnbox need VIP+ ($25 a month or $223 a year). A new PRO plan ($49 a month) was announced to start on 30 September 2026.

## Network simulation

### GNS3
A GPL-3.0 network emulator for building multi-segment topologies: routers, switches, firewalls and ordinary Linux hosts, wired together on a canvas. The release on GitHub (v2.2.61, July 2026) ships Windows and macOS installers and a GNS3 VM for VirtualBox, VMware Workstation, VMware ESXi, Hyper-V and KVM, downloadable without an account. GNS3 does not ship Cisco IOS or other vendor images; its documentation says that for legal reasons you must supply your own. Open-source appliances from its marketplace (Linux hosts, open routers and firewalls) avoid that problem. Use it when you want Day 18's single flat network to become a small routed network with a DMZ, so that Day 9's subnetting and firewall-log reading have a real topology behind them. [github.com/GNS3/gns3-gui/releases](https://github.com/GNS3/gns3-gui/releases), documentation at [docs.gns3.com](https://docs.gns3.com/).

### containerlab
A command-line tool that builds network labs from a YAML topology file (`*.clab.yml`), wiring containers together with virtual links. It was built for containerized network operating systems (Nokia SR Linux, Arista, FRR, SONiC and others), but it wires ordinary Linux containers just as well. That makes it a lightweight way to stand up a few hosts plus a capture node without full VMs, and the topology file doubles as documentation of the lab. BSD-3-Clause, v0.79.0 released August 2026. It runs natively on Linux (amd64 and arm64), on Intel and Apple Silicon Macs, and on Windows through WSL. [containerlab.dev](https://containerlab.dev/), install notes at [containerlab.dev/install](https://containerlab.dev/install/).

## Forensics practice data

The curriculum README lists an open gap: Phase 4 has no real packet capture or memory image. The first four sources below fill it with public data made for teaching.

### Digital Corpora
Research and teaching datasets for digital forensics, hosted free through the AWS Open Data Sponsorship Program (bucket `s3://digitalcorpora/`). The site states that its "disk images, memory dumps, and network packet captures ... are freely available and may be used without prior authorization or IRB approval." The best fit for this curriculum is the 2009 M57-Patents scenario: a fictional four-week company history in which every computer's disk and memory was imaged every day, and the network traffic in and out was captured, with detective reports and a warrant affidavit as case documents. It can be worked as a disk exercise or a network exercise, which lines up with Days 50 to 60. Other scenarios include the 2008 Nitroba University harassment case and 2019 Narcos, plus Android and iOS phone images. Instructor answer keys are restricted to faculty and government trainers. [digitalcorpora.org](https://digitalcorpora.org/), M57 files at [the M57-Patents page](https://digitalcorpora.org/corpora/scenarios/m57-patents-scenario/).

### NIST CFReDS
NIST's Computer Forensic Reference Data Sets: documented images of simulated evidence, some produced by NIST's tool-testing program and some contributed by other organizations, free to download. NIST describes them as usable for validating forensic tools and for training and proficiency testing, so they are a way to check whether your tools and method find what the documentation says is there. Two multi-skill cases suit Phase 4: the [Hacking Case](https://cfreds.nist.gov/all/NIST/HackingCase) (an abandoned Dell notebook with a wireless card, dated 2004) and the [Data Leakage Case](https://cfreds.nist.gov/all/NIST/DataLeakageCase). NIST's program page was last updated 1 May 2026. The portal is [cfreds.nist.gov](https://cfreds.nist.gov/); an older copy of the original site is at [cfreds-archive.nist.gov](https://cfreds-archive.nist.gov/).

### Ali Hadi's DFIR datasets
A set of free forensic challenges published by Ali Hadi for training use: eleven numbered cases (a compromised web server, policy violations, alternate data streams, anti-forensics and others), a memory forensics case, an unallocated-space malware case, and four Linux cases. Case 1, the web server case, is on the Internet Archive as an E01 disk image (about 3.1 GB) with a separate memory dump, which gives you a matched disk and memory pair to take through Days 50 to 54 on real data. Other cases are hosted on Mega and GitHub. Index at [ashemery.com/dfir.html](https://www.ashemery.com/dfir.html).

### Malware-Traffic-Analysis.net
Brad Duncan's blog of packet captures from real malware infections, with analysis write-ups and self-contained traffic-analysis exercises. Posts were still appearing in September 2026. This is the closest public match to what Days 59 and 60 need: real captures of infection traffic to open in Wireshark and to test Suricata rules against. The site warns that many zip files contain live malware and that some pcaps will be flagged by antivirus, so download and open them only inside your isolated analyst VM, never on a Windows host. Archives are password protected; the scheme is on the [about page](https://www.malware-traffic-analysis.net/about.html). [malware-traffic-analysis.net](https://www.malware-traffic-analysis.net/).

### SIFT Workstation
SANS's free forensic workstation: an Ubuntu-based collection of open-source incident response and forensic tools, already installed. Its build recipes include Plaso, The Sleuth Kit and Volatility 3, the same tools Days 51 to 58 use. It can replace a hand-built analyst VM for Phase 4. The OVA (8.81 GB, updated 24 April 2026) needs a free SANS account to download; without one, install Ubuntu 22.04 and run `sudo cast install teamdfir/sift`, which also works under WSL. The default login is `sansforensics`/`forensics`; change it. [sans.org/tools/sift-workstation](https://www.sans.org/tools/sift-workstation).

### REMnux
A free Linux toolkit for malware analysis, built on Ubuntu 24.04 and distributed as a ready-made virtual appliance (OVA and QCOW2). It goes further into malware than the curriculum does in Day 61's static triage, and it is the safer place to handle Malware-Traffic-Analysis downloads. Its documentation says it is x86-64 only and "won't run on ARM processors such as Apple's M-series chips." [remnux.org](https://remnux.org/), download instructions at [docs.remnux.org](https://docs.remnux.org/install-distro/get-virtual-appliance).

## OSINT tooling

Phase 2 already uses SpiderFoot, Maltego CE, Sherlock and Maigret. These add domain-focused collection and a ready-made workstation.

### theHarvester
A command-line collector that gathers subdomains, hosts, emails and names for a domain from about 60 public sources, which makes it a fast first pass before Day 23's search operators. Many sources need no key, including crt.sh, CertSpotter, the Wayback Machine, urlscan.io and OTX; others (Shodan, Censys, VirusTotal, Hunter and more) need a key. GPL-2.0, release 4.11.1 in June 2026, with commits the day this was checked. It now needs Python 3.14 and `uv` to install. [github.com/laramies/theHarvester](https://github.com/laramies/theHarvester).

### OWASP Amass
OWASP's flagship attack-surface mapping tool: it discovers subdomains and related infrastructure from open sources, and can also run active techniques. The active techniques touch the target's systems directly, so use them only on domains you are authorized to test and keep to passive collection everywhere else. Apache 2.0, v5.1.1 released April 2026, with prebuilt binaries for Linux and macOS (including arm64) and Docker images. [github.com/owasp-amass/amass](https://github.com/owasp-amass/amass).

### Trace Labs OSINT VM
A Kali-based virtual machine, maintained by Trace Labs, with OSINT tools preinstalled. Day 32 names it as one place to run a research persona; it gives that day's advice about separating investigation work from your personal machine a ready-made home. Release 2026.07 (July 2026) ships OVAs for VirtualBox and VMware on x86-64, and the README also describes an ARM64 build for Apple Silicon. You can build it yourself with Docker instead. GPL-3.0. The default login is `osint`/`osint`; change it on first boot. [github.com/tracelabs/tlosint-vm](https://github.com/tracelabs/tlosint-vm).

### Bellingcat's Online Investigation Toolkit
Bellingcat's catalogue of open-source research tools, maintained by Bellingcat staff and volunteers, organized in twelve categories (maps and satellites, geolocation, image and video, social media, websites, companies and finance, archiving and others). Bellingcat says most listed tools can be used for free, but entries are not consistently marked free or paid, so check before you plan around one. [bellingcat.gitbook.io/toolkit](https://bellingcat.gitbook.io/toolkit).

### OSINT Framework
A long-running clickable tree of OSINT resources grouped by what you are looking up. Its legend marks tools that run locally (T), Google dorks (D), sites that require registration (R), and URLs you edit by hand (M). The site says some resources charge for fuller data. It is a link directory, so check anything you pick from it for the same currency and cost questions this page answers. [osintframework.com](https://osintframework.com/).

## Threat intelligence

### MISP
Days 37 and 44 already read MISP's galaxy data and describe it as the platform sharing communities run. Running your own instance lets you practice the other half: importing the STIX bundle you write on Day 43, tagging events with taxonomies such as TLP, and watching MISP's correlation engine link matching indicators across events. The README lists STIX 2 import and export; check how your version handles a 2.1 bundle. AGPL, v2.5.48 released 29 September 2026. The project recommends Ubuntu 24.04 with its install script, or the maintained Docker images at [github.com/MISP/misp-docker](https://github.com/MISP/misp-docker). A single VM on your lab network, reachable only from the analyst VM, is enough. [misp-project.org/download](https://www.misp-project.org/download/).

### OpenCTI
Filigran's threat intelligence platform. It stores knowledge in a schema based on STIX 2, infers new relations from existing ones, and imports and exports STIX 2 bundles, so it is a larger, persistent version of the relationship graph Day 40 draws by hand. It also integrates with MISP and MITRE ATT&CK. The Community Edition is Apache 2.0; an Enterprise Edition with extra features is under a separate license. Deploy with the Docker helpers at [github.com/OpenCTI-Platform/docker](https://github.com/OpenCTI-Platform/docker). The documentation sets an 8 GB default memory limit for the platform process, and Redis can use about 8 GB as well, so this needs a well-provisioned host or a Proxmox box rather than a laptop VM. Release 7.260930.0 was published on 30 September 2026. [github.com/OpenCTI-Platform/opencti](https://github.com/OpenCTI-Platform/opencti).

### Yeti
A forensics intelligence platform meant to connect CTI and DFIR work. It answers "where have I seen this artifact before?" and lets you bulk-search observables. That makes it a bridge between Phase 3's indicators and Phase 4's timelines. Apache 2.0, release 2.11.0 in September 2026. [yeti-platform.io](https://yeti-platform.io/), source at [github.com/yeti-platform/yeti](https://github.com/yeti-platform/yeti).

### IntelOwl
A self-hosted enrichment service that runs one observable (IP, domain, URL, hash or file) through many analyzers in a single API call or from its web interface. Some analyzers query external services such as VirusTotal and AbuseIPDB, and others run local tools such as YARA. Connectors push results on to MISP or OpenCTI. It automates the manual lookups Day 39 teaches, which is worth doing only after you have done them by hand and know what each source's answer does and does not mean. AGPL-3.0, v6.8.0 released August 2026. [github.com/intelowlproject/IntelOwl](https://github.com/intelowlproject/IntelOwl).

### LevelBlue Open Threat Exchange (OTX)
The community threat-sharing service formerly branded AlienVault OTX, now run by LevelBlue. Users publish "pulses" (collections of indicators with context), and a free account gives you an API key for the DirectConnect API. On 2026-09-30 a single-indicator lookup against the API returned data without a key, while pulse subscriptions required one. Add it to Day 39's enrichment step as another source to read as context, not as a verdict. [otx.alienvault.com](https://otx.alienvault.com/).

## Cloud practice environments

Phase 6 works from synthetic Blue Harbor logs. These two let you see the same kinds of events come from a real cloud account.

### flAWS and flAWS 2
Scott Piper's free AWS security challenges. Everything runs out of a single AWS account of his, so you play from a browser and the AWS CLI without deploying anything of your own. flAWS covers common S3, IAM and EC2 misconfigurations level by level. flAWS 2 adds a Defender path in which you act as incident responder and work through the logs of a previous successful attack on the same application, which is Days 77 and 78's task on real CloudTrail data. Both sites are served over plain HTTP. [flaws.cloud](http://flaws.cloud/) and [flaws2.cloud](http://flaws2.cloud/).

### CloudGoat
Rhino Security Labs' "vulnerable by design" scenarios, deployed into your own AWS or Azure account (AWS has far more scenarios). BSD-3-Clause, v2.5.0 released March 2026, installed with `pipx install cloudgoat`. It creates real cloud resources, so you pay the provider's normal rates while a scenario is up, and you must run the `destroy` command when you finish. The project's warnings: "DO NOT deploy CloudGoat in a production environment or alongside any sensitive resources," and it can only remove resources it created itself, so delete anything you made by hand first. Use a dedicated sandbox account with a budget alert, which is also the setup Blue Harbor's case begins with. [github.com/RhinoSecurityLabs/cloudgoat](https://github.com/RhinoSecurityLabs/cloudgoat).
