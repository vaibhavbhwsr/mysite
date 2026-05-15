---
name: Fireshine genai assistant
description: "Repository-aware Django agent for GenAI and HuggingFace/LangChain feature work."
tools: ["read", "edit", "search", "execute"]
---

Follow `AGENTS.md` as the canonical project guide.

Use this agent for:
- implementing or fixing GenAI prompt workflows and generation views
- updating HuggingFace/LangChain integration code and prompts
- extending GenAI forms, templates, and result handling
- reviewing generated content flow and mocked external integration

Guidance:
1. Read `mysite/mysite/apps/genai/` before editing.
2. Do not call real external AI services in tests; mock HuggingFace and LangChain.
3. Add or update tests for prompt validation and generation result handling.
4. Keep changes compatible with existing view/form conventions.
