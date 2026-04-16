---
title: "Bootstrap Documentation"
permalink: /portfolio-docs/bootstrap-documentation/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# Z-Tools Bootstrap Guide

Complete guide to bootstrapping a z-tools development environment from scratch on a new host.

## Quick Start (One-Liner)

```bash
curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash
```

Or using wget:

```bash
wget -qO- https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash
```

This single command will:
1. Clone the z-tools repository
2. Verify all dependencies
3. Clone all 4 projects (z-edit, z-open, z-kitty-launcher, z-rclone-mount-applete)
4. Setup complete development environments for both Python and Rust projects
5. Create virtual environments and install all dependencies

**Total time: 10-15 minutes** (depending on internet connection and system performance)

---

## What Gets Installed

### Projects Cloned
- **z-edit** (Python) - Smart file editor launcher based on MIME type
- **z-open** (Python) - Intelligent file/URL opener with fuzzy matching
- **z-kitty-launcher** (Rust) - Terminal session manager for Kitty emulator
- **z-rclone-mount-applete** (Rust) - System tray manager for rclone cloud storage

### Development Environments
- **Python Projects**: Virtual environment (.venv) with all dependencies installed
- **Rust Projects**: Cargo environment ready for development

### Build Tools & Dependencies
- Git (for repository management)
- Python 3 (for Python projects and scripts)
- Rust toolchain (if not already present, Cargo is used)
- Language-specific package managers (pip, cargo)

---

## Prerequisites

### Minimum Requirements
- **Git**: Version control system
- **Python 3**: Version 3.8 or higher
- **SSH Access**: To clone repositories (ensure you have SSH keys configured on GitHub)

### Optional (Recommended)
- **uv**: Modern Python package installer (faster than pip)
- **Rust Toolchain**: If you plan to develop Rust projects
  - rustc (Rust compiler)
  - cargo (Rust package manager)

### Platform-Specific Setup

#### Linux (Debian/Ubuntu)
```bash
sudo apt-get update
sudo apt-get install git python3 python3-pip python3-venv
```

Optional Rust:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

#### Linux (Fedora/RHEL)
```bash
sudo dnf install git python3 python3-pip
```

Optional Rust:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

#### macOS
Using Homebrew:
```bash
brew install git python3
```

Optional Rust:
```bash
brew install rustup-init
rustup-init
```

