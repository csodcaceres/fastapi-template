# Architecture

## Overview

This project follows a layered architecture to separate responsibilities and improve maintainability.

Each layer has a single responsibility and communicates only with adjacent layers.

```
HTTP Request
      │
      ▼
 Router
      │
      ▼
 Service
      │
      ▼
 Repository
      │
      ▼
 Database
      │
      ▲
 Response
```

---

## Layers

### Router

Responsibilities:

- Define API endpoints.
- Validate request parameters.
- Call the appropriate service.
- Return HTTP responses.

Routers must not contain business logic or database queries.

---

### Service

Responsibilities:

- Implement business rules.
- Coordinate application logic.
- Call repositories when data access is required.
- Raise domain-specific exceptions.

Services should not contain HTTP-specific logic.

---

### Repository

Responsibilities:

- Interact with the database.
- Execute queries.
- Persist entities.
- Return models to the service layer.

Repositories should not contain business rules.

---

### Models

Responsibilities:

- Represent database entities.
- Define tables and relationships using SQLAlchemy.

---

### Schemas

Responsibilities:

- Validate incoming requests.
- Serialize outgoing responses.
- Define the public API contract.

---

## Dependency Flow

Dependencies should always move in one direction:

```
Router
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Database
```

Lower layers must never depend on higher layers.

---

## Error Flow

Exceptions should propagate upward.

```
Repository
      │
      ▼
Service
      │
      ▼
Global Exception Handler
      │
      ▼
HTTP Response
```

Repositories should not generate HTTP responses.

Services should not raise HTTPException directly.

---

## Design Principles

- Single Responsibility Principle (SRP)
- Separation of Concerns
- Dependency Injection
- Explicit Dependencies
- Maintainable and Testable Code

---

## Future Components

The architecture is designed to support:

- Authentication
- Authorization
- Background Tasks
- Caching
- External APIs
- Message Queues
- Unit and Integration Tests
- Docker Deployment