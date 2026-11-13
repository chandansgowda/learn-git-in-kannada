## **Advanced Git I: Rebase and Stash**

### **1. What is Rebase?**

Rebase is another way to combine changes from one branch into another, an alternative to `git merge`. Where merge creates a new commit that ties two branches together, rebase takes the commits from your branch and replays them one by one on top of the latest version of the target branch, as if you had written them there from the start.

```
git checkout feature-branch
git rebase main
```

This moves the base of `feature-branch` from wherever it originally branched off, to the current tip of `main`, then reapplies each of your commits on top, one at a time.

### **2. Rebase vs Merge: What Actually Changes**

Both achieve the same end goal, bringing changes from one branch into another, but they produce very different history.

- **Merge** preserves exactly what happened, including a merge commit showing where two branches came together. History branches and reconnects, like a real tree.
- **Rebase** rewrites history to look like a straight line, as if you'd built your feature directly on top of the latest `main`, with no branching visible at all.

Neither is "correct", they're different philosophies. Merge keeps an honest record of what really happened. Rebase keeps history clean and linear, easier to read but technically rewritten.

### **3. The Golden Rule of Rebase**

Never rebase commits that have already been pushed and that other people might be working off of. Since rebase rewrites commit history, doing this on a shared branch can cause serious confusion and broken histories for anyone else who already has the old version. Rebase is safe on your own local, unpushed, unshared branches. Once something is shared, use merge instead.

### **4. Handling Conflicts During a Rebase**

Just like merging, a rebase can hit conflicts, if two branches changed the same lines. Git pauses mid-rebase and lets you resolve the conflict in the file, same as Part 4. Once resolved:

```
git add .
git rebase --continue
```

If it all goes wrong, you can back out entirely:

```
git rebase --abort
```

This returns your branch to exactly how it was before you started the rebase.

### **5. What is Stash?**

Stash is for a very specific, very common situation: you're in the middle of changes, they're not ready to commit, but you suddenly need to switch branches, maybe to fix an urgent bug elsewhere. Git won't let you switch branches cleanly with uncommitted changes sitting in your way. Stash temporarily shelves those changes so your working directory is clean again.

```
git stash
```

This saves your uncommitted changes aside and reverts your working directory back to the last commit. You're now free to switch branches, pull, or do whatever you needed to do.

### **6. Bringing Stashed Changes Back**

Once you're ready to return to what you were doing:

```
git stash pop
```

This reapplies your stashed changes back into your working directory, and removes them from the stash list. If you want to reapply without removing them from the stash, use `git stash apply` instead.

### **7. Managing Multiple Stashes**

You can stash more than once, Git keeps them in a list:

```
git stash list
```

Each entry is labeled by index, `stash@{0}`, `stash@{1}`, and so on, most recent first. You can pop or apply a specific one by referencing its index if you have more than one stashed at a time.

### **8. Key Takeaways**

1. Rebase replays your commits on top of another branch, producing linear history, unlike merge which preserves branching history with a merge commit
2. Never rebase commits that have already been pushed and shared with others, only rebase your own local, unpushed work
3. `git stash` temporarily shelves uncommitted changes so you can switch branches cleanly, `git stash pop` brings them back
4. Both rebase conflicts and stash pop conflicts are resolved the same way you already know from Part 4

---

### **Homework**

1. Create a branch, make two commits on it, then rebase it onto `main` and observe how the history looks with `git log --oneline` compared to a merge from Part 4
2. Make an uncommitted change, stash it, switch branches, switch back, and pop it to bring it back
3. **Build in Public**: Post a before-and-after screenshot of your commit history, merge vs rebase, on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 9 on YouTube](#)

Make sure to subscribe to the channel for more tutorials and updates!