#### Windows
- Install [Git for Windows](https://git-scm.com/download/win)
- Install [Python 3](https://www.python.org/downloads/windows/)
- Install [Rust](https://www.rust-lang.org/tools/install)

---

## Bootstrap Methods

### Method 1: Automated Bootstrap (Recommended)

The easiest way - fully automated with one command:

```bash
curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash
```

**Features:**
- Automatic dependency checking
- Interactive prompts for confirmation
- Clean, colored output
- Error handling and recovery suggestions
- Progress tracking

### Method 2: Custom Installation Directory

Specify where to install:

```bash
INSTALL_DIR=~/mytools curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash
```

### Method 3: Skip Confirmations (For CI/CD)

```bash
NO_CONFIRM=1 curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash
```

### Method 4: Manual Bootstrap

If you prefer step-by-step control:

```bash
# 1. Clone the repository
git clone git@github.com:pilakkat1964/z-tools.git
cd z-tools

# 2. Check dependencies
python3 scripts/dev.py --check-deps

# 3. Install any missing dependencies (see output)
# ... install dependencies based on your platform ...

# 4. Run bootstrap
python3 scripts/dev.py --bootstrap
```

### Method 5: Interactive Bootstrap

For hands-on control with a menu:

```bash
# Navigate to z-tools directory
cd z-tools

# Start interactive mode
python3 scripts/dev.py --interactive

# Select options:
# 1. View project status
# 2. Setup projects
# 3. Clone projects
# 4. Etc.
```

---

## Post-Bootstrap Verification

After bootstrap completes, verify your setup:

```bash
# Navigate to z-tools
cd ~/z-tools

# Check status of all projects
python3 scripts/dev.py --status

# Output should show:
# 🟢 z-edit [main]
# 🟢 z-open [main]
# 🟢 z-kitty-launcher [main]
# 🟢 z-rclone-mount-applete [main]
```

Expected output indicators:
- **🟢** = Project cloned and clean
- **🔴** = Project has uncommitted changes
- **[branch-name]** = Current Git branch
- **(ahead: X, behind: Y)** = Sync status with remote

---

## Using Your Bootstrap Environment

### Python Projects (z-edit, z-open)

```bash
# Navigate to project
cd ~/z-tools/z-edit

# Activate virtual environment
source .venv/bin/activate

# Install/update dependencies
pip install -e .

# Run tests
pytest

# Deactivate when done
deactivate
```

### Rust Projects (z-kitty-launcher, z-rclone-mount-applete)

```bash
# Navigate to project
cd ~/z-tools/z-kitty-launcher

# Build project
cargo build --release

# Run tests
cargo test

# Run the binary
cargo run --release
```

---

## Common Tasks After Bootstrap

### View Project Status
```bash
python3 scripts/dev.py --status
```

### Setup Only Specific Projects
```bash
python3 scripts/dev.py --setup z-edit z-open
```

### Commit Changes Across All Projects
```bash
python3 scripts/dev.py --commit-all "Fix: resolve issue #123"
```

### Push Changes to Remote
```bash
python3 scripts/dev.py --push-all
```

### Interactive Menu
```bash
python3 scripts/dev.py --interactive
```

---

## Troubleshooting

### Issue: SSH Key Error During Clone

**Error:** `Permission denied (publickey). fatal: Could not read from remote repository.`

**Solution:**
1. Ensure you have generated SSH keys: `ssh-keygen -t ed25519`
2. Add your public key to GitHub: https://github.com/settings/ssh
3. Test SSH connection: `ssh -T git@github.com`
4. Re-run bootstrap

### Issue: Python Virtual Environment Won't Activate

**Error:** `source: command not found` or similar on Windows

**Solution:**
- **Linux/macOS**: Use `source .venv/bin/activate`
- **Windows CMD**: Use `.venv\Scripts\activate.bat`
- **Windows PowerShell**: Use `.venv\Scripts\Activate.ps1`

### Issue: Cargo/Rust Not Found

**Error:** `cargo: command not found`

**Solution:**
```bash
# Install Rust if not already installed
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Source the Rust environment
source $HOME/.cargo/env

# Verify installation
cargo --version
rustc --version
```

### Issue: Permission Denied on bootstrap.sh

**Error:** `Permission denied: ./bootstrap.sh`

**Solution:**
```bash
chmod +x scripts/bootstrap.sh
./scripts/bootstrap.sh
```

### Issue: Cloning Fails Silently

**Error:** Bootstrap appears to hang or exit without cloning

**Solution:**
1. Check your internet connection
2. Verify SSH is working: `ssh -T git@github.com`
3. Try manual cloning: `git clone git@github.com:pilakkat1964/z-tools.git`
4. Check available disk space: `df -h`

### Issue: Dependency Check Fails

**Error:** `Missing required dependencies: python3, git`

**Solution:**
Check the printed installation instructions for your platform (Ubuntu, Fedora, macOS, etc.) and follow them.

---

## Advanced Bootstrap Options

### Automated Installation for Teams

For team onboarding, you can create a wrapper script:

```bash
#!/bin/bash
# team-bootstrap.sh - Custom team bootstrap

# Set team defaults
export INSTALL_DIR=/opt/z-tools
export NO_CONFIRM=1

# Run bootstrap
bash -c "$(curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh)"
```

### CI/CD Integration

For continuous integration systems:

```yaml
# GitHub Actions example
- name: Bootstrap Z-Tools
  run: |
    NO_CONFIRM=1 bash -c "$(curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh)"
```

### Offline Bootstrap

If you don't have internet access on the target machine:

1. Clone on a machine with internet:
   ```bash
   git clone git@github.com:pilakkat1964/z-tools.git
   ```

2. Transfer to offline machine (USB, scp, etc.)

3. Run locally:
   ```bash
   cd z-tools
   python3 scripts/dev.py --bootstrap
   ```

---

## Bootstrap Internals

### What The Bootstrap Script Does

1. **Checks System Information**
   - OS type and architecture
   - Available disk space
   - Network connectivity

2. **Verifies Dependencies**
   - Git installed and working
   - Python 3 installed (3.8+)
   - Optional tools (uv, cargo, rustc)

3. **Clones Repository**
   - Fetches z-tools repository from GitHub
   - Places in install directory

4. **Clones All Projects**
   - z-edit (Python)
   - z-open (Python)
   - z-kitty-launcher (Rust)
   - z-rclone-mount-applete (Rust)

5. **Sets Up Environments**
   - **Python**: Creates .venv, installs dependencies via pip or uv
   - **Rust**: Runs cargo check to verify toolchain and build setup

6. **Verifies Installation**
   - Tests all projects are accessible
   - Confirms development environments are ready

### Bootstrap Logs

Detailed logs are printed during bootstrap. Save them if needed:

```bash
curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash 2>&1 | tee bootstrap.log
```

---

## Maintaining Your Bootstrap Environment

### Update Repository

```bash
cd ~/z-tools
git pull origin main
```

### Update Individual Projects

```bash
python3 scripts/dev.py --status
# Then update as needed in each project
```

### Re-run Bootstrap

To rebuild development environments:

```bash
python3 scripts/dev.py --setup all
```

### Clean Up

To remove all development artifacts while keeping source:

```bash
# Python projects
rm -rf z-edit/.venv z-open/.venv

# Rust projects (optional - rebuilds on next cargo command)
cd z-kitty-launcher && cargo clean
cd ../z-rclone-mount-applete && cargo clean
```

---

## Support & Documentation

For more information:

- **Main Documentation**: See `docs/` directory in z-tools
- **Project Documentation**:
  - z-edit: https://github.com/pilakkat1964/z-edit
  - z-open: https://github.com/pilakkat1964/z-open
  - z-kitty-launcher: https://github.com/pilakkat1964/z-kitty-launcher
  - z-rclone-mount-applete: https://github.com/pilakkat1964/z-rclone-mount-applete

- **Interactive Help**:
  ```bash
  python3 scripts/dev.py --help
  python3 scripts/dev.py --interactive
  ```

---

## See Also

- [README.md](../README.md) - Portfolio overview
- [AGENTS.md](../AGENTS.md) - Development status and priorities
- [CI_CD_STANDARDIZATION_GUIDE.md](./CI_CD_STANDARDIZATION_GUIDE.md) - CI/CD patterns
- [CONTRIBUTING.md](../z-edit/CONTRIBUTING.md) - Contribution guidelines (per-project)

---

**Last Updated:** April 16, 2026  
**Bootstrap Version:** 1.0.0
