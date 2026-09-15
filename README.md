# BankyCode

A small, curated collection of reusable Git governance notes, shell-hook examples, and a
Streamlit user-interface prototype.

## Repository status

This repository is a **maintained reference collection**, not a deployed application. No
GitHub Actions deployment workflow, GitHub Pages site, or deployment configuration is
present. Archiving remains a separate decision.

## Contents

| Area | Resource | Purpose |
| --- | --- | --- |
| Repository design | [Repository strategy comparison](docs/repository-strategy.md) | Compare service-, technology-, and feature-oriented repository boundaries. |
| Commit governance | [Commit-message validation](docs/commit-message-validation.md) | Install and understand the sample `commit-msg` hook. |
| Git hook | [`hooks/commit-msg`](hooks/commit-msg) | Validate a commit message locally. |
| CI validation | [`hooks/validate-last-commit.sh`](hooks/validate-last-commit.sh) | Apply the same rule to the latest commit in CI. |
| Release governance | [GitLab release promotion](docs/gitlab-release-promotion.md) | Prefer reviewed merge requests over credential-bearing direct-push jobs. |
| Python example | [Streamlit knowledge-base prototype](examples/streamlit-knowledge-base/README.md) | Run a static, local UI demonstration. |

## Validation

The CI workflow performs offline checks only:

- compiles every Python file without running external services;
- checks both shell scripts with `bash -n`;
- verifies the commit-message hook accepts and rejects representative inputs.

## Security and reuse

- Examples use synthetic data only.
- Never commit access tokens, credentials, internal hostnames, or private business data.
- Review and adapt every hook or pipeline pattern for the target repository.
- Local Git hooks can be bypassed, so enforce important rules again in CI or repository
  controls.
- No license is currently declared; public visibility does not itself grant reuse rights.
