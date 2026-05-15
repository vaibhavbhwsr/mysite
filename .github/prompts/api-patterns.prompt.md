---
name: Fireshine API patterns prompt
description: "Prompt guidance for DRF serializer, viewset, and API pattern work in Fireshine."
applyTo:
  - "mysite/mysite/apps/**/api/**"
  - "mysite/mysite/urls.py"
scope: workspace
---

Use this prompt for tasks related to:
- DRF serializers, viewsets, permissions, and API endpoints
- API versioning, swagger/redoc, and API URL registration
- token auth and API permission rules
- API tests and serializer validation behavior

Guidance:
- Preserve existing DRF patterns and app-local API structure.
- Add or update tests for serializer validation, permission classes, and endpoint responses.
- Avoid broad changes outside the API area unless the feature explicitly spans templates or models.
- Keep API behavior consistent with the current `/api/v1/` structure.
