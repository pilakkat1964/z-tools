# Z-Tools Portfolio

A unified coordination hub for a complementary suite of specialized Linux utilities and tools.

## 🌐 Portfolio Website

**✨ Explore the full portfolio:** [**https://pilakkat.mywire.org/z-tools/**](https://pilakkat.mywire.org/z-tools/)

This repository is also hosted as a professional portfolio website with project showcase, blog, and comprehensive documentation. Built with Jekyll and Minimal Mistakes theme.

## Purpose

This repository serves as the central governance and coordination point for the **z-tools ecosystem** - a collection of focused, single-purpose command-line utilities designed to work together seamlessly.

### What is Z-Tools?

Z-Tools is a portfolio of production-ready utilities that address specific developer and system administration needs:

- **[z-edit](https://github.com/pilakkat1964/z-edit)** - Smart file editor launcher based on MIME type
- **[z-open](https://github.com/pilakkat1964/z-open)** - Intelligent file/URL opener with fuzzy matching
- **[z-kitty-launcher](https://github.com/pilakkat1964/z-kitty-launcher)** - Terminal session manager for Kitty emulator
- **[z-rclone-mount-applete](https://github.com/pilakkat1964/z-rclone-mount-applete)** - System tray manager for rclone cloud storage

## Role of This Repository

This repository provides:

### 📋 Central Documentation
- Standardized CI/CD patterns across all projects
- Multi-architecture build strategies
- Publishing guidelines (PyPI, Crates.io)
- Cross-project index and navigation

### 🛠️ Development Coordination
- Portfolio-wide status tracking (AGENTS.md)
- Unified development workflows
- Synchronized release processes
- Project interdependencies

### 📦 Portfolio Management
- Scripts for local development setup
- Multi-project commit and push workflows
- Version coordination across projects
- Standardization guidelines for new projects

## Getting Started

### 🌐 Portfolio Site

This repository also serves as a **professional portfolio website** using Jekyll and the Minimal Mistakes theme!

**Visit the live site:** [pilakkat.mywire.org/z-tools](http://pilakkat.mywire.org/z-tools/)

**Maintain your portfolio:**
- 📚 [Full User Guide](/guide/) - Complete documentation
- ⚡ [Quick Reference](/quick-ref/) - One-page cheat sheet
- 📋 [Templates](/tree/main/_templates) - Copy & paste templates

**Quick actions:**
- Add a project: Copy `_templates/project-template.md` → `_projects/`
- Write a blog post: Copy `_templates/blog-post-template.md` → `_posts/YYYY-MM-DD-title.md`
- Create a page: Copy `_templates/page-template.md` → `_pages/`

See [_templates/README.md](_templates/README.md) for detailed examples.

### ⚡ Quick Bootstrap (Recommended)

Bootstrap a complete development environment with a single command:

```bash
curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash
```

This automatically:
- Clones the z-tools repository
- Clones all 4 projects
- Checks dependencies
- Sets up Python and Rust environments
- Installs all dependencies

**Takes 10-15 minutes.** See [BOOTSTRAP.md](docs/BOOTSTRAP.md) for details and options.

### Manual Setup

If you prefer step-by-step control:

```bash
# 1. Clone this portfolio and all projects
git clone git@github.com:pilakkat1964/z-tools.git
cd z-tools

# 2. Check dependencies
python3 scripts/dev.py --check-deps

# 3. Setup all projects
python3 scripts/dev.py --setup all
```

Or setup specific projects:

```bash
python3 scripts/dev.py --setup z-edit z-open
```

### View Project Status

```bash
python scripts/dev.py --status
```

### Commit and Push Changes

Commit across all projects:

```bash
python scripts/dev.py --commit-all "Fix: resolve issue X"
```

Push changes:

```bash
python scripts/dev.py --push-all
```

## Documentation

All portfolio-level documentation is available in the `docs/` folder:

- **[BOOTSTRAP.md](docs/BOOTSTRAP.md)** - Complete bootstrap guide for new hosts
- **[MASTER_INDEX.md](docs/MASTER_INDEX.md)** - Complete overview and index
- **[AGENTS.md](AGENTS.md)** - Current development status and priorities
- **[CI_CD_STANDARDIZATION_GUIDE.md](docs/CI_CD_STANDARDIZATION_GUIDE.md)** - Build and deployment standards
- **[CROSS_PROJECT_INDEX.md](docs/CROSS_PROJECT_INDEX.md)** - Detailed project comparison
- **[ARM64_CROSSCOMPILE_GUIDE.md](docs/ARM64_CROSSCOMPILE_GUIDE.md)** - Multi-architecture support
- **[CRATES_IO_QUICK_REFERENCE.md](docs/CRATES_IO_QUICK_REFERENCE.md)** - Package publishing guide

## Repository Structure

```
z-tools/
├── README.md                    # This file
├── AGENTS.md                    # Portfolio status and priorities
├── docs/                        # Standardization and reference guides
│   ├── CI_CD_STANDARDIZATION_GUIDE.md
│   ├── ARM64_CROSSCOMPILE_GUIDE.md
│   ├── CRATES_IO_ANALYSIS.md
│   ├── CRATES_IO_QUICK_REFERENCE.md
│   ├── CROSS_PROJECT_INDEX.md
│   ├── MASTER_INDEX.md
│   └── AGENTS_STANDARDIZATION_GUIDE.md
├── scripts/
│   └── dev.py                  # Portfolio development tool
├── z-edit/                     # Python editor launcher project
├── z-open/                     # Python file opener project
├── z-kitty-launcher/           # Rust terminal manager project
└── z-rclone-mount-applete/     # Rust system tray applet project
```

## Quick Links

### Project Repositories
- z-edit: https://github.com/pilakkat1964/z-edit
- z-open: https://github.com/pilakkat1964/z-open
- z-kitty-launcher: https://github.com/pilakkat1964/z-kitty-launcher
- z-rclone-mount-applete: https://github.com/pilakkat1964/z-rclone-mount-applete

### Documentation Sites
- z-edit: http://pilakkat.mywire.org/z-edit/
- z-open: http://pilakkat.mywire.org/z-open/
- z-kitty-launcher: http://pilakkat.mywire.org/z-kitty-launcher/
- z-rclone-mount-applete: https://pilakkat.mywire.org/z-rclone-mount-applete/

## Development Status

All projects are **production-ready** with:

- ✅ Multi-architecture support (AMD64, ARM64)
- ✅ Automated CI/CD pipelines
- ✅ GitHub Pages documentation
- ✅ Package registry publishing (PyPI, Crates.io)
- ✅ Comprehensive security scanning
- ✅ Professional quality code

## License

All z-tools projects are licensed under the MIT License. See individual project repositories for details.

## Maintainer

**pilakkat1964** - https://github.com/pilakkat1964

---

**Last Updated:** April 16, 2026  
**Status:** Production Ready, Active Development
