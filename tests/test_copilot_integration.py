import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
INSTRUCTIONS = REPO / ".github" / "copilot-instructions.md"
AGENTS = REPO / "AGENTS.md"


class CopilotIntegrationTests(unittest.TestCase):
    def test_copilot_instructions_is_a_thin_pointer_to_canonical_files(self):
        text = INSTRUCTIONS.read_text(encoding="utf-8")

        self.assertIn("CLAUDE.md", text)
        self.assertIn("AGENTS.md", text)
        self.assertIn(".claude/commands/", text)
        self.assertIn(".claude/skills/", text)
        self.assertIn(".agents/skills/*/SKILL.md", text)
        self.assertIn("Do not copy those specifications", text)

    def test_agents_mentions_copilot_adapter(self):
        text = AGENTS.read_text(encoding="utf-8")

        self.assertIn("GitHub Copilot CLI", text)
        self.assertIn(".github/copilot-instructions.md", text)


if __name__ == "__main__":
    unittest.main()
