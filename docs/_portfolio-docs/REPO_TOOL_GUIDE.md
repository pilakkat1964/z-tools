---
title: "Repository Tool Guide"
permalink: /portfolio-docs/repository-tool-guide/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# Git Repo Tool for Z-Tools Portfolio Management

## Overview

The Google "repo" tool is a repository management system built on top of Git that facilitates managing multiple Git repositories as a cohesive project. It's used extensively in Android development and AOSP (Android Open Source Project) but is equally valuable for managing multi-project portfolios like z-tools.

### Why Repo for Z-Tools?

**Current State:**
- 4 separate GitHub repositories (z-edit, z-open, z-kitty-launcher, z-rclone-mount-applete)
- Manual coordination of commits across projects
- Separate version synchronization
- No unified branching strategy

**With Repo:**
- Single checkout command clones all projects
- Unified branching across all projects
- Synchronized version releases
- Single command to commit/push across all projects
- Manifest-based project configuration
- Built-in multi-repository operations

---

## Architecture Overview

### Three-Tier Structure

```
┌─────────────────────────────────────────────────────────┐
│  Z-Tools Manifest Repository                            │
│  (GitHub: pilakkat1964/z-tools)                          │
│  └─ Manifest Files (default.xml)                        │
│     └─ Branch: manifest (or main with docs/)            │
│                                                          │
│  Tracks all project repositories & revisions            │
└─────────────────────────────────────────────────────────┘
         ↓ (references)
┌────────────────────────────────────────┐
│ z-tools/                               │  (Local Workspace)
├─ .repo/                                │  (Created by repo init)
│  ├─ manifests/                         │
│  ├─ projects/                          │
│  └─ repo/                              │
├─ z-edit/                               │  (Synced projects)
├─ z-open/                               │
├─ z-kitty-launcher/                     │
└─ z-rclone-mount-applete/               │
         ↓ (refs)
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ z-edit       │ z-open       │z-kitty-     │z-rclone-     │
│ (GitHub)     │ (GitHub)     │launcher      │mount-applete │
│              │              │ (GitHub)     │ (GitHub)     │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

### Key Components

1. **Manifest Repository** (z-tools)
   - Central coordination point
   - Contains XML manifest files
   - Tracks all project repositories and their branches
   - Hosted on GitHub

2. **Manifest File** (default.xml)
   - XML configuration defining all projects
   - Specifies repositories, branches, revisions
   - Path mapping for local checkout
   - Synchronization rules

3. **Workspace** (.repo directory)
   - Created by `repo init`
   - Manages metadata and synchronization
   - Contains symlinks to manifests and projects

---

## Installation

### Prerequisites

```bash
# Python 3.6+ required
python3 --version

# Git must be installed
git --version

# curl for downloading repo
curl --version
```

### Install Repo Tool

```bash
# Create directory for repo binary
mkdir -p ~/.local/bin

# Download repo tool
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.local/bin/repo

# Make executable
chmod a+x ~/.local/bin/repo

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"

# Verify installation
repo --version
# Output: repo version 2.x.x
```

**For macOS using Homebrew:**
```bash
brew install repo
```

---

## Setting Up Z-Tools with Repo

### Step 1: Prepare Manifest Repository

The z-tools repository will serve as both the manifest repository and the root project.

```bash
# Option A: Use existing z-tools repository
git clone git@github.com:pilakkat1964/z-tools.git z-tools-manifest
cd z-tools-manifest

# Create manifest branch (or use existing 'manifest' branch)
git checkout -b manifest
# or: git checkout manifest  (if already exists)

# Create .gitignore for manifest-only content
cat > .gitignore << 'EOF'
# Local workspace (repo creates this)
.repo/

# Python cache
__pycache__/
*.pyc
.pytest_cache/

# IDE
.vscode/
.idea/
*.swp
EOF

