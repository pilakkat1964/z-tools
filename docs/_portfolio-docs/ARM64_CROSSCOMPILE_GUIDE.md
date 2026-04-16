---
title: "ARM64 Cross-Compile Guide"
permalink: /portfolio-docs/arm64-cross-compile-guide/
layout: single
author_profile: false
toc: true
toc_sticky: true
---

# ARM64 Cross-Compilation Guide for Python Projects

## Overview

This guide documents how to enable ARM64 (aarch64) cross-compilation for Python projects in the z-tools ecosystem (z-edit and z-open).

## Challenge: Python vs Debian Binary Packages

### Python Wheels (`.whl` files)
- **Status**: ✅ Already platform-agnostic (pure Python)
- **Current packages**: Universal wheels work on any Python 3.x installation
- **ARM64 support**: Automatic (no special steps needed)

### Debian Packages (`.deb` files)
- **Status**: 🟡 Currently only built for amd64
- **Problem**: Uses CMake with `cpack` for DEB generation
- **Limitation**: Debian package format requires binary path declarations

## Solution: Multi-Architecture Debian Packages

### Approach 1: Cross-Compilation (Recommended)
Use QEMU to emulate ARM64 and build native DEB packages.

**Pros:**
- True native DEB packages
- Full architecture support
- Follows Debian standards

**Cons:**
- Slower builds (QEMU emulation)
- More complex GitHub Actions setup
- Requires additional dependencies

### Approach 2: Platform-Agnostic DEB (Simpler)
Build single DEB that works on both amd64 and ARM64.

**Pros:**
- Simple implementation
- Fast builds
- One DEB for both architectures

**Cons:**
- Slightly less optimized paths
- Requires absolute compatibility

## Implementation: Option 1 - Cross-Compilation via QEMU

### Updated `release.yml` for z-edit

Add this new job after `build-debian-amd64`:

```yaml
build-debian-arm64:
  needs: prepare
  runs-on: ubuntu-latest
  outputs:
    deb-package: ${{ steps.build.outputs.deb-package }}
  steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Set up QEMU for ARM64 emulation
      uses: docker/setup-qemu-action@v3
      with:
        platforms: linux/arm64

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Build Debian package (arm64)
      uses: docker/build-push-action@v5
      with:
        context: .
        file: debian/Dockerfile.arm64
        platforms: linux/arm64
        outputs: type=local,dest=./build-arm64
        build-args: |
          DEBIAN_VERSION=${{ needs.prepare.outputs.version }}

    - name: Upload Debian arm64 package as artifact
      uses: actions/upload-artifact@v4
      with:
        name: debian-arm64
        path: build-arm64/zedit-*-arm64.deb
        retention-days: 7
```

### Dockerfile for ARM64 builds

Create `debian/Dockerfile.arm64`:

```dockerfile
FROM arm64v8/debian:bookworm

ARG DEBIAN_VERSION=0.1.0

# Install build dependencies
RUN apt-get update && apt-get install -y \
    cmake \
    python3 \
    python3-dev \
    python3-magic \
    dpkg-dev \
    debhelper \
    dh-python \
    git

WORKDIR /build

# Copy source
COPY . .

# Build
RUN cmake -B build -DCMAKE_INSTALL_PREFIX=/opt/zedit -DZEDIT_BUILD_WHEEL=OFF
RUN cmake --build build --target deb

# Output
RUN mkdir -p /output && \
    cp build/zedit-*.deb /output/ && \
    DEB_FILE=$(ls /output/zedit-*.deb | head -1) && \
    DEB_RENAMED="${DEB_FILE%.*}-arm64.deb" && \
    mv "$DEB_FILE" "$DEB_RENAMED"

FROM scratch
COPY --from=0 /output/* /
```

## Implementation: Option 2 - Platform-Agnostic Single DEB (Simpler)

This is simpler and works just as well for pure Python packages.

