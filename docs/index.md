---
layout: splash
title: "Z-Tools Portfolio"
excerpt: "A unified suite of specialized Linux utilities designed to work together seamlessly."
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/header-bg.jpg
  actions:
    - label: "Explore Projects"
      url: "/projects/"
    - label: "View on GitHub"
      url: "https://github.com/pilakkat1964/z-tools"

intro:
  - excerpt: "Production-ready Linux utilities built with modern infrastructure and comprehensive documentation."

feature_row:
  - image_path: /assets/images/z-edit-icon.png
    alt: "Z-Edit"
    title: "Z-Edit"
    excerpt: "Smart file editor launcher. Opens files in the right editor based on MIME type or extension."
    url: "/projects/z-edit/"
    btn_label: "Learn More"
    btn_class: "btn--primary"
  
  - image_path: /assets/images/z-open-icon.png
    alt: "Z-Open"
    title: "Z-Open"
    excerpt: "Intelligent file opener with fuzzy matching. Find and open files by name or URL."
    url: "/projects/z-open/"
    btn_label: "Learn More"
    btn_class: "btn--primary"
  
  - image_path: /assets/images/z-kitty-icon.png
    alt: "Z-Kitty Launcher"
    title: "Z-Kitty Launcher"
    excerpt: "Terminal session manager for Kitty. Create, manage, and switch terminal sessions effortlessly."
    url: "/projects/z-kitty-launcher/"
    btn_label: "Learn More"
    btn_class: "btn--primary"

feature_row2:
  - image_path: /assets/images/z-rclone-icon.png
    alt: "Z-RClone Mount Applete"
    title: "Z-RClone Mount Applete"
    excerpt: "System tray manager for rclone cloud storage. Mount and manage cloud filesystems from your desktop."
    url: "/projects/z-rclone-mount-applete/"
    btn_label: "Learn More"
    btn_class: "btn--primary"

---

{% include feature_row id="intro" type="center" %}

## Featured Projects

{% include feature_row %}

{% include feature_row id="feature_row2" %}

## Navigate the Ecosystem

Each project has its own dedicated documentation site with detailed guides, API references, and examples. Use the links below to explore:

- **[Z-Edit](https://pilakkat.mywire.org/z-edit/)** - Smart file editor launcher (Python)
- **[Z-Open](https://pilakkat.mywire.org/z-open/)** - Intelligent file opener (Python)
- **[Z-Kitty Launcher](https://pilakkat.mywire.org/z-kitty-launcher/)** - Terminal session manager (Rust)
- **[Z-RClone Mount Applete](https://pilakkat.mywire.org/z-rclone-mount-applete/)** - System tray manager for rclone (Rust)

Each project site includes quick-start guides, installation instructions, and links back to this portfolio.

## Why Z-Tools?

### 🎯 **Unix Philosophy**
Each tool does one thing and does it well. Designed to compose seamlessly into powerful workflows.

### ⚡ **Production Ready**
Battle-tested code with modern CI/CD, automated testing, and professional package distribution.

### 📚 **Comprehensive Docs**
From quick-start guides to architecture deep-dives, documentation for every skill level.

### 🔧 **Developer Friendly**
Modern build systems (CMake, Cargo), automated releases, and welcoming contribution guidelines.

### 🐧 **Linux Native**
Optimized for Linux environments. Packaging for Debian, PyPI, Crates.io, and more.

---

## Portfolio Documentation

Comprehensive technical documentation for the entire z-tools ecosystem, including standardization guides, CI/CD pipelines, build infrastructure, and development workflows.

📚 **[Browse Complete Portfolio Documentation →](/documentation/)**

Quick access to common topics:
- **[CI/CD Standardization Guide](/portfolio-docs/ci-cd-standardization-guide/)** - Build pipeline standards across all projects
- **[Crates.io Publishing](/portfolio-docs/crates-io-analysis/)** - Guide to publishing Rust projects
- **[Repository Tool Guide](/portfolio-docs/repo-tool-guide/)** - Multi-project development tool
- **[Bootstrap Documentation](/portfolio-docs/bootstrap/)** - Project setup and initialization
- **[Cross-Project Index](/portfolio-docs/cross-project-index/)** - Overview of all z-tools projects

---

## Quick Start

### Install Z-Edit
```bash
pip install zedit
# or for system-wide: sudo apt install zedit
```

### Use It
```bash
zedit myfile.py              # Opens in vim (auto-selected)
zedit --list                 # Show all configured editors
zedit --init-config          # Create user configuration
```

### Learn More
- 📖 [Full Documentation](/projects/)
- 🚀 [Installation Guide](https://github.com/pilakkat1964/z-edit#installation)
- 💻 [Source Code](https://github.com/pilakkat1964)

---

## Latest Updates

- **v0.6.5** - Z-Tools portfolio synchronized with modern infrastructure
- **v0.6.5** - Z-Edit gains improved Jekyll documentation and GitHub Pages support
- **v0.6.5** - Z-Open released with comprehensive fuzzy matching

---

## Community

- 💬 [GitHub Discussions](https://github.com/pilakkat1964/z-tools/discussions) - Ask questions
- 🐛 [Report Issues](https://github.com/pilakkat1964/z-tools/issues) - Found a bug?
- 🤝 [Contribute](https://github.com/pilakkat1964/z-tools/blob/main/CONTRIBUTING.md) - Help us improve

---

## License

All Z-Tools projects are open source under the **MIT License**. Free for personal and commercial use.

---

**Built with** ❤️ **using** [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) **theme**

