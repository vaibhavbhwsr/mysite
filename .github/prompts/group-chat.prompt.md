---
name: Fireshine group chat prompt
description: "Prompt guidance for group chat rooms, WebSocket consumers, and Channels-based messaging."
applyTo:
  - "mysite/mysite/apps/group_chat/**"
scope: workspace
---

Use this prompt for tasks related to:
- group chat room models, room views, and room templates
- WebSocket consumer behavior, group message handling, and routing
- channel layer use, Redis configuration, and message persistence
- chat room access control and participant membership

Guidance:
- Preserve Django Channels routing in `group_chat/routing.py` and `mysite/mysite/asgi.py`.
- Add or update tests for consumer events, permissions, and group membership.
- Keep frontend chat JS and templates consistent with existing UI patterns.
- Mock WebSocket/network behavior in tests where appropriate.