### Updated `release.yml` Configuration

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
            --prefix="zedit-${VERSION}-source/" \
            -o "zedit-${VERSION}-source.tar.gz" \
            HEAD
          
          if [ ! -f "zedit-${VERSION}-source.tar.gz" ]; then
            echo "Source archive creation failed"
            exit 1
          fi
          
          echo "source-archive=zedit-${VERSION}-source.tar.gz" >> "$GITHUB_OUTPUT"
          ls -lh zedit-*.tar.gz

      - name: Upload source package as artifact
        uses: actions/upload-artifact@v4
        with:
          name: source-package
          path: zedit-*.tar.gz
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
        run: cmake -B build -DCMAKE_INSTALL_PREFIX=/opt/zedit -DZEDIT_BUILD_WHEEL=OFF

      - name: Build Debian package (multiarch)
        id: build
        env:
          VERSION: ${{ needs.prepare.outputs.version }}
        run: |
          # Set Architecture field to "any" for multi-arch support
          mkdir -p build/DEBIAN
          
          # Build the package
          cmake --build build --target deb
          
          DEB_FILE=$(ls build/zedit-*.deb | head -1)
          if [ -z "$DEB_FILE" ]; then
            echo "Debian package creation failed"
            exit 1
          fi
          
          # Rename to indicate multiarch
          DEB_RENAMED="${DEB_FILE%.*}-multiarch.deb"
          mv "$DEB_FILE" "$DEB_RENAMED"
          
          echo "deb-package=$(basename $DEB_RENAMED)" >> "$GITHUB_OUTPUT"
          ls -lh "$DEB_RENAMED"
          
          dpkg -I "$DEB_RENAMED"

      - name: Upload Debian package as artifact
        uses: actions/upload-artifact@v4
        with:
          name: debian-multiarch
          path: build/zedit-*-multiarch.deb
          retention-days: 7

  create-release:
    needs: [prepare, build-source-package, build-debian-multiarch]
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Download source package
        uses: actions/download-artifact@v4
        with:
          name: source-package
          path: ./release-assets/

      - name: Download Debian package
        uses: actions/download-artifact@v4
        with:
          name: debian-multiarch
          path: ./release-assets/

      - name: Verify release assets
        run: |
          echo "Release assets:"
          ls -lh release-assets/
          echo ""
          echo "Asset count: $(ls release-assets/ | wc -l)"

      - name: Generate checksums
        run: |
          cd release-assets/
          sha256sum * > SHA256SUMS
          cat SHA256SUMS
          cd ..

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          name: "zedit ${{ github.ref_name }}"
          generate_release_notes: true
          draft: false
          prerelease: false
          files: release-assets/*
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Update CMakeLists.txt for Multiarch

```cmake
# In CMakeLists.txt, update the Debian package configuration:

set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "any")  # For pure Python
# OR
set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "amd64")  # amd64 specific
# OR
set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "arm64")  # arm64 specific
```

## Current Recommendation: Option 2 (Multiarch)

For z-edit and z-open (pure Python packages):

**Use Option 2 (Platform-Agnostic DEB)** because:
1. ✅ Simpler implementation
2. ✅ Faster CI/CD builds
3. ✅ Works on both amd64 and ARM64
4. ✅ Follows Python packaging best practices
5. ✅ No QEMU complexity

## Implementation Steps

### Step 1: Update debian/control (both projects)

```
Architecture: any
```

This declares the package as architecture-independent (pure Python).

### Step 2: Update .github/workflows/release.yml

Use the multiarch template provided above.

### Step 3: Update CMakeLists.txt

```cmake
set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "any")
```

### Step 4: Test Build

```bash
cmake -B build -DZEDIT_BUILD_WHEEL=OFF
cmake --build build --target deb
dpkg -I build/zedit-*.deb | grep Architecture
```

Should show: `Architecture: any`

## Verification

After implementation, release builds will:
1. ✅ Create single .deb installable on both amd64 and ARM64
2. ✅ Include Python scripts (architecture-independent)
3. ✅ Work with `dpkg -i` on any Debian-based system

## Testing on ARM64

To verify the package works on ARM64:

```bash
# On an ARM64 system or emulator
sudo dpkg -i zedit-0.x.x-multiarch.deb
zedit --version
```

## Future: True Cross-Architecture (if needed)

If you need separate amd64/ARM64 optimized binaries in the future:

1. Use Dockerfile approach with QEMU
2. Build in separate matrix jobs
3. Upload both `*-amd64.deb` and `*-arm64.deb`
4. Mark each with explicit architecture

## Summary

| Approach | Complexity | Build Time | Support |
|----------|-----------|-----------|---------|
| **Option 1: Cross-compile** | High | Slow | Both amd64 & ARM64 |
| **Option 2: Multiarch** | Low | Fast | Both amd64 & ARM64 |
| **Current (amd64 only)** | None | Fast | amd64 only |

**Recommendation**: Start with Option 2 (Multiarch). If performance optimization per architecture is needed later, migrate to Option 1.

---

## Next: Apply to Both Projects

This solution applies to:
- ✅ z-edit
- ✅ z-open

Both are pure Python, so the same multiarch approach works perfectly.
