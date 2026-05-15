---
applyTo:
  - "docker-compose.yaml"
  - "docker-compose.prod.yaml"
  - "mysite/Dockerfile.dev"
  - "mysite/Dockerfile.prod"
  - "Jenkinsfile*"
  - ".github/workflows/**"
  - "nginx/**"
  - "mysite/entrypoint.sh"
---

# Deployment Instructions

Follow `AGENTS.md` as the canonical project guide.

- Keep Docker, Jenkins, GitHub Actions, Nginx, Gunicorn, and Daphne changes compatible with the existing local and production workflows.
- Do not commit secrets, real environment values, API tokens, database passwords, or cloud credentials.
- Preserve environment-driven settings through `python-decouple`.
- When changing CI or deployment commands, consider both local development and Docker production paths.
- Report any checks that require unavailable services such as PostgreSQL, Redis, Docker, or network access.
