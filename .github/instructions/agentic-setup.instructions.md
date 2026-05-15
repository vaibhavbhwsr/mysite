---
applyTo:
  - "AGENTS.md"
  - "CLAUDE.md"
  - "GEMINI.md"
  - ".github/AGENTS.md"
  - ".github/copilot-instructions.md"
  - ".github/agents/**"
  - ".github/instructions/**"
  - ".github/prompts/**"
  - ".cursor/rules/**"
---

# Agentic Setup Instructions

Follow `AGENTS.md` as the canonical source of truth.

- Keep provider-specific files thin and point them back to `AGENTS.md`.
- Put always-on GitHub Copilot guidance in `.github/copilot-instructions.md`.
- Put path-specific Copilot guidance in `.github/instructions/*.instructions.md`.
- Put selectable Copilot custom agents in `.github/agents/*.agent.md`.
- Put reusable task prompts in `.github/prompts/*.prompt.md`.
- Avoid copying long project rules into every provider file; update `AGENTS.md` instead.
