---
applyTo:
  - "mysite/mysite/apps/group_chat/**"
  - "mysite/mysite/apps/private_chat/**"
  - "mysite/mysite/apps/video_chat/**"
  - "mysite/mysite/asgi.py"
---

# Realtime Instructions

Follow `AGENTS.md` as the canonical project guide.

- Preserve Django Channels routing, channel layer assumptions, and room permission semantics.
- For group or private chat changes, read the app's `routing.py`, `consumers.py`, views, models, and related templates.
- For video chat changes, preserve Agora token generation, room access checks, recording state, and credential handling.
- Add focused tests for consumer events, room access, membership, and recording records when behavior changes.
- Do not call live Agora, Redis, or network services from tests.
