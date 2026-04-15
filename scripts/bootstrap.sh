#!/bin/bash
#
# Z-Tools Portfolio Bootstrap Script
#
# Downloads and executes the z-tools development environment bootstrap.
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash
#   OR
#   wget -qO- https://raw.githubusercontent.com/pilakkat1964/z-tools/main/scripts/bootstrap.sh | bash
#
# Options can be passed as environment variables:
#   NO_CONFIRM=1 bash bootstrap.sh          # Skip confirmation prompts
#   INSTALL_DIR=~/mytools bash bootstrap.sh # Custom installation directory
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Configuration
GITHUB_REPO="https://github.com/pilakkat1964/z-tools"
DEFAULT_INSTALL_DIR="${HOME}/z-tools"
INSTALL_DIR="${INSTALL_DIR:-$DEFAULT_INSTALL_DIR}"

# Functions
print_header() {
    echo -e "\n${BOLD}${BLUE}==============================================================================${NC}"
    echo -e "${BOLD}${BLUE}${1}${NC}"
    echo -e "${BOLD}${BLUE}==============================================================================${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓${NC} ${1}"
}

print_error() {
    echo -e "${RED}✗${NC} ${1}"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} ${1}"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} ${1}"
}

# Main logic
print_header "Z-Tools Portfolio Bootstrap"

echo -e "${BOLD}This script will:${NC}"
echo "  1. Clone z-tools repository to ${INSTALL_DIR}"
echo "  2. Run the development environment bootstrap"
echo "  3. Setup all 4 projects (z-edit, z-open, z-kitty-launcher, z-rclone-mount-applete)"
echo ""
echo -e "${BOLD}System Information:${NC}"
echo "  OS: $(uname -s)"
echo "  Architecture: $(uname -m)"
echo "  Install Directory: ${INSTALL_DIR}"
echo ""

# Confirm
if [ "${NO_CONFIRM}" != "1" ]; then
    read -p "Continue? (yes/no): " -n 3 -r
    echo
    if [[ ! $REPLY =~ ^[Yy][Ee][Ss]$ ]]; then
        print_warning "Bootstrap cancelled"
        exit 0
    fi
fi

# Check if git is installed
print_info "Checking for git..."
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install git and try again."
    exit 1
fi
print_success "Git found"

# Check if Python 3 is installed
print_info "Checking for Python 3..."
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed. Please install Python 3.8 or higher and try again."
    exit 1
fi
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
print_success "Python 3 found (version ${PYTHON_VERSION})"

# Clone repository if not already present
if [ -d "${INSTALL_DIR}" ]; then
    print_warning "Directory ${INSTALL_DIR} already exists"
    if [ -d "${INSTALL_DIR}/.git" ]; then
        print_info "Git repository found, pulling latest changes..."
        cd "${INSTALL_DIR}"
        git pull origin main 2>/dev/null || git pull origin master 2>/dev/null || true
    else
        print_error "Directory exists but is not a git repository. Please remove it and try again:"
        echo "    rm -rf ${INSTALL_DIR}"
        exit 1
    fi
else
    print_info "Cloning z-tools repository..."
    mkdir -p "$(dirname "${INSTALL_DIR}")"
    git clone "${GITHUB_REPO}.git" "${INSTALL_DIR}"
    print_success "Repository cloned"
fi

# Change to install directory
cd "${INSTALL_DIR}"

# Run the Python bootstrap
print_header "Starting Development Environment Bootstrap"

# Prepare Python arguments
PYTHON_ARGS="--bootstrap"
if [ "${NO_CONFIRM}" = "1" ]; then
    PYTHON_ARGS="${PYTHON_ARGS} --no-confirm"
fi

# Execute bootstrap
if python3 scripts/dev.py ${PYTHON_ARGS}; then
    print_header "Bootstrap Complete!"
    print_success "Your z-tools development environment is ready!"
    echo ""
    echo -e "${BOLD}Next steps:${NC}"
    echo "  1. cd ${INSTALL_DIR}"
    echo "  2. python3 scripts/dev.py --status          (check project status)"
    echo "  3. python3 scripts/dev.py --interactive     (interactive menu)"
    echo ""
    echo -e "${BOLD}For more information:${NC}"
    echo "  - Read: ${INSTALL_DIR}/docs/BOOTSTRAP.md"
    echo "  - Run:  python3 scripts/dev.py --help"
else
    print_error "Bootstrap failed. Please check the errors above and try again."
    exit 1
fi
