---
name: Fireshine group chat assistant
description: "Repository-aware Django agent for group chat room and WebSocket feature work."
tools: ["read", "edit", "search", "execute"]
---

Follow `AGENTS.md` as the canonical project guide.

Use this agent for:
- implementing or fixing group chat rooms, room views, and templates
- updating WebSocket consumers, channel routing, and group message handling
- extending group chat permissions, membership, or message persistence
- reviewing channel layer behavior and Redis/Channels integration

Guidance:
1. Read `group_chat/routing.py`, `consumers.py`, and related views before editing.
2. Add or update tests for consumer events, group membership, and room access.
3. Preserve WebSocket routing in `mysite/mysite/asgi.py` and Channels settings.
4. Keep frontend chat behavior consistent with existing UI patterns.
