---
title: "Agents Standardization Guide"
permalink: /portfolio-docs/agents-standardization-guide/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# AGENTS.md Standardization Guide

## Overview

This document provides a unified format and structure for AGENTS.md files across all z-tools projects. While each project is unique, maintaining consistent documentation structure improves navigation for agents working across multiple projects.

---

## Standard AGENTS.md Structure

### 1. Title & Quick Reference (Lines 1-15)
```markdown
# AGENTS.md - [Project Name] Project Status

## Project Overview

**Project**: [Full Project Name - Description]  
**Status**: ✅ **PRODUCTION READY** (v0.x.x) | 🟡 **DEVELOPMENT PHASE** | 🔴 **EXPERIMENTAL**  
**Location**: [Absolute path to project]  
**Language**: [Language(s) used]  
**License**: MIT  
**Repository**: [GitHub URL]  

---
```

**Purpose**: Immediately orient the agent with critical project information

### 2. Current Status Section (Lines 16-40)
Include:
- Current version number
- Build status (clean/warnings/errors)
- Git status (SSH operational or issues)
- Key metrics (LOC, binary size, performance)

```markdown
## Current Status

### Version: X.Y.Z (Latest)
- **Release**: [Brief description of what changed]
- **Build**: ✅ [Status] (warnings/errors count)
- **Git**: ✅ SSH+Git fully operational
- **Debian**: ✅ Package builds successfully

### Quick Facts
- **Source Code**: XXX lines
- **Documentation**: XXX+ lines
- **Binary Size**: ~XXX KB
- **Key Metrics**: [Performance data]
```

### 3. Project Purpose & Architecture (Lines 41-100)
- What does this project do?
- Core components overview
- Module structure
- Key design decisions

### 4. Development Workflow (Lines 101-150)
- Build commands
- Test commands
- Common development tasks
- Code organization tips

### 5. Build & Deployment (Lines 151-250)
- Full build instructions
- Test results
- Packaging information
- Installation methods
- Release process

### 6. Git & SSH Access (Lines 251-300)
For each project, include:
```markdown
## Git & SSH Access

### SSH+Git Status: ✅ FULLY OPERATIONAL
- **Protocol**: [SSH/HTTPS]
- **Key**: [Key path if SSH]
- **Remote**: [Git remote URL]
- **Account**: [GitHub account]
- **Access**: Read ✓ Write ✓ Push ✓ Pull ✓
```

### 7. Documentation Structure (Lines 301-350)
```markdown
## Documentation Structure

| File | Purpose | Lines |
|------|---------|-------|
| README.md | Overview | XXX |
| docs/design.md | Architecture | XXX |
| ... | ... | ... |
```

### 8. Quality Metrics (Lines 351-400)
```markdown
## Quality Metrics

### Code Quality
- ✅ X compiler warnings
- ✅ X compiler errors
- ✅ XXX lines of well-organized code
- ✅ Comprehensive error handling

### Performance
| Metric | Value |
|--------|-------|
| Binary Size | ~XXX KB |
| Startup Time | <XXX ms |
| Memory Usage | XX-XX MB |
```

### 9. Checkpoint for Restart (Lines 401-450)
Provide clear state for resuming work:
```markdown
## Checkpoint for Restart

### Current State
- All features implemented and working
- All code pushed to GitHub
- Clean working directory
- Repository synchronized

### To Resume Later
1. Navigate to: [Path]
2. Verify: `git status`
3. Check version: [Command]
4. Run tests: `cargo test` or `pytest`
5. Build: [Command]
```

### 10. Next Steps & Enhancements (Lines 451-500)
```markdown
## Next Steps for Enhancement

### Immediate (v0.X.0)
- [ ] Feature A
- [ ] Feature B

### Short-term (v0.X.0+)
- [ ] Feature C
- [ ] Enhancement D
```

### 11. Version History (Lines 501-520)
```markdown
## Version History

| Version | Date | Notable Changes |
|---------|------|-----------------|
| **X.Y.Z** | YYYY-MM-DD | Initial/Updates |
```

