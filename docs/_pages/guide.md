---
title: "Portfolio Site User Guide"
layout: single
permalink: /guide/
author_profile: false
sidebar:
  nav: "main"
toc: true
toc_sticky: true
---

# Portfolio Site User Guide

Complete guide for maintaining and extending your Z-Tools portfolio site using Jekyll and the Minimal Mistakes theme.

## Table of Contents

- [Quick Start](#quick-start)
- [Site Structure](#site-structure)
- [Configuration](#configuration)
- [Adding Projects](#adding-projects)
- [Writing Blog Posts](#writing-blog-posts)
- [Creating Custom Pages](#creating-custom-pages)
- [Managing Categories & Tags](#managing-categories--tags)
- [Customization](#customization)
- [Local Development](#local-development)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)

---

## Quick Start

### What You Need

- Git repository access
- A text editor (VS Code, Sublime, etc.)
- Basic Markdown knowledge
- Optional: Ruby and Jekyll for local testing

### The Simplest Addition

Add a new blog post in 3 steps:

1. Create a file: `_posts/2026-04-17-my-post.md`
2. Add front matter and content (see examples below)
3. Push to GitHub - the site updates automatically!

---

## Site Structure

Understanding the folder structure helps you know where to add what:

```
z-tools/
├── _config.yml              # Main site configuration
├── index.md                 # Landing page (splash layout)
├── Gemfile                  # Ruby dependencies
│
├── _data/
│   └── navigation.yml       # Left sidebar navigation menu
│
├── _pages/                  # Static pages (About, Projects, etc.)
│   ├── about.md
│   ├── blog.md
│   ├── projects.md
│   └── contribute.md
│
├── _projects/               # Project showcase collection
│   ├── z-edit.md
│   └── z-open.md
│
├── _posts/                  # Blog posts (reverse chronological)
│   └── 2026-04-16-z-tools-v0-6-5-released.md
│
├── assets/                  # Images, CSS, JavaScript
│   └── images/
│       ├── logo.png
│       └── profile.jpg
│
└── .github/workflows/
    └── pages.yml            # GitHub Pages deployment automation
```

### What Each Folder Does

| Folder | Purpose | Add Items | Naming Convention |
|--------|---------|-----------|-------------------|
| `_projects/` | Showcase projects/portfolio items | New `.md` files | `project-name.md` |
| `_posts/` | Blog articles and announcements | New `.md` files | `YYYY-MM-DD-title.md` |
| `_pages/` | Static pages (About, Contact, etc.) | New `.md` files | `page-name.md` |
| `_data/` | Navigation, menus, config data | Edit `navigation.yml` | YAML format |
| `assets/images/` | Project thumbnails, profile pic | Image files | Descriptive names |

---

## Configuration

### Main Site Configuration (`_config.yml`)

The `_config.yml` file controls overall site behavior. Key settings:

```yaml
# Basic Info
title: "Z-Tools Portfolio"
description: "Your tagline here"
name: "Your Name"

# Theme
remote_theme: "mmistakes/minimal-mistakes@4.26.1"
minimal_mistakes_skin: "dark"  # Options: air, aqua, dark, dirt, neon, plum, sunrise

# Author Profile (Sidebar)
author:
  name: "Your Name"
  avatar: "/assets/images/profile.jpg"
  bio: "Your bio text here"
  links:
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/yourusername"

# Pagination
paginate: 10                          # Posts per page
paginate_path: /blog/page:num/

# Collections (Categories for Projects)
collections:
  projects:
    output: true
    permalink: /projects/:name/
```

### Navigation Menu (`_data/navigation.yml`)

Control the left sidebar menu:

```yaml
main:
  - title: "Home"
    url: /
  
  - title: "Projects"
    url: /projects/
  
  - title: "Blog"
    url: /blog/
  
  - title: "About"
    url: /about/
  
  - title: "Contact"
    url: /contact/
```

**Add New Menu Item:**
```yaml
  - title: "Portfolio"
    url: /portfolio/
```

**Add Submenu:**
```yaml
  - title: "Resources"
    url: /resources/
    children:
      - title: "Tutorials"
        url: /resources/tutorials/
      - title: "Templates"
        url: /resources/templates/
```

---

## Adding Projects

### Project Overview

Projects are portfolio items showcasing your work. They appear on `/projects/` and can be filtered by category and tags.

### Create a New Project

**Step 1: Create the file**

Create `_projects/my-awesome-project.md`

**Step 2: Add front matter**

```yaml
---
title: "My Awesome Project"
date: 2026-04-17
categories: [AI, Systems]
tags: [Python, Machine Learning, Open Source]
github: https://github.com/yourusername/project-name
excerpt: "One-sentence description of the project"
---
```

**Step 3: Write the content**

```markdown
## Overview

Describe what this project does and why it matters.

## Problem

What problem does it solve?

## Solution

How did you solve it?

## Key Features

- Feature 1
- Feature 2
- Feature 3

## Technology Stack

- **Language**: Python 3.11+
- **Framework**: Flask
- **Database**: PostgreSQL

## Getting Started

```bash
git clone https://github.com/yourusername/project-name
cd project-name
pip install -r requirements.txt
python main.py
```

## Links

- **GitHub**: [yourname/project](https://github.com/yourusername/project-name)
- **Documentation**: [Read the Docs](https://project-docs.readthedocs.io)
- **Live Demo**: [Example](https://project-demo.com)

---

**Status**: ✅ Active  
**License**: MIT
```

### Complete Project Example

```yaml
---
title: "AI Image Recognition System"
date: 2026-03-15
categories: [AI, Computer Vision]
tags: [Deep Learning, TensorFlow, Python, PyTorch]
github: https://github.com/yourusername/ai-image-recognition
excerpt: "Efficient image recognition system using modern deep learning techniques"
---

## Overview

An end-to-end image recognition system achieving 94% accuracy on ImageNet dataset using EfficientNet architecture.

## Problem

Traditional image recognition systems had high latency and memory requirements, making them unsuitable for edge devices.

## Solution

Implemented EfficientNet with knowledge distillation and quantization:
- 5x faster inference than standard models
- 50% memory reduction through quantization
- Maintained 94% accuracy
- Supports real-time video processing

## Performance Metrics

| Metric | Value |
|--------|-------|
| Accuracy | 94.2% |
| Inference Time | 45ms |
| Model Size | 12MB |
| Supported Devices | GPU, CPU, TPU |

## Architecture Diagram

```
Input Image → Preprocessing → EfficientNet-B4 → Classification Head → Output
                                    ↓
                            Knowledge Distilled
                                    ↓
                            Quantized (INT8)
```

## Getting Started

```bash
# Clone repository
git clone https://github.com/yourusername/ai-image-recognition
cd ai-image-recognition

# Install dependencies
pip install -r requirements.txt

# Download pretrained model
python download_model.py

# Run inference
python infer.py --image path/to/image.jpg
```

## Use Cases

- Real-time surveillance systems
- Medical image diagnosis
- Quality control in manufacturing
- E-commerce product classification

## Technical Stack

- **Language**: Python 3.11
- **Framework**: TensorFlow 2.13 + PyTorch 2.0
- **Deployment**: Docker, Kubernetes
- **Testing**: pytest, TensorFlow Test

## Results

- Published in 3 major ML conferences
- 150+ GitHub stars
- Adopted by 2 companies in production

## Documentation

- **[API Reference](https://github.com/yourusername/ai-image-recognition/wiki/API)**
- **[Training Guide](https://github.com/yourusername/ai-image-recognition/blob/main/TRAINING.md)**
- **[Performance Tuning](https://github.com/yourusername/ai-image-recognition/wiki/Performance)**

## Links

- **GitHub**: [yourusername/ai-image-recognition](https://github.com/yourusername/ai-image-recognition)
- **Paper**: [ArXiv Preprint](https://arxiv.org/abs/2026.xxxxx)
- **Live Demo**: [Web Interface](https://ai-recognition-demo.com)
- **Colab Notebook**: [Try It Now](https://colab.research.google.com/xxx)

---

**Status**: ✅ Production Ready (v2.1.0)  
**License**: MIT  
**Last Updated**: April 2026  
**Contributions**: Welcome! See [Contributing Guide](https://github.com/yourusername/ai-image-recognition/blob/main/CONTRIBUTING.md)
```

### Front Matter Explained

| Field | Purpose | Example |
|-------|---------|---------|
| `title` | Project name | `"My Project"` |
| `date` | Publication date | `2026-04-17` |
| `categories` | High-level grouping | `[AI, DevOps]` |
| `tags` | Detailed keywords | `[Python, Docker]` |
| `github` | GitHub repository link | `https://github.com/...` |
| `excerpt` | One-sentence description | `"Short summary"` |

### Tips for Great Projects

✓ **Lead with impact** - Start with what problem it solves  
✓ **Show metrics** - Include performance numbers, benchmarks  
✓ **Add visuals** - Include diagrams, screenshots, charts  
✓ **Provide examples** - Include code samples and usage  
✓ **Link to resources** - GitHub, documentation, live demos  
✓ **Keep it recent** - Update the date if you revisit the project  

---

## Writing Blog Posts

### Blog Post Overview

Blog posts are time-stamped articles that appear in reverse chronological order on `/blog/`. Perfect for:
- Project announcements
- Development updates
- Tutorials and guides
- Lessons learned
- Industry insights

### Create a New Blog Post

**Step 1: Create the file**

File naming: `_posts/YYYY-MM-DD-post-title.md`

Example: `_posts/2026-04-17-machine-learning-tips.md`

**Step 2: Add front matter**

```yaml
---
title: "5 Machine Learning Tips I Wish I Knew"
date: 2026-04-17
categories: [Learning, AI]
tags: [Machine Learning, Python, Best Practices]
---
```

**Step 3: Write your content**

```markdown
Your article content here...
```

### Complete Blog Post Example

```yaml
---
title: "Z-Edit v0.7.0: Major Performance Improvements"
date: 2026-04-17
categories: [Release, Announcement]
tags: [Version 0.7.0, Performance, Python]
---

## TL;DR

Z-Edit v0.7.0 ships with 40% faster startup time and new fuzzy matching editor selection.

## What's New

### Performance Boost
- Startup time: 230ms → 140ms (40% improvement)
- Configuration parsing optimized with caching
- Lazy loading for optional dependencies

### New Features

#### Fuzzy Editor Selection
Choose editors interactively with fuzzy matching:

```bash
zedit --fuzzy                  # Interactive editor picker
zedit --fuzzy --dry-run        # Preview without opening
```

#### Enhanced MIME Detection
- Added 50 new MIME type mappings
- Improved detection accuracy for obscure formats
- Custom MIME type support via config

### Bug Fixes

- Fixed configuration merge for nested dictionaries
- Resolved symlink handling on different filesystems
- Corrected $EDITOR environment variable resolution

## Benchmark Results

```
Performance Comparison:
┌────────────────────────────────────────┐
│ Metric          │ v0.6.5 │ v0.7.0 │ Δ  │
├────────────────────────────────────────┤
│ Startup Time    │ 230ms  │ 140ms  │ -40% │
│ Config Parse    │ 45ms   │ 18ms   │ -60% │
│ Memory Usage    │ 8.2MB  │ 7.1MB  │ -13% │
│ MIME Detection  │ 12ms   │ 8ms    │ -33% │
└────────────────────────────────────────┘
```

## Upgrading

```bash
# Using pip
pip install --upgrade zedit

# Using uv
uv pip install --upgrade zedit

# Using system package
sudo apt update && sudo apt upgrade zedit
```

## Breaking Changes

⚠️ **Configuration**: Old config format still supported but deprecated. 
[Migration guide](https://github.com/pilakkat1964/z-edit/wiki/Migration-v0.6-to-v0.7)

## Known Limitations

- Fuzzy matching requires Python 3.11+
- libmagic optional dependency recommended for best results
- macOS support still experimental

## Next Steps

We're working on:
- [ ] Real-time configuration reloading
- [ ] Plugin system for custom editors
- [ ] Configuration import from other tools (e.g., neovim init.vim)
- [ ] Cloud-based configuration sync

## Contributing

Found an issue? Have feedback?
- [Report Issues](https://github.com/pilakkat1964/z-edit/issues)
- [Start Discussion](https://github.com/pilakkat1964/z-edit/discussions)
- [Join Development](https://github.com/pilakkat1964/z-edit/blob/main/CONTRIBUTING.md)

## Acknowledgments

Thanks to all contributors and community members who helped test v0.7.0!

---

**Questions?** [See FAQ](https://github.com/pilakkat1964/z-edit/wiki/FAQ)  
**Release Notes**: [Full v0.7.0 Release](https://github.com/pilakkat1964/z-edit/releases/tag/v0.7.0)  
**Next Release**: v0.8.0 (Q3 2026)
```

### Blog Post Front Matter

| Field | Required | Purpose | Example |
|-------|----------|---------|---------|
| `title` | ✅ | Post headline | `"My Post Title"` |
| `date` | ✅ | Publication date | `2026-04-17` |
| `categories` | ❌ | Topic grouping | `[Learning, Tips]` |
| `tags` | ❌ | Searchable keywords | `[Python, AI]` |

### Tips for Great Posts

✓ **Compelling title** - Hook readers immediately  
✓ **TL;DR section** - Summary for busy readers  
✓ **Practical examples** - Code, templates, workflows  
✓ **Clear structure** - Use headings, bullet points  
✓ **Call to action** - Link to GitHub, discussions, resources  
✓ **Publish regularly** - Consistency builds audience  

### Auto-Generated Features

Minimal Mistakes automatically adds to every post:
- **Reading time** - Estimated minutes to read
- **Table of contents** - Jump to sections
- **Related posts** - Suggested reading
- **Share buttons** - Twitter, LinkedIn, Facebook
- **Comments** - Disqus integration (if enabled)

---

## Creating Custom Pages

### Page Overview

Static pages are for content that doesn't change frequently:
- About page
- Contact page
- Portfolio overview
- Services offered
- FAQ
- Documentation index

### Create a Custom Page

**Step 1: Create the file**

Create in `_pages/` folder: `_pages/portfolio-overview.md`

**Step 2: Add front matter**

```yaml
---
title: "My Portfolio"
layout: single
permalink: /portfolio/
author_profile: true
sidebar:
  nav: "main"
---
```

**Step 3: Add content**

```markdown
## My Professional Portfolio

Welcome to my portfolio site...
```

### Common Page Layouts

#### 1. Simple Single Page

```yaml
---
title: "Contact"
layout: single
permalink: /contact/
author_profile: true
sidebar:
  nav: "main"
---

## Get In Touch

Send me an email at hello@example.com
```

#### 2. Archive Page (List of Items)

```yaml
---
title: "All Projects"
layout: archive
permalink: /all-projects/
author_profile: true
sidebar:
  nav: "main"
---

Browse complete project archive.
```

#### 3. Landing Page with Featured Content

```yaml
---
title: "Services"
layout: splash
permalink: /services/
excerpt: "What I offer"
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
---

## Professional Services

Offering consulting, development, and training.
```

### Page Front Matter

| Field | Purpose | Options |
|-------|---------|---------|
| `layout` | Visual template | `single`, `archive`, `splash`, `home` |
| `permalink` | URL path | `/custom-url/` |
| `author_profile` | Show sidebar photo | `true` or `false` |
| `sidebar` | Include navigation | `nav: "main"` |
| `toc` | Table of contents | `true` or `false` |
| `toc_sticky` | Sticky TOC | `true` or `false` |

### Complete Custom Page Example

```yaml
---
title: "Skills & Expertise"
layout: single
permalink: /skills/
author_profile: true
sidebar:
  nav: "main"
toc: true
toc_sticky: true
---

## Technical Skills

### Programming Languages

**Expert Level**
- Python (10+ years)
- JavaScript (8+ years)
- Go (5+ years)

**Proficient**
- Rust (2+ years)
- Java (3+ years)
- C++ (2+ years)

### Frameworks & Tools

- **Web**: Django, Flask, FastAPI
- **Data**: TensorFlow, PyTorch, scikit-learn
- **DevOps**: Docker, Kubernetes, GitHub Actions
- **Cloud**: AWS, GCP, Azure

### Certifications

- AWS Solutions Architect
- Kubernetes Application Developer
- Machine Learning Specialization (Coursera)

## Soft Skills

- Technical leadership
- Cross-functional collaboration
- Public speaking
- Mentoring & coaching

## Languages

- English (Native)
- Spanish (Fluent)
- Mandarin (Intermediate)

```

---

## Managing Categories & Tags

### Understanding Categories vs Tags

**Categories**
- Broad groupings (AI, DevOps, Web, Systems)
- Usually 5-10 categories total
- Appear in project metadata
- Good for site navigation

**Tags**
- Specific keywords (Python, Docker, Linux, AWS)
- Can have many tags (50+)
- Help with search and discovery
- More granular than categories

### Adding Categories

Edit `_config.yml`:

```yaml
# Add more categories in projects collection
collections:
  projects:
    output: true
    permalink: /projects/:name/
```

Then use in projects:

```yaml
---
title: "My Project"
categories: [AI, Web]
---
```

### Adding Tags

Just use in front matter - no configuration needed:

```yaml
---
title: "My Project"
tags: [Python, Docker, AWS, Linux]
---
```

### Common Category Suggestions

- **AI**: Artificial intelligence, machine learning
- **Web**: Web development, frontend, backend
- **Systems**: Operating systems, embedded, drivers
- **DevOps**: Infrastructure, deployment, CI/CD
- **Tools**: CLI tools, utilities, libraries
- **Documentation**: Guides, tutorials, references
- **Research**: Academic work, papers, experiments

### Tag Best Practices

✓ Use **lowercase** and **hyphens** for multi-word tags  
✓ Use **consistent naming** (not both "python" and "Python")  
✓ Keep tags **specific** but not overly granular  
✓ Review existing tags before adding new ones  

---

## Customization

### Changing the Theme Skin

Edit `_config.yml`:

```yaml
minimal_mistakes_skin: "dark"  # Current
```

**Available skins:**
- `air` - Light, minimal
- `aqua` - Blue-tinted
- `contrast` - High contrast
- `dark` - Dark mode (recommended for portfolios)
- `dirt` - Brown, warm tones
- `neon` - Bright, vibrant
- `plum` - Purple theme
- `sunrise` - Orange/yellow

**Try different skins:**

```yaml
minimal_mistakes_skin: "aqua"
```

Then commit and GitHub Pages rebuilds automatically!

### Customizing Author Profile

Edit `_config.yml`:

```yaml
author:
  name: "Your Name"
  avatar: "/assets/images/profile.jpg"
  bio: |
    Your bio text here.
    Can span multiple lines.
  location: "City, Country"
  email: "email@example.com"
  links:
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/yourusername"
     - label: "LinkedIn"
       icon: "fab fa-fw fa-linkedin"
       url: "https://linkedin.com/in/yourprofile"
     - label: "Email"
      icon: "fas fa-fw fa-envelope-square"
      url: "mailto:your.email@example.com"
```

**Available icons:**
- Font Awesome brand icons: `fab fa-fw fa-github`, `fab fa-fw fa-linkedin`, etc.
- Font Awesome solid icons: `fas fa-fw fa-envelope`, `fas fa-fw fa-phone`, etc.

### Adding a Custom Navigation Footer

Edit `_data/navigation.yml`:

```yaml
footer:
  - title: "GitHub"
    url: https://github.com/yourusername
  - title: "LinkedIn"
    url: https://linkedin.com/in/yourprofile
  - title: "Contact"
    url: /contact/
```

### Custom CSS (Advanced)

Create `assets/css/main.scss`:

```scss
---
---

@import "minimal-mistakes/skins/{{ site.minimal_mistakes_skin | default: 'default' }}";
@import "minimal-mistakes";

// Your custom CSS
.custom-heading {
  color: #ff6b6b;
  font-size: 2em;
}
```

---

## Local Development

### Why Test Locally?

- Preview changes before publishing
- Catch formatting issues early
- Test complex layouts
- Build faster than waiting for GitHub Pages

### Setup Local Environment

**Prerequisites:**
- Ruby 2.7+
- Bundler

**Installation:**

```bash
# Navigate to project
cd z-tools

# Install dependencies
bundle install

# Start local server
bundle exec jekyll serve

# Visit http://localhost:4000
```

### Making Changes Locally

```bash
# Terminal 1: Start Jekyll server
bundle exec jekyll serve --livereload

# Terminal 2: Edit files in your editor
# Changes automatically reload in browser!
```

### Common Jekyll Commands

```bash
# Build site
jekyll build

# Serve locally with auto-reload
jekyll serve --livereload

# Clean and rebuild
jekyll clean
jekyll build

# Build with future posts enabled
jekyll build --future

# Build in production mode
JEKYLL_ENV=production jekyll build
```

### Troubleshooting Local Build

**Issue: Port 4000 already in use**
```bash
bundle exec jekyll serve --port 4001
```

**Issue: Cache problems**
```bash
bundle exec jekyll clean
bundle exec jekyll serve
```

**Issue: Dependencies not installed**
```bash
gem update bundler
bundle install --redownload
```

---

## Deployment

### Automatic Deployment (Recommended)

GitHub Pages automatically deploys whenever you push to `main`:

1. **Make changes** in your branch or directly in main
2. **Commit** with a descriptive message
3. **Push** to GitHub
4. **GitHub Actions** automatically builds and deploys
5. **Site updates** in 1-2 minutes

### Manual Push Workflow

```bash
# Make changes
echo "## New section" >> _pages/about.md

# Stage changes
git add _pages/about.md

# Commit with message
git commit -m "docs: add new section to about page"

# Push to GitHub
git push origin main

# Site updates automatically!
```

### Monitoring Deployment

**GitHub Actions Tab:**
1. Go to your repository on GitHub
2. Click "Actions" tab
3. See deployment status in real-time
4. Check logs if build fails

**Check Site Status:**
```bash
# View latest workflow
gh run list --workflow=pages.yml --limit 1

# View logs
gh run view <run-id> --log
```

### Custom Domain (Optional)

To use a custom domain:

1. **GitHub Settings** → Pages → Custom domain
2. **Enter** your domain (e.g., `portfolio.example.com`)
3. **Add DNS records** (CNAME, A, or AAAA records)
4. **Verify** domain and enable HTTPS

---

## Troubleshooting

### Blog Posts Not Showing

**Check:**
- File name follows `YYYY-MM-DD-title.md` format
- File is in `_posts/` folder (not `_post/`)
- Date is not in future (unless using `--future` flag)
- Front matter has correct YAML syntax

**Example correct:**
```
_posts/2026-04-17-my-post.md
```

**Example wrong:**
```
_posts/my-post.md           ❌ Missing date
_posts/04-17-my-post.md     ❌ Wrong date format
_post/2026-04-17-post.md    ❌ Wrong folder name
```

### Projects Not Showing

**Check:**
- File is in `_projects/` folder
- File has `.md` extension
- Front matter includes required fields:
  ```yaml
  ---
  title: "Project Name"
  date: 2026-04-17
  ---
  ```

### Images Not Loading

**Check:**
- Images in `assets/images/` folder
- Reference with correct path: `/assets/images/filename.jpg`
- Image format supported (JPG, PNG, GIF, WebP)

**Example:**
```markdown
![Alt text](/assets/images/my-image.jpg)
```

### Navigation Menu Not Updating

**Solution:**
```bash
# Force rebuild
git add _data/navigation.yml
git commit -m "Update navigation"
git push origin main

# Or trigger rebuild manually
git commit --allow-empty -m "Trigger rebuild"
git push
```

### Site URL Issues

**If `_config.yml` has baseurl:**
```yaml
baseurl: "/z-tools"
url: "https://example.com"
```

**Use in content:**
```markdown
[Link]({{ "/about/" | relative_url }})
```

### Markdown Not Rendering

**Check syntax:**
```markdown
---
title: "Title"
---

# Heading 1

## Heading 2

**Bold text**

*Italic text*

- List item
- Another item

[Link text](https://example.com)
```

### GitHub Pages Not Updating

**Solution steps:**
1. Check GitHub Actions status
2. Review build logs for errors
3. Force rebuild:
   ```bash
   git commit --allow-empty -m "Rebuild"
   git push origin main
   ```
4. Clear browser cache
5. Wait 2-3 minutes for propagation

---

## FAQ

### Q: How often can I publish posts?

**A:** As often as you like! One per day, one per month - whatever works for your audience.

### Q: Can I schedule posts for future dates?

**A:** GitHub Pages builds daily, so posts with future dates won't appear until that date passes.

### Q: How do I edit existing posts?

**A:** Just edit the file and push! GitHub Pages rebuilds automatically.

### Q: Can I have private/draft posts?

**A:** Yes! Prefix with underscore or use a `draft` branch:
- `_posts/2026-05-01-draft-idea.md` (ignored)
- Or keep on separate branch before merging

### Q: How do I add comments to posts?

**A:** Enable Disqus in `_config.yml`:
```yaml
comments:
  provider: "disqus"
  disqus:
    shortname: "your-disqus-shortname"
```

### Q: Can I use more than 3 skins?

**A:** Yes! Create custom CSS in `assets/css/main.scss`

### Q: How do I backup my site?

**A:** Your site is already backed up on GitHub! You can also:
```bash
# Clone as backup
git clone https://github.com/yourusername/z-tools your-backup
```

---

## Next Steps

### Now That You Know the Basics

1. ✅ **Update your bio** in `_config.yml`
2. ✅ **Add your first project** in `_projects/`
3. ✅ **Write a blog post** in `_posts/`
4. ✅ **Customize colors** by changing `minimal_mistakes_skin`
5. ✅ **Add your profile pic** to `assets/images/`

### Ready for Advanced Topics?

- [Jekyll Official Docs](https://jekyllrb.com/docs/)
- [Minimal Mistakes Documentation](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)
- [GitHub Pages Help](https://docs.github.com/en/pages)

### Need Help?

- [GitHub Issues](https://github.com/pilakkat1964/z-tools/issues)
- [GitHub Discussions](https://github.com/pilakkat1964/z-tools/discussions)
- [Jekyll Discourse](https://talk.jekyllrb.com/)

---

**Happy portfolio building!** 🚀

Last updated: April 2026  
Theme version: Minimal Mistakes 4.26.1  
Jekyll version: 4.3.2+
