# Platform trust and safety: vertical taxonomy

These are the per-vertical mechanisms the trust and safety skill in [`../SKILL.md`](../SKILL.md) checks for. They extend the generic [`fraud-pattern-taxonomy.md`](../../../reference/fraud-pattern-taxonomy.md), which still applies. Add an entry only when a documented case supports it, through the [contribution process](../../../../CONTRIBUTING.md).

Each vertical has two tables. The first lists mechanisms and the evidence that shows each one in a specific case. The second lists platform signals: account and listing data a reviewer can pull from the platform's own records. A platform signal raises or lowers priority. It never counts as a mechanism on its own, because new accounts, new domains, and busy sellers are also normal.

A row marked "Needs a documented case" describes a pattern reviewers report but that this repo has not yet tied to a cited case. Use it to prompt a check, not to support a verdict.

## Job boards and professional networks
Applies to job boards, LinkedIn-style networks, and gig platforms that post paid work. [Day 67](../../../../curriculum/phase-5-fraud-social-engineering/day-67.md) covers recruitment fraud in depth.

FTC data shows "task scam" reports growing from none in a sample of 2020 reports, to about 5,000 in 2023, to about 20,000 in the first half of 2024. A secondary summary of FTC data cites $150.4 million in job-scam losses on 25,002 reports in Q4 2025, with a $2,000 median loss. That figure has not been checked against the FTC's own release.

| Mechanism | Evidence that it is present |
|---|---|
| Task scam | Gamified micro-tasks (rating products, liking videos, "optimizing" orders), a small early payout that proves the scheme "works," then a demand for a deposit to unlock earned commissions or a higher tier |
| Fake recruiter using a real company name | A recruiter profile claims a real employer, but the contact email, domain, or careers link does not belong to that employer, or the employer's own careers site has no matching role |
| Newly registered employer domain | The domain in the posting or recruiter email was registered within the last 30 days (WHOIS or RDAP creation date). The 30-day window is a starting threshold for review, not a settled cutoff; record the actual age |
| Chat-only interview | The whole interview happens by text chat, with no voice or video call and no named interviewer who can be verified |

| Platform signal | What to check |
|---|---|
| Account age | Creation date of the poster or recruiter account, compared with the date of the first job post |
| Employer verification status | Whether the platform has verified the employer, and when |
| Messaging-to-off-platform ratio | Share of the account's conversations that include a request to move to email, WhatsApp, Telegram, or another channel |
| Bulk-posting fingerprint | Many near-identical postings across locations or accounts in a short period (same text, same contact details, same pay figure) |
| IP and ASN of poster | Whether the poster's IP or ASN is shared with other flagged accounts, or does not fit the employer's stated location |

## Marketplaces and classifieds
Applies to marketplaces, classifieds, and rental platforms.

| Mechanism | Evidence that it is present |
|---|---|
| Overpayment scam | A buyer sends more than the price and asks for the difference back, often by a different payment method, before the original payment clears |
| Fake escrow or "buyer protection" link | A link to a payment, escrow, or protection page that is not on the platform's own domain, often styled to look like the platform |
| Off-platform payment insistence | Repeated pressure to pay or be paid outside the platform's payment system, such as by gift card, wire, crypto, or a payment app |
| Triangulation fraud | The seller lists goods and fulfils each order by buying the item elsewhere with a stolen card, shipping it straight to the real buyer. Evidence is often a chargeback on the upstream purchase, or a buyer reporting a package from an unrelated retailer |
| Shipping-label swap | The other party supplies or changes the shipping label or tracking number so the item goes to an address the seller did not agree to, or tracking shows a delivery that did not happen. Needs a documented case |
| Rental deposit before viewing | A deposit, first month's rent, or "application fee" is demanded before the renter can view the property, often with a reason the owner cannot meet (overseas, travelling) |

| Platform signal | What to check |
|---|---|
| Payout method changes | Changes to the seller's payout account, especially close to a large sale or to an account shared with other sellers |
| Listing-image reverse match | Listing photos found elsewhere online (another listing, a real-estate site, a retailer's product page) |
| Price-vs-market outlier | Asking price far below comparable listings on the same platform |
| Seller-account velocity | Number of listings, sales, or price changes per day, compared with the account's own history and with similar sellers |

## Dating
[Day 69](../../../../curriculum/phase-5-fraud-social-engineering/day-69.md) lays out the romance and relationship-investment timeline in full. In September 2025, US senators pressed Match Group about romance scams that start on its platforms.

| Mechanism | Evidence that it is present |
|---|---|
| Rapid escalation | Declarations of love or future plans before any verified in-person meeting |
| Video-call avoidance | Repeated refusals or excuses when asked to video call |
| Investment pivot | A "mentor" or the match introduces a trading platform, shares screenshots of profits, asks the user to install a trading app, and refuses to meet in person. This is the relationship-investment scam (older alerts call it pig butchering), the same pattern as investment fraud, started inside a dating-app relationship |

| Platform signal | What to check |
|---|---|
| Profile-photo reverse-image match | Profile photos found under another name, on a stock site, or on a real person's public account |
| Message templates across accounts | The same opening lines or life story sent from several accounts |
| Rapid move to WhatsApp or Telegram | How soon after matching the account asks to move the conversation, and how often it does so across matches |
| Geolocation vs. claimed location | Whether login location and device data fit the location in the profile and conversation |

## Social media and ads
The FTC has been examining platforms' role in impersonation-scam ads as of September 2026.

| Mechanism | Evidence that it is present |
|---|---|
| Celebrity or brand impersonation ad | An ad uses a real person's or brand's name, face, or logo to promote an investment, product, or giveaway they have no connection to |
| Fake giveaway | A prize that requires a fee, a "shipping cost," card details, or a login to claim |
| Recovery-scam page | A page or ad offering to recover money lost to an earlier scam, for an upfront fee, aimed at people who have already reported a loss |

| Platform signal | What to check |
|---|---|
| Ad-account creation date | How long before the ad ran the ad account was created |
| Payment instrument reuse | Whether the card or billing account paying for the ad also paid for ads on accounts already removed |
| Landing-domain age | Registration date of the domain the ad links to |
