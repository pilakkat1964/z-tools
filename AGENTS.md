# AGENTS.md

1. This folder contains multiple subprojects that are part of a set of 
   related utilities.
2. The projects are hosted on github and have their github pages enabled
   and uses Jekyll framework.
3. projects z-edit and z-open has been developed much further with help 
   from various intelligent agents. Each project has an AGENTS.md that
   summarises their state of development and other features for sharing 
   with other agents when developed using multiple of these.
4. We need to synchronize and bring to parity the development of 
   z-kitty-launcher and z-rclone-mount-applete.
5. Note that these projects has different functionalities and some 
   times uses different languages and frameworks for implementation. This 
   shall be be taken into account when synchronizing their development.
6. Though the individual AGENTS.md may provide information about these
   projects, the rest of the artifacts should also be digested as AGENTS.md
   need not be always accurate.
7. Focus on updating development flows, documentation and publishing   
   subprojects for synchronisation first.
8. Strive to provide a modern, unified flow for development, testing, 
   packaging and deployment

---

## Portfolio Status Summary

### ✅ Completed Priorities

**Priority 1-5**: All 5 foundational phases COMPLETE ✅
- Repository Setup: All 4 projects SSH+Git operational
- Build System Unification: ARM64 multiarch, cargo-audit, standardized workflows
- GitHub Pages Deployment: All sites live with Jekyll Slate theme
- PyPI Publishing: z-edit and z-open workflows configured
- Crates.io Publishing: z-kitty-launcher and z-rclone-mount-applete workflows configured

**Priority 6: Enhanced Contribution Guidelines** ✅ COMPLETE (April 16, 2026)

#### What Was Completed
- Created comprehensive `CONTRIBUTING.md` template with language-specific guidance
- Applied standardized CONTRIBUTING.md to all 4 projects with custom sections:
  - **Python Projects**: Development with `uv`, pytest, ruff linting
  - **Rust Projects**: Development with Cargo, clippy, cargo audit
  - Project-specific architecture and testing requirements
  - Release versioning and process documentation
- Updated all project README.md files with prominent "Contributing" sections
- All files pushed to remote repositories

#### Files Created/Modified
- `z-edit/CONTRIBUTING.md` - 275 lines (Python)
- `z-open/CONTRIBUTING.md` - 274 lines (Python)
- `z-kitty-launcher/CONTRIBUTING.md` - 322 lines (Rust)
- `z-rclone-mount-applete/CONTRIBUTING.md` - 381 lines (Rust)
- Updated README.md in all 4 projects with contribution links
- Created `CONTRIBUTING_TEMPLATE.md` in z-tools root for reference

#### Commits Created
- z-edit: 2f91ff6 (CONTRIBUTING.md), 1fced48 (README link)
- z-open: e5f39b8 (CONTRIBUTING.md), 0156b93 (README link)
- z-kitty-launcher: 9ca8548 (CONTRIBUTING.md), dee3613 (README link)
- z-rclone-mount-applete: 60dfd02 (CONTRIBUTING.md), a0d41da (README link)
- **Total: 8 commits across ecosystem**

#### Key Features of CONTRIBUTING.md Files
- Bug reporting guidelines with specific requirements per project
- Feature suggestion template with examples
- Setup instructions (Python venv + uv, Rust + Cargo)
- Development workflow: branching, coding, testing, committing
- Code style guidelines (PEP 8 + type hints for Python, Rust idioms for Rust)
- Testing requirements and coverage expectations
- Documentation contribution guidelines
- Project structure overview
- Building and testing commands
- Understanding the codebase sections
- Release process documentation
- Help and support resources

#### Impact
- Reduces friction for new contributors
- Establishes consistent contribution workflows across projects
- Provides language-appropriate guidance (Python vs Rust)
- Makes contribution process transparent and welcoming
- Aligns with open-source best practices
- Improves code quality through clear standards

### 🔄 In Progress
- None currently

### ⏳ Next Priorities

**Priority 7**: Shared Testing Utilities (Not Started)
- Create cross-project test framework
- Implement integration tests
- Set up performance benchmarking
- Create CI/CD testing matrix

**Priority 8**: Performance Dashboards (Future)
- Track build times across all projects
- Monitor dependency updates
- Display security audit results
- Create GitHub-based metrics dashboard

### Commit Statistics
- **Total commits created**: 18 across ecosystem
- **Projects touched**: 4 (z-edit, z-open, z-kitty-launcher, z-rclone-mount-applete)
- **Lines added**: 1,252 (CONTRIBUTING.md files)
- **Documentation quality**: Professional, comprehensive, consistent
