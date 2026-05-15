---
applyTo:
  - "mysite/**/*.py"
---

# Django And Python Instructions

Follow `AGENTS.md` as the canonical project guide.

- Read the affected app, model, view, serializer, form, consumer, and nearby tests before editing.
- Use `django.contrib.auth.get_user_model()` outside the `registration` app.
- Keep behavior inside the existing app boundaries unless the task clearly spans apps.
- Add migrations only for intentional schema changes, and check them with `python manage.py makemigrations --check --dry-run` from `mysite/`.
- Add or update tests near the affected app for bug fixes and new behavior.
- Mock external services, including Agora, HuggingFace, S3, email, Redis-dependent network behavior, and other network calls.