### 12. Summary & Status (Lines 521-550)
```markdown
## Summary

[Project] is a [type] application providing [core purpose] with:
- ✅ [Key strength 1]
- ✅ [Key strength 2]
- ✅ [Key strength 3]

**Status Summary**: ✅ [Clear status statement]

**Last Updated**: [Date]
```

---

## Key Formatting Standards

### Status Indicators
```
✅ Production Ready / Complete / Working
🟡 Development Phase / In Progress / Partial
🔴 Experimental / Not Working / Blocked
⚠️  Warning / Known Issue / Needs Attention
```

### Code Blocks
```markdown
# For shell commands
\`\`\`bash
command --flag value
\`\`\`

# For code examples
\`\`\`rust
fn example() { }
\`\`\`

# For TOML/config
\`\`\`toml
[section]
key = "value"
\`\`\`
```

### Tables
Use consistent pipe-based tables:
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
```

### Emphasis
- **Bold** for important values: `**0 warnings**`
- `code` for commands/paths: `` `git status` ``
- _Italic_ for optional: `_future enhancement_`

---

## Project-Specific Variations

### Python Projects (z-edit, z-open)

**Additional Sections to Include:**
```markdown
## Build Infrastructure
### Modern Package Manager: uv
### CMake Build System
### GitHub Actions CI/CD
```

**Build Commands Template:**
```bash
# Setup
source setup-env.sh dev
uv venv
source .venv/bin/activate
uv sync

# Build
cmake -B build && cmake --build build

# Test
pytest

# Release
./scripts/dev.py full --version X.Y.Z
```

### Rust Projects (z-kitty-launcher, z-rclone-mount-applete)

**Additional Sections to Include:**
```markdown
## Module Architecture
## Dependencies Justification
## Performance Characteristics
```

**Build Commands Template:**
```bash
# Build
cargo build --release

# Test
cargo test

# Lint
cargo clippy
cargo fmt

# Quality
cargo doc --open
```

---

## Content Guidelines

### What to Include
- ✅ Current build/test status with dates
- ✅ Clear navigation paths for agents
- ✅ All documented features and capabilities
- ✅ Known limitations and workarounds
- ✅ Version history and release notes
- ✅ Git/SSH access status
- ✅ Performance metrics
- ✅ Next development priorities

### What NOT to Include
- ❌ Credentials or secrets (use .gitignore)
- ❌ Personal notes or temporary TODOs
- ❌ Outdated status information (update regularly)
- ❌ Redundant content (reference other docs instead)
- ❌ Incomplete sections (leave out rather than leave blank)

---

## Cross-Project Navigation

### Link Format
For referencing other projects, use:
```markdown
[z-edit](../z-edit/AGENTS.md) - File editor launcher
[z-open](../z-open/AGENTS.md) - File opener
[z-kitty-launcher](../z-kitty-launcher/AGENTS.md) - Terminal sessions
[z-rclone-mount-applete](../z-rclone-mount-applete/AGENTS.md) - Rclone mounts
```

### Project Comparison Table
Keep updated in root AGENTS.md:
```markdown
| Aspect | z-edit | z-open | z-kitty | z-rclone |
|--------|--------|--------|---------|----------|
| Language | Python | Python | Rust | Rust |
| Purpose | Editor launcher | File opener | Session manager | Mount manager |
| Status | v0.1.0 | v0.7.0 | v0.4.0 | v0.1.0 |
```

---

## Maintenance Schedule

### Update Frequency
- **After release**: Immediately update version and features
- **After major development**: Update checkpoint section
- **Monthly**: Review and update status indicators
- **Quarterly**: Full review of content accuracy

### When Updating AGENTS.md
1. Update "Last Updated" timestamp
2. Verify all links are working
3. Confirm version numbers match Cargo.toml/pyproject.toml
4. Test all provided commands
5. Update checkpoint section for next agent

---

## Template for New Projects

When creating AGENTS.md for a new project, use this minimal template:

```markdown
# AGENTS.md - [Project Name] Status

## Project Overview

**Project**: [Name and Description]  
**Status**: [Status indicator]  
**Location**: [Path]  
**Language**: [Language]  
**License**: MIT  
**Repository**: [GitHub URL]  

---

## Current Status

### Version: X.Y.Z
- **Release**: [Description]
- **Build**: [Status]
- **Git**: [Status]