git add .gitignore
git commit -m "chore: add .gitignore for manifest branch"
git push origin manifest
```

### Step 2: Create Default Manifest File

Create `default.xml` in the manifest repository:

```bash
# While on manifest branch
mkdir -p manifests
```

Create `manifests/default.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <!-- Remote repositories -->
  <remote  name="github"
           fetch="https://github.com/pilakkat1964"
           review="github.com" />

  <!-- Default branch and remote for all projects -->
  <default remote="github" revision="master" sync-j="4" />

  <!-- Z-Tools Root Project (manifest)
       This is the manifest repository itself
  -->
  <project path="."
           name="z-tools"
           remote="github"
           revision="manifest"
           groups="manifests" />

  <!-- Python Projects
       Synced to master branch
  -->
  <project path="z-edit"
           name="z-edit"
           remote="github"
           revision="master"
           groups="python,tools" />

  <project path="z-open"
           name="z-open"
           remote="github"
           revision="master"
           groups="python,tools" />

  <!-- Rust Projects
       Synced to master/main branch
  -->
  <project path="z-kitty-launcher"
           name="z-kitty-launcher"
           remote="github"
           revision="master"
           groups="rust,tools" />

  <project path="z-rclone-mount-applete"
           name="z-rclone-mount-applete"
           remote="github"
           revision="main"
           groups="rust,tools" />

  <!-- Groups for selective syncing:
       - python: Python projects (z-edit, z-open)
       - rust: Rust projects (z-kitty-launcher, z-rclone-mount-applete)
       - tools: All tool projects
       - manifests: Manifest repository
  -->
</manifest>
```

Commit and push:

```bash
git add manifests/default.xml
git commit -m "chore: add initial manifest for z-tools portfolio"
git push origin manifest
```

### Step 3: Initialize Repo Workspace

```bash
# Create workspace directory
mkdir ~/workspace/z-tools-repo
cd ~/workspace/z-tools-repo

# Initialize repo with manifest
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m manifests/default.xml

# Sync all projects
repo sync
```

This will:
1. Create `.repo/` directory
2. Clone the manifest repository
3. Clone all projects listed in the manifest
4. Set up tracking branches

### Step 4: Verify Installation

```bash
# Check repo status
repo status

# List all projects
repo list

# Show manifest file
repo manifest -r

# Show current branches
repo branches
```

---

## Manifest File Reference

### XML Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <!-- Define remote repositories -->
  <remote name="github"
          fetch="https://github.com/pilakkat1964"
          review="github.com" />

  <!-- Set defaults for all projects -->
  <default remote="github"
           revision="master"
           sync-j="4"
           dest-branch="master" />

  <!-- Define individual projects -->
  <project path="PROJECT_PATH"
           name="REPO_NAME"
           remote="REMOTE_NAME"
           revision="BRANCH"
           groups="GROUP1,GROUP2" />

  <!-- Include other manifest files -->
  <include name="manifests/other.xml" />
</manifest>
```

### Common Project Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `path` | Local checkout directory | `z-edit` |
| `name` | Repository name on server | `z-edit` |
| `remote` | Remote configuration to use | `github` |
| `revision` | Branch/tag/commit to track | `master`, `v1.0` |
| `groups` | Logical grouping for selective ops | `python,tools` |
| `upstream` | Upstream branch (if different) | `upstream/master` |
| `dest-branch` | Target branch for push | `master` |
| `clone-depth` | Shallow clone depth | `1` (for faster sync) |

### Remote Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `name` | Remote identifier | `github` |
| `fetch` | Base URL for cloning | `https://github.com/pilakkat1964` |
| `review` | Code review system | `github.com` |
| `pushurl` | Alternative push URL (optional) | `git@github.com:pilakkat1964` |

---

## Common Repo Workflows

### Initial Setup & Synchronization

```bash
# Create workspace
mkdir ~/z-tools-workspace
cd ~/z-tools-workspace

# Initialize repo
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m manifests/default.xml

# Download all projects
repo sync -j 4

# Verify all projects are present
repo list
repo status
```

### Creating a Feature Branch

**Scenario:** Develop a new feature across multiple projects

```bash
# Create feature branch in all projects
repo start feature/new-contribution-guide

# Verify branches created
repo branches

# Now each project is on the feature branch
# Make changes in any project:
cd z-edit
# ... edit files ...
git add CONTRIBUTING.md
git commit -m "feat: update contributing guidelines"

# Similarly in z-open:
cd ../z-open
# ... edit files ...
git add CONTRIBUTING.md
git commit -m "feat: update contributing guidelines"
```

### Synchronizing Changes Across Projects

