<p align="center">
  <img src="assets/mascot/pip_flight_loop.gif" alt="Pip, the courier bird" width="200">
</p>

# AI Job Search

An open-source workspace for organizing and improving your job search with AI.

This is a usable public fork of
[MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)
with [GitHub Copilot CLI](https://github.com/github/copilot-cli) support.
The original repository remains the upstream source for broader documentation
and the Claude Code implementation.

**If you're a student, join [GitHub Education](https://github.com/education/students)!**
You may be eligible for the GitHub Student Developer Pack, which includes
GitHub Pro and [Copilot](https://github.com/github-copilot/free_signup).

> This project is independent and is not affiliated with GitHub, Microsoft,
> Anthropic, or any other AI provider.

## What it does

Use it to:

- organize your candidate profile and career history;
- search for relevant job postings;
- evaluate whether a role is a good fit;
- tailor a CV and cover letter;
- track applications; and
- prepare for interviews.

Your profile and application documents stay local. You decide what to share.

## Automation workflow

```text
/setup          /scrape              /apply <url>
  |                |                     |
  v                v                     v
Fill in        Search job           Evaluate fit
your profile   portals              Score & recommend
  |                |                     |
  v                v                     v
Profile        Present matches      Draft CV + Cover Letter
files ready    with fit ratings     (LaTeX, tailored)
                   |                     |
                   v                     v
               Pick a match         Reviewer agent critiques
               -> /apply            -> Revise -> Final output
```

After applying, use `/outcome` to track progress, `/interview` to prepare,
`/upskill` to close skill gaps, and `/html-report` to review your search.

Each workflow keeps you in control: review and approve changes before personal
data or application records are updated. See the canonical command files in
[`.claude/commands/`](.claude/commands/) for details.

## GitHub Copilot CLI support

Copilot CLI reads the repository guidance from:

- [`AGENTS.md`](AGENTS.md)
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md)

These files point Copilot to the canonical workflow specifications under
[`.claude/`](.claude/).

Start Copilot CLI from this repository's root folder:

```powershell
copilot
```

Both Copilot CLI and Claude Code support the canonical slash commands:
`/setup`, `/scrape`, `/rank`, and `/apply`. Copilot CLI also accepts the
natural-language requests shown above.

## Quick start

### 1. Fork and clone

For your own job search, clone this fork:

```bash
git clone https://github.com/arohao/ai-job-search-copilot.git
cd ai-job-search-copilot
```

If you are contributing changes to the original project, fork and clone the
upstream repository instead:

```bash
gh repo fork MadsLorentzen/ai-job-search --clone
cd ai-job-search
```

> **Forks of public repositories are public.** `/setup` writes personal data
> into tracked files, so use a private repository for your personal job search.
> See [SETUP.md, section 8](SETUP.md#8-pulling-upstream-updates-into-your-fork)
> for the private-repository setup.

### 2. Install the tools you need

```bash
python3 tools/install_portal_clis.py   # Windows: python tools\install_portal_clis.py
```
- GitHub Copilot CLI or Claude Code;
- Python 3.10 or newer;
- [Bun](https://bun.sh) for the job-search tools; and
- a LaTeX distribution if you want to generate PDF CVs and cover letters.

See [`SETUP.md`](SETUP.md) for installation details and Windows instructions.

### 3. Start your AI tool and set up your profile

For Copilot CLI:

```bash
copilot
# Then inside Copilot:
/setup
```

For Claude Code:

```bash
claude
# Then inside Claude Code:
/setup
```

Then ask the tool to set up your profile.

## Using the original project

The original repository is the best source for:

- the complete workflow documentation;
- detailed setup and troubleshooting instructions;
- portal-specific search tools;
- CV and cover-letter guidance; and
- updates to the underlying framework.

Visit the original project here:

[github.com/MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)

## Privacy

Do not commit personal CVs, contact details, application documents, salary data,
or other private information to a public repository. Review `.gitignore` and
`git status` before pushing changes.

For a personal job-search workspace, use a private repository or keep your
personal files local. Use a public fork primarily when contributing changes back
to the original project.

## Contributing

Improvements to the Copilot integration and documentation are welcome. Before
making larger workflow changes, check the original project's contribution
guidance in [`CONTRIBUTING.md`](CONTRIBUTING.md) and avoid duplicating the
canonical instructions under `.claude/`.

## License

This project is distributed under the license in [`LICENSE`](LICENSE).
