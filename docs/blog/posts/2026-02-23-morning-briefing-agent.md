---
date: 2026-02-23
categories:
  - Use Case
tags:
  - whatsapp
  - telegram
  - google-calendar
  - exa-search
  - cron
  - claude
  - productivity
image: images/morning-briefing.jpg
---

# Automated Morning Briefing

A daily 7 AM message combining weather, calendar, priority tasks, and curated news -- delivered to WhatsApp or Telegram before you even get out of bed.

<!-- more -->

![Automated Morning Briefing](../../images/morning-briefing.jpg)

## What it does

The agent assembles a personalized morning digest from multiple sources:

- **Weather forecast** for your location with clothing suggestions
- **Today's calendar** with travel time estimates for first meetings
- **Priority tasks** pulled from your task manager (Todoist, Things 3, or Notion)
- **Curated news** matching your interests via Exa Web Search, summarized in 1-2 lines each
- **Reminders** like birthdays, bill due dates, or package deliveries

Everything arrives as a single formatted message at your preferred time.

## Setup overview

1. Install skills: **Google Calendar**, **Exa Web Search**, and your task manager of choice
2. Optionally install a **Weather** skill
3. Write a SOUL.md prompt describing what goes into your briefing and in what order
4. Configure cron: `0 7 * * * openclaw run morning-briefing`
5. Connect WhatsApp or Telegram as the delivery channel

## LLM and tools

Uses **Claude 4.5 Sonnet** for synthesis and summarization. Exa Web Search provides structured news retrieval. The cron scheduler handles timing.

## Source

Based on [OpenClaw Use Cases: 35+ Real Ways People Are Running Their Lives](https://sidsaladi.substack.com/p/openclaw-use-cases-35-real-ways-people) (Feb 22, 2026) and [Master OpenClaw in 30 Minutes](https://creatoreconomy.so/p/master-openclaw-in-30-minutes-full-tutorial) (Feb 4, 2026)
