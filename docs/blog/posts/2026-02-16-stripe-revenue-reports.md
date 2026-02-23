---
date: 2026-02-16
categories:
  - Use Case
tags:
  - slack
  - telegram
  - stripe
  - google-analytics
  - cron
  - gpt-4o
  - business
image: images/stripe-revenue.jpg
---

# Daily Revenue Reports from Stripe

Get a formatted revenue summary delivered to Slack or Telegram every morning -- pulling data from Stripe, Google Analytics, and your CRM automatically.

<!-- more -->

![Daily Revenue Reports from Stripe](../../images/stripe-revenue.jpg)

## What it does

A cron-triggered OpenClaw agent fetches your business metrics at a set time and compiles them into a readable daily report:

- **Stripe data**: Revenue, new subscriptions, churned customers, failed payments
- **Google Analytics**: Traffic, top pages, conversion rates
- **CRM data**: New leads, pipeline value, deals closed
- **Trend comparison**: Yesterday vs. 7-day average vs. previous month

The report arrives as a formatted message in your team's Slack channel or your personal Telegram chat.

## Setup overview

1. Install the **Stripe** and **Google Analytics** skills from ClawHub
2. Configure API keys for each service
3. Set up a cron job: `0 8 * * 1-5 openclaw run revenue-report` (weekdays at 8 AM)
4. Write a SOUL.md prompt specifying which metrics matter and how to format them
5. Connect Slack (for team delivery) or Telegram (for personal)

## LLM and tools

Works with **GPT-4o** or **Claude 4.5 Sonnet** for data interpretation and natural-language summaries. The Stripe and Analytics APIs do the heavy data lifting.

## Source

Based on [25 OpenClaw Automation Ideas You Need to Try](https://openclawready.com/blog/openclaw-automation-ideas/) (Feb 15, 2026)
