---
date: 2026-02-14
slug: notion-meal-planner
categories:
  - Use Case
tags:
  - telegram
  - notion
  - cron
  - claude
  - meal-planning
image: images/splash-notion-meal-planner.jpg
---

# Weekly Meal Planner with Notion Integration

OpenClaw generates a full weekly meal plan in Notion, complete with shopping lists sorted by store aisle, weather-aware grilling suggestions, and recipe cataloguing. Saves about an hour per week.

<!-- more -->

![Weekly Meal Planner with Notion](../../images/splash-notion-meal-planner.jpg)

## What it does

Every Sunday evening, the agent builds your week's food plan and populates your Notion workspace:

- **Meal plan for 7 days** with breakfast, lunch, and dinner, respecting dietary preferences
- **Shopping lists sorted by store** (e.g. Kroger vs. Costco) and grouped by aisle
- **Weather integration**: checks the forecast and suggests grilling nights for good weather, soups for cold days
- **Recipe catalogue**: saves new recipes by chef/cuisine, building a searchable database over time
- **Reminders**: morning/evening digests nudge you to defrost meat or grab groceries

## Setup overview

1. Install the **Notion** skill and configure your API token
2. Create a Notion template with pages for Meal Plan, Shopping List, and Recipes
3. Optionally install the **Weather** skill for forecast-aware suggestions
4. Configure a weekly cron job: `0 18 * * 0 openclaw run meal-plan`
5. Connect Telegram for reminders and quick edits ("swap Tuesday dinner to pasta")

## LLM and tools

Uses **Claude 4.5 Sonnet** for creative meal suggestions and structured Notion page generation. The Notion API handles all database operations.

## Source

Based on [10 Wild Things People Actually Built with OpenClaw](https://medium.com/@alexrozdolskiy/10-wild-things-people-actually-built-with-openclaw-e18f487cb3e0) (Feb 2026)
