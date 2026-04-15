# Content Templates

This directory contains ready-to-use templates for creating content on your Z-Tools portfolio site.

## Available Templates

### 1. Project Template (`project-template.md`)

Use this template to showcase your projects, tools, or portfolio items.

**When to use:**
- Software projects you've built
- Portfolio pieces
- Case studies
- Open source contributions
- Research projects

**How to use:**
```bash
cp project-template.md ../_projects/my-project.md
```

Then edit with your project details.

**Key sections:**
- Overview & Problem Statement
- Solution & Architecture
- Key Features
- Technology Stack
- Getting Started
- Links & Resources

**Tips:**
- Include benchmarks or performance metrics
- Add code examples showing usage
- Link to GitHub, documentation, live demo
- Use realistic dates
- Include impact/results metrics

### 2. Blog Post Template (`blog-post-template.md`)

Use this template for articles, announcements, tutorials, and lessons learned.

**When to use:**
- Project releases or updates
- Technical tutorials
- Development insights
- Lessons learned
- Industry commentary
- How-to guides

**How to use:**
```bash
cp blog-post-template.md ../_posts/2026-04-17-my-post.md
```

Note the date prefix `YYYY-MM-DD-` in the filename!

**Key sections:**
- TL;DR (summary)
- Introduction & Hook
- Main Content with Examples
- Results or Takeaways
- Call to Action
- Resources & Links

**Tips:**
- Start with a compelling hook
- Include TL;DR for busy readers
- Use code blocks for technical content
- Add tables for comparisons
- Link to related resources
- End with clear next steps

### 3. Page Template (`page-template.md`)

Use this template for static pages that don't change often.

**When to use:**
- About page
- Skills & expertise
- Contact information
- Services offered
- FAQ
- Custom landing pages
- Resources index

**How to use:**
```bash
cp page-template.md ../_pages/my-page.md
```

Then update the `permalink` to set the URL.

**Key sections:**
- Introduction
- Main content sections
- Key points summary
- Call to action

**Tips:**
- Make navigation clear
- Use table of contents for long pages
- Include relevant links
- Add contact information
- Keep content evergreen (minimal dates)

## Front Matter Explained

All templates use YAML front matter to configure how content appears.

### Projects

```yaml
---
title: "Project Name"                      # Required
date: 2026-04-17                          # Required
categories: [AI, Web]                      # Recommended
tags: [Python, Docker, AWS]                # Recommended
github: https://github.com/user/repo      # Optional
excerpt: "One-sentence description"        # Recommended
---
```

### Blog Posts

```yaml
---
title: "Post Title"                        # Required
date: 2026-04-17                          # Required
categories: [Learning, Release]            # Recommended
tags: [tag1, tag2]                        # Recommended
---
```

### Pages

```yaml
---
title: "Page Title"                        # Required
layout: single                             # Required
permalink: /page-url/                      # Required (no date)
author_profile: true                       # Recommended
sidebar:
  nav: "main"                              # Recommended
toc: true                                  # Optional (table of contents)
toc_sticky: true                           # Optional (sticky TOC)
---
```

## Markdown Formatting

### Common Elements

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*
~~Strikethrough~~

- Bullet list
  - Nested item
  - Another nested

1. Numbered list
2. Second item

> Block quote
> Can span multiple lines

`inline code`

\`\`\`python
# Code block
def hello():
    return "world"
\`\`\`

| Table | Header |
|-------|--------|
| Cell1 | Cell2  |

[Link text](https://example.com)
![Alt text](image.jpg)
```

### Special Markdown

**Collapsible section:**
```html
<details>
<summary>Click to expand</summary>

Hidden content here

</details>
```

**Embedded gist:**
```
{% gist username/gist-id %}
```

