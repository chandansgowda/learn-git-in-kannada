## **Git vs GitHub, and Your First Push**

### **1. Git vs GitHub**

This is the single most confused pair of terms for beginners, so let's be precise about it.

**Git** is the version control tool itself. It runs entirely on your machine, tracks every commit, branch, and change you make, and needs zero internet connection to work. Everything you've done in Parts 2 to 4, init, add, commit, branch, merge, all of it happened purely on your laptop.

**GitHub** is a website that hosts Git repositories online. It takes your local Git history and puts a copy of it on the internet, then adds a layer of collaboration features on top: pull requests, issues, code review, project boards, and a social layer where developers can find and follow each other's work.

Git is not GitHub, and GitHub is not Git. GitHub is simply one company's product built around Git, similar to how GitLab and Bitbucket are also products built around Git. You could use Git your entire life and never touch GitHub. But since almost every open source project lives on GitHub, that's where this series is headed next.

### **2. Creating a GitHub Account**

- Go to [github.com](https://github.com) and sign up
- Pick a clean, professional username, this is your public identity as a developer
- Verify your email

### **3. Setting Up Your Profile**

- Add a profile photo
- Add a bio, short line about what you do or are learning
- Add your location and a link (portfolio, LinkedIn, X)
- Pin a few repositories you're proud of to your profile

### **4. Creating a Good Profile README**

GitHub has a special, lesser-known feature: a README that lives on your profile page itself, not inside any repository. This is the first thing anyone sees the moment they visit your GitHub profile, before they even look at a single repo of yours.

To set it up, create a new repository with the exact same name as your GitHub username, for example if your username is `chandansgowda`, the repo is named `chandansgowda`. Make it public, and check the box to initialize it with a README. GitHub recognizes this special naming and automatically renders that README's content directly on your profile page.

A good profile README typically includes:

- **A short intro**, who you are and what you do or are learning
- **Your current focus**, what you're building or studying right now
- **Skills and tech stack**, languages, frameworks, tools you work with
- **How to reach you**, links to LinkedIn, X, portfolio, or email
- **Stats or badges**, GitHub often supports widgets showing your activity, top languages, or contribution streaks

This is entirely optional in terms of GitHub functioning, nothing breaks without it, but it's one of the easiest ways to make your profile look put together when a recruiter, collaborator, or fellow open source contributor lands on it.

### **5. Creating a Repository on GitHub**

- New repository, name it, add a description, choose public or private
- Do not initialize with a README if you already have a local project, this avoids conflicts when connecting

### **6. Connecting Local to Remote**

A "remote" is simply a saved address that tells your local Git repository where its online copy lives on GitHub. Right now, your local repo from Parts 2 to 4 and your new GitHub repo have no idea the other exists, this step is what links them together.

You only need to set this up once per project:

```
git remote add origin https://github.com/username/repo-name.git
```

Here, `origin` is just a nickname for that GitHub URL, it's the convention almost everyone uses. To confirm the link worked:

```
git remote -v
```

This should show your GitHub URL listed for both fetch and push.

### **7. Push: Sending Your Code to GitHub**

Pushing is how your local commits actually travel up to GitHub. Everything you've committed so far only exists on your machine, push is what makes it public and shareable.

```
git push -u origin main
```

The `-u` flag links your local `main` branch to the remote one permanently, so every push after this first one is just `git push`, nothing more to type.

The first time you push, GitHub will ask you to authenticate. Use your GitHub username along with a **personal access token**, not your account password, GitHub stopped accepting plain passwords for this a while back. You can generate a token from GitHub's developer settings, and it works exactly like a password for these operations.

### **8. Pull: Getting Updates from GitHub**

Pull is the reverse of push, it brings changes from GitHub down into your local repository.

```
git pull
```

This matters the moment you're not the only one touching a repository, or if you edited something directly on GitHub's website. Get into the habit of pulling before you start any new work session, so you're always building on top of the latest version instead of an outdated one.

### **9. Key Takeaways**

1. Git runs locally, GitHub hosts it online and adds collaboration on top
2. A strong GitHub profile, including a profile README, is how other developers and recruiters judge you at a glance
3. `git remote add origin` connects your local repo to GitHub, only needs to be done once
4. `git push` sends your commits up, `git pull` brings changes down

---

### **Homework**

1. Create your GitHub account and fully fill out your profile, photo, bio, and pinned repos
2. Create your special profile README repository and write a short intro about yourself
3. Push your practice repository from Part 2-4 to GitHub
4. **Build in Public**: Post your GitHub profile link on LinkedIn/X with #engineeringinkannada and tag me so I can see it

### **YouTube Reference**

Watch the following video from my channel:

- [Watch Part 5 on YouTube](#) <!-- add video link once published -->

Make sure to subscribe to the channel for more tutorials and updates!