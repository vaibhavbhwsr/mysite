# Claude Project Instructions

Use `AGENTS.md` as the canonical AI coding guide for this repository. Keep this file as a compact Claude entry point and avoid duplicating rules that belong in `AGENTS.md`.

This is the Fireshine Django social networking project. It includes Django, DRF, Channels/WebSockets, PostgreSQL, Redis, Agora video chat, S3 storage, HuggingFace/LangChain content generation, Docker, and Jenkins deployment files.

When working in this repo:

- Read the affected app and nearby tests before editing.
- Keep changes small and consistent with existing Django patterns.
- Preserve auth, permissions, CSRF, sessions, and WebSocket routing unless explicitly asked to change them.
- Add migrations only for intentional schema changes.
- Add or update tests for behavior changes.
- Do not commit secrets from `.env`, `.env.prod`, `settings.ini`, cloud credentials, API tokens, or database credentials.
- Mock external services in tests.

Common checks from `mysite/`:

```bash
python manage.py check
python manage.py test
python manage.py makemigrations --check --dry-run
```
