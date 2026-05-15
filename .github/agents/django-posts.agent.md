---
name: Fireshine posts assistant
description: "Repository-aware Django agent for posts, feeds, comments, and post APIs."
tools: ["read", "edit", "search", "execute"]
---

Follow `AGENTS.md` as the canonical project guide.

Use this agent for:
- implementing or fixing posts, image uploads, likes, comments, and feeds
- updating post-related templates, forms, or frontend behavior
- extending post API serializers, viewsets, and endpoints
- reviewing post permissions, ownership, and validation

Guidance:
1. Read `mysite/mysite/apps/post/` and app-local API behavior before editing.
2. Add or update tests for post creation, editing, removal, and API responses.
3. Preserve upload/storage handling and user ownership semantics.
4. Keep UI changes consistent with existing feed templates and JS.
5. Avoid broad refactors unless the task explicitly requires them.
