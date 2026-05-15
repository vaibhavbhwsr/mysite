# GitHub AI Coding Files

This directory contains GitHub-specific AI configuration. Use the root `../AGENTS.md` as the canonical source of truth and keep files here short enough that they do not drift from it.

When editing files in `.github/`, preserve the distinction between:

- `copilot-instructions.md`: concise repository-wide Copilot instructions loaded for most requests.
- `instructions/*.instructions.md`: path-specific Copilot instructions that auto-attach by glob.
- `agents/*.agent.md`: selectable Copilot custom agent profiles.
- `prompts/*.prompt.md`: reusable prompt templates for humans or IDE prompt runners.

Provider adapters, listed from the repository root:

- `.github/copilot-instructions.md`: GitHub Copilot workspace instructions
- `.github/instructions/django.instructions.md`: Django/Python path-specific instructions
- `.github/instructions/templates-static.instructions.md`: template and static asset instructions
- `.github/instructions/realtime.instructions.md`: Channels, chat, and video instructions
- `.github/instructions/deployment.instructions.md`: Docker, CI, Jenkins, and Nginx instructions
- `.github/instructions/agentic-setup.instructions.md`: AI coding setup maintenance instructions
- `.github/agents/django-assistant.agent.md`: Copilot custom Django agent
- `.github/prompts/project-coding.prompt.md`: reusable task prompt
- `.cursor/rules/django-project.mdc`: Cursor rule
- `CLAUDE.md`: Claude entry point
- `GEMINI.md`: Gemini entry point

Use the `Fireshine Django assistant` agent when available, or the `Fireshine project coding prompt` template for task-based requests.
