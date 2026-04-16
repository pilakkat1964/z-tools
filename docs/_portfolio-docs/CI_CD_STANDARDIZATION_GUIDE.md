---
title: "CI/CD Standardization Guide"
permalink: /portfolio-docs/ci/cd-standardization-guide/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# CI/CD Standardization Guide for z-tools Projects

## Overview

This guide documents unified CI/CD patterns for GitHub Actions workflows across the z-tools ecosystem. The goal is to standardize:

1. **Continuous Integration (CI)** - Testing, linting, security scanning on every commit
2. **Release Automation** - Automated packaging and publishing on version tags
3. **Multi-Architecture Support** - Building for both amd64 and ARM64
4. **Security Scanning** - Integrated security checks in CI/CD pipeline

## Project Matrix

| Project | Type | Package Manager | CI Workflow | Release Workflow | Architecture |
|---------|------|-----------------|-------------|------------------|--------------|
| z-edit | Python | uv + CMake | ci.yml | release.yml | multiarch (any) |
| z-open | Python | uv + CMake | build-and-release.yml | build-and-release.yml | multiarch (any) |
| z-kitty-launcher | Rust | Cargo | ci.yml | release.yml | Pending |
| z-rclone-mount-applete | Rust | Cargo | ci.yml | release.yml | Pending |

## Standard CI Workflow (ci.yml)

### Purpose
Runs on every push and pull request to ensure code quality and compatibility.

### Trigger
```yaml
on:
  push:
    branches:
      - master
      - main
      - develop
  pull_request:
```

### Standard Jobs

#### 1. Test Job (All Projects)

**Python Projects:**
```yaml
test:
  runs-on: ubuntu-latest
  strategy:
    matrix:
      python-version: ["3.11", "3.12", "3.13"]
  steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt

    - name: Run tests
      run: pytest -v --cov=. --cov-report=xml

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        files: ./coverage.xml
```

**Rust Projects:**
```yaml
test:
  runs-on: ubuntu-latest
  strategy:
    matrix:
      rust-version: [stable, beta]
  steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Set up Rust
      uses: dtolnay/rust-toolchain@master
      with:
        toolchain: ${{ matrix.rust-version }}

    - name: Cache Cargo
      uses: Swatinem/rust-cache@v2

    - name: Run tests
      run: cargo test --verbose

    - name: Run doctests
      run: cargo test --doc
```

#### 2. Linting Job

**Python Projects - Ruff:**
```yaml
lint:
  runs-on: ubuntu-latest
  steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"
        cache: 'pip'

    - name: Install ruff
      run: pip install ruff

    - name: Lint with ruff
      run: ruff check .

    - name: Format check with ruff
      run: ruff format . --check
```

**Rust Projects - Clippy:**
```yaml
lint:
  runs-on: ubuntu-latest
  steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Set up Rust
      uses: dtolnay/rust-toolchain@stable
      components: clippy

    - name: Cache Cargo
      uses: Swatinem/rust-cache@v2

    - name: Run Clippy
      run: cargo clippy --all-targets --all-features -- -D warnings

    - name: Check formatting
      run: cargo fmt --all -- --check
```

#### 3. Security Scanning Job

**Python Projects - Bandit:**
```yaml
security:
  runs-on: ubuntu-latest
  steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"

    - name: Install bandit
      run: pip install bandit

    - name: Run security scan
      run: bandit -r . -f json -o bandit-report.json || true

    - name: Check for critical issues
      run: |
        bandit -r . -ll || {
          echo "Security issues found!"
          exit 1
        }
```

**Rust Projects - Cargo-Audit:**
```yaml
security:
  runs-on: ubuntu-latest
  steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Set up Rust
      uses: dtolnay/rust-toolchain@stable

    - name: Install cargo-audit
      run: cargo install cargo-audit

    - name: Run security audit
      run: cargo audit --deny warnings

    - name: Check for vulnerabilities
      continue-on-error: true
      run: cargo audit
```

## Standard Release Workflow

### Purpose
Runs on version tag pushes (e.g., `v1.2.3`) to build and publish release artifacts.

### Trigger
```yaml
on:
  push:
    tags:
      - 'v*'
```

### Python Projects - Standard Release Workflow

**Location:** `.github/workflows/release.yml`

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write

