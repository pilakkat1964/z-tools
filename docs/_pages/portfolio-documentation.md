---
title: "Portfolio Documentation"
permalink: /documentation/
layout: single
author_profile: false
toc: true
toc_sticky: true
toc_label: "Documentation Index"
---

# Z-Tools Portfolio Documentation

Comprehensive technical documentation for the z-tools ecosystem, including standardization guides, build infrastructure, CI/CD pipelines, and development workflows.

## Overview

This documentation covers cross-project standards, infrastructure setup, packaging and distribution, and detailed development guides for the entire z-tools portfolio.

---

## 📋 Master References

### [Master Index]({{ site.baseurl }}/portfolio-docs/master-index/)
{: .notice--info}
Central navigation hub for all portfolio documentation. Start here to understand the complete documentation structure and find what you need quickly.

### [Cross-Project Index]({{ site.baseurl }}/portfolio-docs/cross-project-index/)
{: .notice--info}
Overview of all z-tools projects, their relationships, and how they work together. Includes project status, version tracking, and interdependencies.

---

## 🏗️ Infrastructure & Build Systems

### [CI/CD Standardization Guide]({{ site.baseurl }}/portfolio-docs/ci-cd-standardization-guide/)
{: .notice--primary}
**Complete standardization of CI/CD pipelines across all projects**

Covers:
- GitHub Actions workflow patterns
- Automated testing, linting, and security scanning
- Release automation and version management
- Multi-architecture build strategies
- Package distribution (PyPI, Debian, Crates.io)

### [ARM64 Cross-Compile Guide]({{ site.baseurl }}/portfolio-docs/arm64-crosscompile-guide/)
{: .notice--primary}
**Build Python packages for ARM64 architecture**

Covers:
- Multi-architecture Docker setup
- QEMU-based cross-compilation
- Build verification on target architecture
- ARM64-specific optimization strategies

### [Bootstrap Documentation]({{ site.baseurl }}/portfolio-docs/bootstrap/)
{: .notice--primary}
**Complete project bootstrap and setup procedures**

Covers:
- Initial repository setup
- Development environment configuration
- Dependency management
- Automated setup scripts

---

## 🔧 Development & Standardization

### [Agents Standardization Guide]({{ site.baseurl }}/portfolio-docs/agents-standardization-guide/)
{: .notice--success}
**OpenCode agent documentation standards and best practices**

Covers:
- AGENTS.md file structure
- Agent documentation patterns
- Project status tracking
- Version synchronization

### [Crates.io Analysis]({{ site.baseurl }}/portfolio-docs/crates-io-analysis/)
{: .notice--success}
**Comprehensive analysis of Rust publishing to Crates.io**

Covers:
- Crates.io account setup
- Publishing workflow
- Version management
- Dependency specifications
- Security and maintenance

### [Crates.io Quick Reference]({{ site.baseurl }}/portfolio-docs/crates-io-quick-reference/)
{: .notice--success}
**Quick reference guide for Crates.io publishing**

Covers:
- Quick start checklist
- Common commands
- Troubleshooting tips
- Publishing checklist

---

## 🛠️ Repository Tools

### [Repository Tool Guide]({{ site.baseurl }}/portfolio-docs/repo-tool-guide/)
{: .notice--warning}
**Complete guide to the multi-project repository tool**

Covers:
- Installation and setup
- Basic commands and workflows
- Configuration options
- Integration with development workflow

### [Repository Tool Tutorial]({{ site.baseurl }}/portfolio-docs/repo-tool-tutorial/)
{: .notice--warning}
**Step-by-step tutorial for common repository tasks**

Covers:
- Getting started scenarios
- Common workflows (commit, push, pull, sync)
- Multi-project operations
- Best practices and tips

### [Repository Tool Advanced Guide]({{ site.baseurl }}/portfolio-docs/repo-tool-advanced/)
{: .notice--warning}
**Advanced repository tool features and customization**

Covers:
- Advanced command options
- Custom scripting and automation
- Integration with CI/CD
- Performance optimization

### [README Repository Tool]({{ site.baseurl }}/portfolio-docs/readme-repo-tool/)
{: .notice--warning}
**README documentation for the repository tool**

Covers:
- Feature overview
- Installation methods
- Quick start examples
- Configuration details

---

## 📚 How to Use This Documentation

### For New Contributors
1. Start with the **[Master Index]({{ site.baseurl }}/portfolio-docs/master-index/)**
2. Review **[Cross-Project Index]({{ site.baseurl }}/portfolio-docs/cross-project-index/)** to understand project relationships
3. Follow the **[Bootstrap Documentation]({{ site.baseurl }}/portfolio-docs/bootstrap/)** to set up your environment

