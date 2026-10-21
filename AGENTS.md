---
framework_version: 1.0.0
---

# Agent Guidelines: AI Job Search

This workspace is structured to manage job search activities, scraper tools, CVs, cover letters, and interview preparation.

## Thin-Pointer Design (Single Source of Truth)

To prevent duplication and configuration drift across different AI agent frameworks (Claude Code, GitHub Copilot CLI, Google Antigravity, Codex, Cursor, Gemini CLI, etc.), this workspace uses a unified thin-pointer design. All agent runtimes should load the canonical specifications and candidate profiles from the files and directories below:

1. **Personal Candidate Profile:**
   - The candidate profile, contact details, education, and target preferences are defined in [CLAUDE.md](CLAUDE.md) and the individual profile methodology files under [.claude/skills/job-application-assistant/](.claude/skills/job-application-assistant/) (specifically `01-*.md` etc.).
2. **Canonical Workflow Specifications:**
   - The step-by-step instructions and triggers for tasks (setup, scrape, rank, apply, upskill, interview) are defined in the [.claude/](.claude/) directory (specifically under `.claude/skills/` and `.claude/commands/`).
   - Do not duplicate these rules or specifications. Treat `.claude/` files as the single source of truth.
3. **Portal Search Skills:**
   - Job-portal search CLIs live under [.agents/skills/](.agents/skills/) in the portable Agent Skills format (with a `SKILL.md` per portal). Copilot CLI, Codex, and Antigravity can discover these skills; the `/scrape` workflow in [.claude/skills/job-scraper/](.claude/skills/job-scraper/) orchestrates them.

## GitHub Copilot CLI

Copilot CLI automatically loads this file and [.github/copilot-instructions.md](.github/copilot-instructions.md). That file is a thin runtime adapter: it maps natural-language requests to the canonical Claude workflow files without copying their instructions. Read the relevant `.claude/commands/*.md` or `.claude/skills/*/SKILL.md` before carrying out a workflow.

Claude-specific files remain the source of truth. In particular, `.claude/settings.json` controls Claude Code permissions only; Copilot CLI uses its own approval prompts and must not treat that file as a Copilot permission configuration.