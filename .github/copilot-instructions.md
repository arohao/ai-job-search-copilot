# GitHub Copilot CLI instructions

This repository is an AI job-search workspace. Its canonical candidate profile and
workflow specifications live in [CLAUDE.md](../CLAUDE.md), [.claude/skills/](../.claude/skills/),
and [.claude/commands/](../.claude/commands/). Do not copy those specifications into
this file or create a second source of truth.

## Before acting

1. Read [AGENTS.md](../AGENTS.md).
2. Read [CLAUDE.md](../CLAUDE.md) and the relevant profile files under
   `.claude/skills/job-application-assistant/`.
3. For a workflow request, read its matching command file under `.claude/commands/`
   and follow it in order. For example:
   - setup or onboarding -> `.claude/commands/setup.md`
   - finding jobs -> `.claude/skills/job-scraper/SKILL.md`
   - ranking jobs -> `.claude/commands/rank.md`
   - applying -> `.claude/commands/apply.md` and
     `.claude/skills/job-application-assistant/SKILL.md`
   - interview preparation -> `.claude/commands/interview.md`
   - skill-gap planning -> `.claude/skills/upskill/SKILL.md`
4. Preserve the workflow's confirmation gates, trust boundaries, factual-accuracy
   rules, and profile update requirements. Do not guess missing personal facts.

## Runtime mapping

Claude Code's `/command` and `Skill(...)` syntax is not a Copilot CLI command.
Interpret requests such as “run setup”, “scrape jobs”, or “apply to this posting”
as natural-language requests, then load and execute the corresponding canonical
file above. The portable portal skills under `.agents/skills/*/SKILL.md` are
available to Copilot CLI; use each portal's documented CLI rather than inventing
flags.

Use normal Copilot CLI tool approvals. Do not interpret `.claude/settings.json` as
Copilot permission configuration, and do not modify it merely to make Copilot CLI
work.

## Repository conventions

- Keep candidate data and generated application outputs private; follow `.gitignore`.
- Use Windows-compatible commands when operating on Windows, and prefer the
  repository's documented Python and Bun entry points.
- For code changes, inspect the relevant files first, make surgical edits, and run
  the smallest applicable test command.
- When generating or changing application documents, follow the verification
  checklist in `CLAUDE.md`, including compilation and PDF inspection when required.