```bash
# Update all projects to latest manifest revisions
repo sync

# See which projects have uncommitted changes
repo status

# See changes in all projects
repo forall -c git diff

# Stage changes in all projects
repo forall -c git add -A

# View commits in all projects
repo forall -c git log --oneline -5

# Show status with more detail
repo status -1
```

### Committing Across Multiple Projects

```bash
# Make changes in multiple projects
cd z-edit
# ... make changes ...
git add .
git commit -m "docs: improve CONTRIBUTING.md"

cd ../z-open
# ... make changes ...
git add .
git commit -m "docs: improve CONTRIBUTING.md"

cd ../z-kitty-launcher
# ... make changes ...
git add .
git commit -m "docs: improve CONTRIBUTING.md"

# Verify commits in all projects
repo forall -c git log --oneline -1

# Push all projects to remote
repo upload
# or: repo forall -c git push origin HEAD
```

### Releasing a New Version

```bash
# Create release branch
repo start release/v0.7.0

# Update version numbers in each project
cd z-edit && vim pyproject.toml zedit.py && git add . && git commit -m "chore: version 0.7.0"
cd ../z-open && vim pyproject.toml zopen.py && git add . && git commit -m "chore: version 0.7.0"
cd ../z-kitty-launcher && vim Cargo.toml && git add . && git commit -m "chore: version 0.7.0"
cd ../z-rclone-mount-applete && vim Cargo.toml && git add . && git commit -m "chore: version 0.7.0"

# Tag all projects with same version
repo forall -c git tag -a v0.7.0 -m "Release v0.7.0"

# Push all changes
repo forall -c git push origin HEAD
repo forall -c git push origin v0.7.0

# Update manifest to track new version tags
cd . # (manifest branch)
vim manifests/default.xml  # Update revision="v0.7.0" for release branch
git add manifests/default.xml
git commit -m "chore: manifest for v0.7.0 release"
git push origin manifest
```

### Syncing with Upstream

```bash
# Sync all projects with latest remote changes
repo sync

# See what changed
repo forall -c git log origin/master --oneline -5

# If you have local changes, handle conflicts
repo forall -c git rebase origin/master
# or: repo forall -c git merge origin/master
```

### Selective Operations

```bash
# Sync only Python projects
repo sync -g python

# Sync only Rust projects
repo sync -g rust

# Run command on Python projects only
repo forall -g python -c git status

# Show status of only z-edit and z-open
repo forall -g python -c 'echo "=== $REPO_PATH ===" && git status'
```

---

## Advanced Manifest Patterns

### Multi-Branch Manifest Strategy

For managing different development streams:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <remote name="github" 
          fetch="https://github.com/pilakkat1964"
          review="github.com" />

  <default remote="github" revision="master" sync-j="4" />

  <!-- Main development branch -->
  <project path="z-edit" name="z-edit" revision="master" />
  <project path="z-open" name="z-open" revision="master" />

  <!-- Stable release branch (optional)
  <project path="z-edit" name="z-edit" revision="release/v0.6" if="release" />
  <project path="z-open" name="z-open" revision="release/v0.6" if="release" />
  -->
</manifest>
```

### Conditional Projects

```xml
<!-- Include optional projects
repo init -u ... --profile=all-projects
-->
<project path="optional-tool" 
         name="optional-tool"
         groups="optional"
         revision="master" />
```

### Project-Specific Configurations

```xml
<!-- Project with custom clone depth -->
<project path="z-edit" name="z-edit" 
         revision="master"
         clone-depth="50" />

<!-- Project with different destination branch -->
<project path="z-kitty-launcher" name="z-kitty-launcher"
         revision="master"
         dest-branch="development" />

<!-- Project with upstream tracking -->
<project path="z-open" name="z-open"
         revision="master"
         upstream="upstream/master"
         dest-branch="master" />
```

---

## Command Reference

### Core Commands

| Command | Purpose |
|---------|---------|
| `repo init` | Initialize workspace with manifest |
| `repo sync` | Sync all projects with manifest revisions |
| `repo start BRANCH` | Create feature branch in all projects |
| `repo upload` | Upload changes for code review (Gerrit) |
| `repo forall` | Run command in all projects |
| `repo status` | Show status of all projects |
| `repo branches` | List branches in all projects |
| `repo list` | List all projects in manifest |
| `repo manifest` | Show manifest file |
| `repo prune` | Delete local branches merged in upstream |
| `repo abandon` | Delete local branch |

### Useful Forall Commands

```bash
# Show git status in all projects
repo forall -c git status

