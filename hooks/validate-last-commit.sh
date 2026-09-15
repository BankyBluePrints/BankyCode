#!/usr/bin/env sh
set -eu

repository_root=$(git rev-parse --show-toplevel)
message_file=$(mktemp)
trap 'rm -f "$message_file"' EXIT HUP INT TERM

git log -1 --pretty=%B > "$message_file"
"$repository_root/hooks/commit-msg" "$message_file"
