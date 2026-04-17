# Z-Tools Site Hierarchy Navigation

## Overview

The Z-Tools portfolio consists of 5 interconnected Jekyll-based GitHub Pages sites organized in a two-level hierarchy:

```
Z-Tools Portfolio (Level 1)
├── Z-Edit (Level 2)
├── Z-Open (Level 2)
├── Z-Kitty Launcher (Level 2)
└── Z-RClone Mount Applete (Level 2)
```

Each project has its own dedicated documentation site with automatic navigation between parent and child sites.

## Site Structure

### Level 1: Z-Tools Portfolio
- **URL**: https://pilakkat.mywire.org/z-tools/
- **Theme**: Minimal Mistakes (customized for portfolio)
- **Purpose**: Unified entry point showing all projects
- **Navigation**: Shows "Navigate the Ecosystem" section with links to all child projects

### Level 2: Child Projects (Z-Edit, Z-Open, Z-Kitty Launcher, Z-RClone Mount Applete)
- **URLs**: 
  - https://pilakkat.mywire.org/z-edit/
  - https://pilakkat.mywire.org/z-open/
  - https://pilakkat.mywire.org/z-kitty-launcher/
  - https://pilakkat.mywire.org/z-rclone-mount-applete/
- **Theme**: Jekyll Theme Architect (professional blue styling)
- **Purpose**: Detailed project documentation and guides
- **Navigation**: Shows "Up to Z-Tools Portfolio" link at top of all pages

## Navigation Implementation

### Automatic Hierarchy Navigation

Each site has automatic "Up" navigation implemented via Jekyll includes:

#### Configuration Files
Each project's `docs/_config.yml` defines hierarchy metadata:

```yaml
# Level 1 (Portfolio)
hierarchy_level: 1
hierarchy_parent_url: /
hierarchy_parent_title: "Santhosh Kumar Pilakkat"

# Level 2 (Projects)
hierarchy_level: 2
hierarchy_parent_url: /z-tools
hierarchy_parent_title: "Z-Tools Portfolio"
```

#### Include File
All projects use a standardized `docs/_includes/hierarchy-nav.html`:

```html
{% if site.hierarchy_level and site.hierarchy_level > 1 %}
  <!-- Site Hierarchy Navigation -->
  <div style="background-color: #f5f5f5; border-bottom: 1px solid #ddd; padding: 12px 0; margin-bottom: 20px;">
    {% if site.hierarchy_parent_url %}
      <div style="padding: 0 15px;">
        <a href="{{ site.hierarchy_parent_url }}" style="color: #0366d6; text-decoration: none; font-size: 14px;">
          ↑ Up to {{ site.hierarchy_parent_title }}
        </a>
      </div>
    {% endif %}
  </div>
{% endif %}
```

**Key Features:**
- Only displays for Level 2+ sites (not on portfolio root)
- Uses absolute URLs (no relative_url filter to avoid baseurl doubling)
- Conditional rendering based on hierarchy_level
- Consistent styling across all projects

#### Layout Integration
The include is called from:
- **z-tools**: `docs/_includes/page__content.html` (minimal-mistakes override)
- **z-edit, z-open, z-kitty-launcher, z-rclone-mount-applete**: `docs/_layouts/default.html` (architect theme)

### Forward Navigation

#### Portfolio Homepage
The z-tools portfolio homepage (`docs/index.md`) includes a "Navigate the Ecosystem" section with direct links to all child projects:

```markdown
## Navigate the Ecosystem

Each project has its own dedicated documentation site with detailed guides, API references, and examples. Use the links below to explore:

- **[Z-Edit](https://pilakkat.mywire.org/z-edit/)** - Smart file editor launcher (Python)
- **[Z-Open](https://pilakkat.mywire.org/z-open/)** - Intelligent file opener (Python)
- **[Z-Kitty Launcher](https://pilakkat.mywire.org/z-kitty-launcher/)** - Terminal session manager (Rust)
- **[Z-RClone Mount Applete](https://pilakkat.mywire.org/z-rclone-mount-applete/)** - System tray manager for rclone (Rust)
```

#### Project Homepages
Each child project's documentation index includes cross-links to other projects for discovery.

## Maintenance Guide

### Adding a New Level 2 Project

To add a new project to the z-tools hierarchy:

1. **Create Jekyll documentation** in the project's `docs/` folder
2. **Add hierarchy metadata** to `docs/_config.yml`:
   ```yaml
   hierarchy_level: 2
   hierarchy_parent_url: /z-tools
   hierarchy_parent_title: "Z-Tools Portfolio"
   ```
3. **Add hierarchy include** to `docs/_layouts/default.html` or similar:
   ```html
   {% include hierarchy-nav.html %}
   ```
4. **Copy the include file** to `docs/_includes/hierarchy-nav.html` (or create it with the standardized content)
5. **Update z-tools portfolio** to include the new project in:
   - Homepage "Navigate the Ecosystem" section
   - Project feature rows (if using feature_row layout)

### Updating Navigation Links

If a project's base URL changes:

1. **Update `docs/_config.yml`** in the child project:
   ```yaml
   baseurl: /new-path
   hierarchy_parent_url: /z-tools  # Parent URL usually stays the same
   ```
