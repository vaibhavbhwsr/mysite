# Gemini Project Instructions

Use `AGENTS.md` as the canonical AI coding guide for this repository. Keep this file as a compact Gemini entry point and avoid duplicating rules that belong in `AGENTS.md`.

This is the Fireshine Django social networking project. It has server-rendered Django pages, DRF APIs, Channels WebSockets, Agora video chat, S3 media/static support, HuggingFace/LangChain GenAI, Docker, and Jenkins deployment files.

Project map:

- Django root: `mysite/`
- Django package: `mysite/mysite/`
- Apps: `mysite/mysite/apps/`
- Settings: `mysite/mysite/settings/`
- Templates: `mysite/mysite/templates/`
- Static assets: `mysite/mysite/static/`

Rules:

- Read the relevant implementation before changing code.
- Prefer small, safe, idiomatic Django changes.
- Preserve app boundaries and existing naming patterns.
- Add tests for new behavior or bug fixes.
- Add migrations only for model/schema changes.
- Never commit real secrets.
- Mock external integrations in tests.

Common checks from `mysite/`:

```bash
python manage.py check
python manage.py test
python manage.py makemigrations --check --dry-run
```