# Commit with message in all projects (must have same changes)
repo forall -c git commit -am "message"

# Push all projects
repo forall -c git push origin HEAD

# Show commit log in all projects
repo forall -c git log --oneline -3

# Show branches in all projects
repo forall -c git branch -a

# Stash changes in all projects
repo forall -c git stash

# Show diff in all projects
repo forall -c git diff

# Sync (rebase) with remote
repo forall -c git rebase origin/master
```

### Environment Variables

```bash
# $REPO_PATH - Path to project directory
# $REPO_NAME - Project name from manifest
# $REPO_REMOTE - Remote name
# $REPO_PROJECT - Full project path

repo forall -c 'echo "Project: $REPO_PROJECT"'
```

---

## Z-Tools Specific Examples

### Example 1: Create Contribution Guidelines Across All Projects

```bash
# Setup workspace
mkdir ~/z-tools-repo && cd ~/z-tools-repo
repo init -u git@github.com:pilakkat1964/z-tools.git -b manifest
repo sync

# Create feature branch
repo start feature/contribution-guidelines

# Update z-edit
cd z-edit
cat > CONTRIBUTING.md << 'EOF'
# Contributing to z-edit
[... content ...]
EOF
git add CONTRIBUTING.md
git commit -m "docs: add contribution guidelines"

# Update z-open
cd ../z-open
cp ../z-edit/CONTRIBUTING.md CONTRIBUTING.md  # Or customize
git add CONTRIBUTING.md
git commit -m "docs: add contribution guidelines"

# ... similar for other projects ...

# View all commits
repo forall -c git log --oneline -1

# Push all changes
repo upload
# or: repo forall -c git push origin feature/contribution-guidelines
```

### Example 2: Release Version 0.7.0

```bash
# Create release branch
repo start release/v0.7.0

# Update versions in each project
for project in z-edit z-open; do
  cd $project
  # Update version (adjust per project)
  grep -r "version.*=" . --include="*.toml" --include="*.py"
  # Make updates...
  git commit -am "chore: bump to 0.7.0"
  cd ..
done

# Tag all projects
repo forall -c git tag -a v0.7.0 -m "Release v0.7.0"

# Push to remote
repo forall -c git push origin HEAD
repo forall -c git push origin v0.7.0

# Update manifest
cd .  # manifest directory
vim manifests/default.xml
# Change revision="v0.7.0" for projects to release
git commit -am "chore: manifest for v0.7.0"
git push origin manifest
```

### Example 3: Develop Python Projects Only

```bash
# Sync only Python projects
repo sync -g python

# View Python projects
repo forall -g python -c 'echo "=== $REPO_PROJECT ==="'

# Make changes in Python projects
repo forall -g python -c git status

# Commit changes
repo forall -g python -c git commit -am "feat: improve error handling"

# Push changes
repo forall -g python -c git push origin master
```

### Example 4: Handle Multi-Project Bug Fix

```bash
# Create hotfix branch
repo start hotfix/critical-security-issue

# Fix bug across all projects
for project in z-edit z-open z-kitty-launcher z-rclone-mount-applete; do
  cd $project
  # Apply fix...
  git add fixed_file.rs or fixed_file.py
  git commit -m "fix: security issue in config parsing"
  cd ..
done

# Test across all projects
repo forall -c 'echo "Testing $REPO_PROJECT..." && cargo test'  # or pytest

# Push all fixes
repo forall -c git push origin hotfix/critical-security-issue

