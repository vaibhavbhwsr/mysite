---
name: Fireshine deployment prompt
description: "Prompt guidance for Docker, CI, Jenkins, and deployment configuration in Fireshine."
applyTo:
  - "docker-compose.yaml"
  - "docker-compose.prod.yaml"
  - "mysite/Dockerfile.dev"
  - "mysite/Dockerfile.prod"
  - "Jenkinsfile*"
  - ".github/workflows/**"
  - "nginx/**"
scope: workspace
---

Use this prompt for tasks related to:
- Docker Compose and container configuration
- production Dockerfiles and environment continuity
- Jenkins pipelines, CI steps, and deployment automation
- Nginx setup, static/media config, and deployment conventions

Guidance:
- Keep infrastructure changes minimal and compatible with existing local and Docker workflows.
- Do not commit secrets or production credentials.
- Review deployment commands and environment variable handling carefully.
- Preserve the repository’s current build, test, and rollout patterns.
