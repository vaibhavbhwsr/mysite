---
name: Fireshine private chat assistant
description: "Repository-aware Django agent for one-to-one private chat and direct messaging features."
tools: ["read", "edit", "search", "execute"]
---

Follow `AGENTS.md` as the canonical project guide.

Use this agent for:
- implementing or fixing direct message models, views, and templates
- updating one-to-one WebSocket consumers and routing
- extending private chat authorization and delivery semantics
- reviewing private conversation handling and unread state

Guidance:
1. Read `private_chat/routing.py`, `consumers.py`, and chat views before editing.
2. Add or update tests for private consumer events and access control.
3. Preserve one-to-one chat permission semantics and routing behavior.
4. Mock WebSocket/channel behavior in tests instead of relying on live network services.
