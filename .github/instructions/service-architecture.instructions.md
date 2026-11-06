---
description: "Use whenever creating or editing Python code inside a service under src/<scope>/<service>/. Defines the service's lightweight Hexagonal Architecture and boundaries between core logic, repository ports, and adapters."
applyTo: "src/*/*/**/*.py"
---

# Service Architecture

Organize each service using a lightweight Hexagonal Architecture (Ports and Adapters). Keep service logic independent of external providers and frameworks.

```text
src/<scope>/<service>/
  service.py             # required: service operations and use-case coordination
  tests/                  # required: unit tests for this service
  models.py               # optional: service-owned data structures
  repository.py           # optional: data-access port
  ports.py                # optional: other outbound ports
  adapters/               # optional: implementations of outbound ports
    <adapter>.py
```

## File and Directory Responsibilities

- `service.py` implements the service's operations and coordinates its use cases. Keep business rules here or in focused core modules, without dependencies on provider-specific SDKs or frameworks.
- `tests/` contains the service's unit tests. Organize tests to reflect the service's modules where useful.
- `models.py` holds data structures and concepts owned by the service. Add it when the service needs shared or meaningful domain data types.
- `repository.py` defines a port for persisted data access when the service needs it. Keep the contract focused on the operations required by the service.
- `ports.py` defines other outbound contracts required by the service, such as external compute or APIs. Keep ports in the service core, close to the use cases that depend on them.
- `adapters/` contains concrete implementations of ports for external systems. Adapters depend on core port contracts; the core must not depend on adapters.

## Dependency Rules

- Pass required ports or adapters into service operations or constructors explicitly.
- Keep `infrastructure/` for computational resources and runtime setup used to run services, organized under the relevant scope. It is not a substitute for service logic or service-level adapters.
- Keep integration tests in the repository-root `tests/` directory.

## Notes

- Add only optional files and directories that the service needs. For example, a pure transformation does not need a repository, port, or adapter.
- A separate `ports/` package or dependency-injection framework is unnecessary unless the service's complexity demonstrates a need.
