---
name: Fireshine authentication prompt
description: "Prompt guidance for registration, auth, and user profile features in Fireshine."
applyTo:
  - "mysite/mysite/apps/registration/**"
scope: workspace
---

Use this prompt for tasks related to:
- custom user and registration flows
- auth views, login/logout, signup, and password reset
- profile forms, user settings, and account updates
- registration REST APIs and token authentication

Guidance:
- Preserve `AUTH_USER_MODEL` conventions and use `get_user_model()` outside the registration app.
- Keep auth, CSRF, session, and permission behavior secure.
- Add or update tests for auth flows and user validation.
- Match existing Bootstrap templates, form styling, and app conventions.
- Do not introduce new external services without a clear repository reason.
