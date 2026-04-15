#!/usr/bin/env python3
"""
Z-Tools Portfolio Development Manager

Simplifies local development environment setup, project management, and multi-project
Git operations across the z-tools ecosystem.

Features:
- Bootstrap mode: Complete setup from scratch on new hosts
- Dependency verification and installation
- Clone/checkout projects in correct relative positions
- Setup all or specific projects
- View status across all projects
- Commit changes across projects (individually or all at once)
- Push changes upstream (per-project or all projects)
- Interactive project selection
"""

import os
import sys
import subprocess
import argparse
import platform
import shutil
from pathlib import Path
from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass
from enum import Enum
import json

# Configuration
PORTFOLIO_ROOT = Path(__file__).parent.parent
OS_TYPE = platform.system()  # "Linux", "Darwin", "Windows"

PROJECTS = {
    "z-edit": {
        "repo": "git@github.com:pilakkat1964/z-edit.git",
        "language": "python",
        "description": "Smart file editor launcher based on MIME type",
    },
    "z-open": {
        "repo": "git@github.com:pilakkat1964/z-open.git",
        "language": "python",
        "description": "Intelligent file/URL opener with fuzzy matching",
    },
    "z-kitty-launcher": {
        "repo": "git@github.com:pilakkat1964/z-kitty-launcher.git",
        "language": "rust",
        "description": "Terminal session manager for Kitty emulator",
    },
    "z-rclone-mount-applete": {
        "repo": "git@github.com:pilakkat1964/z-rclone-mount-applete.git",
        "language": "rust",
        "description": "System tray manager for rclone cloud storage",
    },
}

