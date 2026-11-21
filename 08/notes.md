## **Git Inside the IDE**

### **1. Why Use Git Inside Your Editor**

Everything covered so far, `add`, `commit`, branching, merging, push, pull, PRs, has been done through the terminal. That's essential to understand what's actually happening under the hood. But in daily work, most developers do a large chunk of this directly inside their code editor, since it's faster and shows changes visually instead of as text output.

This video is a demo-first walkthrough inside VS Code, showing where every command from Parts 2 to 7 lives in the UI. These notes are a reference to look back at, not a replacement for watching the demo.

### **2. The Source Control Panel**

VS Code has Git built in natively, no extension needed. The **Source Control** icon in the left sidebar (the branching icon) opens a panel showing every changed file in your repository, grouped by staged and unstaged changes.

### **3. Staging and Committing from the UI**

- Hovering over a file shows a **+** icon, this stages it, equivalent to `git add`
- Staged files move into their own section in the panel
- Typing a message in the box at the top and hitting the checkmark commits, equivalent to `git commit -m`
- You can stage and commit individual files, or all changes at once

### **4. Viewing Diffs Visually**

Clicking any changed file in the Source Control panel opens a side-by-side diff view, red for removed lines, green for added ones. This is the visual equivalent of `git diff`, and it's far easier to read than terminal output for larger changes.

### **5. Branching from the Status Bar**

The bottom-left corner of VS Code always shows your current branch name. Clicking it opens a branch switcher where you can switch branches or create a new one, equivalent to `git checkout -b`.

### **6. Resolving Merge Conflicts in the Editor**

When a conflict happens, VS Code highlights the conflicting section directly in the file with color-coded blocks and inline buttons, **Accept Current Change**, **Accept Incoming Change**, or **Accept Both**. This is the same conflict you saw in the terminal in Part 4, just with buttons instead of manually editing conflict markers.

### **7. Push and Pull from the UI**

The **sync** icon in the status bar, next to your branch name, handles both push and pull in one click, pulling any new commits and pushing yours in sequence. The `...` menu in the Source Control panel also has explicit **Push** and **Pull** options if you want them separate.

### **8. GitHub Integration: PRs and Reviews Inside VS Code**

With the **GitHub Pull Requests** extension installed, you can do everything from Parts 6 and 7 without leaving the editor:

- Create a Pull Request directly from a pushed branch
- View the full list of open PRs on a repository
- Read the diff of a PR inline
- Leave review comments directly on lines of code
- Approve, request changes, or merge, including choosing squash, merge commit, or rebase

### **9. Key Takeaways**

1. VS Code has Git built in, the Source Control panel covers staging, committing, and diffs without touching the terminal
2. Branch switching and creation happens from the status bar at the bottom-left
3. Merge conflicts show up as color-coded blocks in the editor, with one-click resolution buttons
4. The GitHub Pull Requests extension brings PR creation and code review directly into the IDE

---

### **Homework**

1. Redo the full commit cycle from Part 3, staging, committing, viewing a diff, entirely through the Source Control panel, no terminal
2. Install the GitHub Pull Requests extension and open your practice PR from Part 6 directly inside VS Code
3. **Build in Public**: Post a screenshot of your Source Control panel mid-commit on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 8 on YouTube](#)

Make sure to subscribe to the channel for more tutorials and updates!