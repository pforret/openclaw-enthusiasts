---
date: 2026-02-23
slug: overnight-seo-blog-writer
categories:
  - Use Case
tags:
  - cron
  - exa-search
  - wordpress
  - claude
  - content
  - seo
image: images/splash-overnight-seo-blog-writer.jpg
---

# Overnight SEO Blog Writer

Set up an OpenClaw agent that researches keywords, writes SEO-optimized blog posts, and queues them in your CMS while you sleep -- wake up to fresh content ready for review.

<!-- more -->

![Overnight SEO Blog Writer](../../images/splash-overnight-seo-blog-writer.jpg)

## What it does

As [Mustafa Ergisi shared](https://x.com/mustafaergisi/status/2025795939701584070): *"Woke up. My AI agent had already written 7 blog posts overnight. No alarm for a content team. Just an agent doing SEO while I sleep."*

The agent runs a nightly Clawflow that handles the full SEO content cycle:

- **Keyword research**: identifies low-competition, high-intent keywords in your niche using Exa Web Search
- **Competitor analysis**: scans top-ranking pages for each keyword to understand what's already out there
- **Article drafting**: writes SEO-optimized posts with proper heading structure, internal links, meta descriptions, and target keyword density
- **CMS queuing**: pushes each draft to WordPress (or your CMS) as a pending post, ready for human review
- **Morning summary**: sends you a notification with titles, target keywords, and word counts for everything it wrote

Nothing goes live without your approval.

## Setup overview

1. Install skills: **Exa Web Search** for keyword and competitor research, plus your CMS connector (WordPress, Ghost, Webflow)
2. Write a SOUL.md prompt covering your niche, brand voice, target audience, SEO guidelines (word count range, keyword density, heading structure), and any topics to avoid
3. Prepare a seed list of target keywords or topic clusters -- or let the agent discover them via trend scanning
4. Configure a nightly cron: `0 1 * * * openclaw run seo-blog-writer` (runs at 1 AM)
5. Set up the Clawflow: keyword research -> competitor scan -> outline -> draft -> CMS queue -> notify
6. Connect Slack or Telegram for the morning summary notification

## LLM and tools

Uses **Claude 4.5 Sonnet** for high-quality long-form writing that reads naturally and avoids the generic AI feel. Exa Web Search handles keyword research and competitor page analysis. The cron scheduler manages timing so the heavy LLM work runs during off-hours.

For higher volume (7+ posts per night), consider batching with concurrency limits in your cron config to manage API costs and rate limits.

## Tips

- **Keep the human gate**: review every post before publishing. Even great AI writing needs a human eye for brand accuracy and factual claims
- **Vary your content types**: mix how-to guides, listicles, comparisons, and opinion pieces to look natural to search engines
- **Add your own voice**: use the review step to inject personal anecdotes or unique insights -- this is what separates good AI-assisted content from generic output
- **Track performance**: pair this with a weekly analytics agent to see which AI-drafted posts actually rank and drive traffic, then feed that data back into the SOUL.md

## Source

Based on [@mustafaergisi on X](https://x.com/mustafaergisi/status/2025795939701584070) (Feb 23, 2026)