### For Infrastructure Setup
1. Review **[CI/CD Standardization Guide]({{ site.baseurl }}/portfolio-docs/ci-cd-standardization-guide/)** for pipeline patterns
2. Check **[ARM64 Cross-Compile Guide]({{ site.baseurl }}/portfolio-docs/arm64-crosscompile-guide/)** if building multi-arch packages

### For Publishing & Releases
1. Follow **[Crates.io Analysis]({{ site.baseurl }}/portfolio-docs/crates-io-analysis/)** for comprehensive overview
2. Use **[Crates.io Quick Reference]({{ site.baseurl }}/portfolio-docs/crates-io-quick-reference/)** for quick lookup

### For Multi-Project Development
1. Install and configure using **[Repository Tool Guide]({{ site.baseurl }}/portfolio-docs/repo-tool-guide/)**
2. Follow tutorials in **[Repository Tool Tutorial]({{ site.baseurl }}/portfolio-docs/repo-tool-tutorial/)**
3. Explore advanced features in **[Repository Tool Advanced Guide]({{ site.baseurl }}/portfolio-docs/repo-tool-advanced/)**

---

## 📖 All Documents

| Document | Purpose | Length |
|----------|---------|--------|
| [Master Index]({{ site.baseurl }}/portfolio-docs/master-index/) | Central navigation hub | Long |
| [Cross-Project Index]({{ site.baseurl }}/portfolio-docs/cross-project-index/) | Project overview | Medium |
| [CI/CD Standardization Guide]({{ site.baseurl }}/portfolio-docs/ci-cd-standardization-guide/) | Build pipeline standards | Comprehensive |
| [ARM64 Cross-Compile Guide]({{ site.baseurl }}/portfolio-docs/arm64-crosscompile-guide/) | Multi-arch builds | Medium |
| [Bootstrap Documentation]({{ site.baseurl }}/portfolio-docs/bootstrap/) | Project setup | Medium |
| [Agents Standardization Guide]({{ site.baseurl }}/portfolio-docs/agents-standardization-guide/) | Agent documentation | Medium |
| [Crates.io Analysis]({{ site.baseurl }}/portfolio-docs/crates-io-analysis/) | Rust publishing | Comprehensive |
| [Crates.io Quick Reference]({{ site.baseurl }}/portfolio-docs/crates-io-quick-reference/) | Publishing quick ref | Short |
| [Repository Tool Guide]({{ site.baseurl }}/portfolio-docs/repo-tool-guide/) | Tool complete guide | Comprehensive |
| [Repository Tool Tutorial]({{ site.baseurl }}/portfolio-docs/repo-tool-tutorial/) | Tutorial walkthrough | Long |
| [Repository Tool Advanced]({{ site.baseurl }}/portfolio-docs/repo-tool-advanced/) | Advanced features | Medium |
| [README Repository Tool]({{ site.baseurl }}/portfolio-docs/readme-repo-tool/) | Tool README | Short |

---

## 🔍 Quick Search

Looking for something specific?

- **Build & Packaging**: See [CI/CD Standardization Guide]({{ site.baseurl }}/portfolio-docs/ci-cd-standardization-guide/) and [ARM64 Cross-Compile Guide]({{ site.baseurl }}/portfolio-docs/arm64-crosscompile-guide/)
- **Rust & Crates.io**: See [Crates.io Analysis]({{ site.baseurl }}/portfolio-docs/crates-io-analysis/) and [Crates.io Quick Reference]({{ site.baseurl }}/portfolio-docs/crates-io-quick-reference/)
- **Repository Tools**: See [Repository Tool Guide]({{ site.baseurl }}/portfolio-docs/repo-tool-guide/) and [Repository Tool Tutorial]({{ site.baseurl }}/portfolio-docs/repo-tool-tutorial/)
- **Getting Started**: See [Bootstrap Documentation]({{ site.baseurl }}/portfolio-docs/bootstrap/) and [Master Index]({{ site.baseurl }}/portfolio-docs/master-index/)
- **Agent Development**: See [Agents Standardization Guide]({{ site.baseurl }}/portfolio-docs/agents-standardization-guide/)

---

## 📝 Contributing to Documentation

Found an issue or want to improve the documentation? 

1. Visit the [GitHub repository](https://github.com/pilakkat1964/z-tools)
2. Edit the documentation files in `docs/_portfolio-docs/`
3. Submit a pull request with your improvements

---

*Last updated: April 16, 2026*
