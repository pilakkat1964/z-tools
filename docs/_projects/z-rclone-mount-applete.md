---
title: "Z-RClone-Mount-Applete"
date: 2026-01-25
categories: [DevOps, Tools, Storage, GTK4]
tags: [Rust, RClone, System Tray, GTK4, Systemd]
github: https://github.com/pilakkat1964/z-rclone-mount-applete
excerpt: "Complete rclone mount management solution with system tray integration and modern GTK4 GUI, written in Rust."
---

## Overview

**Z-RClone-Mount-Applete** is a complete rclone mount management system providing both lightweight system tray integration and a modern GTK4-based GUI application. Written entirely in Rust, it seamlessly integrates with existing rclone on-demand mounting systems while providing intuitive desktop control and monitoring.

## Links

- **Project Site**: [pilakkat.mywire.org/z-rclone-mount-applete/](https://pilakkat.mywire.org/z-rclone-mount-applete/)
- **GitHub**: [pilakkat1964/z-rclone-mount-applete](https://github.com/pilakkat1964/z-rclone-mount-applete)
- **Issues**: [Report bugs or request features](https://github.com/pilakkat1964/z-rclone-mount-applete/issues)
- **Latest Release**: [GitHub Releases](https://github.com/pilakkat1964/z-rclone-mount-applete/releases)
- **Debian Package**: [AMD64 & ARM64 builds available](https://github.com/pilakkat1964/z-rclone-mount-applete/releases)

## Problem

Developers and power users often manage multiple cloud storage mounts using rclone:
- Google Drive, OneDrive, Dropbox, S3, B2, Box.com and other cloud storage providers
- On-demand mounting via systemd user services for resource efficiency
- Manual status checking requires terminal commands and knowledge of systemd
- No unified interface to control multiple mounts across different cloud providers
- Lack of visual feedback on mount status and quick access to mount controls

Managing mounts becomes tedious without proper integration with desktop environments.

## Solution

A modern Rust-based solution providing:
- **Lightweight System Tray Applet** - Quick status monitoring and one-click controls
- **Modern GTK4 GUI** - Full-featured configuration and management interface
- **Visual Status Indicators** - Color-coded feedback (green/orange/red)
- **Systemd Integration** - Seamless mount/unmount operations
- **Configuration Management** - Easy setup and editing of remote configurations
- **OAuth Support** - Browser-based authentication for cloud services

## Key Features

✅ **System Tray Integration** - Display rclone mount status in the system tray  
✅ **Visual Status Indicators** - Color-coded icons (green/orange/red)  
✅ **One-Click Mount Control** - Mount/unmount directly from tray menu  
✅ **GTK4 GUI Application** - Modern, responsive interface  
✅ **OAuth Authentication** - Browser-based auth with automatic browser launch  
✅ **Systemd User Services** - Seamless integration with systemd  
✅ **Multi-Cloud Support** - Google Drive, OneDrive, Dropbox, S3, B2, Box.com, etc.  
✅ **Auto-Refresh** - Status updates every 5 seconds  
✅ **Minimal Resource Usage** - Written in Rust with minimal dependencies  

## Architecture

### Components

**System Tray Applet** (`rclone-mount-tray`)
- Lightweight status monitoring in system tray
- Quick context menu for mount/unmount operations
- Color-coded status indicator
- Auto-refresh every 5 seconds
- Minimal resource usage (~20-30MB)

**Configuration Manager** (`rclone-config-manager`)
- Modern GTK4-based GUI
- Remote configuration management (add, edit, remove)
- OAuth browser-based authentication flow
- Mount configuration and control
- Visual indicator for systemd service status

### Subsystems

- **Mount Manager** - RClone mount configuration and status checking
- **Systemd Manager** - User service communication and control
- **Tray UI** - System tray display and menu management
- **GTK4 Interface** - Modern GUI components for configuration

## Supported Cloud Services

| Service | Features |
|---------|----------|
| **Google Drive** | OAuth auth, shared drives, folder access |
| **OneDrive** | OAuth auth, Business/Personal, folder access |
| **Dropbox** | OAuth auth, all account types |
| **AWS S3** | AccessKey auth, bucket mounting |
| **Backblaze B2** | AccountID auth, bucket mounting |
| **Box.com** | OAuth auth, folder access |
| And many more... | See rclone documentation |

## Use Cases

### Personal Developer with Cloud Files
```bash
# Configure Google Drive mount
rclone-config-manager

# Add remote: Google Drive (OAuth auth)
# Create mount: ~/gdrive

# System tray shows status
# One-click mount/unmount from tray
```

### Team with Shared Cloud Storage
```bash
# Multiple team members manage shared OneDrive
# Each has personal Dropbox mount
# All statuses visible in one tray

# Systemd services auto-start on login
# Status monitoring without terminal commands
```

### DevOps/Infrastructure Engineer
```bash
# Manage multiple S3 buckets from different AWS accounts
# Monitor backup mounts to B2
# Quick access to archive storage via tray

# No need to remember mount commands
# Visual status prevents accidental operations
```

## Technical Stack

- **Language**: Rust 1.94.1+
- **UI Framework**: GTK4
- **Build System**: Cargo
- **CI/CD**: GitHub Actions
- **Distribution**: Debian packages (AMD64, ARM64), precompiled binaries
- **System Integration**: Systemd, D-Bus
- **Optional Dependencies**: libappindicator3 (for better tray integration)

## System Requirements

- **OS**: Linux (X11 or Wayland)
- **Rust**: 1.94.1+ (for building from source)
- **rclone**: Installed and configured
- **systemd**: User services enabled
- **Desktop Environment**: KDE Plasma, GNOME, XFCE (with tray), or compatible

## Statistics

- **Lines of Code**: ~3,000 (async, modular design)
- **Supported Platforms**: Linux x86_64, ARM64
- **Memory Usage**: ~20-30MB at rest
- **CPU Usage**: <1% idle
- **Startup Time**: <500ms

## Installation

### Debian Package (Recommended)

```bash
# AMD64 Systems
wget https://github.com/pilakkat1964/z-rclone-mount-applete/releases/download/latest/rclone-mount-applete_*_amd64.deb
sudo dpkg -i rclone-mount-applete_*_amd64.deb

# ARM64 Systems (Raspberry Pi, Apple Silicon)
wget https://github.com/pilakkat1964/z-rclone-mount-applete/releases/download/latest/rclone-mount-applete_*_arm64.deb
sudo dpkg -i rclone-mount-applete_*_arm64.deb
```

### From Source

```bash
git clone https://github.com/pilakkat1964/z-rclone-mount-applete
cd z-rclone-mount-applete
cargo build --release
sudo cp target/release/rclone-mount-tray /usr/local/bin/
sudo cp target/release/rclone-config-manager /usr/local/bin/
```

## Getting Started

### Basic Setup

```bash
# 1. Launch the configuration manager
rclone-config-manager

# 2. Add a new remote (e.g., Google Drive)
#    - Click "Add Remote"
#    - Select service (Google Drive)
#    - Browser opens for OAuth authentication
#    - Follow authentication flow

# 3. Create a mount
#    - Mounts tab → Add Mount
#    - Select remote and mount point
#    - Create

# 4. Start the tray applet
rclone-mount-tray

# 5. Auto-start on login (via systemd)
systemctl --user enable rclone-mount-tray.service
systemctl --user start rclone-mount-tray.service
```

### System Tray Usage

```bash
# Check status
~/.local/bin/rclone-mount-tray

# View logs
journalctl --user -u rclone-mount-tray.service -f

# Manual mount/unmount (without tray)
systemctl --user start rclone-gdrive-gdrive_account.service
systemctl --user stop rclone-gdrive-gdrive_account.service
```

## Configuration

### Mount Configuration File

Mounts are configured in:
```
~/.config/rclone-mount-tray/mounts.toml
```

Example:
```toml
[[mounts]]
remote = "gdrive_personal"
mount_point = "/home/user/gdrive"

[[mounts]]
remote = "dropbox_work"
mount_point = "/home/user/dropbox"

[[mounts]]
remote = "s3_backup"
mount_point = "/home/user/s3-backup"
```

### rclone Configuration

Remote configurations stored in:
```
~/.config/rclone/rclone.conf
```

Managed via `rclone-config-manager` GUI with OAuth support.

## Documentation

- [Quick Start Guide](https://github.com/pilakkat1964/z-rclone-mount-applete/blob/main/docs/QUICK_START.md) - 5-minute setup
- [User Guide](https://github.com/pilakkat1964/z-rclone-mount-applete/blob/main/docs/user-guide.md) - Complete reference
- [Configuration Guide](https://github.com/pilakkat1964/z-rclone-mount-applete/blob/main/docs/configuration.md) - Advanced setup
- [CI/CD Pipeline](https://github.com/pilakkat1964/z-rclone-mount-applete/blob/main/docs/CI_CD.md) - Build process
- [Contributing Guide](https://github.com/pilakkat1964/z-rclone-mount-applete/blob/main/CONTRIBUTING.md) - Development workflow

## Security Considerations

- Credentials managed by rclone, not this application
- OAuth tokens stored securely in `~/.config/rclone/rclone.conf`
- Local systemd service communication only
- No network access except to configured rclone mounts

## Troubleshooting

### Applet doesn't appear in system tray

```bash
# Check if running
pgrep -f rclone-mount-tray

# Check logs
journalctl --user -u rclone-mount-tray.service -n 20

# Manual test
rclone-mount-tray
```

### Status doesn't update

```bash
# Verify systemd services
systemctl --user list-units | grep rclone

# Check mount status
/proc/mounts | grep rclone
```

### Mount/Unmount fails

```bash
# Check service status
systemctl --user status rclone-gdrive-personal.service

# View service logs
journalctl --user -u rclone-gdrive-personal.service -f
```

---

**Status**: ✅ Production Ready (v0.2.0)  
**License**: MIT  
**Last Updated**: April 2026
