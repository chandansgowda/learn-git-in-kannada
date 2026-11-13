## **Branching and Merging**

### **1. What is a Branch?**

A branch is an independent line of development inside your project. Every repository starts with one branch, usually called `main`, but you're never limited to just that one.

Think of your project as a tree. `main` is the trunk, always stable, always working. Every new feature or experiment gets its own branch, a separate limb growing off the trunk, so you can work on it without touching the stable version.

### **2. Why Branches Matter**

Without branches, everyone works directly on the same version of the code, at the same time. That means:

- Half-finished, broken code sits in the same place as working code
- One person's experiment can break another person's work
- There's no clean way to try something risky and throw it away if it doesn't work

Branches solve all of this. You can build a feature, break things, experiment freely, and none of it touches `main` until you're ready.

### **3. Creating and Switching Branches**

To create a new branch:

```
git branch feature-login
```

To switch to it:

```
git checkout feature-login
```

Or do both in one step:

```
git checkout -b feature-login
```

To see every branch in your repository, and which one you're currently on:

```
git branch
```

### **4. Working on a Branch**

Once you're on a branch, everything works exactly like before, `git add`, `git commit`, `git log`. The only difference is that these commits now belong to `feature-login`, not `main`. `main` stays untouched until you decide to bring the changes back in.

### **5. Merging: Bringing Changes Back**

Once your feature is done and working, you bring it back into `main`.

```
git checkout main
git merge feature-login
```

This takes every commit from `feature-login` and applies it onto `main`. If nothing conflicting happened on `main` in the meantime, Git merges everything automatically.

### **6. What is a Merge Conflict?**

Sometimes Git can't automatically decide how to combine two branches, usually because the same line in the same file was changed differently on both. This is called a merge conflict, and Git will stop and ask you to resolve it manually.

When it happens, Git marks the conflicting section directly inside the file:

```
<<<<<<< HEAD
This is the version from main
=======
This is the version from feature-login
>>>>>>> feature-login
```

You edit the file to keep whichever version you want, or a combination of both, remove the conflict markers, then stage and commit the resolved file.

### **7. Why Every Beginner Should Cause a Conflict on Purpose**

Merge conflicts feel scary the first time they happen for real, usually mid-project, under pressure. That's the wrong time to see one for the first time. Create a small conflict deliberately, on a throwaway project, and resolve it once so the real one never catches you off guard.

### **8. Key Takeaways**

1. A branch is an independent line of development that keeps `main` stable while you build
2. `git checkout -b branchname` creates and switches to a new branch in one step
3. `git merge` brings the commits from one branch into another
4. A merge conflict happens when the same lines were changed differently on both branches, and Git needs you to resolve it manually

---

### **Homework**

1. Create a new branch called `practice-branch` in your repository and make two commits on it
2. Merge `practice-branch` back into `main` and confirm the changes are there with `git log`
3. Deliberately create a merge conflict: change the same line differently on two branches, try to merge, and resolve it by hand
4. **Build in Public**: Post a screenshot of your resolved merge conflict on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 4 on YouTube](#)

Make sure to subscribe to the channel for more tutorials and updates!