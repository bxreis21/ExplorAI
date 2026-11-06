# ExplorAI

## Context
ExplorAI is an academic project for exploring and profiling semi-structured data, with distributed processing and AI-assisted queries. See the README for the project scope and roadmap.

## Architecture

Organize code by scope, then by service. A scope groups services with related responsibilities; each service contains its own implementation, data-access boundary, and models as needed:

```text
src/
  <scope>/
    <service>/
      service.py
      repository.py
      models.py
```

`service.py` contains the service's operations and coordination, `repository.py` defines its data-access boundary, and `models.py` contains its data structures. Include only the files a service needs; for example, a service that does not access persisted data does not need a repository.

### ExplorAI scopes

- `processing/`: data transformations and profiling. Initial services/components include flattening and profiling.
- `application/`: user-facing capabilities, including catalog exploration and querying.
- `mcp/`: MCP interface for exposing existing capabilities to AI agents; it should delegate to those capabilities rather than duplicate their logic.

#### Infrastructure

`infrastructure/` organizes the computational resources and runtime setup required to run services, such as managed compute, jobs, or containers. Keep it separate from service logic and organize it under the relevant scope. 

#### Tests

Keep each service's unit tests in that service's own `tests/` directory. Reserve the root `tests/` directory for integration tests.

## Rules

- Write all repository content in English, including code, comments, documentation, tests, and agent instructions.
- Follow [service architecture instructions](.github/instructions/service-architecture.instructions.md) when creating or editing service code.
- Follow [processing class instructions](.github/instructions/processing-classes.instructions.md) when creating or editing processing classes under `src/processing/`.
- Follow [service documentation instructions](.github/instructions/service-documentation.instructions.md) when creating or editing service code or documentation.
- Do not create or modify tests during development unless the user explicitly asks for tests to be created or updated.
- Do not create or modify documentation unless the user explicitly asks. If a code change is substantial enough that documentation may be outdated, remind the user in the final response; do not update the documentation automatically.