---
name: Fireshine feature prompts index
description: "Index of feature-specific AI prompts for the Fireshine Django repository."
applyTo:
  - "**/*"
scope: workspace
---

# Fireshine Feature Prompt Index

Use these prompt files when working on a specific application area.

- `.github/prompts/authentication.prompt.md` – registration, auth, profile forms, login, signup, password reset.
- `.github/prompts/posts.prompt.md` – post feed, images, likes, comments, post APIs, post forms.
- `.github/prompts/group-chat.prompt.md` – group chat rooms, WebSocket consumers, Channels routing, message persistence.
- `.github/prompts/private-chat.prompt.md` – direct messages, private chat consumers, one-to-one chat behavior.
- `.github/prompts/video-chat.prompt.md` – Agora video rooms, members, cloud recording, room views.
- `.github/prompts/genai.prompt.md` – HuggingFace/LangChain generation flows, prompt handling, GenAI views.
- `.github/prompts/api-patterns.prompt.md` – DRF serializers, viewsets, API permissions, versioned API patterns.
- `.github/prompts/deployment-ci.prompt.md` – Docker Compose, production config, CI, Jenkins, Nginx, static/media deployment.

When using an AI assistant, prefer the prompt file that matches the affected app or feature area. Always keep the canonical rules in `AGENTS.md` and `.github/copilot-instructions.md` in mind.
