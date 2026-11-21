#!/usr/bin/env python3
"""Merge additive learners.txt-only pull requests from the trusted base branch."""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


MARKER = "<!-- learner-welcome -->"
LEARNERS = "learners.txt"


def run(*args, input=None, env=None, check=True):
    result = subprocess.run(
        args, input=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env
    )
    if check and result.returncode:
        raise RuntimeError(
            f"{args[0]} failed: {result.stderr.decode(errors='replace').strip()}"
        )
    return result


def git(*args, **kwargs):
    return run("git", *args, **kwargs).stdout


def api(path, *args):
    result = run("gh", "api", path, *args)
    return json.loads(result.stdout)


def lines_are_preserved(original, updated):
    """Allow inserted lines, but never edits, removals, or reordered lines."""
    remaining = iter(updated.splitlines())
    return all(any(line == candidate for candidate in remaining) for line in original.splitlines())


def read_regular_file(revision):
    entry = git("ls-tree", revision, "--", LEARNERS).decode().strip()
    if not entry.startswith("100644 blob ") or not entry.endswith("\t" + LEARNERS):
        raise RuntimeError(f"{LEARNERS} must be a regular file in {revision}")
    return git("show", f"{revision}:{LEARNERS}")


def union_contents(ancestor, base, head):
    with tempfile.TemporaryDirectory() as directory:
        paths = [Path(directory) / name for name in ("base", "ancestor", "head")]
        for path, contents in zip(paths, (base, ancestor, head)):
            path.write_bytes(contents)
        result = run(
            "git", "merge-file", "--union", "-p", *(str(path) for path in paths),
            check=False,
        )
    if result.returncode not in (0, 1):
        raise RuntimeError(f"Unable to resolve {LEARNERS}: {result.stderr.decode(errors='replace')}")
    if not lines_are_preserved(base, result.stdout) or not lines_are_preserved(head, result.stdout):
        raise RuntimeError(f"Resolving {LEARNERS} would remove or alter existing lines")
    return result.stdout


def welcome(repo, number, login):
    pages = api(f"repos/{repo}/issues/{number}/comments", "--paginate", "--slurp")
    if any(
        MARKER in comment["body"] and comment["user"]["login"] == "github-actions[bot]"
        for page in pages for comment in page
    ):
        return
    api(
        f"repos/{repo}/issues/{number}/comments",
        "-f", f"body={MARKER}\nThanks for contributing, @{login}! Happy learning! 🎉",
    )


def resolved_tree(base, merge_tree, contents):
    # Start from Git's merge tree so the merge retains all non-conflicting changes.
    # A separate index prevents any PR content from entering the working tree.
    with tempfile.TemporaryDirectory() as directory:
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(Path(directory) / "index")
        git("read-tree", merge_tree, env=env)
        blob = git("hash-object", "-w", "--stdin", input=contents).decode().strip()
        git("update-index", "--add", "--cacheinfo", "100644", blob, LEARNERS, env=env)
        tree = git("write-tree", env=env).decode().strip()
    changed = git("diff-tree", "--no-commit-id", "--name-only", "-r", base, tree).splitlines()
    if any(path != LEARNERS.encode() for path in changed):
        raise RuntimeError("The resolved merge would change files other than learners.txt")
    return tree


def process(repo, base_branch, number):
    pull = api(f"repos/{repo}/pulls/{number}")
    if pull["state"] != "open" or pull["draft"] or pull["base"]["ref"] != base_branch:
        return
    head = pull["head"]["sha"]
    remote_base = f"refs/remotes/origin/{base_branch}"
    remote_head = f"refs/remotes/learner-pr/{number}"
    git(
        "fetch", "--no-tags", "origin",
        f"+refs/heads/{base_branch}:{remote_base}",
        f"+refs/pull/{number}/head:{remote_head}",
    )
    if git("rev-parse", remote_head).decode().strip() != head:
        raise RuntimeError(f"PR #{number} changed while it was being fetched; retry later")
    base = git("rev-parse", remote_base).decode().strip()
    ancestor = git("merge-base", base, head).decode().strip()
    changes = git("diff", "--no-renames", "--name-status", ancestor, head).splitlines()
    if changes != [b"M\tlearners.txt"]:
        print(f"Skipping PR #{number}: it must change only learners.txt", flush=True)
        return
    old, current, proposed = (read_regular_file(rev) for rev in (ancestor, base, head))
    if not lines_are_preserved(old, proposed):
        print(f"Skipping PR #{number}: existing lines must be preserved in order", flush=True)
        return

    welcome(repo, number, pull["user"]["login"])
    merge = run("git", "merge-tree", "--write-tree", base, head, check=False)
    if merge.returncode == 0:
        api(
            f"repos/{repo}/pulls/{number}/merge", "-X", "PUT",
            "-f", f"sha={head}", "-f", "merge_method=merge",
            "-f", f"commit_title=Merge learner submission #{number}",
            "-f", "commit_message=Merge learner submission.",
        )
        print(f"Merged PR #{number} through GitHub", flush=True)
        return
    if merge.returncode != 1:
        raise RuntimeError(f"Cannot calculate merge for PR #{number}: {merge.stderr.decode(errors='replace')}")

    merge_tree = merge.stdout.splitlines()[0].decode()
    contents = union_contents(old, current, proposed)
    tree = resolved_tree(base, merge_tree, contents)
    latest = api(f"repos/{repo}/pulls/{number}")
    if (
        latest["state"] != "open" or latest["draft"] or latest["head"]["sha"] != head
        or latest["base"]["ref"] != base_branch
    ):
        raise RuntimeError(f"PR #{number} changed before merging; retry later")
    env = os.environ.copy()
    env.update({
        "GIT_AUTHOR_NAME": "github-actions[bot]",
        "GIT_AUTHOR_EMAIL": "41898282+github-actions[bot]@users.noreply.github.com",
        "GIT_COMMITTER_NAME": "github-actions[bot]",
        "GIT_COMMITTER_EMAIL": "41898282+github-actions[bot]@users.noreply.github.com",
    })
    commit = git(
        "commit-tree", tree, "-p", base, "-p", head,
        "-m", f"Merge learner submission #{number}", env=env,
    ).decode().strip()
    git("push", "origin", f"{commit}:refs/heads/{base_branch}")
    print(f"Merged PR #{number} with both sides of the conflict", flush=True)


def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    base_branch = os.environ["BASE_BRANCH"]
    git("check-ref-format", "--branch", base_branch)
    pages = api(f"repos/{repo}/pulls?state=open&per_page=100", "--paginate", "--slurp")
    failed = False
    for pull in (pull for page in pages for pull in page):
        try:
            process(repo, base_branch, pull["number"])
        except (RuntimeError, ValueError, KeyError) as error:
            print(f"PR #{pull['number']}: {error}", file=sys.stderr, flush=True)
            failed = True
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
