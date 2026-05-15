---
name: Fireshine posts prompt
description: "Prompt guidance for post feed, image posts, likes, comments, and post APIs in Fireshine."
applyTo:
  - "mysite/mysite/apps/post/**"
scope: workspace
---

Use this prompt for tasks related to:
- post creation, editing, deletion, and moderation
- image uploads, feed rendering, likes, and comments
- post-related templates and frontend JavaScript behavior
- post API serializers, viewsets, and list/detail endpoints

Guidance:
- Keep changes aligned with existing post models and forms.
- Add or update tests for post permissions, form validation, and API behavior.
- Preserve current upload/storage handling and user ownership semantics.
- Avoid broad refactors unless the feature request specifically requires it.
