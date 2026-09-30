# Pre-collected lookup results

> SYNTHETIC TRAINING MATERIAL. Every domain uses the reserved `.example` name, every IP is an RFC 5737 documentation address, and every AS number is an RFC 5398 documentation ASN. Registrars, hosting companies and carriers named here are fictional.

The client's IT contractor ran these passive lookups on 17 March 2026 between 12:40 and 13:30 UTC, using WHOIS, a passive DNS service, a certificate transparency search, a URL scanning service and a favicon-hash search. In a real case you would run them yourself and log each one. Here, reading a section counts as running that lookup: log it in your collection log with the section number as the source and 17 March 2026 as the access date.

Section numbers (L1 to L9) are for citation in your notes and case graph.

## L1: WHOIS

| Field | castellanhardwood.example | castellan-hardwood.example | cstl-docshare.example | marrowline-docs.example | quennmarsh-accounts.example |
|---|---|---|---|---|---|
| Created | 2004-06-14 | 2026-02-24T21:14:09Z | 2026-02-26T03:40:51Z | 2026-02-19T22:05:33Z | 2026-03-14T02:51:17Z |
| Registrar | Beaconhill Domains | Quillfeather Names | Quillfeather Names | Quillfeather Names | Quillfeather Names |
| Registrant org | Castellan Hardwood Supply Inc. | REDACTED FOR PRIVACY | REDACTED FOR PRIVACY | REDACTED FOR PRIVACY | REDACTED FOR PRIVACY |
| Name servers | ns1/ns2.cedarlinedns.example | ns1/ns2.hollowdns.example | ns1/ns2.hollowdns.example | ns1/ns2.hollowdns.example | ns1/ns2.hollowdns.example |
| Expires | 2027-06-14 | 2027-02-24 | 2027-02-26 | 2027-02-19 | 2027-03-14 |

Context from the registrar and DNS host's own public pages: Quillfeather Names is a low-cost registrar with about 3 million domains under management. Hollowdns is a free DNS hosting service with about 90,000 zones.

## L2: current DNS records (17 March 2026)

```
castellanhardwood.example.          A      192.0.2.140
castellanhardwood.example.          MX     10 mail.castellanhardwood.example.
mail.castellanhardwood.example.     A      198.51.100.180
castellanhardwood.example.          TXT    "v=spf1 ip4:198.51.100.180 -all"
_dmarc.castellanhardwood.example.   TXT    "v=DMARC1; p=quarantine; rua=mailto:dmarc@castellanhardwood.example"

castellan-hardwood.example.         A      203.0.113.47
castellan-hardwood.example.         MX     10 mail.castellan-hardwood.example.
mail.castellan-hardwood.example.    A      203.0.113.47
castellan-hardwood.example.         TXT    "v=spf1 ip4:203.0.113.47 -all"
_dmarc.castellan-hardwood.example.  NXDOMAIN

cstl-docshare.example.              A      203.0.113.88
www.cstl-docshare.example.          CNAME  cstl-docshare.example.

marrowline-docs.example.            A      203.0.113.91
portal.marrowline-docs.example.     A      203.0.113.91
mail.marrowline-docs.example.       NXDOMAIN

quennmarsh-accounts.example.        A      203.0.113.91
```

## L3: passive DNS history

| rrname | Type | rdata | First seen (UTC) | Last seen (UTC) |
|---|---|---|---|---|
| castellanhardwood.example | A | 192.0.2.140 | 2019-04-02 | 2026-03-17 |
| mail.castellanhardwood.example | A | 198.51.100.170 | 2017-08-11 | 2026-01-19 |
| mail.castellanhardwood.example | A | 198.51.100.180 | 2026-01-19 | 2026-03-17 |
| castellan-hardwood.example | A | 203.0.113.47 | 2026-02-25 | 2026-03-17 |
| mail.castellan-hardwood.example | A | 203.0.113.47 | 2026-02-25 | 2026-03-17 |
| cstl-docshare.example | A | 203.0.113.88 | 2026-02-27 | 2026-03-17 |
| marrowline-docs.example | A | 203.0.113.91 | 2026-02-20 | 2026-03-17 |
| portal.marrowline-docs.example | A | 203.0.113.91 | 2026-02-20 | 2026-03-17 |
| mail.marrowline-docs.example | A | 198.51.100.23 | 2026-02-20 | 2026-03-09 |
| quennmarsh-accounts.example | A | 203.0.113.91 | 2026-03-15 | 2026-03-17 |

