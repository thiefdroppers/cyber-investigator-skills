# Security Policy

## Scope

This repository is curriculum content, worksheets, and AI agent skill
definitions (Markdown and a small amount of Python/Shell for the lab
exercises and the docs build). It is not a hosted service, and most of
what runs in the labs runs on your own machine against targets you
control. That said, a few things are worth reporting if you find them:

- A shell or Python script in `curriculum/` or `scripts/` that could run
  something unintended (not just "this command is dangerous if misused on
  purpose," which many of the lab exercises intentionally are, but
  unexpected behavior from following the instructions as written).
- Synthetic lab data that turns out to contain a real credential, a real
  person's data, or anything else that shouldn't have been committed.
- An instruction in `ai-agent-skills/` that could be used to bypass the
  scope and ethics rules it states, rather than follow them.
- A supply-chain issue: a referenced tool, package, or URL that's been
  taken over or now points somewhere it shouldn't.

## Reporting a Vulnerability

Please use GitHub's private vulnerability reporting instead of opening a
public issue: go to the **Security** tab of this repository and select
**Report a vulnerability**. This reaches maintainers privately so a fix
can land before the details are public.

If that's not available to you, open an issue describing the category of
problem without the exploitable detail, and a maintainer will follow up
through a private channel.

## What to Expect

This is a community-maintained educational project, not a funded security
team, so response times vary. A real report will get acknowledged, and a
confirmed issue will get fixed and credited (unless you ask not to be)
once a fix is out.
