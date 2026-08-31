# <h1 align="center"> MLCoE Probation </h1>

Welcome to the MLCoE Apprenticeship Program!

This repository is where you will maintain and submit your tasks throughout the probation period. The probation is not just about completing tasks — it is an opportunity to learn, explore, demonstrate your skills, and understand how we work together as a team.

#### What is the Probation Period?

The probation period is the initial phase of your journey with MLCoE, where you will be given a series of tasks and activities designed to understand your:

- Technical skills and problem-solving ability
- Learning attitude and willingness to explore
- Consistency and responsibility
- Communication and teamwork
- Ability to take feedback and improve
- Interest in contributing to the society and its projects

You are not expected to know everything from the beginning. The purpose of this period is to learn, experiment, ask questions, and gradually improve.

---


## Important: Folder Ownership Rule

Every Apprentice have to create their **own dedicated folder** in this repository. You must:

-  Work **only** inside your own folder.
-  **Never** modify, delete, rename, or move files inside another Apprentice's folder — even by accident.

>  **Warning:** Any unnecessary or unauthorized change to another Apprentice's folder may directly affect their probation evaluation. Please double-check your changes before every commit and pull request.

---

<br><br>


## Repository Structure

Each Apprentice has a separate folder containing their tasks and projects:

```
MLCoE Probation'26/
├── Aman-Verma/
│   ├── Task-0/
│   ├── Task-1/
│   └── Task-2/
├── Rahul-Sharma/
│   ├── Task-0/
│   └── Task-1/
└── ...
```

Create a folder with your name → work only inside that folder.

---

<br><br>


## Submission Workflow

You will **not** have direct write access to this repository. All work must go through a **Fork → Branch → Pull Request** process.

```
Fork  →  Clone  →  Branch  →  Work  →  Commit  →  Push  →  Pull Request  →  Review  →  Merge
```
<br>

### Step-by-Step Guide

1. **Fork** this repository (creates your own copy on GitHub).
2. **Clone** your fork to your computer.
   ```
   git clone <your-fork-url>
   ```
3. **Create a new branch** for your task (never work directly on `main`).
   ```
   git switch -c aman/task-0
   ```
4. **Work only inside your own folder.**
5. **Complete** the assigned task.
6. **Check your changes** before staging them.
   ```
   git status
   git diff
   ```
7. **Stage your changes.**
   ```
   git add .
   ```
8. **Commit** with a clear, meaningful message.
   ```
   git commit -m "Add Task-0 - Aman Verma"
   ```
9. **Push** your branch to your fork.
   ```
   git push origin aman/task-0
   ```
10. **Create a Pull Request (PR)** from your branch to the `main` branch of the **original MLCoE repository**.
11. **Wait for review** from the MLCoE team.
12. If changes are requested, **make corrections on the same branch** and push again.
    ```
    git add .
    git commit -m "Address review comments"
    git push
    ```
    > Do **not** create a new PR for every correction — just update the same branch.
13. Once approved, the **MLCoE team will merge** your PR.

---

<br><br>


## Branch Naming Convention

Use this simple format:

```
your-name/task-number
```

**Examples:**
```
aman/task-0
aman/task-1
aman/task-2
```

---

<br><br>


## Commit Message Examples

```
Add Task-0 - Aman Verma
Address review comments
```

Keep messages short and clear about what you did.

---

<br><br>


## Pull Request Direction — Read Carefully

Your PR must always flow in this direction:

```
Your Fork + Your Branch
          ↓
Original MLCoE Repository + main
```

> **Before clicking "Create Pull Request", double-check the base repository and branch.** Creating a PR to the wrong destination can cause confusion during review.

---

<br><br>


## Important Rules

-  Work only in your own folder.
-  Do not work directly on `main`.
-  Do not modify another Apprentice's folder.
-  Do not push directly to the original repository.
-  Submit all work through Pull Requests.
-  Keep your files organized.
-  Do not upload unnecessary or sensitive files.
-  Check your changes carefully before creating a PR.

---

<br><br>


## Essential Git Commands

| Command | Purpose |
|---|---|
| `git clone` | Download the repository to your computer |
| `git status` | See what files have changed |
| `git branch` | List existing branches |
| `git switch -c <branch-name>` | Create and switch to a new branch |
| `git add .` | Stage your changes |
| `git commit -m "message"` | Save your changes with a message |
| `git push` | Upload your branch to your fork |
| `git pull` | Get the latest updates |
| `git diff` | See exact changes made in files |

---
<br><br>



## Before You Create a PR — Checklist

-  I worked only inside my own folder.
-  I created a separate branch.
-  I checked `git status`.
-  I checked `git diff`.
-  I committed my changes.
-  I pushed my branch.
-  My PR targets the original MLCoE repository's `main` branch.
-  My PR contains only my task-related changes.

---

Good luck with your tasks! If you're unsure about anything, reach out to the MLCoE team before making changes.
