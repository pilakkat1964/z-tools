# Contributing to [PROJECT_NAME]

Thank you for your interest in contributing to [PROJECT_NAME]! This document provides guidelines and instructions for contributing code, documentation, bug reports, and feature suggestions.

## Code of Conduct

Be respectful, inclusive, and professional. All contributors are expected to maintain a welcoming environment for everyone.

## How to Contribute

### 1. Reporting Bugs

**Before submitting a bug report:**
- Check existing issues to avoid duplicates
- Verify the bug still exists on the latest version
- Gather relevant information (version, system, error messages)

**When submitting a bug report, include:**
- Clear title summarizing the issue
- Detailed description with steps to reproduce
- Expected vs. actual behavior
- System information (OS, version, architecture)
- Error messages, logs, or stack traces
- Screenshots if applicable

### 2. Suggesting Features

**Feature suggestions should include:**
- Clear use case explaining why this feature is needed
- Detailed description of expected behavior
- Examples or mockups if applicable
- Discussion of potential implementation approaches
- Links to related discussions or features

### 3. Submitting Code Changes

#### Setup Your Development Environment

**For Python Projects (z-edit, z-open):**
```bash
# Clone the repository
git clone git@github.com:pilakkat1964/[PROJECT_NAME].git
cd [PROJECT_NAME]

# Set up Python virtual environment
source scripts/activate.sh
# or manually:
uv venv && source .venv/bin/activate

# Install development dependencies
uv sync
# or with pip:
pip install -e ".[dev]"

# Verify setup
python --version
pytest --version
```

**For Rust Projects (z-kitty-launcher, z-rclone-mount-applete):**
```bash
# Clone the repository
git clone git@github.com:pilakkat1964/[PROJECT_NAME].git
cd [PROJECT_NAME]

# Build the project
cargo build --release

# Run tests
cargo test

# Verify setup
rustc --version
cargo --version
```

