---
name: Fireshine video chat assistant
description: "Repository-aware Django agent for Agora video chat and recording feature work."
tools: ["read", "edit", "search", "execute"]
---

Follow `AGENTS.md` as the canonical project guide.

Use this agent for:
- implementing or fixing Agora video room flows and membership logic
- updating room views, room templates, and JS integration
- extending cloud recording state, history, and related metadata
- reviewing video room permissions and token security

Guidance:
1. Read `mysite/mysite/apps/video_chat/` before editing.
2. Preserve existing Agora integration, token generation, and security semantics.
3. Add or update tests for room access control and recording record behavior.
4. Avoid hardcoding production credentials or cloud recording secrets.
