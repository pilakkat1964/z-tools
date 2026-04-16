---
title: "Repository Tool Tutorial"
permalink: /portfolio-docs/repository-tool-tutorial/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# Git Repo Tool Tutorial: Z-Tools Portfolio Workflows

Complete, hands-on tutorial for implementing Google repo tool with the z-tools portfolio.

## Table of Contents

1. [Prerequisites & Installation](#prerequisites--installation)
2. [Initial Setup](#initial-setup)
3. [Common Workflows](#common-workflows)
4. [Release Management](#release-management)
5. [Team Collaboration](#team-collaboration)
6. [Automation & CI/CD](#automation--cicd)

---

## Prerequisites & Installation

### System Requirements

```bash
# Check Python version (3.6+ required)
python3 --version
# Output: Python 3.x.x (where x >= 6)

# Check Git version
git --version
# Output: git version 2.x.x

# Check curl
curl --version
```

### Install Repo Tool

```bash
# Create bin directory if it doesn't exist
mkdir -p ~/.local/bin

# Download repo tool
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.local/bin/repo

# Make executable
chmod a+x ~/.local/bin/repo

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Make permanent (add to ~/.bashrc or ~/.zshrc)
if ! grep -q "~/.local/bin" ~/.bashrc; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
fi

# Reload shell
source ~/.bashrc

# Verify
repo --version
# Output: repo version 2.x (...)
```

### Configure Git

```bash
# Set global git config (if not already done)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify
git config --global --list | grep user
```

---

## Initial Setup

### Phase 1: Prepare Manifest Repository

The z-tools repository will serve as both the manifest repository and source of truth for all projects.

#### 1a. Clone and Set Up Manifest Branch

```bash
# Clone existing z-tools repository
cd ~/workspace
git clone git@github.com:pilakkat1964/z-tools.git z-tools-manifests
cd z-tools-manifests

# Create manifest branch
git checkout -b manifest

# Verify you're on manifest branch
git branch
# Output: * manifest
#           main (or master)

# Create manifest directory structure
mkdir -p manifests
```

#### 1b. Create .gitignore for Manifest Branch

```bash
# Create .gitignore to exclude workspace artifacts
cat > .gitignore << 'EOF'
# Git Repo tool workspace
.repo/
.git/sync-lock

# Local workspace files
*~
*.swp
*.swo

# Python cache
__pycache__/
*.pyc
.pytest_cache/

# IDE files
.vscode/
.idea/
*.iml

# OS files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
EOF

git add .gitignore
git commit -m "chore: add .gitignore for manifest branch"
```

### Phase 2: Create Manifest File

#### 2a. Create Default Manifest (manifests/default.xml)

```bash
# While on manifest branch in z-tools-manifests directory

cat > manifests/default.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Z-Tools Portfolio Manifest
  
  Defines all projects in the z-tools ecosystem.
  
  Groups:
  - python: Python projects (z-edit, z-open)
  - rust: Rust projects (z-kitty-launcher, z-rclone-mount-applete)
  - tools: All tool projects
  - manifests: This manifest repository
  
  Usage:
  repo sync             # Sync all projects
  repo sync -g python   # Sync Python projects only
  repo sync -g rust     # Sync Rust projects only
-->

<manifest>
  <!-- Remote repository definitions -->
  <remote  name="github"
           fetch="https://github.com/pilakkat1964"
           review="github.com" />

  <!-- Default settings for all projects -->
  <default remote="github"
           revision="master"
           sync-j="4"
           dest-branch="master" />

  <!-- Manifest Repository (this repository on manifest branch) -->
  <project path="."
           name="z-tools"
           remote="github"
           revision="manifest"
           groups="manifests"
           dest-branch="manifest" />

  <!-- Python Projects -->
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

  <!-- Rust Projects -->
  <project path="z-kitty-launcher"
           name="z-kitty-launcher"
           remote="github"
           revision="master"
           groups="rust,tools" />

  <project path="z-rclone-mount-applete"
           name="z-rclone-mount-applete"
           remote="github"
           revision="main"
           groups="rust,tools"
           dest-branch="main" />

</manifest>
EOF

# Verify the file was created
cat manifests/default.xml

# Commit the manifest
git add manifests/default.xml
git commit -m "chore: add initial manifest for z-tools portfolio"

# Push manifest branch to remote
git push origin manifest

# Verify on GitHub
echo "✓ Manifest branch pushed. Verify at:"
echo "  https://github.com/pilakkat1964/z-tools/tree/manifest"
```

### Phase 3: Initialize Repo Workspace

#### 3a. Create Workspace Directory

```bash
# Create a fresh workspace directory for repo
mkdir -p ~/workspace/z-tools-repo
cd ~/workspace/z-tools-repo

# This directory will contain:
# .repo/                 <- repo metadata
# z-edit/                <- z-edit project
# z-open/                <- z-open project
# z-kitty-launcher/      <- z-kitty-launcher project
# z-rclone-mount-applete/<- z-rclone-mount-applete project
```

#### 3b. Initialize Repo

```bash
# Initialize repo with z-tools manifest
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m manifests/default.xml

# Verify initialization
ls -la
# Output should show:
# .repo/                (created by repo)
# (no projects yet)
```

#### 3c. Sync All Projects

```bash
# Sync all projects from manifest
repo sync

# This will:
# 1. Clone all projects from manifest
# 2. Checkout correct branches
# 3. Set up tracking

# Verify projects are cloned
ls -la

# Expected output:
# .repo/
# z-edit/
# z-open/
# z-kitty-launcher/
# z-rclone-mount-applete/
```

#### 3d. Verify Installation

```bash
# Show all projects in manifest
repo list
# Output:
# .                              : manifest (manifest)
# z-edit                         : z-edit (python)
# z-open                         : z-open (python)
# z-kitty-launcher               : z-kitty-launcher (rust)
# z-rclone-mount-applete         : z-rclone-mount-applete (rust)

# Show current status
repo status
# Output shows any uncommitted changes

# Show branches
repo branches
# Output shows current branch in each project

# Show repo version
repo --version
```

---

## Common Workflows

### Workflow 1: Feature Development Across Multiple Projects

**Scenario:** Add new documentation feature to all projects simultaneously.

#### Step 1: Create Feature Branch

```bash
cd ~/workspace/z-tools-repo

# Create feature branch in all projects
repo start feature/improve-documentation

# Verify branches created
repo branches
# Output:
# *  feature/improve-documentation : z-edit (python)
# *  feature/improve-documentation : z-open (python)
# *  feature/improve-documentation : z-kitty-launcher (rust)
# *  feature/improve-documentation : z-rclone-mount-applete (rust)
```

#### Step 2: Make Changes in Each Project

```bash
# Edit z-edit documentation
cd z-edit
cat >> docs/CONTRIBUTION.md << 'EOF'

## Code Review Process

All pull requests require:
1. Green CI checks
2. At least one approval
3. No merge conflicts
EOF

git add docs/CONTRIBUTION.md
git commit -m "docs: improve contribution documentation"
cd ..

# Edit z-open documentation
cd z-open
cat >> docs/CONTRIBUTION.md << 'EOF'

## Code Review Process

All pull requests require:
1. Green CI checks
2. At least one approval
3. No merge conflicts
EOF

git add docs/CONTRIBUTION.md
git commit -m "docs: improve contribution documentation"
cd ..

# Edit z-kitty-launcher documentation
cd z-kitty-launcher
cat >> docs/CONTRIBUTION.md << 'EOF'

## Code Review Process

All pull requests require:
1. Green CI checks
2. At least one approval
3. No merge conflicts
EOF

git add docs/CONTRIBUTION.md
git commit -m "docs: improve contribution documentation"
cd ..

# Edit z-rclone-mount-applete documentation
cd z-rclone-mount-applete
cat >> docs/CONTRIBUTION.md << 'EOF'

## Code Review Process

All pull requests require:
1. Green CI checks
2. At least one approval
3. No merge conflicts
EOF

git add docs/CONTRIBUTION.md
git commit -m "docs: improve contribution documentation"
cd ..
```

#### Step 3: Verify Changes Across All Projects

```bash
# View commits in all projects
repo forall -c 'echo "=== $REPO_PROJECT ===" && git log --oneline -1'
# Output:
# === z-edit ===
# abc1234 docs: improve contribution documentation
# === z-open ===
# def5678 docs: improve contribution documentation
# === z-kitty-launcher ===
# ghi9012 docs: improve contribution documentation
# === z-rclone-mount-applete ===
# jkl3456 docs: improve contribution documentation

# View all diffs
repo forall -c 'echo "=== $REPO_PROJECT ===" && git diff HEAD~1'

# Show files changed
repo forall -c 'echo "=== $REPO_PROJECT ===" && git show --name-only'
```

#### Step 4: Push Changes for Review

```bash
# Push feature branch to all projects
repo forall -c git push origin feature/improve-documentation

# Verify pushed
repo forall -c 'echo "=== $REPO_PROJECT ===" && git log --oneline origin/feature/improve-documentation -1'

# Now create pull requests on GitHub (manual for now)
# In each project:
# 1. Go to GitHub
# 2. Click "Compare & pull request"
# 3. Select feature/improve-documentation -> master/main
# 4. Add description
# 5. Create pull request
```

### Workflow 2: Selective Project Operations

**Scenario:** Work on Python projects only (z-edit and z-open).

#### Option A: Sync Only Python Projects

```bash
cd ~/workspace/z-tools-repo

# Sync only Python projects
repo sync -g python

# Verify only Python projects updated
repo status -1
# Only z-edit and z-open will show updates
```

#### Option B: Operations on Python Projects Only

```bash
# Show status of Python projects
repo forall -g python -c 'echo "=== $REPO_PROJECT ===" && git status'

# Commit changes across Python projects
repo forall -g python -c 'git commit -am "fix: improve error handling"'

# Push Python projects only
repo forall -g python -c 'git push origin master'

# See branches in Python projects
repo forall -g python -c 'echo "$REPO_PROJECT: $(git branch)"'
```

#### Option C: Run Commands with Context

```bash
# Complex command with environment variables
repo forall -g python -c '
  echo "Project: $REPO_PROJECT"
  echo "Branch: $(git branch --show-current)"
  echo "Remote: $(git config --get remote.origin.url)"
  echo "---"
'

# Run tests on Python projects
repo forall -g python -c 'pytest'

# Run tests on Rust projects
repo forall -g rust -c 'cargo test'
```

### Workflow 3: Bug Fix Across All Projects

**Scenario:** Fix security issue in all projects.

#### Step 1: Create Hotfix Branch

```bash
cd ~/workspace/z-tools-repo

# Create hotfix branch
repo start hotfix/security-fix-config-parsing

# Verify
repo branches
```

#### Step 2: Apply Fix to All Projects

```bash
# Apply security fix to z-edit
cd z-edit
# Edit config parsing code to fix security issue
vim zedit.py
git add zedit.py
git commit -m "security: fix config parsing vulnerability"
cd ..

# Apply to z-open
cd z-open
vim zopen.py
git add zopen.py
git commit -m "security: fix config parsing vulnerability"
cd ..

# Apply to z-kitty-launcher
cd z-kitty-launcher
vim src/main.rs
git add src/main.rs
git commit -m "security: fix config parsing vulnerability"
cd ..

# Apply to z-rclone-mount-applete
cd z-rclone-mount-applete
vim src/mount_manager.rs
git add src/mount_manager.rs
git commit -m "security: fix config parsing vulnerability"
cd ..
```

#### Step 3: Test All Projects

```bash
# Run tests across all projects
repo forall -c '
  echo "Testing $REPO_PROJECT..."
  if [ -f pytest.ini ]; then
    pytest
  elif [ -f Cargo.toml ]; then
    cargo test
  fi
'

# View test results
echo "All tests completed. Check output above for any failures."
```

#### Step 4: Push and Create PRs

```bash
# Push all fixes
repo forall -c git push origin hotfix/security-fix-config-parsing

# Create PRs on GitHub (manual step)
# Go to each project and create PR from hotfix branch
```

---

## Release Management

### Scenario: Release Version 0.7.0

#### Phase 1: Prepare Release

```bash
cd ~/workspace/z-tools-repo

# Sync all projects with latest changes
repo sync

# Verify clean working directory
repo status
# Should show no changes

# Create release branch
repo start release/v0.7.0
```

#### Phase 2: Update Version Numbers

```bash
# Update z-edit version
cd z-edit
sed -i 's/version = "0.6.5"/version = "0.7.0"/' pyproject.toml
sed -i 's/__version__ = "0.6.5"/__version__ = "0.7.0"/' zedit.py
git add pyproject.toml zedit.py
git commit -m "chore: bump version to 0.7.0"
cd ..

# Update z-open version
cd z-open
sed -i 's/version = "0.6.5"/version = "0.7.0"/' pyproject.toml
sed -i 's/__version__ = "0.6.5"/__version__ = "0.7.0"/' zopen.py
git add pyproject.toml zopen.py
git commit -m "chore: bump version to 0.7.0"
cd ..

# Update z-kitty-launcher version
cd z-kitty-launcher
sed -i 's/version = "0.4.0"/version = "0.7.0"/' Cargo.toml
git add Cargo.toml
git commit -m "chore: bump version to 0.7.0"
cd ..

# Update z-rclone-mount-applete version
cd z-rclone-mount-applete
sed -i 's/version = "0.1.0"/version = "0.7.0"/' Cargo.toml
git add Cargo.toml
git commit -m "chore: bump version to 0.7.0"
cd ..

# Verify version updates
repo forall -c 'echo "=== $REPO_PROJECT ===" && git show --stat'
```

#### Phase 3: Tag Release

```bash
# Tag all projects with same version
repo forall -c git tag -a v0.7.0 -m "Release v0.7.0

This release includes:
- Enhanced contribution guidelines
- Improved documentation
- Bug fixes and security updates"

# Verify tags created
repo forall -c 'echo "$REPO_PROJECT: $(git tag -l v0.7.0)"'
```

#### Phase 4: Update Manifest

```bash
# Go to manifest repo directory
# (repo creates this at root of workspace as ".")
cd .

# Edit manifest to track release version
# Update revision from "master" to "v0.7.0" for all projects
cat > manifests/default.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <remote  name="github"
           fetch="https://github.com/pilakkat1964"
           review="github.com" />

  <default remote="github"
           revision="v0.7.0"
           sync-j="4"
           dest-branch="master" />

  <!-- Manifest Repository -->
  <project path="."
           name="z-tools"
           remote="github"
           revision="manifest"
           groups="manifests"
           dest-branch="manifest" />

  <!-- Python Projects - v0.7.0 -->
  <project path="z-edit"
           name="z-edit"
           remote="github"
           revision="v0.7.0"
           groups="python,tools" />

  <project path="z-open"
           name="z-open"
           remote="github"
           revision="v0.7.0"
           groups="python,tools" />

  <!-- Rust Projects - v0.7.0 -->
  <project path="z-kitty-launcher"
           name="z-kitty-launcher"
           remote="github"
           revision="v0.7.0"
           groups="rust,tools" />

  <project path="z-rclone-mount-applete"
           name="z-rclone-mount-applete"
           remote="github"
           revision="v0.7.0"
           groups="rust,tools"
           dest-branch="main" />
</manifest>
EOF

# Commit manifest update
git add manifests/default.xml
git commit -m "chore: manifest for v0.7.0 release

All projects now track v0.7.0 tag."

# Push manifest changes
git push origin manifest
```

#### Phase 5: Push All Changes

```bash
# Push version updates and tags from all projects
repo forall -c 'git push origin release/v0.7.0'
repo forall -c 'git push origin v0.7.0'

# Verify pushes on GitHub
echo "Release v0.7.0 pushed to all projects!"
echo "View releases at:"
echo "  - https://github.com/pilakkat1964/z-edit/releases/tag/v0.7.0"
echo "  - https://github.com/pilakkat1964/z-open/releases/tag/v0.7.0"
echo "  - https://github.com/pilakkat1964/z-kitty-launcher/releases/tag/v0.7.0"
echo "  - https://github.com/pilakkat1964/z-rclone-mount-applete/releases/tag/v0.7.0"
```

---

## Team Collaboration

### Scenario: Multi-Developer Working on Different Aspects

#### Setup: Three Developers

```bash
# Alice: Works on Python projects
# Bob: Works on Rust projects
# Charlie: Works on documentation and coordination

# All developers use same repo workspace setup:
mkdir ~/z-tools-repo
cd ~/z-tools-repo
repo init -u git@github.com:pilakkat1964/z-tools.git -b manifest -m manifests/default.xml
repo sync
```

#### Workflow: Parallel Development

```bash
# Alice works on Python projects
repo start feature/alice-python-improvements
repo forall -g python -c git checkout feature/alice-python-improvements
cd z-edit
# ... Alice makes changes to z-edit ...
git commit -am "feat: improve error messages"
cd ../z-open
# ... Alice makes changes to z-open ...
git commit -am "feat: improve error messages"
cd ..
repo forall -g python -c git push origin feature/alice-python-improvements

# Bob works on Rust projects
repo start feature/bob-rust-improvements
repo forall -g rust -c git checkout feature/bob-rust-improvements
cd z-kitty-launcher
# ... Bob makes changes ...
git commit -am "perf: optimize session loading"
cd ../z-rclone-mount-applete
# ... Bob makes changes ...
git commit -am "perf: optimize mount detection"
cd ..
repo forall -g rust -c git push origin feature/bob-rust-improvements

# Charlie coordinates and works on docs
repo start feature/charlie-docs
cd .  # manifest repo
# ... Charlie updates documentation ...
git commit -am "docs: update architecture diagrams"
git push origin feature/charlie-docs
```

#### Reviewing Changes

```bash
# Alice reviews Bob's Rust changes
repo forall -g rust -c 'echo "=== $REPO_PROJECT ===" && git log --oneline feature/bob-rust-improvements -1'

# Bob reviews Alice's Python changes
repo forall -g python -c 'echo "=== $REPO_PROJECT ===" && git log --oneline feature/alice-python-improvements -1'

# Everyone sees Charlie's documentation updates
cd .
git log --oneline feature/charlie-docs -1
```

---

## Automation & CI/CD

### Create Release Automation Script

```bash
# File: ~/z-tools-repo/scripts/release.sh
cat > scripts/release.sh << 'EOF'
#!/bin/bash
set -e

VERSION=$1
if [ -z "$VERSION" ]; then
  echo "Usage: $0 <version>"
  echo "Example: $0 0.7.0"
  exit 1
fi

echo "=== Starting Release v$VERSION ==="

# Create release branch
echo "Creating release branch..."
repo start release/v$VERSION

# Update versions
echo "Updating version numbers..."
repo forall -c "
  if [ -f pyproject.toml ]; then
    sed -i \"s/version = \\\".*\\\"/version = \\\"$VERSION\\\"/\" pyproject.toml
  fi
  if [ -f Cargo.toml ]; then
    sed -i \"s/version = \\\".*\\\"/version = \\\"$VERSION\\\"/\" Cargo.toml
  fi
"

# Commit version changes
echo "Committing version updates..."
repo forall -c 'git add . && git commit -m "chore: bump version to '$VERSION'"'

# Tag all projects
echo "Tagging release..."
repo forall -c "git tag -a v$VERSION -m \"Release v$VERSION\""

# Push changes
echo "Pushing changes..."
repo forall -c git push origin release/v$VERSION
repo forall -c git push origin v$VERSION

echo "=== Release v$VERSION Complete ==="
echo ""
echo "Next steps:"
echo "1. Review release branches and tags on GitHub"
echo "2. Update manifest for release version"
echo "3. Create GitHub release notes"
echo "4. Publish to PyPI and Crates.io"
EOF

chmod +x scripts/release.sh

# Usage
cd ~/z-tools-repo
./scripts/release.sh 0.7.0
```

### Create Sync Helper Script

```bash
# File: ~/z-tools-repo/scripts/sync-all.sh
cat > scripts/sync-all.sh << 'EOF'
#!/bin/bash

echo "=== Syncing all projects ==="
repo sync -j 4

echo ""
echo "=== Project Status ==="
repo status

echo ""
echo "=== Branch Summary ==="
repo forall -c 'echo "$REPO_PROJECT: $(git branch --show-current)"'
EOF

chmod +x scripts/sync-all.sh

# Usage
cd ~/z-tools-repo
./scripts/sync-all.sh
```

---

## Tips & Tricks

### Speed Up Operations

```bash
# Use parallel jobs for faster sync
repo sync -j 8  # Use 8 parallel jobs

# Shallow clone for faster initial sync
repo init --depth=1 -u ... -b manifest

# Partial sync (only what's needed)
repo sync --no-tags
```

### Better Visibility

```bash
# Create an alias for quick status
alias repo-status='repo forall -c "echo \"=== \$REPO_PROJECT ===\" && git status -s"'
repo-status

# Show all branches
alias repo-branches='repo forall -c "echo \"=== \$REPO_PROJECT ===\" && git branch -a"'
repo-branches

# Show recent commits
alias repo-log='repo forall -c "echo \"=== \$REPO_PROJECT ===\" && git log --oneline -3"'
repo-log
```

### Handling Multiple Workspaces

```bash
# Development workspace
mkdir ~/z-tools-dev
cd ~/z-tools-dev
repo init -u git@github.com:pilakkat1964/z-tools.git -b manifest
repo sync

# Release workspace
mkdir ~/z-tools-release
cd ~/z-tools-release
repo init -u git@github.com:pilakkat1964/z-tools.git -b manifest -m manifests/release.xml
repo sync

# Documentation workspace
mkdir ~/z-tools-docs
cd ~/z-tools-docs
repo init -u git@github.com:pilakkat1964/z-tools.git -b manifest -g manifests,python,docs
repo sync
```

---

## Summary of Key Commands

### Daily Operations

```bash
# Start day
repo sync                          # Get latest changes

# During development
repo start feature/my-feature       # Create feature branch
repo forall -c git status          # See what changed
repo forall -c git diff            # See diffs

# End of day
repo forall -c git push origin HEAD # Push changes
repo status                        # Verify nothing left
```

### Release Operations

```bash
repo sync                                    # Fresh start
repo start release/v0.7.0                    # Create release branch
repo forall -c git tag -a v0.7.0 -m "..."    # Tag all
repo forall -c git push origin v0.7.0        # Push tags
```

### Review & Cleanup

```bash
repo status -1                    # See what's different from manifest
repo forall -c git log -1         # See latest commits
repo branches                     # See all branches
repo prune                        # Clean up merged branches
repo abandon feature/old-feature  # Delete feature branch
```

---

## Next Steps

1. **Set up manifest** in z-tools repository
2. **Test locally** with sample workspace
3. **Document** team-specific workflows
4. **Train team** on repo tool basics
5. **Integrate** with CI/CD systems
6. **Monitor** adoption and iterate

For more help:
- `repo help` - Show repo help
- `repo help sync` - Show help for specific command
- `man repo` - Manual page (if installed)

Good luck with your z-tools portfolio!
