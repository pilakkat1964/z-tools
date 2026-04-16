---
title: "Cross-Project Index"
permalink: /portfolio-docs/cross-project-index/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# Z-Tools Projects - Cross-Project Index & Synchronization Guide

## Overview

This document provides a unified view of all z-tools projects, their synchronization status, and guidance for agents working across multiple projects.

**Last Updated**: April 16, 2026

---

## Quick Project Reference

### All Projects at a Glance

| Project | Language | Purpose | Version | Status | Lines | Build |
|---------|----------|---------|---------|--------|-------|-------|
| **z-edit** | Python | File editor launcher | v0.1.0 | ✅ Production | 1,725 | CMake + uv |
| **z-open** | Python | File opener utility | v0.7.0+ | ✅ Production | 1,400+ | CMake + uv |
| **z-kitty-launcher** | Rust | Terminal session manager | v0.4.0 | ✅ Production | 957 | Cargo |
| **z-rclone-mount-applete** | Rust | RClone mount manager | v0.1.0 | ✅ Production | 591 | Cargo |

---

## Project Descriptions

### 1. Z-Edit 📝
**File Editor Launcher - Smart Editor Selection**

- Opens files in appropriate editor based on MIME type or extension
- Single Python file architecture (1,725 lines)
- Sophisticated configuration system with layered overrides
- Modern CI/CD with testing, linting, security scanning
- Production-ready Debian packaging (amd64)

