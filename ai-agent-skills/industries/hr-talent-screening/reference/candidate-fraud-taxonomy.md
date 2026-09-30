# Candidate fraud taxonomy (starter set)

These are the mechanisms the candidate-fraud triage in [`../SKILL.md`](../SKILL.md) checks for. This is the inverse of the recruitment and job fraud section in [`../../../reference/fraud-pattern-taxonomy.md`](../../../reference/fraud-pattern-taxonomy.md). That file covers fake employers targeting job seekers. This file covers fake candidates targeting employers. Add an entry only when a documented case supports it, through the [contribution process](../../../../CONTRIBUTING.md).

A pattern name alone cannot score a case. Each entry below gives the mechanism and the evidence that shows it is present in a specific case. Every mechanism is a screening signal, not a decision. Route every finding to HR and legal.

Some rows are marked "needs a documented case." Those rows describe a plausible mechanism that the sources this file currently cites do not describe directly. Report them as lower confidence, and replace the mark with a citation once a documented case supports them.

## Identity discontinuity

| Mechanism | Evidence that it is present |
|---|---|
| Name mismatch across records | The name on the ID differs from the name on the payroll or bank account, or from the name on GitHub or LinkedIn, with no documented reason such as a legal name change |
| Equipment shipping mismatch | The shipping address given for company equipment differs from the residence the candidate stated |

Source status: the use of stolen identities to obtain remote jobs is documented in the US Department of Justice actions announced in June 2025. The equipment shipping row needs a documented case.

## Interview evasion

| Mechanism | Evidence that it is present |
|---|---|
| Refusal of live video | The candidate declines every live video interview, with no accommodation request on file |
| Camera off partway through | The camera is on at the start, then goes off or is described as "broken" after the interview starts |
| Face-swap indicators | Lip movement out of sync with the audio, or blinking that looks unnatural, observed in the recording |
| Second voice | A second voice is audible during the call, prompting or answering |

Source status: face-swap software in video interviews, with the camera switched off partway through, is documented in August 2026 reporting on the North Korean IT-worker scheme. The lip-sync and blink row and the second voice row need a documented case. A declined camera with an accommodation request on file is not evidence and is excluded from the count.

## Manufactured history

| Mechanism | Evidence that it is present |
|---|---|
| Recently registered portfolio domain | The portfolio or personal-site domain was registered recently, compared with the career length the resume claims (cite the WHOIS record and date) |
| Email-only references | References can be reached only by email, with no phone number or independently listed contact |
| Prior employer with no footprint | A listed prior employer has no independent footprint: no registry record, archived site, or third-party mention |

Source status: all three rows need a documented case. A closed or renamed company, or a reference who prefers email, has an innocent explanation. Check it before recording the mechanism.

## Generated application text

| Mechanism | Evidence that it is present |
|---|---|
| Machine-generated text result | The base skill's machine-generated text check returns "likely machine-generated" for the resume, cover letter, or written answers, with quoted tells |
| Cross-applicant phrasing | Identical phrasing appears across several applicants for the same role (quote the matching passages and name each application) |

Source status: both rows need a documented case. The first row is a supporting signal only, for the same reason the base skill gives: many honest applicants use writing tools. It never counts as a mechanism on its own. Cross-applicant phrasing is more useful as a labeled edge in a link-analysis graph than as a finding about one person.

## Post-hire signals

Checking these rows needs the employer's own authorization for a review of an employee, not only the hiring requisition.

| Mechanism | Evidence that it is present |
|---|---|
| Several remote-access tools on day one | More than one remote-access tool is installed on company equipment on the first day, outside the employer's approved tooling (cite the endpoint log) |
| Hours misaligned with stated timezone | Working hours consistently fall outside what the stated timezone would suggest (cite login or activity logs over a stated period) |
| Equipment rerouting request | A request to ship company equipment to a third-party address rather than to the stated residence |

Source status: extortion after hiring is documented in the FBI's January 2025 advisory on North Korean IT workers. All three rows here need a documented case. Timezone misalignment has common innocent explanations, such as caregiving, a second shift, or an agreed flexible schedule, and must never be read as a proxy for national origin.
