# Copilot Workspace Instructions

Follow the canonical repository guide in `AGENTS.md`. Treat this file as a short always-on reminder; use `.github/instructions/*.instructions.md` for path-specific detail and `.github/prompts/*.prompt.md` for reusable task prompts.

This repository is a Django social networking application rooted at `mysite/`. It includes server-rendered pages, DRF APIs, Django Channels WebSockets, Agora video chat, HuggingFace/LangChain content generation, Docker files, and Jenkins deployment files.

- Preserve existing Django conventions and app structure.
- Analyze the relevant files before making changes.
- Avoid breaking authentication, session handling, or channel routing.
- Add or update migrations only when schema changes are required.
- Update tests for any new behavior or bug fix.
- Keep template and frontend updates aligned with existing site styling and JS.
- Do not introduce unrelated external dependencies without a compelling reason.
- Prefer minimal safe changes that satisfy the request.
- Do not commit secrets from `.env`, `.env.prod`, `settings.ini`, API tokens, cloud credentials, or database credentials.
- Mock Agora, HuggingFace, S3, email, and other network integrations in tests.

When implementing a change, identify the current code path, make the smallest safe patch, add/update tests, and report the checks that were run.

For targeted work, start with `.github/prompts/feature-index.prompt.md` and choose the prompt that matches the affected app or capability.
