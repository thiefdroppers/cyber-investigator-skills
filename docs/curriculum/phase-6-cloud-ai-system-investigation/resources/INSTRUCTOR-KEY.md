# Case Blue Harbor: instructor key

Do not read this before finishing day 82. It states the traps built into the case data directly; working them out from the evidence is the point of days 77 through 82.

## The traps

The reconnaissance lives in the Data Access log. Six of the seven calls in the 01:47 to 01:52 burst are read methods that were denied, and read methods are logged as `ADMIN_READ` in `audit-data-access.json`. A learner who queries only the Admin Activity log sees one event for `sam.reyes@vendor-example.com` (the key creation at 01:58:31) and misses the probing that preceded it.

The identity changes mid-intrusion in both clouds. After 01:58:31 the GCP actions are logged as `reporting-sa`, and after 02:22:02 the AWS actions are logged as `svc-reporting`. Filtering on the contractor's identity alone loses everything after the pivot. The links are the source IP, the GCP key ID `a41c9e0f2b7d4e6a8c1f3b5d7e9a0c2e4f6b8d0a` (in the `CreateServiceAccountKey` response and in `authenticationInfo.serviceAccountKeyName` on every later call), and the AWS access key `AKIA-EXAMPLE-NOT-REAL` (in the `CreateAccessKey` response and in `userIdentity.accessKeyId` on every later call).

The logging tiers differ between clouds. GCP `DATA_READ` was off, so no file shows which Cloud Storage objects were read; the evidence for the read is the flow log (about 46.3 GB arriving at the VM from 199.36.153.8 between 02:07 and 02:17) and the jump in Class B operations on the billing file. AWS S3 data events were on for the mirror bucket, so the 14 `GetObject` calls name every object taken and their sizes (2,161,502,322 bytes in total).

`lookup-events` and the Azure export are newest first. A learner who reads them top to bottom reverses the order of the AWS steps.

Request `r-1003` in the app log is unrelated. It comes from a different user (`u-91`) at a different address (203.0.113.140), targets a session token, and matches nothing else in the case. It belongs in the injection note as a separate attempt and must stay out of the Blue Harbor timeline.

The model in `r-1011` complied. It issued the `generate_signed_url` tool call the injected comment asked for, and only the missing `iam.serviceAccounts.signBlob` permission on `support-bot` stopped it. A note that records `r-1011` as "refused" has misread the log.

## Other paths the graphs should show

In GCP, 10 identities can reach object contents in the bucket once group membership, service account key administration, `actAs` and the VM's runtime identity are expanded (the day 80 script prints the list). The cheapest edge to cut for this intrusion is the `roles/iam.serviceAccountKeyAdmin` binding for `group:data-eng` on `reporting-sa`, because nothing legitimate uses it and removing it breaks the path for all three group members.

In AWS, the `RotateOwnKeys` statement in `vendor-sam`'s inline policy uses `user/*` where it meant `user/${aws:username}`. That lets `vendor-sam` create keys for every IAM user, including `dana-admin` with `AdministratorAccess` and `old-etl` with an inline `"Action": "*"`. The attacker took `svc-reporting`. The lookup-events file shows only one `CreateAccessKey` in the window, which is the evidence that the admin path was not used during it.

## The deliberate loose ends

Attribution. Sam's account worked normally from 192.0.2.44 with a browser user agent on 10 and 11 September, and the same account acted from 198.51.100.23 with a Python client at 01:47 on a Saturday. Nothing in the data says whether Sam did it or someone holding Sam's credentials did. The actor also called `ListServiceAccountKeys` on `reporting-sa` directly after `ListServiceAccounts` was denied, so they knew the service account's name in advance. That fits an insider and fits someone who read internal documents; it proves neither.

Byte mismatch. The VM pushed 48,213,847,552 bytes to 203.0.113.77 but pulled about 46.3 GB from Cloud Storage during the intrusion. The VM's disk still held the previous night's export (about 2.37 GB, pulled at 00:31), which could account for the difference, but no file shows what was on the disk. A good report states the gap instead of rounding it away.

Egress destination. Nothing identifies who controls 203.0.113.77.