jobs:
  prepare:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.VERSION }}
    steps:
      - name: Extract version from tag
        id: version
        run: echo "VERSION=${GITHUB_REF_NAME#v}" >> "$GITHUB_OUTPUT"
      
      - name: Validate version format
        run: |
          VERSION=${{ steps.version.outputs.VERSION }}
          if [[ ! $VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+ ]]; then
            echo "Invalid version format: $VERSION"
            exit 1
          fi
          echo "Version validated: $VERSION"

  build-source-package:
    needs: prepare
    runs-on: ubuntu-latest
    outputs:
      source-archive: ${{ steps.build.outputs.source-archive }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Build source archive
        id: build
        env:
          VERSION: ${{ needs.prepare.outputs.version }}
        run: |
          git archive --format=tar.gz \
            --prefix="PROJECT-${VERSION}-source/" \
            -o "PROJECT-${VERSION}-source.tar.gz" \
            HEAD
          
          echo "source-archive=PROJECT-${VERSION}-source.tar.gz" >> "$GITHUB_OUTPUT"

      - name: Upload source package as artifact
        uses: actions/upload-artifact@v4
        with:
          name: source-package
          path: PROJECT-*.tar.gz
          retention-days: 7

  build-debian-multiarch:
    needs: prepare
    runs-on: ubuntu-latest
    outputs:
      deb-package: ${{ steps.build.outputs.deb-package }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install build dependencies
        run: |
          sudo apt-get update -q
          sudo apt-get install -y cmake python3-magic dpkg-dev debhelper dh-python

      - name: Configure CMake
        run: cmake -B build -DCMAKE_INSTALL_PREFIX=/opt/PROJECT -DPROJECT_BUILD_WHEEL=OFF

      - name: Build Debian package (multiarch)
        id: build
        env:
          VERSION: ${{ needs.prepare.outputs.version }}
        run: |
          cmake --build build --target deb
          
          DEB_FILE=$(ls build/PROJECT-*.deb | head -1)
          if [ -z "$DEB_FILE" ]; then
            echo "Debian package creation failed"
            exit 1
          fi
          
          # Verify Architecture: any
          ARCH=$(dpkg -I "$DEB_FILE" | grep "Architecture:" | awk '{print $2}')
          if [ "$ARCH" != "any" ]; then
            echo "ERROR: Expected Architecture: any, got $ARCH"
            exit 1
          fi
          
          # Rename to indicate multiarch
          DEB_RENAMED="${DEB_FILE%.*}-multiarch.deb"
          mv "$DEB_FILE" "$DEB_RENAMED"
          
          echo "deb-package=$(basename $DEB_RENAMED)" >> "$GITHUB_OUTPUT"
          dpkg -I "$DEB_RENAMED"

      - name: Upload Debian package as artifact
        uses: actions/upload-artifact@v4
        with:
          name: debian-multiarch
          path: build/PROJECT-*-multiarch.deb
          retention-days: 7

  create-release:
    needs: [prepare, build-source-package, build-debian-multiarch]
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Download all artifacts
        uses: actions/download-artifact@v4
        with:
          path: ./release-assets/

      - name: Verify release assets
        run: |
          echo "Release assets:"
          find release-assets -type f -exec ls -lh {} \;

      - name: Generate checksums
        run: |
          cd release-assets
          find . -type f | sort | xargs sha256sum > SHA256SUMS
          cat SHA256SUMS
          cd ..

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          name: "PROJECT ${{ github.ref_name }}"
          generate_release_notes: true
          draft: false
          prerelease: false
          files: release-assets/**/*
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Rust Projects - Standard Release Workflow

**Location:** `.github/workflows/release.yml`

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write

jobs:
  prepare:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.VERSION }}
    steps:
      - name: Extract version from tag
        id: version
        run: echo "VERSION=${GITHUB_REF_NAME#v}" >> "$GITHUB_OUTPUT"
      
      - name: Validate version format
        run: |
          VERSION=${{ steps.version.outputs.VERSION }}
          if [[ ! $VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+ ]]; then
            echo "Invalid version format: $VERSION"
            exit 1
          fi

  build-source-archive:
    needs: prepare
    runs-on: ubuntu-latest
    outputs:
      source-archive: ${{ steps.build.outputs.source-archive }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Build source archive
        id: build
        env:
          VERSION: ${{ needs.prepare.outputs.version }}
        run: |
          git archive --format=tar.gz \
            --prefix="PROJECT-${VERSION}/" \
            -o "PROJECT-${VERSION}.tar.gz" \
            HEAD
          
          echo "source-archive=PROJECT-${VERSION}.tar.gz" >> "$GITHUB_OUTPUT"

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: source-archive
          path: PROJECT-*.tar.gz
          retention-days: 7

  build-binary-amd64:
    needs: prepare
    runs-on: ubuntu-latest
    outputs:
      binary: ${{ steps.build.outputs.binary }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Rust
        uses: dtolnay/rust-toolchain@stable

      - name: Cache Cargo
        uses: Swatinem/rust-cache@v2

      - name: Build release binary
        env:
          VERSION: ${{ needs.prepare.outputs.version }}
        run: |
          cargo build --release
          BINARY=$(ls target/release/PROJECT | head -1)
          RENAMED="${BINARY}-amd64"
          cp "$BINARY" "$RENAMED"
          echo "binary=$RENAMED" >> "$GITHUB_OUTPUT"

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: binary-amd64
          path: PROJECT-amd64
          retention-days: 7

  create-release:
    needs: [prepare, build-source-archive, build-binary-amd64]
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Download all artifacts
        uses: actions/download-artifact@v4
        with:
          path: ./release-assets/

      - name: Generate checksums
        run: |
          cd release-assets
          find . -type f | sort | xargs sha256sum > SHA256SUMS
          cat SHA256SUMS
          cd ..

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          name: "PROJECT ${{ github.ref_name }}"
          generate_release_notes: true
          draft: false
          prerelease: false
          files: release-assets/**/*
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Multi-Architecture Support

### Strategy for Python Projects

Pure Python projects use **multiarch (Architecture: any)** Debian packages:

1. Set `Architecture: any` in `debian/control`
2. Set `CPACK_DEBIAN_PACKAGE_ARCHITECTURE "any"` in CMakeLists.txt
3. Build once; package works on all architectures
4. No QEMU or cross-compilation needed

**Advantages:**
- Fast builds (single architecture)
- No complexity overhead
- Works on amd64, ARM64, ARM32, etc.
- Industry standard for pure Python packages

### Strategy for Rust Projects

Rust projects use **separate architecture binaries**:

**Approach A: Single-Architecture (Simple)**
- Build for amd64 only initially
- Release includes source tarball + amd64 binary
- Future: Expand to ARM64 when needed

**Approach B: Multi-Architecture Matrix (Advanced)**
```yaml
build:
  strategy:
    matrix:
      include:
        - os: ubuntu-latest
          target: x86_64-unknown-linux-gnu
          suffix: amd64
        - os: ubuntu-latest
          target: aarch64-unknown-linux-gnu
          suffix: arm64
  runs-on: ${{ matrix.os }}
  steps:
    # Standard build steps with matrix.target and matrix.suffix
```

## Security Scanning Integration

### Python Security Scanning

**Tools:**
- `bandit` - Security linter for Python
- `ruff` - Fast Python linter (includes some security checks)
- Optional: `pip-audit` for dependency vulnerabilities

**CI Integration:**
```yaml
security:
  runs-on: ubuntu-latest
  steps:
    - name: Bandit - Security linter
      run: |
        pip install bandit
        bandit -r . --severity-level medium || true

    - name: Pip-audit - Dependency check
      run: |
        pip install pip-audit
        pip-audit --desc || true
```

### Rust Security Scanning

**Tools:**
- `cargo-audit` - Check for known vulnerabilities
- `cargo-deny` - Comprehensive dependency checking
- `clippy` - Linter with security warnings

**CI Integration:**
```yaml
security:
  runs-on: ubuntu-latest
  steps:
    - name: Cargo-audit - Vulnerability check
      run: |
        cargo install cargo-audit
        cargo audit --deny warnings || true

    - name: Cargo-deny - Dependency policy
      run: |
        cargo install cargo-deny
        cargo deny check || true
```

## Job Dependencies and Ordering

### CI Workflow Order
```
┌─────────────────┐
│  Checkout       │
└────────┬────────┘
         │
    ┌────┴────┐
    │          │
┌───▼───┐  ┌──▼────┐  ┌─────────┐
│ Test  │  │ Lint  │  │Security │
└───────┘  └───────┘  └─────────┘
```

All jobs run in parallel (no dependencies).

### Release Workflow Order
```
┌──────────┐
│ prepare  │
└────┬─────┘
     │
  ┌──┴──────────────────┐
  │                     │
┌─▼──────────┐  ┌──────▼──────┐
│build-source│  │build-debian  │
└─┬──────────┘  └──────┬───────┘
  │                    │
  └──────────┬─────────┘
             │
        ┌────▼──────────┐
        │create-release │
        └───────────────┘
```

Sequential: `prepare` → `build-*` (parallel) → `create-release`.

## Testing Workflow Changes

When updating CI/CD workflows:

1. **Test locally** (if possible):
   ```bash
   act -j test  # Run GitHub Actions locally
   ```

2. **Create test branch and workflow file**:
   ```bash
   git checkout -b test/ci-changes
   # Make workflow changes
   git push origin test/ci-changes
   ```

3. **Monitor test run in GitHub Actions**

4. **Merge after verification**

## Migration Path

### For Python Projects (Already Complete)
- ✅ z-edit: Multiarch CI/CD implemented
- ✅ z-open: Multiarch CI/CD implemented

### For Rust Projects (Next Phase)
- ⏳ z-kitty-launcher: Adopt standard Rust CI/CD template
- ⏳ z-rclone-mount-applete: Adopt standard Rust CI/CD template

**Implementation checklist:**
- [ ] Create unified `ci.yml` with test, lint, security jobs
- [ ] Create unified `release.yml` for binary release
- [ ] Add `cargo-audit` to security scanning
- [ ] Test on fresh repository
- [ ] Document in project AGENTS.md

## Configuration Checklist

### Python Projects
- [ ] CI triggers on push and PR
- [ ] Test matrix includes Python 3.11, 3.12, 3.13
- [ ] Ruff linting configured
- [ ] Bandit security scanning enabled
- [ ] Release triggers on `v*` tags
- [ ] Debian package architecture set to `any`
- [ ] Source archive included in release
- [ ] Checksums generated and included

### Rust Projects
- [ ] CI triggers on push and PR
- [ ] Test matrix includes stable and beta
- [ ] Clippy linting enabled with -D warnings
- [ ] Cargo-audit security scanning enabled
- [ ] Release triggers on `v*` tags
- [ ] Source archive created
- [ ] Binary built for target architecture
- [ ] Checksums generated and included

## Troubleshooting

### Workflow Not Triggering
**Problem:** Release workflow doesn't run on tag push
**Solution:** 
- Verify tag format matches `v*` pattern
- Check branch protection rules allow tags
- Ensure workflow file is on `master` branch

### Security Scan Failures
**Problem:** Bandit/cargo-audit finds issues and blocks release
**Solution:**
- Review findings: `bandit -r . -v`
- Fix security issues before release
- For false positives: use tool configuration to skip

### Artifact Download Order
**Problem:** `create-release` can't find artifacts
**Solution:**
- Use `actions/download-artifact@v4` with `path: ./release-assets/`
- Artifact names must match exactly
- Use `find release-assets -type f` to debug

## Future Enhancements

1. **Automated Changelog Generation**
   - Parse conventional commits
   - Generate release notes automatically

2. **Multi-Architecture Rust Builds**
   - Matrix jobs for amd64, ARM64, ARM32
   - Docker-based cross-compilation

3. **Automated Security Updates**
   - Dependabot for Python/Rust deps
   - Automated PR creation for updates

4. **Performance Dashboards**
   - Track CI/CD build times
   - Alert on regressions

5. **Artifact Retention Policies**
   - Automatic cleanup of old artifacts
   - S3-based long-term storage

## References

- GitHub Actions: https://docs.github.com/en/actions
- Bandit: https://bandit.readthedocs.io/
- Clippy: https://doc.rust-lang.org/clippy/
- Cargo-audit: https://rustsec.org/
- Multiarch DEB: https://wiki.debian.org/Multiarch

---

## Summary

This standardization guide provides:

✅ **Unified CI patterns** for all projects  
✅ **Consistent release workflows** across Python and Rust  
✅ **Security scanning integration** in all pipelines  
✅ **Multi-architecture support** (multiarch for Python, matrix for Rust)  
✅ **Troubleshooting guidance** for common issues  
✅ **Clear migration path** for remaining projects  

All patterns follow GitHub Actions best practices and industry standards.
