# OpenClaw Terminology

A glossary of the key terms and concepts you'll encounter when working with OpenClaw.

## Architecture

**Gateway**
:   The always-on central server that acts as OpenClaw's control plane. It runs as a single Node.js process (default port `ws://127.0.0.1:18789`) and coordinates everything: routing messages between channels and agents, managing sessions, scheduling cron jobs, and handling configuration. It watches `~/.openclaw/openclaw.json` and hot-reloads changes automatically.

**Node**
:   A companion device app (iOS, Android, macOS) that pairs with the Gateway via WebSocket and exposes device-local capabilities. Nodes let agents access things like camera snapshots, screen content, location, or shell execution on remote hosts.

**Instance**
:   A running deployment of the OpenClaw system. When you run `openclaw gateway`, you start one instance -- a single process handling all WebSocket connections from channel adapters, CLI tools, the web UI, and companion nodes.

## Core Concepts

**Agent**
:   An AI assistant powered by the Agent Core runtime. Each agent has its own workspace, model configuration, tool policies, and authentication profiles. Agents process incoming messages, assemble system prompts, call LLM providers, execute tools, and can escalate to humans when needed. You can run multiple isolated agents on a single instance.

**Skill**
:   A self-contained bundle of prompts and metadata that extends an agent's capabilities. Skills live in the agent's `workspace/skills/` directory and are automatically discovered and injected into system prompts. They're installed from ClawHub. Examples: Google Calendar, Home Assistant, Stripe, PDF 2, Exa Web Search.

**Session**
:   The unit of conversation state. Each session is identified by a unique key encoding the agent ID, channel, chat type, and peer. Sessions maintain message history, model settings, and tool execution state. Transcripts are persisted as JSONL files in `~/.openclaw/agents/<agentId>/sessions/`. Session scoping can be per-channel, per-peer, or per-account.

**Channel**
:   A messaging platform adapter that normalizes platform-specific protocols into a unified message format. Each channel handles authentication and access control policies (pairing, allowlist, open, or disabled). Supported channels: WhatsApp, Telegram, Discord, Slack, Signal, Email, SMS.

**Cron**
:   The scheduled task automation system built into the Gateway. Lets agents execute actions at specified times or intervals using standard cron syntax. Example: `0 7 * * * openclaw run morning-briefing` runs a briefing agent daily at 7 AM. Managed by the CronManager component with settings for max concurrent runs and session retention.

**SOUL.md**
:   The Markdown instruction file that defines an agent's behavior, personality, rules, and decision logic. This is where you tell the agent *what* to do and *how* to do it.

**ClawHub**
:   The marketplace where OpenClaw skills are published, discovered, and installed from.

**ClawFlow**
:   OpenClaw's workflow orchestration system for chaining multiple skills and services into multi-step automations. Also referred to as "Clawflows" (plural).

## How They Fit Together

```
Gateway (port 18789)
├── Routes messages between Channels → Agents
├── Manages Sessions (one per conversation context)
├── Schedules Cron jobs (time-based triggers)
└── Communicates with Nodes (device capabilities)

Agent
├── Loads Skills from workspace
├── Maintains Sessions with conversation history
├── Calls LLM providers (Claude, GPT-4o, Llama)
└── Executes tools (filtered by policy)

Channel → creates Sessions → routed to Agent by Gateway
```

## Triggers

**Trigger**
:   An event that causes an agent to start running. Can be time-based (cron), event-based (webhook), or manual.

**Webhook**
:   An event-based trigger where an external service (GitHub, Stripe, etc.) sends a notification to start an agent.

## Agent Behavior

**Persistent Memory**
:   OpenClaw's architecture that allows agents to retain context across sessions. Agents can remember customer patterns, preferences, invoice history, and more.

**Escalation**
:   When an agent encounters a situation it cannot handle autonomously and alerts a human instead. Escalation logic is defined in the SOUL.md.

**Human-Approval Gate**
:   A required step where a human must approve an agent's output before it gets published or executed.

**Structured Extraction**
:   Parsing unstructured documents (PDFs, contracts, emails) and converting them into organized, actionable data fields.

**Auto-triage**
:   Automatic categorization and prioritization of incoming items (emails, issues, errors) based on rules and content analysis.

**Auto-remediation**
:   Automatic fixing of known issues by agents, such as restarting crashed services or clearing full disks.

## Skills & Integrations

**PDF 2**
:   Skill for intelligent PDF document extraction, including tables and structured data that naive text extraction misses.

**Exa Web Search**
:   Skill for web search and trend discovery, used for news retrieval, competitor monitoring, and content research.

**AgentMail**
:   Skill for sending emails from managed identities on behalf of the user.

**Playwright Scraper**
:   Browser automation skill for scraping JavaScript-heavy websites where simple HTTP requests fail.

**Whisper**
:   OpenAI's speech-to-text model, available as a skill for transcribing voice notes and audio messages.

## LLMs Used

**Claude 4.5 Sonnet**
:   Anthropic's LLM, commonly used as the default "brain" for OpenClaw agents requiring high-quality reasoning and writing.

**GPT-4o**
:   OpenAI's multimodal model, used in some agents for structured extraction and analysis.

**Llama 4**
:   Open-source LLM (run locally via Ollama) for cost-effective agent reasoning without API costs.

## Common Patterns

**Morning Briefing**
:   A daily digest agent that combines weather, calendar, tasks, and news into a single message delivered at a set time.

**Inbox Triage**
:   An agent that categorizes incoming emails by urgency, drafts replies, and auto-archives or unsubscribes from noise.

**Content Pipeline**
:   A multi-stage workflow: monitoring trends → gathering sources → generating outlines → drafting content → queuing for approval.

**Self-Healing Monitor**
:   A server monitoring agent that detects issues (high CPU, full disk, crashed services) and automatically remediates known problems.
