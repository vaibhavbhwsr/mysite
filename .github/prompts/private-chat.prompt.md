---
name: Fireshine private chat prompt
description: "Prompt guidance for one-to-one private chat, consumers, and direct messaging in Fireshine."
applyTo:
  - "mysite/mysite/apps/private_chat/**"
scope: workspace
---

Use this prompt for tasks related to:
- private direct message models, views, and templates
- one-to-one WebSocket consumers and chat routing
- private message delivery, unread state, and conversation handling
- access control and user-to-user chat authorization

Guidance:
- Preserve private chat permission semantics and one-to-one routing.
- Add or update tests for private consumer events and authorization.
- Keep changes localized to the private chat app unless the task explicitly spans other chat features.
- Mock Channels and WebSocket behavior in tests rather than relying on external network services.
