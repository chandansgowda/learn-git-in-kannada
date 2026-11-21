## **The Commit Cycle**

### **1. What is a Commit?**

A commit is a snapshot of your project at a specific point in time. Every time you make progress, big or small, you save that progress as a commit. Over time, this builds a complete history of your project that you can look back through or return to at any point.

Think of commits as checkpoints in a game. If something breaks later, you always have a checkpoint to go back to.

### **2. Checking What's Changed: git status**

Before doing anything else, always check what state your project is in:

```
git status
```

This tells you which files are new, which are modified, and which are already tracked. Get into the habit of running this constantly, it's the command you'll use the most.

### **3. Staging Changes: git add**

Staging is how you tell Git "I want this change to be part of my next commit."

```
git add filename.txt
```

To stage everything in the project at once:

```
git add .
```

Staging is a separate step from committing on purpose. It lets you pick exactly which changes go into a commit, instead of dumping every change into one.

### **4. Saving a Snapshot: git commit**

Once changes are staged, commit them with a message describing what you did:

```
git commit -m "Add homepage layout"
```

A good commit message is short, clear, and describes what changed, not how you felt about it. "Fix login bug" is a good message. "Fixed stuff" is not.

### **5. Viewing History: git log**

To see every commit you've made so far:

```
git log
```

This shows the commit message, author, date, and a unique ID for each commit. For a shorter view:

```
git log --oneline
```

### **6. Seeing Exact Changes: git diff**

Before staging, you can see exactly what changed line by line:

```
git diff
```

This shows additions and deletions in a file since the last commit, which is useful for double checking your changes before committing them.

### **7. The Full Cycle, Put Together**

This is the loop you'll repeat constantly, in every project, for the rest of your coding life:

1. Make a change to your code
2. `git status` to see what changed
3. `git diff` to review the exact changes
4. `git add` to stage what you want to commit
5. `git commit -m "message"` to save the snapshot
6. `git log` to confirm it's there

### **8. Key Takeaways**

1. A commit is a saved snapshot of your project you can always return to
2. `git add` stages changes, `git commit` saves them, they are two separate steps on purpose
3. `git log` shows your full project history, `git diff` shows exact line-by-line changes
4. This add, commit, log cycle is the single most repeated workflow in Git, get comfortable with it before moving forward

---

### **Homework**

1. In your practice repository, make three separate commits, each with a meaningful message describing what changed
2. Run `git log --oneline` and take a screenshot of your commit history
3. Make one change to a file, run `git diff` before staging it, and see what the output looks like
4. **Build in Public**: Post your commit history screenshot on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 3 on YouTube](#)

Make sure to subscribe to the channel for more tutorials and updates!