2. **If portfolio root changes**, update `hierarchy_parent_url` in ALL child projects
3. **Update z-tools homepage** to reflect any new URLs

### Testing Navigation

1. **Build locally**:
   ```bash
   cd docs && jekyll serve
   ```
2. **Verify links** - Navigate up and down the hierarchy
3. **Test in production** after deploying to GitHub Pages

### Common Issues

**Issue**: Navigation not showing on child sites
- **Cause**: `hierarchy_level` not set to 2 in `_config.yml`
- **Fix**: Add `hierarchy_level: 2` to `_config.yml`

**Issue**: "Up" links point to wrong location
- **Cause**: `hierarchy_parent_url` is incorrect or has extra paths
- **Fix**: Use absolute paths starting with `/`: `/z-tools`, not `/z-tools/`

**Issue**: Navigation showing on portfolio site
- **Cause**: The include check `site.hierarchy_level > 1` is being ignored
- **Fix**: Ensure `hierarchy_level: 1` is set in portfolio `_config.yml`

**Issue**: Broken links after theme update
- **Cause**: `relative_url` filter being reapplied to navigation links
- **Fix**: Remove `| relative_url` filter from hierarchy-nav.html - use raw URLs

## Files Involved

### Z-Tools Portfolio
- `docs/index.md` - Homepage with ecosystem navigation section
- `docs/_includes/page__content.html` - Includes hierarchy navigation (minimal-mistakes override)
- `docs/_config.yml` - Site hierarchy metadata (level 1)

### Each Child Project (Z-Edit, Z-Open, Z-Kitty Launcher, Z-RClone Mount Applete)
- `docs/_includes/hierarchy-nav.html` - Standardized navigation include
- `docs/_layouts/default.html` - Includes hierarchy navigation in page layout
- `docs/_config.yml` - Site hierarchy metadata (level 2)

## Navigation Flow Diagram

```
┌─────────────────────────────────────────────┐
│    Z-Tools Portfolio Homepage               │
│  https://pilakkat.mywire.org/z-tools/      │
│                                             │
│  Navigate the Ecosystem                     │
│  [Z-Edit] [Z-Open] [Kitty] [RClone]        │
└──────────┬──────────────────────────────────┘
           │
           ├─────────────┬────────────┬──────────────┐
           │             │            │              │
           ▼             ▼            ▼              ▼
        ┌──────┐  ┌──────────┐  ┌──────────────┐  ┌─────────────┐
        │Z-Edit│  │  Z-Open  │  │ Z-Kitty Lnch │  │ Z-RClone    │
        │ Page │  │   Page   │  │   Page       │  │ Mount Page  │
        │      │  │          │  │              │  │             │
        │ ↑    │  │  ↑       │  │   ↑          │  │  ↑          │
        │ Up   │  │  Up      │  │   Up         │  │  Up         │
        │ to   │  │  to      │  │   to         │  │  to         │
        │ Z-   │  │  Z-      │  │   Z-Tools    │  │  Z-Tools    │
        │Tools │  │  Tools   │  │   Portfolio  │  │  Portfolio  │
        └──────┘  └──────────┘  └──────────────┘  └─────────────┘
```

## GitHub Pages Deployment

All sites are deployed on GitHub Pages with automatic rebuilds on every push:

- **Build Trigger**: Push to master/main branch in `/docs` folder
- **Build Time**: ~1-2 minutes per site
- **HTTPS**: Enabled with valid certificates
- **Automatic**: No manual rebuild needed

### Repository URLs
- **Z-Tools**: https://github.com/pilakkat1964/z-tools
- **Z-Edit**: https://github.com/pilakkat1964/z-edit
- **Z-Open**: https://github.com/pilakkat1964/z-open
- **Z-Kitty Launcher**: https://github.com/pilakkat1964/z-kitty-launcher
- **Z-RClone Mount Applete**: https://github.com/pilakkat1964/z-rclone-mount-applete

## User Experience

### From Z-Tools Portfolio
Users can:
1. See all projects at https://pilakkat.mywire.org/z-tools/
2. Click on any project to go to its dedicated site
3. Each project site links back to the portfolio

### From Child Project
Users can:
1. Read detailed project documentation
2. Click "↑ Up to Z-Tools Portfolio" at the top to return to main site
3. See cross-project links for related tools

## History

**Implementation Date**: April 17, 2026

**Components**:
- Fixed field name inconsistency: `parent_url` → `hierarchy_parent_url` (all 5 sites)
- Removed `relative_url` filter from navigation links (prevented URL doubling)
- Added hierarchy_level check to prevent displaying navigation on portfolio root
- Added "Navigate the Ecosystem" section to z-tools homepage
- Created this documentation guide

**Commits**:
- z-edit: 28f5818, 7d30fd7, 7534e59
- z-open: 8d40f3f, c226636, 3969064
- z-kitty-launcher: 6af56e8, 1238260, aae7e42
- z-rclone-mount-applete: 6f122d5, bf8821d, 4f70beb
- z-tools: ae03b8d, 7b793af, 79699a8
