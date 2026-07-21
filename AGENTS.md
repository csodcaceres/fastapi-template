# AGENTS.md

## Project Overview

This repository contains a FastAPI application following a layered architecture.

Before making any code changes, read the following documentation:

- docs/project-rules.md
- docs/architecture.md
- docs/api-conventions.md

## General Rules

- Keep routers focused only on HTTP concerns.
- Business logic belongs in services.
- Database access belongs in repositories.
- Use Pydantic schemas for validation and serialization.
- Do not modify the project structure without updating the documentation.

## Code Quality

- Follow Python type hints.
- Keep functions small and focused.
- Avoid duplicated logic.
- Write clear and maintainable code.