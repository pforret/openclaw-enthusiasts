---
date: 2026-02-25
slug: competitor-price-monitor
categories:
  - Use Case
tags:
  - playwright
  - slack
  - telegram
  - cron
  - claude
  - e-commerce
  - business
image: images/splash-competitor-price-monitor.jpg
description: "Track competitor pricing across e-commerce sites with OpenClaw and get instant Slack or Telegram alerts when prices change."
---

# Competitor Price Monitoring

Track competitor pricing across e-commerce sites and get instant alerts when prices change -- so you can adjust your own pricing before customers notice.

<!-- more -->

![Competitor Price Monitoring](../../images/splash-competitor-price-monitor.jpg)

## What it does

The agent scrapes competitor product pages on a schedule and compares prices against your baseline:

- **Tracks specific products** across Amazon, Shopify stores, or any public product page
- **Detects price changes** and calculates percentage differences from your own pricing
- **Sends alerts** via Slack or Telegram when a competitor undercuts you by more than a threshold you define
- **Maintains a price history** so you can spot trends like seasonal discounts or gradual increases
- **Weekly summary report** with all price movements across your tracked products

## Setup overview

1. Install the **Playwright** skill for JavaScript-heavy e-commerce sites
2. Install **Slack** or **Telegram** for alerts
3. Create a product list with competitor URLs and your baseline prices
4. Write a SOUL.md prompt specifying alert thresholds and report format
5. Configure cron: `0 6 * * * openclaw run price-check` (daily at 6 AM)

## LLM and tools

Uses **Claude 4.5 Sonnet** for page interpretation and report generation. Playwright handles the actual scraping -- essential for sites that render prices with JavaScript. Be mindful of scraping frequency; once or twice daily per product is usually sufficient and respectful.

## Source

Based on [25 OpenClaw Automation Ideas You Need to Try](https://openclawready.com/blog/openclaw-automation-ideas/) (Feb 15, 2026)
