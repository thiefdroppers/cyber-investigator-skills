# Phase 6 lab data (synthetic)

Every file under this folder is synthetic training data. Blue Harbor Analytics, its staff, its contractor, its cloud projects and accounts, and every event in these logs are invented. Public IP addresses come from the RFC 5737 documentation ranges (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24). The one exception is 199.36.153.8, the published private.googleapis.com address that Private Google Access uses, which appears in the flow logs as the far end of Cloud Storage reads. Internal addresses are RFC 1918. AWS account 111122223333 and the access key IDs ending in `EXAMPLE` are the placeholder values AWS uses in its own documentation. Nothing here describes a real breach, company or person.

The files follow the shape of the real exports (`gcloud logging read --format=json`, `aws cloudtrail lookup-events`, CloudTrail S3 log files, `aws iam get-account-authorization-details`, `az monitor activity-log list`) with fields trimmed to what the exercises use. They are not byte-exact copies of any provider's output. SKU names and prices in the billing file are invented for the lab; read your own billing export for real SKU descriptions and rates.

## Case Blue Harbor in one paragraph

Blue Harbor Analytics is a small analytics company. It keeps customer exports in the Cloud Storage bucket `blueharbor-customer-exports` in the GCP project `blueharbor-analytics`, and a nightly job on the VM `report-runner-1` (running as `reporting-sa`) mirrors each export to the S3 bucket `blueharbor-exports-mirror` in AWS account 111122223333. A small Azure subscription hosts the marketing site. On Sunday 13 September 2026 at 09:40 UTC a budget alert fires: network egress for 12 September came to about 47 GiB against a normal 2.2 GiB. Between 01:47 and 03:07 UTC on 12 September, someone at 198.51.100.23 used the external contractor account `sam.reyes@vendor-example.com` in GCP and the IAM user `vendor-sam` in AWS, minted new credentials for a more powerful identity in each cloud, and moved data out. Two days earlier the same address submitted a support ticket that tried to get Blue Harbor's LLM support assistant to hand over a download link for the export. Days 77 to 82 work this case from evidence intake to the final report. Whether Sam Reyes did this, or someone else holding Sam's credentials did, is not shown by any file here, and your report should say so.

## Audit and logging configuration during the window

GCP: Admin Activity logs are always on. The project's audit config (visible in `gcp/iam-project-policy.json`) enables `ADMIN_READ` Data Access logs for all services and leaves `DATA_READ` and `DATA_WRITE` off, so reads of object contents in Cloud Storage are not logged. VPC Flow Logs are on for `reporting-subnet` with a 5-minute aggregation interval and a sampling rate of 1.0, so byte counts in `gcp/vpc-flows.json` are complete for that subnet. A billing export to BigQuery was configured before the window; `gcp/billing-daily.csv` is a daily summary of it.

AWS: one multi-region trail, `blueharbor-trail`, records management events and S3 data events for `blueharbor-exports-mirror` only.

Azure: the Activity Log for the subscription. No Entra ID sign-in logs are included.

## Files

| Path | What it is | Used on |
|---|---|---|
| `case-blueharbor/gcp/audit-activity.json` | Cloud Audit Logs, Admin Activity, 10 to 12 September | 77, 78, 82 |
| `case-blueharbor/gcp/audit-data-access.json` | Cloud Audit Logs, Data Access (ADMIN_READ plus BigQuery jobs), same window | 77, 78, 82 |
| `case-blueharbor/gcp/iam-project-policy.json` | `get-iam-policy` export for the project, including `auditConfigs` | 77, 79, 80 |
| `case-blueharbor/gcp/iam-reporting-sa-policy.json` | IAM policy on the `reporting-sa` service account | 79, 80 |
| `case-blueharbor/gcp/iam-bucket-customer-exports.json` | IAM policy on the customer exports bucket | 79, 80 |
| `case-blueharbor/gcp/groups-export.csv` | Group membership export | 79, 80 |
| `case-blueharbor/gcp/service-accounts.csv` | Service account inventory, with what each one is attached to | 79, 80 |
| `case-blueharbor/gcp/vpc-flows.json` | VPC Flow Logs for `reporting-subnet`, same window | 82 |
| `case-blueharbor/gcp/billing-daily.csv` | Daily cost and usage by SKU, 1 to 12 September | 82 |
| `case-blueharbor/aws/cloudtrail-lookup-events.json` | `lookup-events` style management events, newest first | 77, 78, 82 |
| `case-blueharbor/aws/cloudtrail-s3-data-events.json` | Trail log file with S3 data events for the mirror bucket | 77, 82 |
| `case-blueharbor/aws/iam-authorization-details.json` | `get-account-authorization-details` export | 79, 80 |
| `case-blueharbor/azure/activity-log.json` | `az monitor activity-log list` style events, newest first | 78, 82 |
| `case-blueharbor/app/support-tickets.jsonl` | Three support tickets, including the one that carried the injection | 81, 82 |
| `day-81-app-log.jsonl` | Support assistant request log (input, retrieved context, tool calls, output) | 81, 82 |
| `case-blueharbor/generate_synthetic.py` | Regenerates every data file above deterministically | any |

Run `python3 case-blueharbor/generate_synthetic.py` from this folder to rebuild the data. The output is identical on every run, so your hashes from day 77 will match anyone else's copy of the repo at the same commit.

## Instructor key

`INSTRUCTOR-KEY.md` in this folder states the case's built-in traps and loose ends directly. Do not read it before finishing day 82; finding them from the evidence is the exercise.

## Still missing

There is no AWS billing data, no Entra ID sign-in log, no packet capture and no disk image of `report-runner-1`. Day 82 asks you to list what each of those would have told you.
