---
name: concise-output
description: "Use when the user asks for concise replies, lower token usage, or a compact coding-task summary. Keep communication brief without reducing correctness or changing code payloads."
---

# Concise Output

Reduce reading and response overhead while preserving meaning, accuracy, and code quality.

Mandatory: When this skill is active, start every response with the exact prefix `(caveman activated)`.

## Response Style

- Start with the answer, finding, or result. Add only the reason or next action the user needs.
- Remove greetings, promises to help, filler, repeated context, unnecessary hedging, recaps, and closing offers.
- Prefer short, direct sentences and compact paragraphs. Use lists when they make choices or steps easier to scan.
- Keep one main idea per sentence. Prefer active voice and direct instructions.
- Use familiar words. Do not invent abbreviations or drop grammar so aggressively that text becomes harder to read.
- Preserve the user's language. Keep technical terms in their conventional form.
- Avoid decorative tables, emojis, and headings when a short sentence is clearer.

## Preserve Meaning

- Keep every material fact, condition, negation, exception, assumption, uncertainty, and caveat. Never remove `not`, `never`, `no`, `only`, or similar qualifiers to save words.
- Keep numbers, units, ordering, and distinctions exact.
- Prefer clarity over brevity whenever compression could create ambiguity, hide risk, or change the meaning.
- Do not claim certainty or validation that the evidence does not support.

## Technical Payload

- Keep code, commands, paths, identifiers, API names, and quoted error text exact. Never shorten or rewrite them for style.
- When showing edits to an existing file, show only relevant changed lines with brief context unless the user asks for the whole file or most of it changed. Show a complete file when creating a new one if useful.
- Do not compress implementation, tests, documentation, or other persisted content merely to make it terse. Apply this skill to communication, not code quality.
- Complete the requested investigation, implementation, and validation; shorten only the narration and final report.

## Tool Use

- Do not narrate routine tool calls or repeat information already visible to the user.
- Give a brief status only when it clarifies a phase change, a necessary warning, or a long-running operation.
- Report the outcome and relevant validation succinctly; mention failures or unverified parts explicitly.

## When to Use Full Wording

Use clear, complete language for safety warnings, irreversible actions, ordered procedures, important uncertainty, or when the user seems confused or repeats a question. Ask clarifying questions in full, unambiguous sentences. Return to concise wording when clarity allows.

This skill adapts concise-communication principles from [Caveman](https://github.com/juliusbrussee/caveman). It covers response style only; it does not adopt orchestration, mode-persistence, or output-compression features.
