# Case LAB-P4: instructor key

Do not read this before finishing day 58. It states the traps built into the case data directly; working them out from the evidence is the point of days 49 through 58.

## The two timing traps

The firewall writes local time. On 14 March 2026 New York is on daylight time (UTC-4), because US daylight saving time started on 8 March 2026. A learner who assumes UTC-5 will misplace every firewall event by an hour.

`fs01` has an 83-second fast clock. The SSH hop from `bastion01` appears at 03:19:21 UTC in the firewall log and at 03:20:45 in `fs01-auth.log`: 83 seconds of skew plus about a second for the TCP and SSH handshake.

## The deliberate loose end

`ws-fin-07-security.csv` shows 23 network logon failures against WS-FIN-07 from `bastion01` between 02:10 and 02:16, before the external spray against `bastion01` begins at 02:51. Nothing in the data explains them. A good day 64 report lists them under limitations as not determined instead of forcing them into the story.