COLORS = {
    "RESET": "\033[0m",
    "BOLD": "\033[1m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "RED": "\033[91m",
    "BLUE": "\033[94m",
    "CYAN": "\033[96m",
}


def colored(text: str, color: str) -> str:
    """Return colored text for terminal output."""
    return f"{COLORS[color]}{text}{COLORS['RESET']}"


class BootstrapChecker:
    """Checks and manages bootstrap dependencies."""

    def __init__(self):
        self.missing_deps = []
        self.optional_deps = []

    def check_command_exists(self, cmd: str) -> bool:
        """Check if a command exists in PATH."""
        return shutil.which(cmd) is not None

    def check_all_dependencies(self) -> bool:
        """Check all required dependencies. Returns True if all present."""
        print(header("Checking Dependencies"))

        # Required dependencies
        required = {
            "git": "Git (version control)",
            "python3": "Python 3 (runtime)",
            "pip": "Pip (Python package manager)",
        }

        # Language-specific requirements
        python_deps = {
            "uv": "Uv (Python package installer - recommended)",
        }

        rust_deps = {
            "cargo": "Cargo (Rust package manager)",
            "rustc": "Rustc (Rust compiler)",
        }

        # Check required
        print(f"\n{colored('Required Dependencies:', 'BOLD')}")
        for cmd, desc in required.items():
            if self.check_command_exists(cmd):
                print(success(f"{desc}"))
            else:
                print(error(f"{desc} - NOT FOUND"))
                self.missing_deps.append(cmd)

        # Check optional Python tools
        print(f"\n{colored('Python Development Tools:', 'BOLD')}")
        for cmd, desc in python_deps.items():
            if self.check_command_exists(cmd):
                print(success(f"{desc}"))
            else:
                print(warning(f"{desc} - NOT FOUND (will use pip instead)"))
                self.optional_deps.append(cmd)

        # Check optional Rust tools
        print(f"\n{colored('Rust Development Tools:', 'BOLD')}")
        for cmd, desc in rust_deps.items():
            if self.check_command_exists(cmd):
                print(success(f"{desc}"))
            else:
                print(warning(f"{desc} - NOT FOUND (optional for Rust projects)"))
                self.optional_deps.append(cmd)

        if self.missing_deps:
            print(f"\n{warning('Some required dependencies are missing!')}")
            return False

        print(success("All required dependencies present!"))
        return True

    def get_install_instructions(self) -> str:
        """Return installation instructions for missing dependencies."""
        if not self.missing_deps:
            return ""

        instructions = []

        if OS_TYPE == "Darwin":
            instructions.append("macOS (using Homebrew):")
            instructions.append(f"  brew install {' '.join(self.missing_deps)}")
        elif OS_TYPE == "Linux":
            instructions.append("Linux (using apt):")
            instructions.append(f"  sudo apt-get update")
            instructions.append(f"  sudo apt-get install {' '.join(self.missing_deps)}")
            instructions.append(
                "\nOr on other distributions, use your package manager:"
            )
            instructions.append(
                f"  dnf install {' '.join(self.missing_deps)}  # Fedora/RHEL"
            )
            instructions.append(f"  pacman -S {' '.join(self.missing_deps)}    # Arch")

        # Add Rust instructions if needed
        if "cargo" in self.missing_deps or "rustc" in self.missing_deps:
            instructions.append("\nFor Rust toolchain:")
            instructions.append(
                "  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
            )

        return "\n".join(instructions)


def run_command(
    cmd: List[str], cwd: Optional[Path] = None, capture: bool = True
) -> Tuple[int, str, str]:
    """Run a command and return (returncode, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=capture,
            text=True,
            timeout=120,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "Command timed out"
    except Exception as e:
        return 1, "", str(e)


def header(text: str) -> str:
    """Return formatted header text."""
    return colored(f"\n{'=' * 70}\n{text}\n{'=' * 70}", "BOLD")


def success(text: str) -> str:
    """Return success message."""
    return colored(f"✓ {text}", "GREEN")


def error(text: str) -> str:
    """Return error message."""
    return colored(f"✗ {text}", "RED")


def info(text: str) -> str:
    """Return info message."""
    return colored(f"ℹ {text}", "BLUE")


def warning(text: str) -> str:
    """Return warning message."""
    return colored(f"⚠ {text}", "YELLOW")


class ProjectStatus:
    """Represents the status of a project."""

    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path
        self.exists = path.exists()
        self.is_git = (path / ".git").exists() if self.exists else False
        self.branch = None
        self.status = None
        self.ahead = 0
        self.behind = 0

        if self.is_git:
            self._load_git_info()

    def _load_git_info(self) -> None:
        """Load Git information for the project."""
        try:
            # Get current branch
            result = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=self.path,
                capture_output=True,
                text=True,
                timeout=5,
            )
            self.branch = result.stdout.strip() if result.returncode == 0 else "unknown"

            # Get status
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.path,
                capture_output=True,
                text=True,
                timeout=5,
            )
            self.status = (
                "clean" if result.returncode == 0 and not result.stdout else "dirty"
            )

            # Get ahead/behind count
            result = subprocess.run(
                ["git", "rev-list", "--left-right", "--count", "@{u}...HEAD"],
                cwd=self.path,
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                behind, ahead = result.stdout.strip().split()
                self.behind = int(behind)
                self.ahead = int(ahead)
        except (subprocess.TimeoutExpired, Exception):
            pass

    def display_status(self) -> str:
        """Return formatted status display."""
        if not self.exists:
            return error(f"{self.name}: NOT CLONED")

        status_icon = "🟢" if self.status == "clean" else "🔴"
        branch_info = f" [{self.branch}]" if self.branch else ""

        sync_info = ""
        if self.ahead > 0 or self.behind > 0:
            sync_info = f" (ahead: {self.ahead}, behind: {self.behind})"

        return f"{status_icon} {self.name}{branch_info}{sync_info}"


def get_project_status(project_name: str) -> ProjectStatus:
    """Get status of a specific project."""
    project_path = PORTFOLIO_ROOT / project_name
    return ProjectStatus(project_name, project_path)


def get_all_projects_status() -> List[ProjectStatus]:
    """Get status of all projects."""
    return [get_project_status(name) for name in PROJECTS.keys()]


def show_status(projects: Optional[List[str]] = None) -> None:
    """Display status of projects."""
    print(header("Portfolio Status"))

    if projects:
        statuses = [get_project_status(p) for p in projects if p in PROJECTS]
    else:
        statuses = get_all_projects_status()

    for status in statuses:
        print(status.display_status())

    print()


def select_projects(all_projects: bool = False) -> List[str]:
    """Interactively select projects to work with."""
    if all_projects:
        return list(PROJECTS.keys())

    print(header("Select Projects"))
    print("Available projects:")
    for i, (name, info) in enumerate(PROJECTS.items(), 1):
        print(f"{i}. {colored(name, 'CYAN')} - {info['description']}")

    print(f"\n{len(PROJECTS) + 1}. {colored('All projects', 'CYAN')}")

    while True:
        try:
            choice = input(
                f"\nSelect project(s) (comma-separated, e.g., 1,2,4): "
            ).strip()

            if choice == str(len(PROJECTS) + 1):
                return list(PROJECTS.keys())

            choices = [int(c.strip()) for c in choice.split(",")]
            projects = [
                name for i, name in enumerate(PROJECTS.keys(), 1) if i in choices
            ]

            if projects:
                return projects
            else:
                print(error("Invalid selection. Please try again."))
        except (ValueError, IndexError):
            print(error("Invalid input. Please enter valid numbers."))


def clone_projects(project_names: List[str], verbose: bool = False) -> Tuple[int, int]:
    """Clone specified projects. Returns (success_count, failure_count)."""
    print(header(f"Cloning {len(project_names)} Project(s)"))

    success_count = 0
    failure_count = 0

    for name in project_names:
        if name not in PROJECTS:
            print(error(f"Unknown project: {name}"))
            failure_count += 1
            continue

        project_path = PORTFOLIO_ROOT / name
        if project_path.exists():
            print(warning(f"{name}: Already exists, skipping"))
            continue

        repo_url = PROJECTS[name]["repo"]
        print(f"Cloning {colored(name, 'CYAN')}...")

        try:
            result = subprocess.run(
                ["git", "clone", repo_url, str(project_path)],
                capture_output=not verbose,
                timeout=120,
            )

            if result.returncode == 0:
                print(success(f"{name}: Cloned successfully"))
                success_count += 1
            else:
                print(error(f"{name}: Clone failed"))
                failure_count += 1
        except subprocess.TimeoutExpired:
            print(error(f"{name}: Clone timed out"))
            failure_count += 1
        except Exception as e:
            print(error(f"{name}: {str(e)}"))
            failure_count += 1

    return success_count, failure_count


def setup_projects(project_names: List[str], verbose: bool = False) -> None:
    """Setup local development environment for projects."""
    print(header(f"Setting Up {len(project_names)} Project(s)"))

    # First, clone any missing projects
    missing = [p for p in project_names if not (PORTFOLIO_ROOT / p).exists()]
    if missing:
        print(info(f"Found {len(missing)} project(s) to clone"))
        clone_projects(missing, verbose)

    # Setup each project based on language
    for name in project_names:
        project_path = PORTFOLIO_ROOT / name
        if not project_path.exists():
            print(error(f"{name}: Path not found"))
            continue

        language = PROJECTS[name]["language"]
        print(f"\nSetting up {colored(name, 'CYAN')} ({language})...")

        if language == "python":
            setup_python_project(project_path)
        elif language == "rust":
            setup_rust_project(project_path)

    print(success("Setup complete!"))


def setup_python_project(project_path: Path) -> None:
    """Setup Python project environment."""
    try:
        # Check if setup-env.sh exists
        setup_script = project_path / "setup-env.sh"
        if setup_script.exists():
            print(f"  Running {setup_script.name}...")
            result = subprocess.run(
                ["bash", str(setup_script), "dev"],
                cwd=project_path,
                capture_output=True,
                timeout=120,
            )
            if result.returncode == 0:
                print(success("  Python environment setup"))
            else:
                print(warning(f"  setup-env.sh exited with code {result.returncode}"))
        else:
            print(warning("  No setup-env.sh found, creating venv manually"))
            subprocess.run(
                ["python3", "-m", "venv", ".venv"],
                cwd=project_path,
                capture_output=True,
            )
            print(success("  Virtual environment created"))
    except Exception as e:
        print(warning(f"  Setup failed: {str(e)}"))


def setup_rust_project(project_path: Path) -> None:
    """Setup Rust project environment."""
    try:
        print(f"  Running cargo check...")
        result = subprocess.run(
            ["cargo", "check"],
            cwd=project_path,
            capture_output=True,
            timeout=120,
        )
        if result.returncode == 0:
            print(success("  Rust environment ready"))
        else:
            print(warning(f"  cargo check exited with code {result.returncode}"))
    except Exception as e:
        print(warning(f"  Setup failed: {str(e)}"))


def commit_projects(project_names: List[str], message: str) -> Tuple[int, int]:
    """Commit changes in specified projects. Returns (success_count, failure_count)."""
    print(header(f"Committing Changes in {len(project_names)} Project(s)"))
    print(f"Message: {colored(message, 'CYAN')}\n")

    success_count = 0
    failure_count = 0

    for name in project_names:
        project_path = PORTFOLIO_ROOT / name
        if not project_path.exists():
            print(warning(f"{name}: Project not found"))
            continue

        if not (project_path / ".git").exists():
            print(warning(f"{name}: Not a Git repository"))
            continue

        print(f"Committing {colored(name, 'CYAN')}...")

        try:
            # Check if there are changes
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=10,
            )

            if not result.stdout.strip():
                print(info(f"{name}: No changes to commit"))
                continue

            # Stage all changes
            subprocess.run(
                ["git", "add", "-A"],
                cwd=project_path,
                capture_output=True,
                timeout=10,
            )

            # Commit
            result = subprocess.run(
                ["git", "commit", "-m", message],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                print(success(f"{name}: Committed"))
                success_count += 1
            else:
                print(warning(f"{name}: Commit failed - {result.stderr[:100]}"))
                failure_count += 1
        except Exception as e:
            print(error(f"{name}: {str(e)}"))
            failure_count += 1

    return success_count, failure_count


def push_projects(project_names: List[str]) -> Tuple[int, int]:
    """Push changes in specified projects. Returns (success_count, failure_count)."""
    print(header(f"Pushing Changes in {len(project_names)} Project(s)"))

    success_count = 0
    failure_count = 0

    for name in project_names:
        project_path = PORTFOLIO_ROOT / name
        if not project_path.exists():
            print(warning(f"{name}: Project not found"))
            continue

        if not (project_path / ".git").exists():
            print(warning(f"{name}: Not a Git repository"))
            continue

        # Get current branch
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=5,
            )
            branch = result.stdout.strip() if result.returncode == 0 else "master"
        except Exception:
            branch = "master"

        print(f"Pushing {colored(name, 'CYAN')} (branch: {branch})...")

        try:
            result = subprocess.run(
                ["git", "push", "origin", branch],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode == 0:
                print(success(f"{name}: Pushed"))
                success_count += 1
            else:
                # Check if everything is already up to date
                if "Everything up-to-date" in result.stdout:
                    print(info(f"{name}: Already up to date"))
                else:
                    print(warning(f"{name}: Push failed - {result.stderr[:100]}"))
                    failure_count += 1
        except Exception as e:
            print(error(f"{name}: {str(e)}"))
            failure_count += 1

    return success_count, failure_count


def bootstrap(check_only: bool = False, skip_confirmation: bool = False) -> bool:
    """Bootstrap the development environment from scratch."""
    print(header("Z-Tools Bootstrap"))

    checker = BootstrapChecker()

    # Check dependencies
    deps_ok = checker.check_all_dependencies()

    if not deps_ok:
        print(f"\n{error('Installation instructions:')}")
        print(checker.get_install_instructions())
        print(f"\n{warning('Please install missing dependencies and try again.')}")
        return False

    if check_only:
        print(f"\n{success('All dependencies satisfied! Bootstrap is ready.')}")
        return True

    # Ask for confirmation before proceeding
    if not skip_confirmation:
        print(f"\n{info('Bootstrap will:')}")
        print("  1. Clone all 4 z-tools projects")
        print("  2. Setup Python and Rust development environments")
        print("  3. Create virtual environments and install dependencies")
        print("\nThis may take 10-15 minutes depending on your connection.")

        response = input(f"\n{colored('Continue? (yes/no): ', 'CYAN')}").strip().lower()
        if response not in ["yes", "y"]:
            print(warning("Bootstrap cancelled"))
            return False

    print(f"\n{info('Starting bootstrap...')}\n")

    # Clone all projects
    print(header("Step 1: Cloning Projects"))
    missing = [p for p in PROJECTS.keys() if not (PORTFOLIO_ROOT / p).exists()]
    if missing:
        success_count, failure_count = clone_projects(missing)
        if failure_count > 0:
            print(
                error(
                    "Some projects failed to clone. Please check your SSH keys and try again."
                )
            )
            return False
    else:
        print(success("All projects already cloned"))

    # Setup all projects
    print(f"\n{header('Step 2: Setting Up Projects')}")
    setup_projects(list(PROJECTS.keys()))

    print(f"\n{header('Bootstrap Complete!')}")
    print(success("Your z-tools development environment is ready!"))
    print(f"\n{info('Next steps:')}")
    print("  1. Source your shell profile: source ~/.bashrc  (or ~/.zshrc for zsh)")
    print("  2. Navigate to projects: cd z-tools/z-edit  (or any other project)")
    print("  3. For Python projects: source .venv/bin/activate")
    print("  4. For Rust projects: cargo build")
    print("\nUse 'python scripts/dev.py --status' to see project status")

    return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Z-Tools Portfolio Development Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python dev.py --bootstrap                 # Full bootstrap from scratch
  python dev.py --check-deps                # Check dependencies only
  python dev.py --status                    # Show status of all projects
  python dev.py --setup all                 # Setup all projects
  python dev.py --setup z-edit z-open       # Setup specific projects
  python dev.py --interactive               # Interactive mode (default)
  python dev.py --commit-all "Fix: issue"   # Commit all projects with message
  python dev.py --push z-edit               # Push specific project
  python dev.py --push-all                  # Push all projects
        """,
    )

    parser.add_argument(
        "--bootstrap",
        action="store_true",
        help="Bootstrap complete development environment from scratch",
    )
    parser.add_argument(
        "--check-deps",
        action="store_true",
        help="Check if all dependencies are installed",
    )
    parser.add_argument(
        "--no-confirm",
        action="store_true",
        help="Skip confirmation prompts (for automated bootstrap)",
    )
    parser.add_argument(
        "--status",
        nargs="*",
        help="Show project status (all if no projects specified)",
        metavar="PROJECT",
    )
    parser.add_argument(
        "--setup",
        nargs="+",
        help="Setup projects (use 'all' for all projects)",
        metavar="PROJECT",
    )
    parser.add_argument(
        "--clone",
        nargs="+",
        help="Clone projects",
        metavar="PROJECT",
    )
    parser.add_argument(
        "--commit",
        nargs="+",
        help="Commit changes in projects with message (last arg is message)",
        metavar="PROJECT_OR_MESSAGE",
    )
    parser.add_argument(
        "--commit-all",
        help="Commit all projects with message",
        metavar="MESSAGE",
    )
    parser.add_argument(
        "--push",
        nargs="+",
        help="Push projects upstream",
        metavar="PROJECT",
    )
    parser.add_argument(
        "--push-all",
        action="store_true",
        help="Push all projects upstream",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Interactive mode (default if no args)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    # Handle --bootstrap
    if args.bootstrap:
        success_result = bootstrap(skip_confirmation=args.no_confirm)
        sys.exit(0 if success_result else 1)

    # Handle --check-deps
    if args.check_deps:
        checker = BootstrapChecker()
        success_result = checker.check_all_dependencies()
        sys.exit(0 if success_result else 1)

    # If no arguments provided, show interactive menu
    if len(sys.argv) == 1 or args.interactive:
        show_interactive_menu()
        return

    # Handle --status
    if args.status is not None:
        if args.status:
            show_status(args.status)
        else:
            show_status()
        return

    # Handle --setup
    if args.setup:
        if args.setup == ["all"]:
            projects = list(PROJECTS.keys())
        else:
            projects = args.setup
        setup_projects(projects, args.verbose)
        return

    # Handle --clone
    if args.clone:
        clone_projects(args.clone, args.verbose)
        return

    # Handle --commit-all
    if args.commit_all:
        projects = list(PROJECTS.keys())
        success, failure = commit_projects(projects, args.commit_all)
        print(f"\n{success(f'Committed: {success}')} {error(f'Failed: {failure}')}")
        return

    # Handle --commit
    if args.commit:
        message = args.commit[-1]
        projects = args.commit[:-1] if len(args.commit) > 1 else list(PROJECTS.keys())
        success, failure = commit_projects(projects, message)
        print(f"\n{success(f'Committed: {success}')} {error(f'Failed: {failure}')}")
        return

    # Handle --push-all
    if args.push_all:
        projects = list(PROJECTS.keys())
        success, failure = push_projects(projects)
        print(f"\n{success(f'Pushed: {success}')} {error(f'Failed: {failure}')}")
        return

    # Handle --push
    if args.push:
        success, failure = push_projects(args.push)
        print(f"\n{success(f'Pushed: {success}')} {error(f'Failed: {failure}')}")
        return


def show_interactive_menu():
    """Show interactive menu for portfolio management."""
    while True:
        print(header("Z-Tools Portfolio Manager"))
        print("1. View project status")
        print("2. Setup projects")
        print("3. Clone projects")
        print("4. Commit changes")
        print("5. Push changes")
        print("6. Exit")

        choice = input("\nSelect option (1-6): ").strip()

        if choice == "1":
            show_status()
        elif choice == "2":
            projects = select_projects()
            setup_projects(projects)
        elif choice == "3":
            projects = select_projects()
            clone_projects(projects)
        elif choice == "4":
            projects = select_projects()
            message = input("Commit message: ").strip()
            if message:
                success, failure = commit_projects(projects, message)
                print(
                    f"\n{success(f'Committed: {success}')} {error(f'Failed: {failure}')}"
                )
            else:
                print(error("No commit message provided"))
        elif choice == "5":
            projects = select_projects()
            success, failure = push_projects(projects)
            print(f"\n{success(f'Pushed: {success}')} {error(f'Failed: {failure}')}")
        elif choice == "6":
            print(success("Goodbye!"))
            break
        else:
            print(error("Invalid option"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{warning('Operation cancelled by user')}")
        sys.exit(0)
    except Exception as e:
        print(error(f"Error: {str(e)}"))
        sys.exit(1)