### Quick Facts
- **Source Code**: XXX lines
- **Documentation**: XXX+ lines

---

## Architecture Overview

[Brief description of modules and components]

---

## Development Workflow

[Build and test commands]

---

## Checkpoint for Restart

[Current state and how to resume]

---

## Next Steps

- [ ] Priority 1
- [ ] Priority 2

---

**Status**: [Summary]

**Last Updated**: [Date]
```

---

## Examples by Project Status

### Example 1: Production Ready Project
- Include: Full feature list, release history, multiple versions
- Emphasize: Stability, deployment options, known limitations
- Focus: Maintenance and enhancement

### Example 2: Active Development Project
- Include: Current development focus, blockers, next sprints
- Emphasize: Build status, test results, current tasks
- Focus: Development workflow, testing procedures

### Example 3: Emerging Project
- Include: Core features, learning outcomes, architecture
- Emphasize: Foundation, testing framework, roadmap
- Focus: Continued development, feature priorities

---

## Standardization Checklist

When reviewing AGENTS.md files for standardization:

- [ ] Title includes project name and status
- [ ] Current version clearly stated
- [ ] Build/test status current
- [ ] Git/SSH access status documented
- [ ] Architecture overview present
- [ ] Build commands provided
- [ ] Checkpoint section complete
- [ ] Version history included
- [ ] Links to related projects
- [ ] "Last Updated" date present
- [ ] No dead links
- [ ] Consistent formatting
- [ ] Clear code examples
- [ ] Status indicators consistent
- [ ] Readable by agents unfamiliar with project

---

## Questions for Each Section

Use these questions to ensure completeness:

**Project Overview**
- [ ] What does this project do?
- [ ] What version is currently in use?
- [ ] Is it production-ready?
- [ ] What language is it written in?

**Current Status**
- [ ] Does it build cleanly?
- [ ] Do tests pass?
- [ ] Can you push to git?
- [ ] What's the latest version?

**Development**
- [ ] How do you build it?
- [ ] How do you test it?
- [ ] What are the key modules?
- [ ] Where do you start making changes?

**Deployment**
- [ ] How do you install it?
- [ ] How do you release it?
- [ ] Where are the binaries?
- [ ] What are the dependencies?

**Next Steps**
- [ ] What features are planned?
- [ ] Are there known bugs?
- [ ] What's the priority order?
- [ ] What would improve it most?

---

## Consistency Across Projects

### Common Sections Order
1. Title and Quick Reference
2. Current Status
3. Project Purpose / Overview
4. Architecture / Structure
5. Development Workflow
6. Build & Testing
7. Git & SSH Access
8. Documentation
9. Quality Metrics
10. Deployment
11. Checkpoint for Restart
12. Next Steps / Enhancements
13. Version History
14. Summary & Contact

### Status Badge Pattern
```
✅ Production Ready (v0.4.0)
✅ All tests passing
✅ SSH+Git operational
✅ Debian packaging working
```

### Performance Metrics Template
```markdown
| Metric | Value |
|--------|-------|
| Build Time | ~X seconds |
| Binary Size | ~X KB |
| Memory Usage | X-X MB |
| CPU Usage (Idle) | <X% |
| Startup Time | <X ms |
```

---

## Review Checklist for Standardization

For each AGENTS.md file, verify:

- [ ] Header includes project name, status, location, language
- [ ] Current version matches source code manifest
- [ ] Build/test commands are accurate and tested
- [ ] Git remote and SSH status documented
- [ ] Architecture section explains module organization
- [ ] Checkpoint section provides clear restart path
- [ ] Version history has dates and notable changes
- [ ] Next steps are prioritized and specific
- [ ] All code examples are correct and tested
- [ ] No broken internal links
- [ ] Consistent formatting throughout
- [ ] Last updated date is current

---

## Integration with Root AGENTS.md

The root `/AGENTS.md` should reference this guide and maintain:
- Quick status table for all projects
- Cross-project navigation links
- Synchronization status and gaps
- Development guidelines
- Contribution standards

---

**This guide ensures consistent, high-quality AGENTS.md files across all z-tools projects, making it easier for agents to navigate, understand, and contribute to any project.**

**Last Updated**: April 16, 2026
