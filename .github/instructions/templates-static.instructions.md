---
applyTo:
  - "mysite/mysite/templates/**"
  - "mysite/mysite/static/**"
---

# Template And Static Instructions

Follow `AGENTS.md` as the canonical project guide.

- Keep templates consistent with the existing Bootstrap-based site structure.
- Scope JavaScript and CSS changes to the relevant template or static file.
- Preserve CSRF handling, form field names, upload behavior, and existing URL names.
- Test permission-sensitive rendered flows when templates expose auth, profile, chat, post, or video actions.