# Create pull requests in each project (manual step)
# ... or use repo upload if using Gerrit ...
```

---

## Integration with CI/CD

### GitHub Actions Integration

Create `.github/workflows/repo-check.yml` in each project:

```yaml
name: Multi-Repo Check
on:
  push:
    branches: [master, main]
  pull_request:
    branches: [master, main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          if [ -f "pytest.ini" ]; then
            pytest
          else
            cargo test
          fi
```

### Synchronized Release Workflow

```bash
# Script: release.sh
#!/bin/bash
set -e

VERSION=$1
if [ -z "$VERSION" ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

# Create release branch
repo start release/v$VERSION

# Update all projects
repo forall -c "
  if [ -f Cargo.toml ]; then
    sed -i 's/version = .*/version = \"$VERSION\"/' Cargo.toml
  elif [ -f pyproject.toml ]; then
    sed -i 's/version = .*/version = \"$VERSION\"/' pyproject.toml
  fi
  git add .
  git commit -m \"chore: release v$VERSION\"
"

# Tag all
repo forall -c git tag -a v$VERSION -m "Release v$VERSION"

# Push all
repo forall -c git push origin HEAD
repo forall -c git push origin v$VERSION

echo "Released v$VERSION across all projects!"
```

---

## Best Practices

### 1. Manifest Management

✅ **DO:**
- Keep manifest on separate branch (e.g., `manifest`)
- Version manifest with release tags
- Document manifest changes
- Test manifest before pushing

❌ **DON'T:**
- Mix manifest and project content on same branch
- Manually sync manifests
- Forget to update manifest for releases

### 2. Branch Strategy

✅ **DO:**
- Use consistent branch names across projects
- Create feature branches with `repo start`
- Sync before starting new features
- Push feature branches for review

❌ **DON'T:**
- Create branches manually (use repo start)
- Have different branch names in different projects
- Work on detached HEAD states without tracking

### 3. Synchronization

✅ **DO:**
- `repo sync` frequently before starting work
- `repo sync -j 4` to speed up operations
- Use `repo forall` for bulk operations
- Check `repo status` before committing

❌ **DON'T:**
- Mix manual git operations with repo operations
- Forget to sync before pushing
- Leave uncommitted changes during sync

### 4. Code Review

✅ **DO:**
- Use `repo upload` with Gerrit for integrated reviews
- Review all projects in feature branch
- Link related reviews across projects
- Tag issues with project name

❌ **DON'T:**
- Push directly without review
- Mix reviews from different projects
- Lose context of multi-project changes

---

## Troubleshooting

### Issue: "repo: command not found"

```bash
# Solution: Ensure repo is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Add to ~/.bashrc or ~/.zshrc permanently
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Issue: Merge Conflicts During Sync

```bash
# See which projects have conflicts
repo status

# Manually resolve in each project
cd conflicted_project
git status  # see conflicts
# Edit files to resolve
git add resolved_files
git rebase --continue
# Back to root
cd ..

# Verify all resolved
repo forall -c git status
```

### Issue: Detached HEAD State

```bash
# Recover from detached HEAD
repo forall -c 'if [ "$(git rev-parse --abbrev-ref HEAD)" = "HEAD" ]; then 
  git checkout master
fi'

# Or track back to manifest
repo sync
```

### Issue: Accidental Commits on Wrong Branch

```bash
# Create correct branch and cherry-pick
repo start feature/correct-branch

# In each project with wrong commits:
cd project_with_wrong_commit
git log --oneline -3  # Find commit SHA
git cherry-pick COMMIT_SHA
cd ..

# Go back to wrong branch and reset
repo start old_branch
repo forall -c git reset --hard HEAD~1  # Or appropriate number
```

---

## Next Steps

### For Z-Tools Portfolio

1. **Create manifest branch** in z-tools repository
2. **Write default.xml** manifest file
3. **Test manifest** locally with repo sync
4. **Document team workflows** specific to your patterns
5. **Automate releases** using repo forall commands
6. **Integrate with CI/CD** for automated testing

### Further Learning

- [Official Repo Documentation](https://gerrit.googlesource.com/git-repo/+/master/docs/)
- [Android Repo Setup Guide](https://source.android.com/docs/setup/create/downloading)
- [Gerrit Code Review Integration](https://gerrit-documentation.storage.googleapis.com/)
- [Git Repo Reference Manual](https://man7.org/linux/man-pages/man1/git-repo.1.html)

---

## Conclusion

The Google repo tool provides powerful portfolio management capabilities, especially for multi-project ecosystems like z-tools. By implementing a manifest-based approach, you can:

- Streamline development workflows
- Synchronize versions across projects
- Automate multi-project operations
- Improve collaboration and code review
- Maintain consistency across the portfolio

This document serves as both reference and tutorial for implementing repo-based workflow in z-tools.
