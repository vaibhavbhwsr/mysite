# Agentic Coding Guide

This file is the canonical AI coding guide for this repository. It is written to be usable by any coding assistant, including GitHub Copilot, Cursor, Claude, Codex, Gemini, Continue, Aider, and other LLM-based tools.

Provider-specific files in this repo should point back here instead of duplicating project rules.

## Project Snapshot

Fireshine is a Django social networking application with traditional server-rendered pages, REST APIs, WebSocket chat, video chat, and deployment automation.

Main paths:

- Django project root: `mysite/`
- Django package: `mysite/mysite/`
- Settings: `mysite/mysite/settings/base.py`, `dev.py`, `prod.py`
- Apps: `mysite/mysite/apps/`
- Templates: `mysite/mysite/templates/`
- Static assets: `mysite/mysite/static/`
- Docker: `docker-compose.yaml`, `docker-compose.prod.yaml`, `mysite/Dockerfile.dev`, `mysite/Dockerfile.prod`
- CI/deployment: `Jenkinsfile`, `Jenkinsfile.dev`, `Jenkinsfile.prod`, `.github/workflows/`

Important apps:

- `registration`: custom `User`, auth views, profile forms, DRF token setup
- `post`: post feed, images, likes, comments, post APIs
- `group_chat`: group chat models, views, WebSocket consumer
- `private_chat`: one-to-one chat models, views, WebSocket consumer
- `video_chat`: Agora video rooms, members, cloud recording records
- `genai`: HuggingFace/LangChain content generation
- `core`: shared base model and common app behavior

## Operating Principles

- Read the relevant code before editing.
- Make the smallest safe change that satisfies the task.
- Preserve the existing Django app boundaries and naming style.
- Do not rewrite broad areas of the project unless explicitly asked.
- Do not remove or regenerate user changes that are unrelated to the task.
- Keep changes compatible with both local development and Docker deployment.
- Prefer readable, boring Django code over clever abstractions.
- Update tests when behavior changes.
- Add migrations only when model/schema changes require them.

## Local Setup Assumptions

The app expects environment-driven settings through `python-decouple`.

Typical local settings:

- `MODE=dev`
- `DEBUG=True`
- `USE_S3=False`
- PostgreSQL available locally, default database `mysitedb`
- Redis available locally for Channels/cache

Use `example.env` and `mysite/example.ini` only as examples. Do not commit real secrets.

## Common Commands

Run commands from `mysite/` unless noted otherwise.

```bash
python manage.py check
python manage.py test
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py runserver 0.0.0.0:7000
```

Docker development from repository root:

```bash
docker compose build
docker compose up
```

Production compose from repository root:

```bash
docker compose -f docker-compose.prod.yaml up --build
```

Formatting/linting tools are listed in `mysite/requirements.txt` and `mysite/setup.cfg`. Prefer the repository's existing formatting over introducing a new formatter configuration.

## Architecture Notes

- `AUTH_USER_MODEL` is `registration.User`; import users with `django.contrib.auth.get_user_model()` in app code.
- HTTP routes are registered in `mysite/mysite/urls.py`.
- ASGI/WebSocket routes are wired in `mysite/mysite/asgi.py`.
- WebSocket consumers use Django Channels and `channels_redis`.
- REST APIs live under app-local `api/` packages and are exposed below `/api/v1/`.
- Swagger and Redoc are exposed from the root URL config.
- Static/media files can be local or S3-backed depending on `USE_S3`.
- Production starts both Gunicorn for WSGI and Daphne for ASGI from `mysite/entrypoint.sh`.

## Coding Standards

- Follow existing class-based view, form, serializer, and URL patterns.
- Use `get_user_model()` instead of importing `registration.User` directly outside that app.
- Keep view logic concise; move repeated or integration-heavy behavior into helpers/services.
- Prefer Django ORM relationships and queryset APIs over manual data shaping.
- Use transactions for multi-step database writes when partial writes would be unsafe.
- Avoid adding dependencies unless the task clearly needs one.
- Keep templates consistent with the existing Bootstrap-based styling.
- Keep JavaScript changes scoped to the relevant static file or template.
- Do not call external services from tests; mock Agora, HuggingFace, S3, email, and network requests.

