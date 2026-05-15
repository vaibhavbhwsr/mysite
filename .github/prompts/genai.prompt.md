---
name: Fireshine genai prompt
description: "Prompt guidance for GenAI generation and HuggingFace/LangChain features in Fireshine."
applyTo:
  - "mysite/mysite/apps/genai/**"
scope: workspace
---

Use this prompt for tasks related to:
- HuggingFace text generation and LangChain prompt handling
- GenAI views, forms, and content creation workflows
- model selection, generation caching, and result rendering
- tests for GenAI integration and mocked external behavior

Guidance:
- Do not call real external AI services in tests; mock HuggingFace and LangChain calls.
- Keep generated content behavior aligned with existing views and templates.
- Add or update tests for prompt validation and generation result handling.
- Preserve repository conventions for small, safe changes.