Reverse lookups on the same service:

| IP | Hostnames seen resolving to it | PTR record |
|---|---|---|
| 198.51.100.23 | mail.marrowline-docs.example (2026-02-20 to 2026-03-09) | vps-23.pinecrate.example |
| 203.0.113.47 | castellan-hardwood.example, mail.castellan-hardwood.example | vps-47.pinecrate.example |
| 203.0.113.91 | marrowline-docs.example, portal.marrowline-docs.example, quennmarsh-accounts.example | none |

## L4: certificate transparency

| Log entry ID | Names on certificate | Issuer | Not before (UTC) |
|---|---|---|---|
| 9048820415 | marrowline-docs.example, portal.marrowline-docs.example | Let's Encrypt | 2026-02-20 01:37 |
| 9048820911 | mail.marrowline-docs.example | Let's Encrypt | 2026-02-20 01:39 |
| 9051182231 | castellan-hardwood.example, www.castellan-hardwood.example, mail.castellan-hardwood.example | Let's Encrypt | 2026-02-25 06:02 |
| 9051497710 | cstl-docshare.example, www.cstl-docshare.example | Let's Encrypt | 2026-02-27 04:11 |
| 9063310054 | quennmarsh-accounts.example | Let's Encrypt | 2026-03-15 00:22 |
| (routine) | castellanhardwood.example, www.castellanhardwood.example | Let's Encrypt | Renewed every 60 to 90 days since 2019; latest 2025-12-30 |

## L5: co-hosting (reverse IP)

| IP | Hosting | Domains currently hosted | Sample |
|---|---|---|---|
| 203.0.113.47 | Pinecrate VPS, single-tenant virtual server | 2 hostnames | See L3 |
| 203.0.113.88 | Pinecrest Shared Hosting, shared web server | 1,412 domains | ferncastle-bakery.example, oakhollow-dental.example, rivermint-yoga.example, tidepost-news.example, cstl-docshare.example, (1,407 more) |
| 203.0.113.91 | Driftwood Cloud VPS, single-tenant virtual server | 3 hostnames | See L3 |

## L6: URL scan results

S1. Scanned by the client's IT contractor, 17 March 2026 13:20 UTC, sandboxed scanner.

```
URL:         https://cstl-docshare.example/view/r?u=b3JyaW52YWxsZXkuZXhhbXBsZQ%3D%3D&t=anBpa2U%3D
Final URL:   (same)            Status: 200        IP: 203.0.113.88
Page title:  Secure Document Viewer
Page text:   "Castellan Hardwood Supply shared a secure document with you.
              Sign in with your work email to view Remittance_Form.pdf"
Resources:   /assets/js/vw-portal.min.js   sha256 9e41c0b7d2a85f3e16c47d09ab3f58e2c1d06b7a94e2f35c8b01d7e6a4c9f218
             /assets/css/vw.css
             /favicon.ico                  mmh3 -1742093313
             https://castellanhardwood.example/img/logo.png   (third-party image load)
Form:        POST /view/auth   fields: email (prefilled "jpike@orrinvalley.example"), password
Notes:       https://cstl-docshare.example/ returns 404. Scanner followed no redirect.
```

S2. From a public scan database. Submitted by an unknown third party on 22 February 2026 09:14 UTC.

