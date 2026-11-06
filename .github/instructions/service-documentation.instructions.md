---
description: "Use when the user asks to create or edit service documentation. Defines the concise README.md structure for a service."
applyTo:
  - "src/*/*/**/*.py"
  - "src/*/*/README.md"
---

# Service Documentation

Every service must have a concise `README.md` in its service directory. Create or update it only when the user explicitly asks for documentation changes.

Use these sections:

1. **Concept** — briefly explain the service's purpose.
2. **Responsibilities** — summarize what the service owns and does.
3. **Input and output contracts** — explain the contracts only when their behavior or structure is complex. Otherwise, refer to the relevant schemas or types in the code.
4. **Notes** — include only important caveats or usage notes; omit the section content when there is nothing noteworthy.

Keep the README focused on service-specific information. Do not duplicate details that are clear from the code or documented elsewhere.

When substantial code changes may make the service documentation outdated, remind the user that an update may be needed. Do not edit documentation without an explicit request.
