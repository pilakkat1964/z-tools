---
title: "Repository Tool Advanced Guide"
permalink: /portfolio-docs/repository-tool-advanced-guide/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# Git Repo Tool: Advanced Scenarios & Patterns

Advanced workflows and patterns for using Google repo tool with z-tools portfolio.

---

## Table of Contents

1. [Multi-Manifest Strategy](#multi-manifest-strategy)
2. [Development Environments](#development-environments)
3. [CI/CD Integration](#cicd-integration)
4. [Complex Workflows](#complex-workflows)
5. [Performance Optimization](#performance-optimization)
6. [Troubleshooting Advanced Issues](#troubleshooting-advanced-issues)

---

## Multi-Manifest Strategy

### Use Case: Separate Development, Release, and Documentation Tracks

```bash
# Create separate manifest files for different purposes

# Development manifest (all projects, latest code)
# manifests/development.xml - tracks master/main branches

# Release manifest (released versions only)
# manifests/release.xml - tracks v* tags

# Documentation manifest (docs + minimal code)
# manifests/docs.xml - only manifest + doc resources

# CI/CD manifest (lean, for testing)
# manifests/ci.xml - minimal subset for automation
```

### Example: Release Manifest (manifests/release.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <remote  name="github"
           fetch="https://github.com/pilakkat1964"
           review="github.com" />

  <default remote="github"
           revision="v0.6.5"
           sync-j="4" />

  <!-- All projects locked to release version -->
  <project path="z-edit" name="z-edit" revision="v0.6.5" />
  <project path="z-open" name="z-open" revision="v0.6.5" />
  <project path="z-kitty-launcher" name="z-kitty-launcher" revision="v0.4.0" />
  <project path="z-rclone-mount-applete" name="z-rclone-mount-applete" revision="v0.1.0" />
</manifest>
```

### Example: Documentation Manifest (manifests/docs.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <remote  name="github"
           fetch="https://github.com/pilakkat1964"
           review="github.com" />

  <default remote="github" revision="master" />

  <!-- Only manifest repository for documentation work -->
  <project path="."
           name="z-tools"
           revision="manifest"
           groups="manifests" />

  <!-- Lightweight projects for docs (shallow clone) -->
  <project path="z-edit" name="z-edit" clone-depth="1" />
  <project path="z-open" name="z-open" clone-depth="1" />
  <project path="z-kitty-launcher" name="z-kitty-launcher" clone-depth="1" />
  <project path="z-rclone-mount-applete" name="z-rclone-mount-applete" clone-depth="1" />
</manifest>
```

### Using Multiple Manifests

```bash
# Create separate workspaces for different purposes

# Development workspace
mkdir ~/z-tools-dev
cd ~/z-tools-dev
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m manifests/default.xml

# Release workspace
mkdir ~/z-tools-release
cd ~/z-tools-release
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m manifests/release.xml

# Documentation workspace
mkdir ~/z-tools-docs
cd ~/z-tools-docs
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m manifests/docs.xml

# Switch manifests in existing workspace
cd ~/z-tools-dev
repo init -m manifests/ci.xml  # Switch to CI manifest
repo sync                      # Sync with new manifest
```

---

## Development Environments

### Scenario: Lightweight Development (Fast Setup)

For faster initial setup with shallow clones:

```bash
# Create shallow manifest (manifests/shallow.xml)
cat > ~/shallow-manifest.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <remote name="github" fetch="https://github.com/pilakkat1964" />
  <default remote="github" revision="master" sync-j="8" />
  
  <!-- Shallow clones for faster setup -->
  <project path="z-edit" name="z-edit" clone-depth="50" />
  <project path="z-open" name="z-open" clone-depth="50" />
  <project path="z-kitty-launcher" name="z-kitty-launcher" clone-depth="50" />
  <project path="z-rclone-mount-applete" name="z-rclone-mount-applete" clone-depth="50" />
</manifest>
EOF

# Use for faster setup
mkdir ~/z-tools-quick
cd ~/z-tools-quick
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m ~/shallow-manifest.xml
repo sync

# Later upgrade to full history
repo forall -c git fetch --unshallow
```

### Scenario: Focused Development (Single Language)

Develop only Python or only Rust projects:

```bash
# Python-only development
mkdir ~/z-tools-python
cd ~/z-tools-python
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m manifests/default.xml
repo sync
# Remove Rust projects if needed
rm -rf z-kitty-launcher z-rclone-mount-applete

# Rust-only development
mkdir ~/z-tools-rust
cd ~/z-tools-rust
repo init -u git@github.com:pilakkat1964/z-tools.git \
          -b manifest \
          -m manifests/default.xml
repo sync
# Remove Python projects if needed
rm -rf z-edit z-open
```

### Custom Profile-Based Setup

Create profiles for different team members:

```bash
# manifests/profiles.xml - Include profile-specific projects
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <remote name="github" fetch="https://github.com/pilakkat1964" />
  <default remote="github" revision="master" />
  
  <!-- Projects for different roles -->
  <project path="z-edit" name="z-edit" groups="python,maintainer,contributor" />
  <project path="z-open" name="z-open" groups="python,contributor" />
  <project path="z-kitty-launcher" name="z-kitty-launcher" groups="rust,maintainer" />
  <project path="z-rclone-mount-applete" name="z-rclone-mount-applete" groups="rust,contributor" />
</manifest>

# Usage:
repo init -m manifests/profiles.xml
repo sync -g maintainer   # For maintainers
repo sync -g contributor  # For contributors
```

---

## CI/CD Integration

### GitHub Actions Workflow with Repo

```yaml
# .github/workflows/repo-sync.yml
name: Repository Sync and Test

on:
  push:
    branches: [master, main, release/*]
  pull_request:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC

jobs:
  setup-and-test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Install Python and repo
        run: |
          sudo apt-get update
          sudo apt-get install -y python3 curl
          mkdir -p ~/.local/bin
          curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.local/bin/repo
          chmod a+x ~/.local/bin/repo
          export PATH="$HOME/.local/bin:$PATH"
          repo --version

      - name: Configure Git
        run: |
          git config --global user.name "CI Bot"
          git config --global user.email "ci@example.com"

      - name: Initialize Repo Workspace
        run: |
          export PATH="$HOME/.local/bin:$PATH"
          mkdir -p workspace
          cd workspace
          repo init -u https://github.com/pilakkat1964/z-tools.git \
                    -b manifest \
                    -m manifests/default.xml
          repo sync --jobs=8

      - name: Run Tests - Python Projects
        run: |
          export PATH="$HOME/.local/bin:$PATH"
          cd workspace
          repo forall -g python -c '
            if [ -f pytest.ini ]; then
              echo "Testing $REPO_PROJECT..."
              pytest --cov
            fi
          '

      - name: Run Tests - Rust Projects
        run: |
          export PATH="$HOME/.local/bin:$PATH"
          cd workspace
          repo forall -g rust -c '
            if [ -f Cargo.toml ]; then
              echo "Testing $REPO_PROJECT..."
              cargo test
              cargo clippy
              cargo audit
            fi
          '

      - name: Lint and Format Check
        run: |
          export PATH="$HOME/.local/bin:$PATH"
          cd workspace
          repo forall -c '
            if [ -f .ruff.toml ] || [ -f pyproject.toml ]; then
              echo "Checking Python style in $REPO_PROJECT..."
              ruff check . 2>/dev/null || true
            elif [ -f Cargo.toml ]; then
              echo "Checking Rust style in $REPO_PROJECT..."
              cargo fmt -- --check 2>/dev/null || true
            fi
          '
```

### Automated Release with Repo

```bash
#!/bin/bash
# scripts/automated-release.sh

set -e

VERSION=$1
if [ -z "$VERSION" ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

export PATH="$HOME/.local/bin:$PATH"

echo "=== Automated Release Process v$VERSION ==="

cd ~/workspace/z-tools-repo

# Ensure clean state
repo sync
repo status | grep -q "nothing to commit" || {
  echo "ERROR: Uncommitted changes detected!"
  exit 1
}

# Create release branch
echo "1. Creating release branch..."
repo start release/v$VERSION

# Update versions (assumes consistent version format)
echo "2. Updating version numbers..."
repo forall -c '
  if [ -f pyproject.toml ]; then
    sed -i "s/version = .*/version = \"$VERSION\"/" pyproject.toml
  fi
  if [ -f Cargo.toml ]; then
    sed -i "s/version = .*/version = \"$VERSION\"/" Cargo.toml
  fi
  git add . && git commit -m "chore: bump version to $VERSION" || true
'

# Run all tests
echo "3. Running tests..."
repo forall -g python -c 'pytest --tb=short' || { echo "Python tests failed!"; exit 1; }
repo forall -g rust -c 'cargo test' || { echo "Rust tests failed!"; exit 1; }

# Tag all projects
echo "4. Tagging release..."
repo forall -c git tag -a v$VERSION -m "Release v$VERSION"

# Push all
echo "5. Pushing changes..."
repo forall -c git push origin release/v$VERSION
repo forall -c git push origin v$VERSION

# Update manifest
echo "6. Updating manifest..."
cd .
sed -i "s/revision=\"master\"/revision=\"v$VERSION\"/g" manifests/default.xml
sed -i "s/revision=\"main\"/revision=\"v$VERSION\"/g" manifests/default.xml
git add manifests/default.xml
git commit -m "chore: manifest for v$VERSION release"
git push origin manifest

echo ""
echo "=== Release v$VERSION Complete! ==="
```

---

## Complex Workflows

### Multi-Team Coordination

```bash
# Scenario: Three teams working in parallel

# Team 1: Python developers
repo start feature/python-performance-improvements
repo forall -g python -c 'git checkout feature/python-performance-improvements'
# ... make changes ...
repo forall -g python -c 'git push origin feature/python-performance-improvements'

# Team 2: Rust developers
repo start feature/rust-security-updates
repo forall -g rust -c 'git checkout feature/rust-security-updates'
# ... make changes ...
repo forall -g rust -c 'git push origin feature/rust-security-updates'

# Team 3: Documentation team
repo start feature/docs-overhaul
cd .  # manifest repo
# ... update docs ...
git push origin feature/docs-overhaul

# Integration review
echo "=== Reviewing all feature branches ==="
repo forall -c 'echo "$REPO_PROJECT: $( git log HEAD...master --oneline | wc -l) new commits"'
```

### Synchronized Feature with Different Project Needs

```bash
# Create feature branch for "Improve Error Handling" across all projects
repo start feature/error-handling-improvements

# Different changes needed in each project
cd z-edit
# Add better error messages to zedit.py
git commit -am "feat: add contextual error messages"
cd ../z-open
# Add error recovery mechanism
git commit -am "feat: add error recovery logic"
cd ../z-kitty-launcher
# Add structured error reporting
git commit -am "feat: add structured error types"
cd ../z-rclone-mount-applete
# Add error logging and reporting
git commit -am "feat: add comprehensive error logging"
cd ..

# Push all
repo forall -c 'git push origin feature/error-handling-improvements'

# Verify all pushed
repo forall -c 'echo "$REPO_PROJECT: $(git log -1 --oneline)"'
```

### Large-Scale Refactoring

```bash
# Refactor: Update all project build systems

repo start feature/modernize-build-system

# Update Python projects
cd z-edit
# Update setup.py to pyproject.toml
# Update build configuration
git commit -am "build: migrate to pyproject.toml"
cd ../z-open
git commit -am "build: migrate to pyproject.toml"
cd ..

# Update Rust projects
cd z-kitty-launcher
# Update Cargo.toml metadata
git commit -am "build: update Cargo.toml metadata"
cd ../z-rclone-mount-applete
git commit -am "build: update Cargo.toml metadata"
cd ..

# Test everywhere
repo forall -c 'echo "Building $REPO_PROJECT..." && (cargo build 2>/dev/null || python -m build 2>/dev/null)'

# Push refactoring
repo forall -c 'git push origin feature/modernize-build-system'
```

---

## Performance Optimization

### Fast Sync Operations

```bash
# For faster sync with large history

# 1. Use parallel jobs
repo sync -j 8              # Increase parallelism

# 2. Shallow clone for new setups
repo init --depth=1 -u ...
repo sync

# 3. Skip tags for faster sync
repo sync --no-tags

# 4. Combine options
repo sync -j 8 --no-tags    # Fast sync, no tags

# Later: Unshallow repository when needed
repo forall -c git fetch --unshallow
```

### Caching Strategies

```bash
# Pre-fetch all objects for faster offline work
repo forall -c 'git fetch --all --prune'

# Create local cache
mkdir ~/git-cache
cd ~/git-cache
for project in z-edit z-open z-kitty-launcher z-rclone-mount-applete; do
  git clone --mirror https://github.com/pilakkat1964/$project.git $project.git
done

# Use cache for faster clones
repo init -u https://github.com/pilakkat1964/z-tools.git \
          -b manifest \
          --reference=~/git-cache
repo sync
```

### Reducing Workspace Size

```bash
# Remove unnecessary files
repo forall -c '
  # Remove test data
  rm -rf tests/fixtures/large-data
  
  # Clean build artifacts
  rm -rf build/ dist/ target/
  
  # Remove CI caches
  rm -rf .github/cache
'

# Garbage collect
repo forall -c 'git gc --aggressive'

# Check sizes
du -sh z-* | sort -h
```

---

## Troubleshooting Advanced Issues

### Issue: Diverged Manifest Branches

```bash
# Problem: Manifest branch has diverged from master

# Solution: Reset manifest to main branch state
cd .  # manifest repo
git fetch origin
git reset --hard origin/master
git push origin manifest --force-with-lease

# Then resync all projects
cd ..
repo sync --force-sync
```

### Issue: Mixed Merge States Across Projects

```bash
# Problem: Some projects have merge conflicts, others don't

# See which projects have conflicts
repo forall -c '
  if [ -d .git/MERGE_HEAD ]; then
    echo "$REPO_PROJECT: MERGE IN PROGRESS"
  fi
'

# Resolve conflicts one by one
cd z-edit
git status
# ... resolve conflicts ...
git add resolved-files
git commit

# Abort all merges if too complex
repo forall -c 'git merge --abort 2>/dev/null || true'
```

### Issue: Accidentally Deleted Projects

```bash
# Problem: rm -rf deleted a project

# Recovery: Restore from manifest
cd ~/z-tools-repo

# Resync will restore deleted directories
repo sync

# Or manually
git clone https://github.com/pilakkat1964/z-edit.git z-edit
cd z-edit && git checkout master && cd ..
```

### Issue: Branch Name Conflicts

```bash
# Problem: Same branch name in multiple projects causes confusion

# Solution: Use descriptive branch names with project prefix
repo start feature/python-error-handling

# Rename in specific project if needed
cd z-edit
git branch -m feature/python-error-handling feature/z-edit-error-handling
git push origin feature/z-edit-error-handling

cd ../z-open
git branch -m feature/python-error-handling feature/z-open-error-handling
git push origin feature/z-open-error-handling
```

### Issue: Repository URL Changes

```bash
# Problem: GitHub username or repository URL changed

# Update manifest remote
cd .  # manifest repo
vim manifests/default.xml
# Update fetch URLs

git commit -am "chore: update repository URLs"
git push origin manifest

# Update local repos
cd ..
repo forall -c 'git remote set-url origin $(repo manifest -r | grep fetch | tail -1)/$REPO_PROJECT'
```

---

## Helpful Aliases and Functions

Add to ~/.bashrc or ~/.zshrc:

```bash
# Repo aliases
alias repo-sync='repo sync -j 8'
alias repo-status='repo forall -c "echo \"=== \$REPO_PROJECT ===\" && git status -s"'
alias repo-log='repo forall -c "echo \"=== \$REPO_PROJECT ===\" && git log --oneline -3"'
alias repo-branches='repo forall -c "echo \"=== \$REPO_PROJECT ===\" && git branch"'
alias repo-diff='repo forall -c "echo \"=== \$REPO_PROJECT ===\"&& git diff"'
alias repo-clean='repo forall -c git clean -fd'
alias repo-stash='repo forall -c git stash'
alias repo-pop='repo forall -c git stash pop'

# Useful functions
repo-add-all() {
  repo forall -c 'git add .'
}

repo-commit-all() {
  repo forall -c "git commit -m \"$1\""
}

repo-push-all() {
  repo forall -c 'git push origin $(git branch --show-current)'
}

repo-pull-all() {
  repo forall -c 'git pull origin $(git branch --show-current)'
}

repo-feature() {
  repo start feature/$1
}

repo-hotfix() {
  repo start hotfix/$1
}

repo-release() {
  repo start release/v$1
}

# Show project statistics
repo-stats() {
  echo "=== Repository Statistics ==="
  echo "Total projects: $(repo list | wc -l)"
  echo ""
  echo "Lines of code:"
  repo forall -c 'echo -n "$REPO_PROJECT: " && find . -name "*.py" -o -name "*.rs" | xargs wc -l 2>/dev/null | tail -1'
}
```

---

## Summary

Advanced patterns covered:

✅ Multi-manifest strategies for different workflows
✅ Development environment configurations
✅ CI/CD integration with GitHub Actions
✅ Complex multi-team coordination
✅ Performance optimization techniques
✅ Troubleshooting common issues
✅ Helpful aliases and functions

Use these patterns to optimize your z-tools portfolio workflow!
