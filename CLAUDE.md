# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MkDocs Material site for **OpenClaw Enthusiasts** (`openclaw.mkdox.com`), a blog about OpenClaw automation use cases. Built with the [pforret/mkdox](https://github.com/pforret/mkdox) template. Deployed via Laravel Forge.

## Commands

- **Website:** [https://openclaw.mkdox.com/](https://openclaw.mkdox.com/)
- **Serve locally:** `mkdox serve` (http://localhost:8040/)
- **Build site:** `mkdox build` (output in `site/` and auto git commit + push)

## Architecture

- `mkdocs.yml` — site config (theme, plugins, extensions, analytics)
- `docs/blog/posts/` — blog posts (main content)
- `docs/images/` — post images
- `docs/icon/` — favicons and app icons
- `docs/overrides/` — MkDocs Material theme overrides (custom analytics)
- `articles/` — research/source lists used to develop blog posts

## Blog Post Conventions

- Filename: `YYYY-MM-DD-slug-title.md`
- Frontmatter: `date`, `categories` (always "Use Case"), `tags`, `image`
- Use `<!-- more -->` to mark the excerpt break
- Images referenced as `../../images/filename.jpg` from post files
- Each post covers a concrete OpenClaw automation use case with sections: what it does, how to set it up, configuration/code, tips

## Web Content Fetching

When asked to read, fetch, summarize, or analyze a web article/blog post/URL, always use the Jina Reader API (`https://r.jina.ai/<URL>`) to get clean Markdown content. Use the script at `.claude/skills/jina-reader/scripts/jina_fetch.py` or `curl -s "https://r.jina.ai/<URL>"`.
