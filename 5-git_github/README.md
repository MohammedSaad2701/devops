# Git and GitHub Basics

This exercise demonstrates a simple Git workflow: create a repository, save changes with commits, work on a feature branch, and inspect the project history.

## Repository and commits

Start a repository and record file changes with commits:

```bash
git init
git add <file>
git commit -m "message"
git log --oneline
```

The example includes an initial README commit, updates to `file.txt`, and three commits to `main.txt`.

![Repository initialization and commits](screenshots/Screenshot%202026-09-03%20at%2011.46.14%E2%80%AFAM.png)

## Branches

Branches allow work to continue separately from `main`:

```bash
git checkout -b feature
git add feature.txt
git commit -m "Feature commit"
git branch
git log --oneline --all
```

The `feature` branch contains its own commits in `feature.txt`, while `main` keeps its original history.

![Feature branch history](screenshots/Screenshot%202026-09-03%20at%2011.46.29%E2%80%AFAM.png)

## Cherry-pick and conflicts

`git cherry-pick <commit>` copies one commit onto the current branch. If the same file changed in both branches, Git may report a conflict that must be resolved before continuing.

```bash
git checkout main
git cherry-pick <commit>
git add <resolved-file>
git cherry-pick --continue
```

The final screenshot shows the feature history and a cherry-pick conflict involving `feature.txt`.

![Cherry-pick conflict and history](screenshots/Screenshot%202026-09-03%20at%2011.48.19%E2%80%AFAM.png)

## Key takeaway

Commits save project versions, branches isolate new work, and Git history helps track changes. Conflicts happen when changes overlap and must be resolved manually.