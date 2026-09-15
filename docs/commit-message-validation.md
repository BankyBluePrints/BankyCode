# Commit-message validation

The sample policy requires the first line to use this shape:

```text
TASK-123: description of at least 20 characters
```

Change the regular expression in [`hooks/commit-msg`](../hooks/commit-msg) to match your
real issue-key convention.

## Install locally

Run from the repository root:

```bash
cp hooks/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

Git invokes `commit-msg` after the message is prepared and passes the message-file path as
its first argument. A `pre-commit` hook is intended for staged-content checks and does not
receive that path.

## Validate in CI

Use [`hooks/validate-last-commit.sh`](../hooks/validate-last-commit.sh):

```bash
./hooks/validate-last-commit.sh
```

Local hooks are developer-side convenience controls and can be skipped with `--no-verify`.
For an enforceable policy, repeat validation in CI and protect the target branch.
