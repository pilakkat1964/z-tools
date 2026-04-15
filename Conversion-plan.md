# Jekyll Portfolio Conversion Guide (z-tools → Minimal Mistakes)

## 🎯 Objective

Convert the existing GitHub Pages site (`z-tools`) into a structured **portfolio site** using the **Minimal Mistakes** Jekyll theme with:

* Left sidebar navigation
* Support for projects, blog posts, and static pages
* Categories and tags

---

## 🧱 Target Repository Structure

```
z-tools/
├── _config.yml
├── _data/
│   └── navigation.yml
├── _pages/
│   ├── about.md
│   ├── projects.md
│   └── blog.md
├── _projects/
├── _posts/
├── assets/
├── index.md
└── Gemfile
```

---

## ⚙️ Step 1 — Configure Theme

Update `_config.yml`:

```yaml
title: "Santhosh Kumar Pilakkat"
description: "AI / CV / Systems Portfolio"

remote_theme: "mmistakes/minimal-mistakes"

plugins:
  - jekyll-include-cache

collections:
  projects:
    output: true
    permalink: /projects/:path/

defaults:
  - scope:
      path: ""
      type: projects
    values:
      layout: single
```

---

## 🧭 Step 2 — Navigation (Left Sidebar)

Create `_data/navigation.yml`:

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
```

---

## 📄 Step 3 — Create Pages

### `_pages/projects.md`

```yaml
---
title: "Projects"
layout: archive
author_profile: true
sidebar:
  nav: "main"
permalink: /projects/
---
```

---

### `_pages/blog.md`

```yaml
---
title: "Blog"
layout: home
author_profile: true
sidebar:
  nav: "main"
permalink: /blog/
---
```

---

### `_pages/about.md`

```yaml
---
title: "About"
layout: single
author_profile: true
sidebar:
  nav: "main"
permalink: /about/
---
```

---

## 📁 Step 4 — Add Projects Collection

Create `_projects/`

### Example: `_projects/sample-project.md`

```yaml
---
title: "Sample Project"
date: 2026-01-01
layout: single
categories: [AI, Computer Vision]
tags: [Deep Learning, CV]
---

## Overview

Describe the project.

## Problem

Explain the problem.

## Approach

Explain your solution.

## Results

Summarize outcomes.
```

---

## 📰 Step 5 — Add Blog Posts

Create `_posts/`

### Example:

`_posts/2026-04-16-first-post.md`

```yaml
---
title: "First Post"
categories: [Learning]
tags: [Linear Algebra]
---

This is your first blog post.
```

---

## 🏠 Step 6 — Landing Page

Create `index.md`:

```yaml
---
layout: splash
title: "Santhosh Kumar Pilakkat"
excerpt: "AI / Computer Vision / Systems Engineering"
---

## Featured Projects

- AI Portfolio  
- Linear Algebra for Deep Learning  
- Jekyll Automation  

## About

Short introduction goes here.
```

---

## ⚙️ Step 7 — Gemfile (Local Build)

Create `Gemfile`:

```ruby
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
```

---

## 🧪 Step 8 — Run Locally

```bash
bundle install
bundle exec jekyll serve
```

Visit:

```
http://localhost:4000
```

---

## 🌐 Step 9 — GitHub Pages Deployment

1. Go to:

   ```
   Settings → Pages
   ```

2. Configure:

   ```
   Source: Deploy from branch
   Branch: main / root
   ```

---

## 🔄 Step 10 — Replace Current Workflow

### Old:

```
z-open → published output
z-edit → editable version
```

### New:

```
main branch → production
dev branch → development
```

---

## 🎨 Enhancements (Recommended)

* Add project thumbnails in `assets/images/`
* Use categories for grouping:

  * AI
  * Systems
  * DevOps
* Add tags for finer classification
* Customize sidebar with profile info

---

## ⚠️ Common Pitfalls

### Sidebar not appearing

Ensure every page includes:

```yaml
sidebar:
  nav: "main"
```

---

### Projects not showing

Ensure `_config.yml` includes:

```yaml
collections:
  projects:
    output: true
```

---

### Pages not accessible

Ensure `permalink` is set correctly in `_pages/*.md`

---

## 🚀 Outcome

After completing these steps, your site will have:

* Structured portfolio layout
* Left sidebar navigation
* Projects collection
* Blog with categories and tags
* GitHub Pages compatibility

---

## 📌 Next Steps (Optional)

* Add custom homepage sections (hero, featured grid)
* Integrate GitHub repo links per project
* Add CV download page
* Optimize SEO via `_config.yml`

---

**End of Guide**

