---
title: "Quick Reference"
layout: single
permalink: /quick-ref/
author_profile: false
sidebar:
  nav: "main"
---

# Portfolio Site Quick Reference

One-page cheat sheet for adding content to your Z-Tools portfolio site.

## File Locations

```
_projects/          → Portfolio showcase items
_posts/             → Blog articles  
_pages/             → Static pages
_data/              → Navigation & config
assets/images/      → Pictures & images
_templates/         → Copy & paste templates
```

## Adding a Project

```bash
# 1. Create file
cp _templates/project-template.md _projects/my-project.md

# 2. Edit file with your content
# 3. Commit and push
git add _projects/my-project.md
git commit -m "feat: add project"
git push origin main
```

**File naming:** `my-project-name.md` (lowercase, hyphens)

**Required fields:**
```yaml
---
title: "Project Name"
date: 2026-04-17
---
```

## Adding a Blog Post

```bash
# 1. Create file with date prefix
cp _templates/blog-post-template.md _posts/2026-04-17-my-post.md

# 2. Edit and save
# 3. Push to GitHub
git add _posts/2026-04-17-my-post.md
git commit -m "docs: add blog post"
git push origin main
```

**File naming:** `YYYY-MM-DD-post-title.md`

**Required fields:**
```yaml
---
title: "Post Title"
date: 2026-04-17
---
```

## Adding a Custom Page

```bash
# 1. Create in _pages/
cp _templates/page-template.md _pages/my-page.md

# 2. Update title and permalink
# 3. Commit and push
git add _pages/my-page.md
git commit -m "docs: add new page"
git push origin main
```

**Set custom URL:**
```yaml
---
title: "Page Name"
permalink: /my-custom-url/
---
```

## Updating Navigation Menu

Edit `_data/navigation.yml`:

```yaml
main:
  - title: "Home"
    url: /
  - title: "My New Page"
    url: /my-custom-url/
```

Then commit:
```bash
git add _data/navigation.yml
git commit -m "docs: update navigation"
git push origin main
```

## Changing Theme

Edit `_config.yml`:

```yaml
minimal_mistakes_skin: "dark"
```

**Available:** `air`, `aqua`, `contrast`, `dark`, `dirt`, `neon`, `plum`, `sunrise`

```bash
git add _config.yml
git commit -m "style: change theme to aqua"
git push origin main
```

## Updating Profile

Edit `_config.yml`:

```yaml
author:
  name: "Your Name"
  avatar: "/assets/images/profile.jpg"
  bio: "Your bio here"
  links:
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/yourusername"
```

## Adding an Image

1. Save image to `assets/images/`
2. Use in content:

```markdown
![Alt text](/assets/images/filename.jpg)
```

Or with sizing:

```html
<img src="/assets/images/filename.jpg" width="400">
```

## Markdown Cheat Sheet

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*
~~Strikethrough~~

- Bullet list
- Item 2
  - Nested item

1. Numbered list
2. Item 2

[Link text](https://example.com)
![Image alt](image.jpg)

> Blockquote text

`inline code`

```code block```

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

## Front Matter Quick Ref

**Projects:**
```yaml
---
title: "Project Name"
date: 2026-04-17
categories: [AI, Web]
tags: [Python, Docker]
github: https://github.com/...
excerpt: "One sentence summary"
---
```

**Blog Posts:**
```yaml
---
title: "Post Title"
date: 2026-04-17
categories: [Learning]
tags: [Python, Tips]
---
```

**Pages:**
```yaml
---
title: "Page Title"
layout: single
permalink: /page-url/
author_profile: true
sidebar:
  nav: "main"
---
```

## Common Git Commands

```bash
# Create a new branch for changes
git checkout -b feature/add-project

# Stage changes
git add .

# Commit with message
git commit -m "feat: add new project"

# Push to GitHub
git push origin feature/add-project

# Or commit directly to main
git push origin main
```

## Testing Locally

```bash
# Install dependencies
bundle install

# Start server
bundle exec jekyll serve

# Visit http://localhost:4000
```

## Troubleshooting

**Posts not showing?**
- Check filename: `YYYY-MM-DD-title.md`
- Check date: not in the future
- Check folder: in `_posts/` not elsewhere

**Images not loading?**
- Use absolute path: `/assets/images/file.jpg`
- Check file exists in `assets/images/`

**Navigation not updating?**
- Wait 1-2 minutes for rebuild
- Hard refresh browser (Ctrl+Shift+R)

**Site not building?**
- Check GitHub Actions tab
- Fix YAML syntax in front matter
- Ensure valid Markdown

## Common Categories

- **AI** - Machine learning, deep learning, NLP
- **Web** - Web dev, frontend, backend
- **Systems** - OS, infrastructure, performance
- **DevOps** - Deployment, CI/CD, containers
- **Tools** - Utilities, libraries, CLI
- **Learning** - Guides, tutorials, how-tos
- **Research** - Academic, papers, experiments

## Category Best Practices

✅ Use **2-3 categories** per item  
✅ Keep list **consistent** across projects  
✅ Review existing categories before adding  
❌ Avoid **too many** categories  
❌ Don't use **single-item** categories  

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Project | `lowercase-with-hyphens.md` | `my-awesome-project.md` |
| Post | `YYYY-MM-DD-lowercase.md` | `2026-04-17-new-features.md` |
| Page | `lowercase-with-hyphens.md` | `skills-and-expertise.md` |
| Image | `descriptive-lowercase.jpg` | `project-demo-screenshot.jpg` |

## When Your Site Updates

1. **Push to GitHub** - `git push origin main`
2. **GitHub Actions triggers** - Automatic
3. **Jekyll builds** - 10-30 seconds
4. **Site deploys** - Instant
5. **Live!** - 1-2 minutes total

Check progress: GitHub → Actions tab

## Links & Resources

- [Portfolio Guide](/guide/) - Full guide
- [Jekyll Docs](https://jekyllrb.com/) - Official docs
- [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) - Theme docs
- [Markdown Guide](https://www.markdownguide.org/) - Markdown reference
- [GitHub Pages Help](https://docs.github.com/en/pages) - GitHub Pages docs

---

**Last updated:** April 2026  
**Questions?** [Start a discussion](https://github.com/pilakkat1964/z-tools/discussions)