#### Development Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   # or for bug fixes:
   git checkout -b fix/issue-number-description
   ```

2. **Make your changes:**
   - Write clear, focused commits with descriptive messages
   - Follow project code style guidelines
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests and checks:**

   **For Python projects:**
   ```bash
   # Run all checks
   ./scripts/dev.py test

   # Or individually:
   pytest                    # Run tests
   ruff check               # Lint check
   ruff format              # Auto-format code
   mypy zedit.py            # Type checking (if available)
   ```

   **For Rust projects:**
   ```bash
   # Run all checks
   cargo test               # Run tests
   cargo clippy             # Lint checking
   cargo fmt --check        # Check formatting
   cargo build --release    # Release build
   cargo doc --open         # Generate docs
   ```

4. **Commit your changes:**
   ```bash
   git add [files]
   git commit -m "type: brief description

   More detailed explanation if needed.
   - Use bullet points for multiple changes
   - Reference issue numbers: fixes #123"
   ```

   **Commit message guidelines:**
   - Use conventional commits: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `style:`, `chore:`
   - First line should be concise (50 chars or less)
   - Provide detailed explanation in the body
   - Reference related issues or PRs

5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request:**
   - Clear title describing the change
   - Reference related issues (e.g., "Fixes #123")
   - Describe what changed and why
   - List any breaking changes
   - Include screenshots for UI changes

#### Code Style Guidelines

**Python Projects (z-edit, z-open):**
- Use Python 3.10+ (3.11+ preferred)
- Follow PEP 8 style guide
- Use type hints (PEP 484)
- Maximum line length: 100 characters
- Use descriptive variable and function names
- Auto-format with `ruff format`

**Rust Projects (z-kitty-launcher, z-rclone-mount-applete):**
- Follow Rust conventions and idioms
- Use `cargo fmt` for formatting
- Address all `cargo clippy` warnings
- Write tests for public APIs
- Document public items with doc comments
- Use meaningful error messages with `anyhow::Context`

#### Testing Requirements

**Python Projects:**
- Write unit tests for new features
- Ensure all tests pass: `pytest`
- Aim for >80% code coverage
- Test both success and error paths
- Include docstring examples if applicable

**Rust Projects:**
- Write unit tests for new functions
- Ensure all tests pass: `cargo test`
- Test error handling and edge cases
- Use meaningful assertions with context
- Add documentation with examples

### 4. Documentation Contributions

Documentation improvements are valuable! You can contribute by:

- **Fixing typos and clarifying text** in existing docs
- **Adding examples** to user guides or API documentation
- **Creating new guides** for common use cases
- **Improving architecture documentation** for developers
- **Translating documentation** to other languages
- **Adding code comments** for complex sections

**Documentation guidelines:**
- Use clear, accessible language
- Include examples and code snippets
- Keep examples up-to-date and tested
- Use consistent formatting and terminology
- Link related documentation sections
- Maintain YAML front matter for Jekyll pages

### 5. Review Process

**What to expect:**
1. Automated checks run (tests, linting, security)
2. Maintainers review code for:
   - Correctness and logic
   - Code style and consistency
   - Test coverage
   - Documentation updates
   - Breaking changes
3. Feedback provided as code review comments
4. Address feedback with additional commits
5. Once approved, your PR will be merged

**Tips for quick reviews:**
- Keep PRs focused (one feature or fix per PR)
- Write clear commit messages
- Add tests before submitting
- Run local checks before pushing
- Respond promptly to review feedback

## Project Structure

### Python Projects (z-edit, z-open)

```
project/
├── zedit.py / zopen.py      # Main application
├── pyproject.toml           # Project configuration
├── setup-env.sh             # Environment setup
├── CMakeLists.txt           # Build system
├── scripts/
│   ├── dev.py              # Development wrapper
│   ├── activate.sh         # Virtual env setup
│   └── with-venv           # Run commands in venv
├── tests/                  # Test suite
├── debian/                 # Debian packaging
├── docs/                   # User documentation
├── .github/workflows/      # CI/CD
├── README.md               # Project overview
└── AGENTS.md               # Agent documentation
```

### Rust Projects (z-kitty-launcher, z-rclone-mount-applete)

```
project/
├── Cargo.toml              # Project manifest
├── Cargo.lock              # Dependency lock
├── src/
│   ├── main.rs            # Entry point
│   └── *.rs               # Modules
├── tests/                 # Integration tests
├── debian/                # Debian packaging
├── docs/                  # Documentation
├── data/                  # Assets (.desktop, etc.)
├── .github/workflows/     # CI/CD
├── README.md              # Project overview
└── AGENTS.md              # Agent documentation
```

## Building and Testing Locally

### Python Projects

```bash
# Setup
source setup-env.sh dev
# or: source scripts/activate.sh

# Build
cmake -B build && cmake --build build
# or: python -m build

# Test
./scripts/dev.py test
# or: pytest

# Package
./scripts/dev.py package
# or: cmake --build build --target package
```

### Rust Projects

```bash
# Build
cargo build --release

# Test
cargo test

# Check
cargo clippy
cargo fmt --check

# Package
cargo build --release
# Debian: dpkg-buildpackage -us -uc
```

## Release Process

### Versioning

All projects follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### Creating a Release

1. **Update version number** in project files
2. **Update CHANGELOG** (if applicable)
3. **Commit changes**: `git commit -m "chore: bump version to X.Y.Z"`
4. **Create git tag**: `git tag vX.Y.Z -m "Release vX.Y.Z"`
5. **Push to remote**: `git push origin master && git push origin vX.Y.Z`
6. **GitHub Actions will automatically:**
   - Run tests and security checks
   - Build release artifacts
   - Create GitHub Release
   - Publish to PyPI (Python) or Crates.io (Rust)

See individual AGENTS.md files for project-specific details.

## Getting Help

- **Documentation**: See `docs/` folder in each project
- **Issues**: Check existing issues or create a new one
- **Discussions**: Use GitHub Discussions for questions
- **Code Examples**: See `docs/examples.md` or project README

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors are valued and recognized! We may mention contributors in:
- Release notes
- Project README
- Contributor list

Thank you for contributing to [PROJECT_NAME]! 🙏