## Database And Migrations

- Inspect existing migrations before changing models.
- Create migrations only for intentional schema changes.
- Do not edit old migrations unless the user explicitly asks and the repo has not yet shipped them.
- Check migration generation with:

```bash
python manage.py makemigrations --check --dry-run
```

## Testing Expectations

For bug fixes and new behavior, add or update tests near the affected app:

- `mysite/mysite/apps/<app>/tests.py`
- API tests for serializer/viewset behavior
- View tests for permissions, redirects, and rendered behavior
- Consumer tests for WebSocket behavior when practical

At minimum, run:

```bash
python manage.py check
python manage.py test
```

If local infrastructure is missing, report exactly what could not run and why.

## Security Rules

- Never commit real secrets, credentials, tokens, private keys, database passwords, or `.env` values.
- Treat `.env`, `.env.prod`, `settings.ini`, and cloud/API credentials as sensitive.
- Do not weaken authentication, authorization, CSRF, session, or permission behavior without explicit instruction.
- Be careful with user-uploaded files, image fields, and S3/public media behavior.
- Avoid logging sensitive settings or request data.
- For APIs, preserve permission classes unless the requested change requires a review.

## External Integrations

Be careful when touching:

- Agora token generation and cloud recording in `video_chat`
- HuggingFace/LangChain generation in `genai`
- S3 storage backends in `commons/storage_backends.py`
- Redis/Channels settings
- Email/password reset configuration
- Sentry production initialization

Mock external calls in tests.

## Agent Workflow

For non-trivial tasks:

1. Identify the affected app, URL, model, template, serializer, or consumer.
2. Read the current implementation and nearby tests.
3. Summarize the existing behavior briefly.
4. Implement the smallest safe change.
5. Add or update tests.
6. Run focused checks first, then broader checks when feasible.
7. Report files changed, commands run, and any remaining risks.

For review tasks:

- Lead with bugs, regressions, security issues, and missing tests.
- Include precise file and line references.
- Keep summaries secondary to findings.

## Provider Files

These files adapt the same guidance for specific tools:

- `AGENTS.md`: canonical guide for Codex/OpenAI-style agents and general LLM tools
- `.github/copilot-instructions.md`: GitHub Copilot workspace instructions
- `.github/instructions/*.instructions.md`: path-specific GitHub Copilot instructions
- `.github/agents/django-assistant.agent.md`: Copilot custom agent
- `.github/agents/django-auth.agent.md`: auth and registration assistant
- `.github/agents/django-posts.agent.md`: post/feed assistant
- `.github/agents/django-group-chat.agent.md`: group chat assistant
- `.github/agents/django-private-chat.agent.md`: private chat assistant
- `.github/agents/django-video.agent.md`: video chat assistant
- `.github/agents/django-genai.agent.md`: GenAI assistant
- `.github/agents/django-api.agent.md`: API assistant
- `.github/agents/django-ops.agent.md`: deployment/CI assistant
- `.github/prompts/feature-index.prompt.md`: feature prompt index
- `.github/prompts/authentication.prompt.md`: auth feature prompt
- `.github/prompts/posts.prompt.md`: posts feature prompt
- `.github/prompts/group-chat.prompt.md`: group chat feature prompt
- `.github/prompts/private-chat.prompt.md`: private chat feature prompt
- `.github/prompts/video-chat.prompt.md`: video chat feature prompt
- `.github/prompts/genai.prompt.md`: GenAI feature prompt
- `.github/prompts/api-patterns.prompt.md`: API patterns prompt
- `.github/prompts/deployment-ci.prompt.md`: deployment and CI prompt
- `.github/prompts/project-coding.prompt.md`: reusable task prompt
- `.cursor/rules/django-project.mdc`: Cursor project rule
- `CLAUDE.md`: Claude Code/project memory entry point
- `GEMINI.md`: Gemini CLI/project instruction entry point
