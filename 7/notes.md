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
## 10. Best Practices for Code Review

Follow these best practices when reviewing code:

- **Be respectful:** Give feedback politely and professionally.
- **Be specific:** Mention the exact line or section that needs improvement.
- **Explain why:** Describe why a change is necessary instead of simply saying it is wrong.
- **Keep reviews focused:** Review only the changes related to the Pull Request.
- **Check for security issues:** Look for exposed API keys, passwords, and sensitive information.
- **Avoid unnecessary changes:** Suggest improvements only when they provide real value.
- **Test the changes:** Run the code when possible to verify its behavior.

## 11. How to Review a Pull Request on GitHub

Follow these steps to review a Pull Request:

1. Open the repository on GitHub.
2. Click the **Pull requests** tab.
3. Open the Pull Request you want to review.
4. Click the **Files changed** tab.
5. Read the code changes carefully.
6. Click the **+** icon beside a line to add a comment.
7. Click **Review changes** when you finish reviewing.
8. Choose one of the following:
   - Comment
   - Approve
   - Request changes
9. Submit your review.

**Remember:** Approve only when you believe the changes are ready and meet the project's requirements.

## 12. Common Code Review Mistakes

Avoid these common mistakes during code review:

- Reviewing code without understanding its purpose.
- Approving code without checking the changes.
- Focusing only on formatting and ignoring logic errors.
- Writing rude or unclear comments.
- Ignoring missing tests or potential security problems.
- Requesting unnecessary changes that do not improve the code.
- Forgetting to review the updated code after fixes are submitted.

## 13. Example of a Good Code Review Comment

Consider this example:

**Code:**
```javascript
function calculateTotal(price, quantity) {
    return price * quantity;
}
```

**Review comment:**

"Could we validate the price and quantity before calculating the total? This would help prevent unexpected results when invalid values are provided."

**Why is this a good comment?**

- It identifies a possible issue.
- It explains why the change could be useful.
- It suggests an improvement politely.

## 14. Code Review vs. Testing

| Code Review | Software Testing |
|---|---|
| Examines code changes. | Executes code to check its behavior. |
| Can identify logic, readability, and design issues. | Can identify failures and unexpected outputs. |
| Usually involves human reviewers or automated analysis. | Uses manual or automated test cases. |
| Helps improve code quality before merging. | Helps verify that the software works as expected. |

Both practices are important for producing reliable software.

## 15. Useful GitHub Code Review Terms

- **Pull Request (PR):** A request to merge changes from one branch into another.
- **Diff:** A view showing the differences between two versions of a file.
- **Reviewer:** A person who examines proposed code changes.
- **Approval:** A review indicating that the changes are acceptable.
- **Review Comment:** Feedback about a particular code change.
- **Resolved Conversation:** A review discussion marked as addressed.
- **Merge Conflict:** A situation where Git cannot automatically combine certain changes.
- **CI/CD:** Automated workflows that can build, test, and deploy software.

## 16. Code Review Checklist

Before approving a Pull Request, check the following:

- [ ] Does the code solve the intended problem?
- [ ] Is the code readable and understandable?
- [ ] Does it follow the project's coding standards?
- [ ] Are errors and edge cases handled?
- [ ] Are appropriate tests included?
- [ ] Are there any security risks?
- [ ] Are unnecessary changes avoided?
- [ ] Does the code pass the required checks?

## 17. Final Practice Challenge

Practice reviewing a Pull Request in a repository you own or have permission to contribute to.

1. Create a new branch and make a small code change.
2. Commit the change and push the branch to GitHub.
3. Open a Pull Request.
4. Review the changes using the Files changed tab.
5. Add a review comment.
6. Fix the issue and push another commit.
7. Review the updated changes and merge the Pull Request when appropriate.

**Goal:** Understand the complete code review process, from creating a Pull Request to reviewing, fixing, and merging changes.

### **Homework**

1. Find an open Pull Request on any public repository and read through it end to end, notice what reviewers commented on
2. On your own practice PR from Part 6, leave a review comment on it yourself, then resolve it, just to feel the full loop once
3. **Build in Public**: Post one thing you learned about code review on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 7 on YouTube](#)

Make sure to subscribe to the channel for more tutorials and updates!