**YouTube video:**
```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/xxx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## File Naming Conventions

### Projects
- **Format**: `lowercase-with-hyphens.md`
- **Examples**:
  - `machine-learning-classifier.md`
  - `web-scraping-tool.md`
  - `kubernetes-deployment-guide.md`

### Blog Posts
- **Format**: `YYYY-MM-DD-lowercase-title.md`
- **Examples**:
  - `2026-04-17-release-announcement.md`
  - `2026-04-10-performance-tips.md`
  - `2026-03-25-tutorial-getting-started.md`
- **Date order**: Year → Month → Day

### Pages
- **Format**: `lowercase-with-hyphens.md`
- **Examples**:
  - `skills-and-expertise.md`
  - `my-services.md`
  - `contact-information.md`

### Images
- **Format**: `descriptive-lowercase.jpg`
- **Examples**:
  - `project-architecture-diagram.png`
  - `demo-screenshot-01.jpg`
  - `profile-headshot.jpg`

## Step-by-Step Workflow

### Adding a New Project

1. **Copy template**
   ```bash
   cp _templates/project-template.md _projects/my-project.md
   ```

2. **Edit content**
   - Update title, date, categories, tags
   - Replace placeholder sections with real content
   - Add links and resources
   - Review formatting

3. **Add images** (optional)
   ```bash
   cp /path/to/image.jpg assets/images/project-screenshot.jpg
   ```

4. **Commit and push**
   ```bash
   git add _projects/my-project.md assets/images/
   git commit -m "feat: add project - my project"
   git push origin main
   ```

5. **Verify** (1-2 minutes)
   - Check GitHub Actions
   - Visit yoursite.com/projects/
   - See your project listed!

### Adding a Blog Post

1. **Copy template with date**
   ```bash
   cp _templates/blog-post-template.md _posts/2026-04-17-my-post.md
   ```

2. **Edit content**
   - Update title and date
   - Add your content
   - Include code examples, images, links

3. **Commit and push**
   ```bash
   git add _posts/2026-04-17-my-post.md
   git commit -m "docs: add blog post - my post"
   git push origin main
   ```

4. **Verify**
   - Visit yoursite.com/blog/
   - Latest posts appear at top!

### Adding a Custom Page

1. **Copy template**
   ```bash
   cp _templates/page-template.md _pages/my-page.md
   ```

2. **Update front matter**
   - Set title and custom permalink
   - Example: `permalink: /my-services/`

3. **Edit content**
   - Add sections and information
   - Include calls to action

4. **Update navigation** (optional)
   - Edit `_data/navigation.yml`
   - Add link to new page

5. **Commit and push**
   ```bash
   git add _pages/my-page.md _data/navigation.yml
   git commit -m "docs: add page - my page"
   git push origin main
   ```

## Categories & Tags Best Practices

### Recommended Categories (5-10 total)

- **AI** - Artificial intelligence, ML, NLP, Computer Vision
- **Web** - Web development, frontend, backend, fullstack
- **Systems** - Operating systems, embedded, infrastructure
- **DevOps** - Deployment, CI/CD, containers, orchestration
- **Tools** - Utilities, libraries, CLI tools
- **Learning** - Tutorials, guides, educational content
- **Research** - Academic work, papers, experiments
- **Writing** - Blog, documentation, articles

### Recommended Tags (50+ total)

Choose specific technologies and concepts:
- **Languages**: Python, JavaScript, Rust, Go, Java
- **Frameworks**: Django, FastAPI, React, Vue, Spring
- **Tools**: Docker, Kubernetes, GitHub Actions, AWS, GCP
- **Concepts**: Machine Learning, DevOps, Cloud, Security
- **Skills**: Leadership, Communication, Architecture

### Tag Naming Rules

✅ **DO**:
- Use lowercase: `python` not `Python`
- Use hyphens for multi-word: `machine-learning` not `machine learning`
- Be consistent: `javascript` everywhere, not `JS` or `js`

❌ **DON'T**:
- Create single-use tags
- Use inconsistent capitalization
- Use too many tags (5-8 per item)
- Create overlapping tags

## Examples

### Project with All Sections

See `project-template.md` for a complete example with:
- Architecture diagrams
- Code snippets
- Performance benchmarks
- Resource links
- Status indicator

### Blog Post with Structure

See `blog-post-template.md` for:
- TL;DR summary
- Introduction hook
- Structured content
- Code examples
- Resource links
- Call to action

### Page with Navigation

See `page-template.md` for:
- Clear sections
- Table of contents
- Structured information
- Navigation back

## Troubleshooting Templates

**Content not showing?**
- Check file is in correct folder (`_projects/`, `_posts/`, `_pages/`)
- Check filename format matches convention
- Check YAML syntax in front matter (no typos!)

**Images not loading?**
- Use absolute path: `/assets/images/filename.jpg`
- Verify file exists in `assets/images/`
- Check file extension (jpg, png, gif, webp)

**Post in wrong date order?**
- Check filename date `YYYY-MM-DD` format
- Posts ordered reverse chronologically (newest first)
- Future-dated posts won't appear until that date

**Category/tag not showing?**
- Categories/tags from front matter are auto-created
- No configuration needed
- Just use in front matter

## Getting More Help

- [Full Portfolio Guide](/guide/) - Complete documentation
- [Quick Reference](/quick-ref/) - One-page cheat sheet
- [Jekyll Docs](https://jekyllrb.com/docs/templates/) - Template documentation
- [Minimal Mistakes Theme](https://mmistakes.github.io/minimal-mistakes/docs/) - Theme documentation

---

**Happy creating!** 🎉

Last updated: April 2026
