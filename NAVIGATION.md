# Z-Tools Portfolio Site Hierarchy Navigation

> **📚 Shared Documentation**: This navigation scheme is documented at the portfolio level.  
> See `/pilakkat1964-github-io/NAVIGATION.md` for the generic multi-level portfolio navigation guide.  
> This document provides Z-Tools specific implementation details.

## Quick Overview

The Z-Tools portfolio uses the shared multi-level navigation system with:
- **Portfolio Lead (Level 1)**: Z-Tools Portfolio at `/z-tools/`
- **Child Projects (Level 2)**: Z-Edit, Z-Open, Z-Kitty Launcher, Z-RClone Mount Applete

Each project shows an "↑ Up to Z-Tools Portfolio" navigation link, and the portfolio shows a "Navigate the Ecosystem" section with all projects.

## Z-Tools Specific Configuration

### Portfolio Lead Configuration
**File**: `docs/_config.yml`
```yaml
hierarchy_level: 1
hierarchy_parent_url: /
hierarchy_parent_title: "Santhosh Kumar Pilakkat"
```

### Child Projects Configuration
**Files**: `z-edit/docs/_config.yml`, `z-open/docs/_config.yml`, etc.
```yaml
hierarchy_level: 2
hierarchy_parent_url: /z-tools
hierarchy_parent_title: "Z-Tools Portfolio"
```

## Z-Tools Implementation Files

### Navigation Include (Standardized)
- Location: `docs/_includes/hierarchy-nav.html` (all projects)
- Function: Renders "↑ Up to [Parent]" link for Level 2+ sites
- Status: ✅ Implemented and working

### Layout Integration
- **Z-Tools (Portfolio)**: `docs/_includes/page__content.html`
- **Projects**: `docs/_layouts/default.html`

### Homepage Navigation
- **File**: `docs/index.md`
- **Feature**: "Navigate the Ecosystem" section with links to all 4 child projects

## Z-Tools Project Structure

```
Z-Tools Portfolio
├── Z-Edit
│   ├── https://pilakkat.mywire.org/z-edit/
│   └── "↑ Up to Z-Tools Portfolio"
├── Z-Open
│   ├── https://pilakkat.mywire.org/z-open/
│   └── "↑ Up to Z-Tools Portfolio"
├── Z-Kitty Launcher
│   ├── https://pilakkat.mywire.org/z-kitty-launcher/
│   └── "↑ Up to Z-Tools Portfolio"
└── Z-RClone Mount Applete
    ├── https://pilakkat.mywire.org/z-rclone-mount-applete/
    └── "↑ Up to Z-Tools Portfolio"
```

## Implementation Details

### What Works
✅ Backward navigation: All 4 projects show "↑ Up to Z-Tools Portfolio" link  
✅ Forward navigation: Portfolio homepage lists all 4 projects  
✅ Correct URLs: All links point to correct locations  
✅ Styled consistently: Light gray background, blue links  
✅ Automatic on GitHub Pages: No manual rebuilds needed  

### Files Involved

**Z-Tools Portfolio**:
- `docs/index.md` - Ecosystem navigation section
- `docs/_includes/page__content.html` - Navigation include call
- `docs/_config.yml` - Hierarchy metadata

**Each Child Project**:
- `docs/_includes/hierarchy-nav.html` - Navigation include
- `docs/_layouts/default.html` - Include call
- `docs/_config.yml` - Hierarchy metadata

## Adding a New Project to Z-Tools

To add a new project to the Z-Tools portfolio:

1. **Set up documentation** in project's `docs/` folder
2. **Add to `docs/_config.yml`**:
   ```yaml
   hierarchy_level: 2
   hierarchy_parent_url: /z-tools
   hierarchy_parent_title: "Z-Tools Portfolio"
   ```
3. **Copy navigation include**: `docs/_includes/hierarchy-nav.html`
4. **Add include to layout**: `docs/_layouts/default.html`
5. **Update portfolio**: Add project to `z-tools/docs/index.md` "Navigate the Ecosystem" section

## Testing Navigation

```bash
# Verify portfolio shows ecosystem navigation
curl https://pilakkat.mywire.org/z-tools/ | grep -A 5 "Navigate the Ecosystem"

# Verify each project shows parent link
curl https://pilakkat.mywire.org/z-edit/ | grep -A 1 "Up to Z-Tools"
curl https://pilakkat.mywire.org/z-open/ | grep -A 1 "Up to Z-Tools"
curl https://pilakkat.mywire.org/z-kitty-launcher/ | grep -A 1 "Up to Z-Tools"
curl https://pilakkat.mywire.org/z-rclone-mount-applete/ | grep -A 1 "Up to Z-Tools"
```

## Troubleshooting

See the shared navigation guide at `/pilakkat1964-github-io/NAVIGATION.md` for:
- Common issues and solutions
- Maintenance procedures
- Link troubleshooting
- Theme-specific integration

## Implementation History

**Date**: April 17, 2026

**Changes**:
- Fixed `parent_url` → `hierarchy_parent_url` inconsistency
- Removed `relative_url` filter (prevented URL doubling)
- Added hierarchy_level check (prevents portfolio showing nav)
- Added ecosystem navigation section to homepage
- All commits pushed and deployed

**Commits**:
- 28f5818, 7d30fd7, 7534e59 - z-edit fixes
- 8d40f3f, c226636, 3969064 - z-open fixes
- 6af56e8, 1238260, aae7e42 - z-kitty-launcher fixes
- 6f122d5, bf8821d, 4f70beb - z-rclone-mount-applete fixes
- ae03b8d, 7b793af, 79699a8 - z-tools fixes and ecosystem navigation

## See Also

- **Shared Guide**: `../pilakkat1964.github.io/NAVIGATION.md` - Generic multi-level portfolio navigation
- **Z-Tools Portfolio**: https://pilakkat.mywire.org/z-tools/
- **GitHub**: https://github.com/pilakkat1964/z-tools
