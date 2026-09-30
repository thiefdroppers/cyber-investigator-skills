# Chain-of-custody form

Use one form per evidence item. Fill it in ink or in a file you hash at the end of each day. Never edit a past row; correct it with a new dated row that names the row it corrects. Lab use only: case LAB-P4 is synthetic.

## Part A: item identification

| Field | Entry |
|---|---|
| Case number | |
| Evidence item number | |
| Description (make, model, capacity, colour, markings) | |
| Serial number | |
| Collected from (location, host name, custodian role) | |
| Legal authority for collection (warrant, consent form, employer policy clause, engagement letter) | |
| Collected by (name, role) | |
| Date and time collected (UTC, and the local time zone in use) | |
| Condition when collected (powered on/off, screen state, damage, seals) | |
| Photographs taken (file names and hashes) | |
| Packaging and seal number | |

## Part B: acquisition record

| Field | Entry |
|---|---|
| Write blocker used (hardware model or software method) | |
| Acquisition tool and exact version | |
| Exact command or GUI options used | |
| Source device hash, algorithm | |
| Image file name(s) and format (raw/dd, E01, AFF4) | |
| Image hash, algorithm | |
| Hashes match? (yes/no, and what was done if no) | |
| Bad sectors or read errors reported | |
| Acquisition start and end time (UTC) | |
| Examiner signature | |

## Part C: transfer log

Every time the item or its image changes hands or location, add a row. A gap between rows is a gap in custody.

| # | Date and time (UTC) | Released by | Received by | Purpose | Location after transfer | Seal intact? | Hash re-verified (value or "n/a, sealed") |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

## Part D: final disposition

| Field | Entry |
|---|---|
| Disposition (returned, retained, destroyed) and authority | |
| Date and time (UTC) | |
| Witness | |
