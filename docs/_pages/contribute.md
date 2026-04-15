---
title: "Contribute"
layout: single
permalink: /contribute/
author_profile: true
sidebar:
  nav: "main"
---

## Contributing to Z-Tools

We welcome contributions from developers of all experience levels. This guide will help you get started.

### Ways to Contribute

1. **Report Bugs** - Found a problem? [Open an issue](https://github.com/pilakkat1964/z-tools/issues)
2. **Suggest Features** - Have an idea? [Start a discussion](https://github.com/pilakkat1964/z-tools/discussions)
3. **Improve Documentation** - Help us improve guides and examples
4. **Fix Bugs** - Submit pull requests for existing issues
5. **Add Tests** - Increase test coverage for reliability
6. **Create Examples** - Share useful configurations and workflows

### Getting Started

Each Z-Tools project has its own repository with detailed development instructions:

- **[Z-Edit](https://github.com/pilakkat1964/z-edit)** - See `DEVELOPMENT.md`
- **[Z-Open](https://github.com/pilakkat1964/z-open)** - See `DEVELOPMENT.md`
- **[Z-Kitty Launcher](https://github.com/pilakkat1964/z-kitty-launcher)** - See `DEVELOPMENT.md`
- **[Z-RClone Mount Applete](https://github.com/pilakkat1964/z-rclone-mount-applete)** - See `DEVELOPMENT.md`

### General Guidelines

#### Code Quality
- Write clean, readable code
- Follow project-specific style guides
- Include docstrings and comments for complex logic
- Maintain or improve test coverage

#### Commit Messages
- Use clear, descriptive commit messages
- Reference relevant issues: `fixes #123`
- Follow conventional commits when possible: `feat:`, `fix:`, `docs:`, etc.

#### Pull Requests
- Create a feature branch: `git checkout -b feature/my-feature`
- Make focused changes addressing one concern per PR
- Write a clear PR description explaining the changes
- Link related issues and discussions
- Ensure CI/CD checks pass before requesting review

#### Documentation
- Update relevant documentation with your changes
- Add examples for new features
- Keep README.md current
- Document breaking changes clearly

### Development Workflow

```bash
# Clone the repository
git clone https://github.com/pilakkat1964/z-tools.git
cd z-tools

# Set up development environment
source setup-env.sh dev

# Create feature branch
git checkout -b feature/my-feature

# Make changes and test
# See individual project DEVELOPMENT.md for testing commands

# Commit and push
git commit -m "feat: description of changes"
git push origin feature/my-feature

# Open a pull request on GitHub
```

### Project Structure

```
z-tools/
├── z-edit/                    # Smart file editor launcher
├── z-open/                    # Intelligent file/URL opener
├── z-kitty-launcher/          # Terminal session manager
├── z-rclone-mount-applete/    # Cloud storage management
├── scripts/                   # Portfolio-wide tooling
├── docs/                      # Documentation
└── README.md                  # This site's content
```

### Community Standards

- Be respectful and inclusive
- Assume good intentions
- Provide constructive feedback
- Help others learn and grow
- Celebrate contributions

### Questions?

- [GitHub Discussions](https://github.com/pilakkat1964/z-tools/discussions) - Ask questions
- [GitHub Issues](https://github.com/pilakkat1964/z-tools/issues) - Report problems
- [Email](mailto:dev@example.com) - Contact the maintainers

### Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/). By participating, you are expected to uphold this code.

---

**Thank you for contributing to Z-Tools!** 🎉
