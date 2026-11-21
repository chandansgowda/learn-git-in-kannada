## **Clone, Fork, and Pull Requests**

### **1. Clone: Getting a Repository onto Your Machine**

Cloning is how you download a full copy of any GitHub repository onto your own computer, complete with its entire commit history, not just the latest files.

```
git clone https://github.com/username/repo-name.git
```

This creates a new folder with the project inside it, already set up as a Git repository with `origin` pointing back to that GitHub URL. This is different from `git init`, which starts a brand new empty repository. Cloning is what you do when a repository already exists and you want your own working copy of it.

### **2. The Problem: You Can't Push to Someone Else's Repo**

Here's something every beginner runs into immediately. If you clone someone else's open source project and try to make changes, you'll find you have no permission to push those changes back to their repository. And that's exactly how it should be, imagine if anyone on the internet could push code directly into a project like React or VS Code.

So how does open source collaboration actually work if you can't directly edit someone else's repo? That's exactly what forking solves.

### **3. Fork: Your Own Copy of Someone Else's Repository**

A fork is a complete copy of someone else's repository, made under your own GitHub account. It's not a local copy like a clone, it's a new repository that lives on GitHub, in your namespace, that you have full write access to.

To fork a repo, go to the original repository on GitHub and click the **Fork** button in the top right. GitHub creates `your-username/repo-name` as a new repository, a full copy of the original, including its history.

### **4. Clone Your Fork, Not the Original**

Once you've forked a repository, you clone your fork, not the original project, since that's the one you actually have write access to:

```
git clone https://github.com/your-username/repo-name.git
```

Now you have a local copy of your fork, connected to your fork as `origin`, which you can freely commit and push to.

### **5. The Fork Workflow, Put Together**

This is the complete loop for contributing to any open source project you don't have direct write access to:

1. Fork the original repository on GitHub
2. Clone your fork locally
3. Create a new branch for your change (Part 4)
4. Make your changes and commit them
5. Push the branch to your fork
6. Open a Pull Request from your fork back to the original repository

### **6. What is a Pull Request?**

A Pull Request, or PR, is a formal request asking the maintainers of the original repository to pull your changes into their project. It's not automatic, a maintainer reviews what you've done, may ask for changes, and only merges it once they're satisfied.

To open one: push your branch to your fork, then go to the original repository on GitHub, it usually shows a banner suggesting you open a PR from your recently pushed branch. Alternatively, use the **Contribute** or **Pull Requests** tab and click **New Pull Request**.

### **7. Writing a Good Pull Request**

- **A clear title**, describing what the PR does in one line
- **A description**, explaining what changed and why, and linking any related issue
- **Small, focused changes**, a PR that does one thing is far more likely to get merged than one touching twenty files at once

### **8. Key Takeaways**

1. `git clone` downloads a full copy of an existing repository, including its history
2. You can't push directly to a repository you don't own, forking gives you your own writable copy on GitHub
3. The fork workflow is: fork, clone your fork, branch, commit, push to your fork, then open a PR to the original
4. A Pull Request asks a maintainer to review and merge your changes, it's a conversation, not an automatic action

---

### **Homework**

1. Fork any small public repository on GitHub, and clone your fork locally
2. Make a small change on a new branch, push it to your fork, and open a Pull Request back to the original repository, even a typo fix in a README is a perfectly valid first PR
3. **Build in Public**: Post a screenshot of your open Pull Request on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 6 on YouTube](#)

Make sure to subscribe to the channel for more tutorials and updates!