**Key Links:**
- [Full AGENTS.md](z-edit/AGENTS.md) - 631 lines
- [GitHub](https://github.com/pilakkat1964/z-edit)
- [Live Docs](http://pilakkat.mywire.org/z-edit/)

**Technology:**
- Build: CMake 3.20+
- Package Manager: uv (with pip fallback)
- Testing: pytest with coverage
- CI/CD: GitHub Actions

---

### 2. Z-Open 📂
**File Opener Utility - Intelligent Application Resolution**

- Opens files with most appropriate application
- Extensive documentation (5,500+ lines)
- Role-based reading paths for different user types
- Python API for programmatic access
- Recently promoted uv as primary package manager

**Key Links:**
- [Full AGENTS.md](z-open/AGENTS.md) - 990 lines
- [GitHub](https://github.com/pilakkat1964/z-open)
- [Live Docs](http://pilakkat.mywire.org/z-open/)

**Recent Achievements:**
- Fixed Jekyll GitHub Pages compatibility
- Deployed UV promotion documentation
- Enhanced virtual environment infrastructure

---

### 3. Z-Kitty-Launcher 🎮
**Terminal Session Manager for Kitty Emulator**

- Create, manage, and launch terminal sessions
- Multi-architecture support (AMD64 native, ARM64 cross-compile)
- Comprehensive test suite (7/7 passing)
- Shell completions (Bash, Zsh)
- Desktop environment integration

**Key Links:**
- [Full AGENTS.md](z-kitty-launcher/AGENTS.md) - 407 lines
- [GitHub](https://github.com/pilakkat1964/kitty-launcher)
- [Documentation](z-kitty-launcher/README.md)

**Standout Features:**
- Pure Rust implementation (957 lines)
- Zero external dependencies
- Multi-architecture GitHub Actions
- Shell completion automation

---

### 4. Z-RClone-Mount-Applete 🔧
**RClone Mount Manager - System Tray & Configuration GUI**

- System tray applet for rclone mount status monitoring
- GTK4-based configuration manager
- Seamless bash script integration
- Systemd user service management
- Multi-mount support with auto-refresh

**Key Links:**
- [Full AGENTS.md](z-rclone-mount-applete/AGENTS.md) - 637 lines (NEW)
- [GitHub](https://github.com/pilakkat1964/z-rclone-mount-applete)
- [README](z-rclone-mount-applete/README.md) - 420 lines

**Architecture:**
- 591 lines of Rust code (4 focused modules)
- Minimal dependencies (6 crates)
- Async/await for non-blocking I/O
- Comprehensive documentation (2,000+ lines)

---

## Synchronization Status

### Documentation Completeness

| Aspect | z-edit | z-open | z-kitty | z-rclone |
|--------|--------|--------|---------|----------|
| **AGENTS.md** | ✅ 631 lines | ✅ 990 lines | ✅ 407 lines | ✅ 637 lines (NEW) |
| **README** | ✅ Comprehensive | ✅ Comprehensive | ✅ 614 lines | ✅ 420 lines |
| **Build Guide** | ✅ Detailed | ✅ Detailed | ✅ Scripts | ✅ Documented |
| **Design Docs** | ✅ Deep | ✅ Deep | ✅ Learning guide | ✅ Architecture |
| **GitHub Pages** | ✅ Live | ✅ Live | 🟡 Configured | 🟡 Needs setup |

### Build System Parity

| Aspect | z-edit | z-open | z-kitty | z-rclone |
|--------|--------|--------|---------|----------|
| **Build System** | CMake | CMake | Cargo | Cargo |
| **Package Manager** | uv | uv | N/A | N/A |
| **Testing** | pytest | pytest | cargo test | cargo test |
| **CI/CD** | ✅ Full | ✅ Full | ✅ Multi-arch | ✅ Basic |
| **Linting** | ✅ ruff | ✅ ruff | ✅ clippy | ✅ clippy |
| **Security** | ✅ bandit | ✅ bandit | 🟡 audit | 🟡 audit |

### Deployment Readiness

| Component | z-edit | z-open | z-kitty | z-rclone |
|-----------|--------|--------|---------|----------|
| **Debian (amd64)** | ✅ Ready | ✅ Ready | ✅ Ready | ✅ Ready |
| **Debian (arm64)** | 🟡 N/A | 🟡 N/A | ✅ Ready | 🟡 Possible |
| **Binary Release** | ✅ Auto | ✅ Auto | ✅ Auto | ✅ Auto |
| **GitHub Pages** | ✅ Live | ✅ Live | 🟡 Config | 🟡 Config |
| **PyPI** | 🟡 Possible | 🟡 Possible | N/A | N/A |

---

## Known Synchronization Gaps

### Gap 1: GitHub Pages Deployment
**Status**: 🟡 Partial  
**Affected**: z-kitty-launcher, z-rclone-mount-applete

- z-edit and z-open: ✅ Live production sites
- z-kitty-launcher: Configured but not deployed
- z-rclone-mount-applete: Needs setup

**Action**: Deploy both projects' GitHub Pages before Priority 2 work

### Gap 2: Multi-Architecture Builds
**Status**: 🟡 Partial  
**Affected**: z-edit, z-open

- z-kitty-launcher: ✅ AMD64 + ARM64
- z-rclone-mount-applete: ✅ Available but not auto-built
- Python projects: ❌ No ARM64 builds

**Action**: Add cross-compilation support for Python projects in Priority 2

### Gap 3: Security Scanning
**Status**: ✅ Python, 🟡 Rust

- z-edit: ✅ bandit + cargo-audit
- z-open: ✅ bandit + cargo-audit
- z-kitty-launcher: 🟡 cargo-audit configured
- z-rclone-mount-applete: 🟡 cargo-audit configured

**Action**: Enable consistent security scanning across all projects

### Gap 4: Development Workflow Automation
**Status**: ✅ Python, 🟡 Rust

- z-edit: ✅ scripts/dev.py (full workflow)
- z-open: ✅ scripts/dev.py (full workflow)
- z-kitty-launcher: 🟡 scripts/build.sh only
- z-rclone-mount-applete: 🟡 No automation script

**Action**: Create unified development workflow scripts for Rust projects

---

## Shared Infrastructure & Patterns

### Package Managers
```
Python: uv (recommended) + pip (fallback)
Rust: Cargo (standard)
```

### Build Frameworks
```
Python: CMake + uv
Rust: Cargo
```

### Testing Frameworks
```
Python: pytest
Rust: cargo test
```

### Linting & Formatting
```
Python: ruff (lint), black/ruff format
Rust: clippy (lint), cargo fmt
```

### CI/CD Platform
```
All: GitHub Actions
```

### Documentation Format
```
All: Markdown + Jekyll
Theme: Slate (z-edit, z-open configured)
```

### Versioning Strategy
```
All: Semantic Versioning (v0.0.0)
Release: Git tags (v*)
```

---

## Development Workflows

### Python Projects Workflow (z-edit, z-open)

**Setup**
```bash
source setup-env.sh dev
# or
uv venv && source .venv/bin/activate && uv sync
```

**Development Cycle**
```bash
# Edit code
vim src/project.py

# Test
./scripts/dev.py test

# Build
./scripts/dev.py build

# Package
./scripts/dev.py package

# Release
./scripts/dev.py release --version 0.x.x
```

**Key Files**
- `scripts/dev.py` - Main development automation
- `pyproject.toml` - Project metadata and dependencies
- `CMakeLists.txt` - Build configuration
- `uv.lock` - Locked dependencies

### Rust Projects Workflow (z-kitty-launcher, z-rclone-mount-applete)

**Setup**
```bash
cd project
rustup update  # Ensure Rust is current
```

**Development Cycle**
```bash
# Edit code
vim src/main.rs

# Test
cargo test

# Lint
cargo clippy
cargo fmt

# Build release
cargo build --release

# Run
./target/release/[binary]
```

**Key Files**
- `Cargo.toml` - Project manifest
- `Cargo.lock` - Locked dependencies
- `src/main.rs` - Entry point
- `.github/workflows/` - CI/CD configuration

---

## Cross-Project Dependencies

### Does Any Project Depend on Another?
**No** - All projects are standalone utilities that can be used independently.

### Are They Compatible?
**Yes** - They can be used together in complementary workflows:
- z-open calls z-edit (or similar editor launchers)
- z-kitty-launcher creates terminals that run z-rclone utilities
- z-rclone-mount-applete works with the bash mount manager

---

## Recommended Development Order

If starting work on multiple projects:

### Order 1: If Fixing Issues
1. Start with **z-edit** (most mature, best patterns)
2. Apply patterns to **z-open**
3. Translate to **z-kitty-launcher** (Python → Rust)
4. Apply to **z-rclone-mount-applete**

### Order 2: If Adding Features
1. Implement in **z-rclone-mount-applete** (newest, less settled)
2. Adapt for **z-kitty-launcher**
3. Implement in **z-open** (more complex)
4. Implement in **z-edit** (most complex)

### Order 3: If Doing Documentation
1. Create templates in **z-edit** (most documented)
2. Apply to **z-open**
3. Adapt for **z-kitty-launcher**
4. Use for **z-rclone-mount-applete**

---

## Cross-Project Navigation Guide

### Finding Information

**How do I...?**

| Question | z-edit | z-open | z-kitty | z-rclone |
|----------|--------|--------|---------|----------|
| Set up development? | setup-env.sh | setup-env.sh | Rust docs | Cargo docs |
| Run tests? | `./scripts/dev.py test` | `./scripts/dev.py test` | `cargo test` | `cargo test` |
| Build release? | `./scripts/dev.py package` | `./scripts/dev.py package` | `cargo build --release` | `cargo build --release` |
| Check code quality? | `cargo clippy` + ruff | `cargo clippy` + ruff | `cargo clippy` | `cargo clippy` |
| Deploy? | `./scripts/dev.py full` | `./scripts/dev.py full` | Tag push | Tag push |
| View docs? | `http://pilakkat.mywire.org/z-edit/` | `http://pilakkat.mywire.org/z-open/` | README.md | README.md |

### Common Tasks Across Projects

**Building**
```bash
# Python
cmake -B build && cmake --build build

# Rust
cargo build --release
```

**Testing**
```bash
# Python
pytest

# Rust
cargo test
```

**Linting**
```bash
# Python
ruff check .
cargo clippy

# Rust
cargo clippy
cargo fmt --check
```

**Packaging**
```bash
# Python
./scripts/dev.py package

# Rust
cargo build --release
# Then use cargo-deb or manual packaging
```

---

## Agent Hand-Off Template

When transitioning work between agents or projects, use this template:

```markdown
## Starting State

- **Project**: [Project Name]
- **Latest Version**: X.Y.Z (verified: git tag)
- **Latest Commit**: [commit hash] (verified: git log -1)
- **Build Status**: [Status] (verified: cargo build / pytest)
- **Git Branch**: master (verified: git branch)
- **SSH Status**: [Status] (verified: git push --dry-run)

## Recent Work

- [Most recent change 1]
- [Most recent change 2]
- [Any blockers or notes]

## Next Priority

1. [Next task]
2. [Following task]

## Important Files

- [Key file 1] - [Purpose]
- [Key file 2] - [Purpose]

## Commands to Know

\`\`\`bash
# Development setup
[Setup command]

# Run tests
[Test command]

# Build
[Build command]

# Common workflow
[Workflow command]
\`\`\`

## Documentation to Read First

- [AGENTS.md](./AGENTS.md) - Project status
- [README.md](./README.md) - Overview
- [Design docs] - Architecture details

## Questions for Continuing Agent

1. What should I focus on first?
2. Are there any known blockers?
3. What's the priority for the next release?
```

---

## Synchronization Checklist for Agents

When working across projects, verify:

### Before Starting
- [ ] Read root AGENTS.md (this file)
- [ ] Read project-specific AGENTS.md
- [ ] Verify git status in target project
- [ ] Confirm build/test passing
- [ ] Check latest version matches git tags

### While Working
- [ ] Keep AGENTS.md updated with progress
- [ ] Commit frequently with clear messages
- [ ] Test after each logical change
- [ ] Document any new features
- [ ] Note any blockers or decisions

### Before Finishing
- [ ] All tests passing
- [ ] Code formatted (cargo fmt / ruff)
- [ ] No lint warnings (cargo clippy / ruff)
- [ ] Documentation updated
- [ ] AGENTS.md checkpoint section updated
- [ ] Git status clean or committed
- [ ] Ready for next agent

---

## Inter-Project Communication

### Documentation Standards
All projects follow:
- **Format**: Markdown with Jekyll compatibility
- **Theme**: Slate (primary), custom layouts available
- **Structure**: See AGENTS_STANDARDIZATION_GUIDE.md
- **Updates**: Within 1 day of release

### Commit Message Standards
```
# Feature
feat: Add new feature description

# Bug fix
fix: Resolve issue description

# Documentation
docs: Update or add documentation

# Testing
test: Add or improve tests

# Refactoring
refactor: Restructure code for clarity

# Build/CI
ci: Update build or CI configuration

# Performance
perf: Optimize performance

# Maintenance
chore: Update dependencies or maintenance
```

### Version Tagging
```
# Format
vX.Y.Z

# Examples
v0.1.0   # Initial release
v0.2.0   # Minor feature addition
v0.1.1   # Bug fix patch
v0.2.0-rc1  # Release candidate
```

---

## Next Steps for Synchronization

### Priority 2: Build System Unification (After Priority 1 Complete)
- [ ] Create unified dev workflow scripts for Rust projects
- [ ] Add ARM64 cross-compilation for Python projects
- [ ] Standardize CI/CD patterns across all projects
- [ ] Enable security scanning on all projects

### Priority 3: GitHub Pages Deployment (After Priority 2 Complete)
- [ ] Deploy z-kitty-launcher GitHub Pages
- [ ] Deploy z-rclone-mount-applete GitHub Pages
- [ ] Create master index linking all projects
- [ ] Set up cross-project navigation

### Priority 4: Future Enhancements
- [ ] PyPI publishing for Python projects
- [ ] Crates.io publishing for Rust projects
- [ ] Create shared testing utilities
- [ ] Establish contribution guidelines
- [ ] Create developer onboarding guide

---

## Important Repositories

| Project | GitHub URL | Clone URL |
|---------|-----------|-----------|
| z-edit | https://github.com/pilakkat1964/z-edit | `git@github.com:pilakkat1964/z-edit.git` |
| z-open | https://github.com/pilakkat1964/z-open | `git@github.com:pilakkat1964/z-open.git` |
| z-kitty-launcher | https://github.com/pilakkat1964/kitty-launcher | `git@github.com:pilakkat1964/kitty-launcher.git` |
| z-rclone-mount-applete | https://github.com/pilakkat1964/z-rclone-mount-applete | `git@github.com:pilakkat1964/z-rclone-mount-applete.git` |

---

## Account & SSH Information

**GitHub Account**: pilakkat1964 (pilakkat1964@gmail.com)

**SSH Keys Available**:
- `~/.ssh/id_ed25519_pilakkat` - Primary ED25519 key
- SSH Config: `~/.ssh/config` (auto-created)

**SSH Status**: ✅ Fully operational for all projects

---

## Quick Reference: Project Statistics

### Code Volume
```
z-edit:                    1,725 lines (Python)
z-open:                    1,400+ lines (Python)
z-kitty-launcher:          957 lines (Rust)
z-rclone-mount-applete:    591 lines (Rust)
────────────────────────────────────────
Total Source Code:         ~5,700 lines
```

### Documentation Volume
```
z-edit AGENTS.md:          631 lines
z-open AGENTS.md:          990 lines
z-kitty AGENTS.md:         407 lines
z-rclone AGENTS.md:        637 lines (NEW)
Other documentation:       2,000+ lines
────────────────────────────────────────
Total Documentation:       ~5,700 lines
```

### Build & Binary Sizes
```
z-edit:              Built on-demand (Python)
z-open:              Built on-demand (Python)
z-kitty-launcher:    ~509 KB release binary
z-rclone-mount:      ~975 KB release binary
────────────────────────────────────────
Total Binary Size:   ~1.5 MB
```

---

## Getting Help

### When You're Stuck

1. **Read the project AGENTS.md** - Most answers are there
2. **Check README.md** - User-focused documentation
3. **Look at recent git history** - See what changed
4. **Run tests** - Verify the system is working
5. **Check CI/CD logs** - Find build/test failures
6. **Review error messages carefully** - They usually point to the issue

### Common Issues & Solutions

**Build fails on first try**
- [ ] Read setup section of AGENTS.md
- [ ] Run: `source setup-env.sh dev` (Python) or check Rust install
- [ ] Check DEVELOPMENT.md for troubleshooting

**Tests fail**
- [ ] Run with verbose output
- [ ] Check test requirements in docs
- [ ] Look at recent test changes

**Git operations fail**
- [ ] Verify SSH key: `ssh-keyscan github.com`
- [ ] Check SSH config: `cat ~/.ssh/config`
- [ ] Test connection: `ssh git@github.com`

**Can't find a file**
- [ ] It might be generated during build
- [ ] Check .gitignore for excluded paths
- [ ] Run: `find . -name "filename"`

---

## Contact & Support

For issues or questions:

1. Check **project AGENTS.md** first
2. Review **README.md** for user questions
3. Check **GitHub issues** for known problems
4. Look at **recent commits** for context
5. Read **DEVELOPMENT.md** for workflow questions

---

## Document Status

- **Created**: April 16, 2026
- **Last Updated**: April 16, 2026
- **Maintained By**: Project Agents
- **Next Review**: May 16, 2026

**Remember**: Keep this document up-to-date as projects evolve!

---

**This guide helps agents navigate and contribute effectively across the entire z-tools project ecosystem.**
