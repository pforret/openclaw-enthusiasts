#!/usr/bin/env bash
# Recreate all splash images from source images using splashmark
set -euo pipefail

WIDTH=1200
HEIGHT=600
EFFECTS="dark,dark,pixel,grain"
IMG_DIR="docs/images"

create_splash() {
  local source="$1" output="$2" title="$3"
  echo ">>> $output"
  splashmark -w "$WIDTH" -c "$HEIGHT" -e "$EFFECTS" -i "$title" file "$source" "$output"
}

create_splash "$IMG_DIR/agent-friendly-file-storage.jpg"  "$IMG_DIR/splash-agent-friendly-file-storage.jpg"  "Agent-Friendly\nFile Storage"
create_splash "$IMG_DIR/ai-video-story-editor.jpg"        "$IMG_DIR/splash-ai-video-story-editor.jpg"        "AI Video Story Editor\n500GB to 16 Films"
create_splash "$IMG_DIR/calendar-management.jpg"          "$IMG_DIR/splash-calendar-management.jpg"          "Calendar Management\nvia Chat"
create_splash "$IMG_DIR/ci-cd-monitor.png"                "$IMG_DIR/splash-ci-cd-monitor.png"                "CI/CD Pipeline Monitor\nwith GitHub"
create_splash "$IMG_DIR/competitor-price-monitor.jpg"     "$IMG_DIR/splash-competitor-price-monitor.jpg"     "Competitor Price\nMonitoring"
create_splash "$IMG_DIR/content-research-pipeline.png"    "$IMG_DIR/splash-content-research-pipeline.png"    "Content Research\n& Publishing Pipeline"
create_splash "$IMG_DIR/email-inbox-triage.jpg"           "$IMG_DIR/splash-email-inbox-triage.jpg"           "Email Inbox Triage\nwith Smart Sorting"
create_splash "$IMG_DIR/invoice-monitor.jpg"              "$IMG_DIR/splash-invoice-monitor.jpg"              "Invoice Monitor\nThat Learns Patterns"
create_splash "$IMG_DIR/morning-briefing.jpg"             "$IMG_DIR/splash-morning-briefing.jpg"             "Automated\nMorning Briefing"
create_splash "$IMG_DIR/notion-meal-planner.jpg"          "$IMG_DIR/splash-notion-meal-planner.jpg"          "Weekly Meal Planner\nwith Notion"
create_splash "$IMG_DIR/overnight-seo-blog-writer.jpg"    "$IMG_DIR/splash-overnight-seo-blog-writer.jpg"    "Overnight SEO\nBlog Writer"
create_splash "$IMG_DIR/pdf-contract-parser.png"          "$IMG_DIR/splash-pdf-contract-parser.png"          "PDF Contract Parser\nwith Renewal Tracking"
create_splash "$IMG_DIR/reddit-digest.png"                "$IMG_DIR/splash-reddit-digest.png"                "Reddit Digest Bot\non Telegram"
create_splash "$IMG_DIR/self-healing-server.jpg"          "$IMG_DIR/splash-self-healing-server.jpg"          "Self-Healing\nServer Monitor"
create_splash "$IMG_DIR/smart-home-control.jpg"           "$IMG_DIR/splash-smart-home-control.jpg"           "Smart Home Control\nvia Messaging"
create_splash "$IMG_DIR/stripe-revenue.jpg"               "$IMG_DIR/splash-stripe-revenue.jpg"               "Daily Revenue Reports\nfrom Stripe"
create_splash "$IMG_DIR/voice-note-journal.png"           "$IMG_DIR/splash-voice-note-journal.jpg"           "Voice Note to Journal\nTranscription"
create_splash "$IMG_DIR/seo-machine-agent-browser.jpg"    "$IMG_DIR/splash-seo-machine-agent-browser.jpg"    "SEO Machine\nwith Agent-Browser"
create_splash "$IMG_DIR/youtube-substack-analytics.png"   "$IMG_DIR/splash-youtube-substack-analytics.jpg"   "YouTube & Substack\nWeekly Analytics"
create_splash "$IMG_DIR/ecommerce-order-monitor.jpg"      "$IMG_DIR/splash-ecommerce-order-monitor.jpg"      "E-Commerce\nOrder Monitor"
create_splash "$IMG_DIR/ironclaw-local-ai-crm.jpg"        "$IMG_DIR/splash-ironclaw-local-ai-crm.jpg"        "IronClaw\nLocal AI CRM"
create_splash "$IMG_DIR/workflow-automation-recipes.jpg"   "$IMG_DIR/splash-workflow-automation-recipes.jpg"   "12 Workflow\nAutomation Recipes"
create_splash "$IMG_DIR/sales-reporting-automation.jpg"    "$IMG_DIR/splash-sales-reporting-automation.jpg"    "AI Sales Reporting\nAutomation"
