---
description: "Use when creating or editing Python processing classes in services under src/processing/. Defines class structure, naming, typing, atomic processing methods, and the result interface for linear processing."
applyTo: "src/processing/*/**/*.py"
---

# Processing Class Design

Use object-oriented design for processing code. A processing class represents one linear transformation, retaining reusable configuration and coordinating small processing steps.

## 1. Class and File Structure

### 1.1 One Main Class per File

- Each Python file has one main class.
- Name the class with a short verb that describes its action, in PascalCase, such as `Consolidate` or `Process`.
- Keep each class focused on one processing responsibility.

### 1.2 Constructor

- Use `__init__` to store input and configuration that the instance reuses across processing steps.
- Add type annotations to constructor parameters and attributes.
- Avoid doing the full processing workflow in `__init__`.

## 2. Processing Methods

### 2.1 Atomic Operations

- Implement processing as small methods, each with one clear responsibility.
- Prefer methods that process a single item when the workflow iterates over items.
- Add type annotations to every method's parameters and return value.
- Give every method a concise, one-sentence docstring.

### 2.2 Keep Iteration Central

- Let the result orchestration own the main item-by-item loop.
- Avoid scattering repeated loops across helper methods when each helper can operate on one item.
- Add additional loops only when they represent a meaningful processing stage.

## 3. Result Interface

### 3.1 Synchronous Processing

- Expose the final output through a typed `result` property.
- Accessing `Processor(args).result` runs the workflow: validate or prepare input, coordinate atomic methods, and return the documented output shape.
- Keep orchestration in `result`; keep individual transformations in focused methods.

### 3.2 Asynchronous Processing

- When a stage requires asynchronous work, complete the preparation pass before starting that stage.
- Run independent asynchronous operations concurrently, then perform a separate finalization pass when needed.
- Preserve the association and ordering between inputs and results when the output contract requires it.
- Since Python properties cannot be awaited idiomatically, expose asynchronous processing as `async def result(...)` and call it with `await processor.result(...)` when the workflow itself must await I/O.

## 4. Output Contract

- Return the output shape expected by the caller.
- Keep output models or schemas explicit in code and use them in type annotations where practical.
- Raise or propagate meaningful errors; do not silently return incomplete or success-shaped fallback results.
