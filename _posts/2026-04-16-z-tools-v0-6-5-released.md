---
title: "Z-Tools v0.6.5 Released"
date: 2026-04-16
categories: [Release, Announcement]
tags: [Version 0.6.5, GitHub Pages, Documentation]
---

We're excited to announce the release of **Z-Tools v0.6.5**, featuring major improvements to documentation, build infrastructure, and GitHub Pages support across all projects.

## What's New

### GitHub Pages & Documentation
- ✨ **Minimal Mistakes Theme** - Beautiful, professional documentation site
- 🎨 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- 📚 **Better Navigation** - Improved sidebar and cross-project links
- 🔍 **Search Support** - Built-in documentation search

### Build & CI/CD Improvements
- 🚀 **Modernized Infrastructure** - uv package manager integration
- 🛠️ **CMake Build System** - Professional-grade build automation
- 🔄 **GitHub Actions Workflows** - Automated testing and releases
- 📦 **Multi-platform Packaging** - DEB, PyPI, and Crates.io support

### Project Infrastructure
- 📖 **Comprehensive Documentation** - Architecture guides, API references
- 🧪 **Enhanced Testing** - Improved test coverage and CI validation
- 🔐 **Security Scanning** - Automated security vulnerability checks
- ♿ **Accessibility** - Better documentation accessibility

## Z-Tools Projects

This release includes updates to all Z-Tools projects:

### Z-Edit v0.6.5
- Smart file editor launcher based on MIME type
- Layered TOML configuration system
- Zero hard dependencies

**[View Z-Edit on GitHub →](https://github.com/pilakkat1964/z-edit)**

### Z-Open v0.6.5
- Intelligent file/URL opener with fuzzy matching
- Content-aware file type detection
- Interactive selection modes

**[View Z-Open on GitHub →](https://github.com/pilakkat1964/z-open)**

### Z-Kitty Launcher
- Terminal session manager for Kitty emulator
- Fast session switching and management

**[View on GitHub →](https://github.com/pilakkat1964/z-kitty-launcher)**

### Z-RClone Mount Applete
- System tray manager for rclone cloud storage
- Mount cloud filesystems from your desktop

**[View on GitHub →](https://github.com/pilakkat1964/z-rclone-mount-applete)**

## Getting Started

### Install Z-Edit
```bash
pip install zedit
# or
uv pip install zedit
```

### Quick Usage
```bash
zedit myfile.py              # Auto-select editor
zedit --list                 # Show all mappings
zedit --init-config          # Create user config
```

## Documentation

- **[Projects](/projects/)** - Browse all Z-Tools utilities
- **[About](/about/)** - Learn about Z-Tools philosophy
- **[Contributing](/contribute/)** - Join our community
- **[GitHub](https://github.com/pilakkat1964/z-tools)** - Source code

## Upgrading

If you're using a previous version:

```bash
pip install --upgrade zedit
# or
uv pip install --upgrade zedit
```

## Known Issues & Limitations

- MacOS support is experimental
- Some features require libmagic for full functionality
- See individual project repositories for detailed issue tracking

## Looking Ahead

Future releases will focus on:
- Enhanced MIME detection capabilities
- Performance optimizations
- Additional platform support
- Community-driven features

## Thank You

We appreciate the support from the community and look forward to your feedback and contributions!

---

**Questions?** [Start a Discussion](https://github.com/pilakkat1964/z-tools/discussions)  
**Found a bug?** [Open an Issue](https://github.com/pilakkat1964/z-tools/issues)  
**Want to contribute?** [See Contributing Guide](/contribute/)
