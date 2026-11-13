## **Code Review**

### **1. What is Code Review?**

Code review is the process of examining someone else's proposed changes before they get merged into a project. On GitHub, this happens on the Pull Request itself, reviewers read the diff, leave comments, and decide whether the change is ready to merge, needs work, or shouldn't be merged at all.

### **2. What to Look For When Reviewing**

- **Correctness**: does the code actually do what it claims to do
- **Readability**: can someone else understand this code six months from now
- **Scope**: does the PR stay focused on one thing, or does it wander
- **Style**: does it follow the project's existing conventions
- **Tests**: are the changes covered, if the project expects tests

### **3. The Three Review Verdicts**

Every PR review on GitHub ends in one of three states:

- **Comment**: general feedback, no explicit approval or rejection
- **Approve**: the change is good to merge as is
- **Request changes**: something needs to be fixed before this can be merged

### **4. Leaving Review Comments**

Comments can be left on specific lines of the diff, or as a general comment on the PR as a whole. Good review comments are specific, kind, and explain the "why" behind a suggested change, not just "fix this."

### **5. Resolving Review Comments**

As the PR author, once you've addressed a comment, either by pushing a fix or replying with context, mark that conversation as **Resolved**. This keeps the PR clean and tells the reviewer exactly what's left to check versus what's already handled.

### **6. Re-requesting Review**

After pushing fixes for requested changes, re-request a review from the same reviewer instead of assuming they'll notice on their own. This is what actually pulls the PR back onto their radar.

### **7. Merging a Pull Request: The Three Options**

GitHub gives you three ways to merge a PR, and the choice matters for how your project's history looks:

- **Merge commit**: keeps every individual commit from the PR, plus adds one new merge commit tying it all together. Preserves full history but can get noisy.
- **Squash and merge**: combines every commit in the PR into a single, clean commit on the target branch. Most common choice for open source projects, keeps history readable.
- **Rebase and merge**: replays each commit from the PR individually onto the target branch, no merge commit at all. Keeps history linear but preserves individual commits.

### **8. Which One Should You Use?**

Most open source projects default to **squash and merge**, especially for contributions with messy or exploratory commit history, one contributor, one clean commit. Save merge commits or rebase merges for projects with strict commit conventions that specifically ask for them, check the project's CONTRIBUTING guide if unsure.

### **9. Key Takeaways**

1. Code review happens directly on the PR, through comments, approvals, and change requests
2. Good reviews check correctness, readability, scope, style, and tests, not just "does it work"
3. Resolve comments as you address them, and re-request review after pushing fixes
4. Squash and merge is the most common choice for open source, keeping history clean and readable

---

### **Homework**

1. Find an open Pull Request on any public repository and read through it end to end, notice what reviewers commented on
2. On your own practice PR from Part 6, leave a review comment on it yourself, then resolve it, just to feel the full loop once
3. **Build in Public**: Post one thing you learned about code review on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 7 on YouTube](#)

Make sure to subscribe to the channel for more tutorials and updates!