```
URL:         https://portal.marrowline-docs.example/view/r?u=[redacted by database]
Status:      200        IP: 203.0.113.91
Page title:  Secure Document Viewer
Page text:   "Marrowline Freight Services shared a secure document with you.
              Sign in with your work email to view Updated_Payment_Instructions.pdf"
Resources:   /assets/js/vw-portal.min.js   sha256 9e41c0b7d2a85f3e16c47d09ab3f58e2c1d06b7a94e2f35c8b01d7e6a4c9f218
             /assets/css/vw.css
             /favicon.ico                  mmh3 -1742093313
             https://marrowlinefreight.example/images/brand.png   (third-party image load)
Form:        POST /view/auth   fields: email, password
```

S3. From a public scan database. Submitted by an unknown third party on 8 October 2025 16:02 UTC.

```
URL:         https://files.brightquay-legal.example/
Status:      200        IP: 192.0.2.201
Page title:  Secure Document Viewer | Brightquay Legal
Resources:   /static/viewer.js             sha256 3b7f0e92c4d15a8e6f20b9c7d41e5a3f8c62d09e1b4a7f35e8d0c6b2a91f4e07
             /favicon.ico                  mmh3 -1742093313
Form:        POST /sso/login
Page footer: "Built on the OpenDocViewer template"
Cert history: certificates for files.brightquay-legal.example continuously since 2021
```

## L7: favicon hash search

| mmh3 hash | Hosts returned |
|---|---|
| -1742093313 | cstl-docshare.example, portal.marrowline-docs.example, files.brightquay-legal.example |
| 884215106 | castellanhardwood.example, castellan-hardwood.example |

## L8: IP enrichment

| IP | ASN | Network owner | Network type | Location (as reported by the geolocation service) | Other context |
|---|---|---|---|---|---|
| 192.0.2.10 | AS64496 | Wrenmoor Fibre | Business fibre | Client's metro area | Orrin Valley office NAT address (confirmed by IT) |
| 192.0.2.25 | AS64496 | Wrenmoor Fibre | Business fibre | Client's metro area | Orrin Valley mail gateway gw01 (confirmed by IT) |
| 192.0.2.140 | AS64500 | Cedarline Web Hosting | Managed hosting | Client's region | Castellan's real website |
| 192.0.2.201 | AS64500 | Cedarline Web Hosting | Managed hosting | Client's region | Brightquay Legal document portal |
| 198.51.100.23 | AS64510 | Pinecrate VPS | Datacenter / VPS | EU-West datacenter | None |
| 198.51.100.77 | AS64508 | Skerrow Mobile | Mobile carrier, carrier-grade NAT | Client's metro area | Shared by many mobile subscribers |
| 198.51.100.170 | AS64502 | Northfold Mail Services | Email hosting | Client's region | Castellan's previous mail server |
| 198.51.100.180 | AS64502 | Northfold Mail Services | Email hosting | Client's region | Castellan's current mail server |
| 203.0.113.47 | AS64510 | Pinecrate VPS | Datacenter / VPS | EU-West datacenter | None |
| 203.0.113.88 | AS64505 | Pinecrest Shared Hosting | Shared web hosting | North America | 1,412 co-hosted domains (L5) |
| 203.0.113.91 | AS64511 | Driftwood Cloud | Datacenter / VPS | North America | None |
| 203.0.113.200 | AS64507 | Keelson Hosting | Datacenter | Asia-Pacific datacenter | Listed on a public blocklist for password spraying against cloud mail tenants since January 2026 |

Geolocation for datacenter and VPS addresses reports where the server sits, which says nothing about where its operator is.

## L9: other lookups

| Item | Result |
|---|---|
| Phone 555-0112 | Landline. Carrier Wrenmoor Telephone. Directory listing: Castellan Hardwood Supply Inc., listed since 1998. |
| Phone 555-0148 | VoIP. Carrier Callwisp VoIP. No directory listing. |
| Domain `freemail.example` | Large consumer webmail provider. Anyone can register an address. No lookup was run on the address `dwhitlock.castellan@freemail.example` itself (out of scope). |
| Public phishing feed | `marrowline-docs.example` reported 24 February 2026. `cstl-docshare.example` reported 12 March 2026 14:30 UTC by a reporter outside the client. `castellan-hardwood.example` and `quennmarsh-accounts.example` not listed. |
