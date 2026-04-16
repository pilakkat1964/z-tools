---
title: "Master Index"
permalink: /portfolio-docs/master-index/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# Z-Tools Master Documentation Index

## Welcome to Z-Tools

**Z-Tools** is a collection of production-ready utilities for Linux terminal users and developers. This page provides a unified entry point to all documentation across all z-tools projects.

---

## 🎯 Projects Overview

Z-Tools consists of four complementary projects:

### 📝 Text Editing & File Management

#### **Z-Edit** - Smart File Editor Launcher
**Status:** ✅ Production Ready (v0.1.0)

Automatically opens files in the appropriate editor based on MIME type or file extension.

- **Type:** Python CLI utility
- **GitHub:** https://github.com/pilakkat1964/z-edit
- **Documentation:** http://pilakkat.mywire.org/z-edit/
- **Key Features:**
  - Accurate MIME detection via libmagic
  - Layered configuration (system → user → project)
  - Editor mappings fully customizable via TOML
  - Works with any editor (vim, VS Code, nano, etc.)

**Quick Links:**
- [Installation & Usage](http://pilakkat.mywire.org/z-edit/user-guide.html)
- [Configuration Guide](http://pilakkat.mywire.org/z-edit/design.html)
- [Developer Guide](http://pilakkat.mywire.org/z-edit/build.html)

---

#### **Z-Open** - Application Launcher Based on File Type
**Status:** ✅ Production Ready (v0.6.5)

Opens files and URLs with the most appropriate application automatically.

- **Type:** Python CLI utility
- **GitHub:** https://github.com/pilakkat1964/z-open
- **Documentation:** http://pilakkat.mywire.org/z-open/
- **Key Features:**
  - Mimetype-based application routing
  - Support for files and URLs
  - Extensible with custom handlers
  - Smart fallback to defaults

**Quick Links:**
- [User Guide](http://pilakkat.mywire.org/z-open/)
- [Examples & Recipes](http://pilakkat.mywire.org/z-open/examples.html)
- [Python API Reference](http://pilakkat.mywire.org/z-open/api.html)
- [FAQ & Troubleshooting](http://pilakkat.mywire.org/z-open/faq.html)

---

### 🖥️ Terminal & System Tools

#### **Kitty Launcher** - Terminal Session Manager
**Status:** ✅ Production Ready (v0.4.0)

Lightning-fast terminal session manager for the Kitty emulator.

- **Type:** Rust CLI utility
- **GitHub:** https://github.com/pilakkat1964/kitty-launcher
- **Documentation:** https://pilakkat1964.github.io/kitty-launcher/
- **Key Features:**
  - Session management with .session files
  - Shell completions (bash/zsh)
  - Desktop integration via .desktop files
  - Zero external dependencies

**Quick Links:**
- [Quick Reference](https://pilakkat1964.github.io/kitty-launcher/QUICK_REFERENCE.html)
- [Installation Guide](https://pilakkat1964.github.io/kitty-launcher/INSTALL.html)
- [Learning Guide for Developers](https://pilakkat1964.github.io/kitty-launcher/LEARNING_GUIDE.html)

---

#### **RClone Mount Applete** - Cloud Storage System Tray Manager
**Status:** ✅ Production Ready (v0.1.0)

System tray applet and GUI for managing rclone cloud storage mounts.

- **Type:** Rust GUI application
- **GitHub:** https://github.com/pilakkat1964/z-rclone-mount-applete
- **Documentation:** https://pilakkat1964.github.io/z-rclone-mount-applete/
- **Key Features:**
  - System tray integration
  - Mount/unmount one-click control
  - Real-time status monitoring
  - Systemd user service integration
  - GTK4-based configuration UI

**Quick Links:**
- [Quick Start](https://pilakkat1964.github.io/z-rclone-mount-applete/QUICK_START.html)
- [Architecture & Design](https://pilakkat1964.github.io/z-rclone-mount-applete/ARCHITECTURE.html)
- [Tutorial](https://pilakkat1964.github.io/z-rclone-mount-applete/TUTORIAL.html)

---

## 📚 Documentation by Role

### 👤 End Users
Want to use these tools? Start here:

1. **Choose your project:**
   - [Z-Edit User Guide](http://pilakkat.mywire.org/z-edit/user-guide.html)
   - [Z-Open User Guide](http://pilakkat.mywire.org/z-open/)
   - [Kitty Launcher Quick Start](https://pilakkat1964.github.io/kitty-launcher/QUICK_REFERENCE.html)
   - [RClone Mount Applete Quick Start](https://pilakkat1964.github.io/z-rclone-mount-applete/QUICK_START.html)

2. **Installation:** Each project includes platform-specific installation instructions
3. **Configuration:** Follow the project-specific configuration guides
4. **Troubleshooting:** Check the FAQ and troubleshooting sections

---

### 👨‍💻 Python Developers
Want to contribute to z-edit or z-open?

**Setup:**
- Modern build infrastructure: CMake 3.20+, uv package manager
- Dev workflow automation: `./scripts/dev.py`
- Comprehensive test suite: pytest with coverage

**Resources:**
- [z-edit Development Guide](http://pilakkat.mywire.org/z-edit/build.html)
- [z-open Development Guide](http://pilakkat.mywire.org/z-open/)
- [Python API Documentation](http://pilakkat.mywire.org/z-open/api.html)

**Key Files:**
- `pyproject.toml` - Project configuration
- `CMakeLists.txt` - Build system
- `scripts/dev.py` - Development workflow
- `tests/` - Test suite

---

### 🦀 Rust Developers
Want to contribute to Kitty Launcher or RClone Mount Applete?

**Setup:**
- Rust 1.94.1+ (latest stable)
- `cargo build --release` for optimized builds
- Multi-architecture GitHub Actions CI/CD

**Resources:**
- [Kitty Launcher Learning Guide](https://pilakkat1964.github.io/kitty-launcher/LEARNING_GUIDE.html)
- [RClone Mount Applete Architecture](https://pilakkat1964.github.io/z-rclone-mount-applete/ARCHITECTURE.html)
- [Rust Learning Guide](https://pilakkat1964.github.io/z-rclone-mount-applete/RUST_LEARNING_GUIDE.html)

**Key Files:**
- `Cargo.toml` - Project manifest
- `src/main.rs` - Implementation
- `scripts/dev.sh` - Development workflow
- `.github/workflows/` - CI/CD configuration

---

### 🛠️ System Administrators
Want to deploy these tools at scale?

**Deployment Options:**
1. **Debian Packages** (.deb) - Recommended for most systems
   - AMD64 and ARM64 multiarch support
   - Available in GitHub releases
   - `sudo dpkg -i package-name.deb`

2. **Source Installation** - For customization
   - Python: `pip install -e .`
   - Rust: `cargo install --path .`

3. **Container Deployment** - For isolated environments
   - All projects can run in Docker/Podman
   - See individual project documentation

**Resources:**
- [Z-Edit Packaging](http://pilakkat.mywire.org/z-edit/build.html)
- [Z-Open Packaging](http://pilakkat.mywire.org/z-open/)
- [Kitty Launcher Deployment](https://pilakkat1964.github.io/kitty-launcher/INSTALL.html)
- [RClone Mount Applete Deployment](https://pilakkat1964.github.io/z-rclone-mount-applete/QUICK_START.html)

---

### 👨‍🔬 Maintainers & DevOps Engineers
Managing the entire z-tools ecosystem?

**Key Resources:**
- [CI/CD Standardization Guide](../CI_CD_STANDARDIZATION_GUIDE.md)
- [Build System Unification](../AGENTS_STANDARDIZATION_GUIDE.md)
- [GitHub Pages Deployment](../CROSS_PROJECT_INDEX.md)

**Automation:**
- GitHub Actions CI/CD workflows in `.github/workflows/`
- Automated multi-architecture builds
- Security scanning with cargo-audit and bandit
- Automated release creation and asset upload

---

## 🔗 Cross-Project Navigation

### GitHub Repositories
All z-tools projects are open source and available on GitHub under the pilakkat1964 account:

| Project | Repository | Language | Status |
|---------|-----------|----------|--------|
| z-edit | [pilakkat1964/z-edit](https://github.com/pilakkat1964/z-edit) | Python | ✅ Active |
| z-open | [pilakkat1964/z-open](https://github.com/pilakkat1964/z-open) | Python | ✅ Active |
| Kitty Launcher | [pilakkat1964/kitty-launcher](https://github.com/pilakkat1964/kitty-launcher) | Rust | ✅ Active |
| RClone Mount Applete | [pilakkat1964/z-rclone-mount-applete](https://github.com/pilakkat1964/z-rclone-mount-applete) | Rust | ✅ Active |

### GitHub Pages Sites
Official documentation for each project:

| Project | Documentation URL | Theme |
|---------|------------------|-------|
| z-edit | http://pilakkat.mywire.org/z-edit/ | Slate |
| z-open | http://pilakkat.mywire.org/z-open/ | Slate |
| Kitty Launcher | https://pilakkat1964.github.io/kitty-launcher/ | Slate |
| RClone Mount Applete | https://pilakkat1964.github.io/z-rclone-mount-applete/ | Slate |

---

## 📊 Project Statistics

### Code Metrics
```
Z-Edit:                    1,725 lines (Python)
Z-Open:                    1,400+ lines (Python)
Kitty Launcher:            957 lines (Rust)
RClone Mount Applete:      591 lines (Rust)
────────────────────────────────────
Total Source Code:         ~5,700 lines
```

### Documentation
```
Z-Edit:                    5,500+ lines
Z-Open:                    5,500+ lines
Kitty Launcher:            2,200+ lines
RClone Mount Applete:      2,000+ lines
────────────────────────────────────
Total Documentation:       15,200+ lines
```

### Quality
- ✅ 0 compiler warnings across all projects
- ✅ Comprehensive test coverage
- ✅ Security scanning enabled (bandit + cargo-audit)
- ✅ Automated CI/CD pipelines
- ✅ Multi-architecture support

---

## 🚀 Quick Start by Use Case

### "I want to use these tools"
→ Choose a project from the overview above and follow the installation link

### "I want to contribute to a Python project"
→ See [Python Developers](#-python-developers) section

### "I want to contribute to a Rust project"
→ See [Rust Developers](#-rust-developers) section

### "I want to deploy at scale"
→ See [System Administrators](#-system-administrators) section

### "I want to maintain the ecosystem"
→ See [Maintainers & DevOps Engineers](#-maintainers--devops-engineers) section

---

## 🤝 Contributing

All z-tools projects welcome contributions! Each project has its own:
- Development workflow documentation
- Testing procedures
- Release process
- AGENTS.md file with project-specific guidance

**General process:**
1. Fork the project on GitHub
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Run tests and linting
6. Push and open a pull request

See individual project documentation for specific contribution guidelines.

---

## 📞 Support & Questions

- **Bug Reports:** Use GitHub Issues in the specific project repository
- **Feature Requests:** Open an issue with the `enhancement` label
- **Questions:** Check the FAQ sections in each project's documentation
- **Discussions:** GitHub Discussions available in most repositories

---

## 📄 License

All z-tools projects are licensed under the **MIT License**, making them suitable for both personal and commercial use.

---

## 🔄 What's New

### Priority 2 Complete: Build System Unification ✅
- ARM64 multiarch support for Python projects
- Cargo-audit security scanning for Rust projects
- Unified CI/CD patterns across all projects
- Comprehensive standardization guide

### Priority 3 In Progress: GitHub Pages Deployment ✅
- Z-Edit: Published ✅
- Z-Open: Published ✅
- Kitty Launcher: Published ✅
- RClone Mount Applete: Published ✅

### Upcoming: Priority 4 - Package Repository Publishing
- PyPI publishing for Python projects
- Crates.io publishing for Rust projects
- Shared testing utilities
- Enhanced contribution guidelines

---

**Last Updated:** April 16, 2026  
**Master Index Version:** 1.0  
**Total Documentation Pages:** 15,200+ lines across 4 projects
