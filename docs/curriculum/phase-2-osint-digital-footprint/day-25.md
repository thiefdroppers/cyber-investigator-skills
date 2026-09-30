# Day 25: Social media investigation, part 1: platform-specific recon

Phase: 2. OSINT and digital footprint · Track goal: Use each major platform's own search syntax and transparency features to reconstruct a public organization's activity, and assemble it into a cross-platform timeline.

## Concept
Every platform indexes its content differently, and its own search is usually better than a general search engine at reaching it. X has an operator language for filtering by author, date, and content type. Meta publishes a Page transparency panel and an Ad Library that show when a Page was created, whether it changed name, and what it paid to promote. YouTube channels show a join date and exact upload dates. Reddit's search accepts `site:` and `url:`, which lets you find every discussion that linked to a domain. LinkedIn company pages show headcount trends and posts.

For an investigator, the value is time. Fraud and influence operations leave timing signatures: a Page renamed three times in a year, a burst of accounts created in the same week, promoted posts that start the day a domain is registered. A timeline across platforms is where those signatures show up. Your Day 29 registration dates will line up against today's account creation dates.

Three limits apply. Most platforms now require a logged-in account to search. Until Day 31 covers sock puppets, use your own account and act strictly passively: search and read, never follow, like, comment, or message. Second, platform terms generally forbid automated collection; everything today is manual. Third, what the platform shows is what it chooses to show. A creation date in a transparency panel is the platform's claim, and a good one, but still one source.

The subject is again a public organization's official accounts. Do not build a timeline of a private person's posting history.

## Resources
- [X advanced search](https://x.com/search-advanced) is the form version of the operators below; build a query there, then read the operator string it produces.
- [Meta Ad Library](https://www.facebook.com/ads/library/) lets you search ads by Page, including inactive ads, with extended retention for ads about social issues, elections, or politics.
- [Knight Lab TimelineJS](https://timeline.knightlab.com/) builds an interactive timeline from a Google Sheets template. Free.
- [Bellingcat toolkit, social media section](https://bellingcat.gitbook.io/toolkit) keeps up with which platform tools still work.

## Practical: platform search syntax and TimelineJS: a cross-platform activity timeline
Pick the organization's official accounts on at least three platforms. Their website footer usually links them; record those links in the recon log as the source of attribution. An account the organization does not link to is not "theirs" until you have other evidence.

Step 1: X. These operators work in the main search box (logged in):

```
from:ExampleOrg since:2025-01-01 until:2025-07-01
from:ExampleOrg filter:media
from:ExampleOrg filter:links -filter:replies
to:ExampleOrg
@ExampleOrg -from:ExampleOrg
url:example.org
from:ExampleOrg min_retweets:100
```

`since:` and `until:` take `YYYY-MM-DD`, with `until:` exclusive. `url:example.org` finds posts by anyone that link to the domain, which surfaces campaigns and complaints alike. Use the Latest tab for chronological order. X has changed operator behavior before; test each one against a post you can see exists.

The profile page shows "Joined Month YYYY". Record it.

Step 2: Facebook. On the organization's Page, open About, then Page transparency (on some layouts it is a section on the main Page). It lists the creation date, any previous names with the date of each change, and the countries where the people managing the Page are located. Screenshot it and capture it with SingleFile. Then open the Meta Ad Library, set the country and "All ads", and search the Page name. Note the earliest ad date, whether ads are running now, and for issue or political ads, the "Paid for by" disclaimer.

Step 3: YouTube. On the channel page, open the description or "more" panel to find the join date and total views. Under Videos, sort by Oldest. For exact upload dates, the date under each video's title is enough for a timeline.

Step 4: Reddit. Reddit's search accepts:

```
site:example.org
url:example.org
"Example Organization" subreddit:yourcity
```

Sort by New. Each result is a public discussion of the organization or its links. For one thread, append `.json` to its URL (`https://www.reddit.com/r/SUB/comments/ID/SLUG/.json`) to see the exact `created_utc` Unix timestamps; convert one with `date -u -r 1735689600` (macOS) or `date -u -d @1735689600` (Linux). Read the JSON in your browser; do not script bulk downloads.

Step 5: LinkedIn. The company page's About tab shows founding year, size band, and headquarters as the organization entered them. The Posts tab gives dates. LinkedIn's User Agreement prohibits scraping and automated access, so this step is manual only.

Step 6: build the timeline. Open the TimelineJS Google Sheets template (linked from timeline.knightlab.com, "Get the Spreadsheet Template"), make a copy, and add one row per event. Keep the template's column headers; the essential ones are Year, Month, Day, Headline, Text, Media, and Group. Use Group for the platform, so events stack by platform. Illustrative rows:

| Year | Month | Day | Headline | Text | Group |
|---|---|---|---|---|---|
| 2014 | 3 | 11 | Facebook Page created | Page transparency panel; capture log #31 | Facebook |
| 2016 | 9 | | X account joined | Profile "Joined September 2016"; log #33 | X |
| 2021 | 5 | 4 | Page renamed | Previous name "Example Org Events"; log #31 | Facebook |
| 2023 | 2 | 1 | First promoted ad | Meta Ad Library; log #34 | Facebook |
| 2024 | 11 | 18 | Reddit thread links events site | `created_utc` 1731888000; log #36 | Reddit |

Every Text cell cites a collection-log row. Then in the Sheet use File > Share > Publish to web, paste the published link into the TimelineJS page, and copy the generated embed or preview link.

The artifact is the published TimelineJS timeline with at least 12 events from at least three platforms, and matching rows in the recon log.

## Checkpoint
Look at the timeline for clustering: any week or month where several platforms show activity at once. Write two sentences on the densest cluster and what external event (a launch, a rebrand, a news story) explains it, with a source. Every event must cite a log row. Confirm in your notes that you took no action on any platform beyond searching and reading.
