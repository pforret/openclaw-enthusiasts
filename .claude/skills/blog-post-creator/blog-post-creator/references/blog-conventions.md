# Blog Post Conventions

## File location and naming

- Posts go in `docs/blog/posts/`
- Filename format: `YYYY-MM-DD-slug-title.md`
- Images go in `docs/images/`
- Splash images: `docs/images/splash-<slug>.jpg`

## Frontmatter (required fields)

```yaml
---
date: YYYY-MM-DD
slug: slug-from-filename
categories:
  - Use Case
tags:
  - tag1
  - tag2
image: images/splash-<slug>.jpg
---
```

### Tag conventions

Use lowercase kebab-case. Common tags:
- Messaging: `whatsapp`, `telegram`, `slack`
- LLMs: `claude`, `gpt-4o`, `llama-4`
- Tools: `playwright`, `cron`, `n8n`, `supabase`
- Services: `stripe`, `notion`, `github`, `google-calendar`, `youtube`, `gmail`
- Domains: `productivity`, `business`, `devops`, `e-commerce`, `finance`, `legal`, `creator`, `smart-home`

## Post structure

```markdown
# Title of the Use Case

One-sentence summary of what the agent does and the value it delivers.

<!-- more -->

![Alt text](../../images/splash-<slug>.jpg)

## What it does

Bullet list of 4-5 capabilities, each with a **bold label** and description.

## Setup overview

Numbered list of 5 steps: install skills, configure services, write SOUL.md, set up cron, connect messaging.

## LLM and tools

One paragraph: which LLM, which tools/APIs, and one security/access consideration.

## Source

Based on [Article Title](URL) (Date)
```

## Style guidelines

- Practical, not promotional
- Each bullet starts with a **bold capability label**
- Include a cron example where applicable: `0 8 * * 1-5 openclaw run <name>`
- Mention security/access considerations in "LLM and tools"
- Keep posts under 50 lines of content
