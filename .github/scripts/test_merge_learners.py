import contextlib
import importlib.util
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock


spec = importlib.util.spec_from_file_location(
    "merge_learners", Path(__file__).with_name("merge_learners.py")
)
merger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(merger)


class LearnerMergeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.repo = root / "work"
        self.repo.mkdir()
        self.remote = root / "remote.git"
        self.git("init", "--bare", "-q", str(self.remote))
        self.git("init", "-q", str(self.repo))
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        self.git("remote", "add", "origin", str(self.remote))
        self.write("learners.txt", "Welcome\n")
        self.git("add", "learners.txt")
        self.git("commit", "-qm", "Initial")
        self.git("branch", "-M", "main")
        self.git("checkout", "-qb", "submission")
        self.write("learners.txt", "Welcome\nBob\n")
        self.git("commit", "-qam", "Add Bob")
        self.head = self.git("rev-parse", "HEAD").strip()
        self.git("checkout", "-q", "main")
        self.write("learners.txt", "Welcome\nAlice\n")
        self.git("commit", "-qam", "Add Alice")
        self.git("push", "-q", "origin", "main", f"{self.head}:refs/pull/42/head")
        self.pull = {
            "number": 42, "state": "open", "draft": False,
            "base": {"ref": "main"}, "head": {"sha": self.head},
            "user": {"login": "learner"},
        }

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], cwd=self.repo, stderr=subprocess.PIPE, text=True
        )

    def write(self, name, contents):
        (self.repo / name).write_text(contents)

    @contextlib.contextmanager
    def in_repo(self):
        previous = os.getcwd()
        os.chdir(self.repo)
        try:
            yield
        finally:
            os.chdir(previous)

    def test_conflicting_submissions_preserve_both_and_welcome_author(self):
        calls = []

        def fake_api(path, *args):
            calls.append((path, args))
            if path.endswith("/pulls/42"):
                return self.pull
            if path.endswith("/issues/42/comments") and "--paginate" in args:
                return [[]]
            return {}

        with self.in_repo(), mock.patch.object(merger, "api", side_effect=fake_api):
            merger.process("owner/repo", "main", 42)

        contents = self.git("--git-dir", str(self.remote), "show", "main:learners.txt")
        self.assertIn("Alice\n", contents)
        self.assertIn("Bob\n", contents)
        parents = self.git("--git-dir", str(self.remote), "rev-list", "--parents", "-n", "1", "main").split()
        self.assertEqual(len(parents), 3)
        self.assertEqual(parents[2], self.head)
        message = self.git("--git-dir", str(self.remote), "log", "-1", "--format=%B", "main")
        self.assertNotIn("Co-authored-by:", message)
        self.assertTrue(any("@learner" in " ".join(args) for _, args in calls))

    def test_pr_with_another_file_is_not_merged_or_welcomed(self):
        self.git("checkout", "-q", "submission")
        self.write("other.txt", "unrelated")
        self.git("add", "other.txt")
        self.git("commit", "-qm", "Add unrelated file")
        self.head = self.git("rev-parse", "HEAD").strip()
        self.pull["head"]["sha"] = self.head
        self.git("push", "-q", "--force", "origin", f"{self.head}:refs/pull/42/head")
        with self.in_repo(), mock.patch.object(merger, "api", return_value=self.pull) as api:
            merger.process("owner/repo", "main", 42)
        self.assertEqual(api.call_count, 1)

    def test_mergeable_submission_uses_github_merge_with_expected_head(self):
        self.write("learners.txt", "Welcome\n")
        self.git("commit", "-qam", "Remove concurrent addition")
        self.git("push", "-q", "origin", "main")
        calls = []

        def fake_api(path, *args):
            calls.append((path, args))
            if path.endswith("/pulls/42"):
                return self.pull
            if path.endswith("/issues/42/comments") and "--paginate" in args:
                return [[{
                    "body": merger.MARKER,
                    "user": {"login": "github-actions[bot]"},
                }]]
            return {}

        with self.in_repo(), mock.patch.object(merger, "api", side_effect=fake_api):
            merger.process("owner/repo", "main", 42)
        merge_calls = [(path, args) for path, args in calls if path.endswith("/merge")]
        self.assertEqual(len(merge_calls), 1)
        self.assertIn(f"sha={self.head}", merge_calls[0][1])
        self.assertEqual(sum(path.endswith("/issues/42/comments") for path, _ in calls), 1)

    def test_removed_existing_line_is_not_eligible(self):
        self.assertFalse(merger.lines_are_preserved(b"First\nSecond\n", b"First\nNew\n"))
        self.assertTrue(merger.lines_are_preserved(b"First\nSecond\n", b"First\nNew\nSecond\n"))

    def test_union_preserves_multiple_conflicting_insertions(self):
        result = merger.union_contents(
            b"First\nMiddle\nLast\n",
            b"First\nAlice\nMiddle\nCarol\nLast\n",
            b"First\nBob\nMiddle\nDave\nLast\n",
        )
        for name in (b"Alice", b"Bob", b"Carol", b"Dave"):
            self.assertIn(name + b"\n", result)


if __name__ == "__main__":
    unittest.main()
