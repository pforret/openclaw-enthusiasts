# OpenClaw Enthusiasts

![GitHub](https://img.shields.io/github/license/pforret/openclaw.mkdox)

A blog about **OpenClaw** automation use cases — real-world examples of what people are building with OpenClaw agents.

Live site: **[openclaw.mkdox.com](https://openclaw.mkdox.com)**

## Topics covered

- Calendar management via chat
- Smart home voice control
- Reddit digest bots
- CI/CD monitoring on GitHub
- Notion meal planning
- Stripe revenue reports
- Content research pipelines
- PDF contract parsing
- Invoice monitoring with memory
- Morning briefing agents

## Built with

- [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfundamentals.github.io/mkdocs-material/)
- [pforret/mkdox](https://github.com/pforret/mkdox) template
- Deployed via [Laravel Forge](https://forge.laravel.com/)

## Development

```bash
# serve locally
mkdox serve

# build and deploy
mkdox build
```

## Adding a blog post

1. Create `docs/blog/posts/YYYY-MM-DD-slug-title.md`
2. Add frontmatter (`date`, `categories`, `tags`, `image`)
3. Place the post image in `docs/images/`
4. Use `<!-- more -->` to mark the excerpt break

## Author

[pforret](https://github.com/pforret) — [blog.forret.com](https://blog.forret.com)
