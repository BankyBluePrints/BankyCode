# GitLab release promotion

The earlier scratch example automatically cherry-picked and directly pushed between release
branches. That pattern is risky for protected branches because conflicts, approvals, pipeline
results, and credential handling become difficult to audit.

## Recommended flow

1. Identify the exact source commit or release tag.
2. Create a short-lived promotion branch from the target release branch.
3. Cherry-pick the exact commit with `git cherry-pick -x`.
4. Push the promotion branch using GitLab's supported CI authentication.
5. Open a merge request into the target release branch.
6. Require the normal approvals, status checks, and conflict resolution.
7. Promote to the next release only after the previous merge request succeeds.

## Safety requirements

- Never print tokens, token lengths, authenticated remote URLs, or other secret-derived data.
- Do not embed a personal access token in `git remote set-url` or command arguments.
- Use protected CI variables and the least-privileged supported GitLab token mechanism.
- Use explicit commit SHAs or immutable tags; do not infer “latest” from an unrestricted log.
- Make repeated execution idempotent by checking whether the commit is already present.
- Stop on conflicts and require a human-reviewed resolution.
- Prefer GitLab API-created merge requests over direct pushes to protected release branches.

This document intentionally does not provide a drop-in pipeline because permissions,
protected-branch policy, runner configuration, and promotion rules differ by GitLab
installation.
