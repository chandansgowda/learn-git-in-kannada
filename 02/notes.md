## **Installing Git and Your First Repository**

### **1. Installing Git on Your System**

- **Windows**: Download the installer from [git-scm.com](https://git-scm.com), run it, and the default settings are fine for beginners
- **Mac**: Use Homebrew, `brew install git`, or install it via Xcode Command Line Tools
- **Linux**: `sudo apt install git` on Debian/Ubuntu, or the equivalent package manager command for your distro
- Verify it worked by running `git --version` in your terminal

### **2. Terminal Basics You Actually Need**

You don't need to master the terminal, just these five commands:

- `pwd` - shows which folder you're currently in
- `cd foldername` - moves into a folder
- `cd ..` - moves up one level
- `ls` (Mac/Linux) or `dir` (Windows) - lists files in the current folder
- `mkdir foldername` - creates a new folder

That's the entire terminal literacy required before Git becomes usable.

### **3. Creating Your First Repository**

#### **Step 1: Create and enter a folder**

```
mkdir my-first-repo
cd my-first-repo
```

#### **Step 2: Initialize Git**

```
git init
```

This creates a hidden `.git` folder inside your project. That folder is where Git stores your entire project history. Nothing is tracked yet, this step just turns a normal folder into a Git repository.

#### **Step 3: Check the status**

```
git status
```

Git will tell you it's an empty repository with nothing to commit yet. That's expected, we'll fix that in Part 3.

### **4. Setting Up Your Git Identity**

Every commit you ever make needs an author attached to it. Set this up once, and Git remembers it:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### **5. Key Takeaways**

1. Git works identically on Windows, Mac, and Linux once installed, only the install step differs
2. You only need a handful of terminal commands to get started, not a full command line course
3. `git init` turns any folder into a Git repository by creating a hidden `.git` folder
4. Your Git identity (name and email) needs to be set up once, before your first commit

---

### **Homework**

1. Install Git on your system and confirm it with `git --version`
2. Create a folder, run `git init` inside it, and take a screenshot of the output
3. **Build in Public**: Post your `git init` screenshot on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 2 on YouTube](#)

Make sure to subscribe to the channel for more tutorials and updates!