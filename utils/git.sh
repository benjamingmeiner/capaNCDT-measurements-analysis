#!/bin/bash
set -e

data_dir=$1
scripts=$2
message=$3
branch=$(basename "$data_dir")

current_branch=$(git rev-parse --abbrev-ref HEAD)

if [ "$current_branch" != "$branch" ]; then
    if [ -n "$(git show-ref refs/heads/"$branch")" ]; then
        git checkout "$branch"
    else
        git checkout -b "$branch"
    fi
fi
git add $data_dir $scripts
git commit -m "$message"
