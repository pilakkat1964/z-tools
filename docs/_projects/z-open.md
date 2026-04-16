---
title: "Z-Open"
date: 2026-01-10
categories: [DevOps, Tools]
tags: [Python, File Navigation, Fuzzy Matching]
github: https://github.com/pilakkat1964/z-open
excerpt: "Intelligent file and URL opener with fuzzy matching and content-aware handling."
---

## Overview

**Z-Open** is a versatile file and URL opener that intelligently routes content to the most appropriate application using fuzzy matching and MIME type detection.

## Links

- **Project Site**: [pilakkat.mywire.org/z-open/](https://pilakkat.mywire.org/z-open/)
- **GitHub**: [pilakkat1964/z-open](https://github.com/pilakkat1964/z-open)
- **Issues**: [Report bugs or request features](https://github.com/pilakkat1964/z-open/issues)
- **Discussions**: [Ask questions](https://github.com/pilakkat1964/z-open/discussions)

## Problem

Opening files typically requires knowing the exact command or application. Users often find themselves typing verbose commands or struggling to remember which tool handles which file type. Z-Open simplifies this by:
- Supporting partial filenames with fuzzy matching
- Automatically detecting file types
- Routing to appropriate applications
- Providing interactive selection when ambiguous

## Solution

A Python application that extends the Z-Edit philosophy with:
- **Fuzzy File Matching** - Find files with partial names
- **Smart Content Detection** - MIME-based routing
- **URL Handling** - Direct browser/mail client integration
- **Interactive Selection** - Choose between multiple options
- **Batch Operations** - Process multiple files efficiently

## Key Features

✅ **Fuzzy Matching** - Find files with partial paths  
✅ **MIME Detection** - Content-based file type recognition  
✅ **URL Support** - Open links in appropriate applications  
✅ **Interactive Mode** - Choose from matching files  
✅ **Dry-Run Mode** - Preview without opening  
✅ **Batch Processing** - Handle multiple files at once  

## Architecture

### File Discovery
- Recursive directory searching with fuzzy matching
- Configurable search depth and patterns
- Caching for improved performance

### Type Detection
- MIME-based routing using file content
- Extension-based fallback
- Customizable application mappings

### Application Routing
- Priority-based handler selection
- Environment variable expansion ($BROWSER, $MAIL, etc.)
- Fallback chains for missing applications

## Use Cases

### Developer Workflow
```bash
z-open readme                 # Finds and opens README.md
z-open config.yaml            # Opens config in YAML editor
z-open *.log                  # Select from matching logs
z-open https://github.com     # Opens in default browser
```

### System Administration
```bash
z-open app.conf --dry-run     # Preview without opening
z-open backup.tar.gz          # Extract or open archive
z-open report.pdf --print     # Route to printer
```

## Technical Stack

- **Language**: Python 3.11+
- **Build System**: CMake, uv
- **CI/CD**: GitHub Actions
- **Distribution**: PyPI, system packages (DEB, RPM)
- **Documentation**: GitHub Pages, Jekyll

## Statistics

- **Lines of Code**: ~1,600 (modular design)
- **Test Coverage**: Comprehensive test suite
- **Dependencies**: Minimal (python-magic optional)
- **Python Version Support**: 3.11, 3.12, 3.13

## Getting Started

```bash
# Installation
pip install z-open
# or
uv pip install z-open

# Basic usage
z-open README.md              # Fuzzy find and open
z-open --list config          # Show matching files
z-open --dry-run *.py         # Preview matches
z-open --init-config          # Create user config
```

## Configuration

Like Z-Edit, Z-Open uses layered TOML configuration:

```toml
[defaults]
interactive = true
prefer_mime = true

[mime_types]
"application/json" = "jq"
"text/plain" = "$EDITOR"
"application/pdf" = "evince"

[urls]
"http*" = "$BROWSER"
"mailto:*" = "thunderbird"
"ssh://*" = "kitty"
```

## Documentation

- [User Guide](https://github.com/pilakkat1964/z-open/blob/main/docs/user-guide.md) - Complete reference
- [Design Document](https://github.com/pilakkat1964/z-open/blob/main/docs/design.md) - Architecture details
- [Examples](https://github.com/pilakkat1964/z-open/blob/main/docs/examples.md) - Real-world usage

---

**Status**: ✅ Production Ready (v0.6.5)  
**License**: MIT  
**Last Updated**: April 2026
