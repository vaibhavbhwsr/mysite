---
name: Fireshine video chat prompt
description: "Prompt guidance for Agora video chat rooms, members, and recording features in Fireshine."
applyTo:
  - "mysite/mysite/apps/video_chat/**"
scope: workspace
---

Use this prompt for tasks related to:
- Agora room creation, membership, and token generation
- room views, templates, and JS integration
- cloud recording state, history, and room metadata
- video call entry/exit flows and room permissions

Guidance:
- Preserve existing Agora integration and token/security behavior.
- Add or update tests for room access, recording records, and view permissions.
- Avoid hardcoding secrets or cloud recording credentials in code.
- Keep changes consistent with the project’s existing static assets and page layout.
