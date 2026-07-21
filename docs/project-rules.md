# Project Rules

## Purpose

The goal of this project is to build a maintainable, scalable, and production-ready FastAPI application following modern Python development practices.

## Development Principles

- Prioritize readability over clever code.
- Prefer simplicity whenever possible.
- Write code that is easy to understand and maintain.
- Follow the existing project structure and conventions.

## Layer Responsibilities

- Routers handle HTTP requests and responses only.
- Services contain business logic.
- Repositories handle database access.
- Models define database entities.
- Schemas validate and serialize data.

## Code Standards

- Use Python type hints for all public functions.
- Keep functions focused on a single responsibility.
- Avoid duplicated code.
- Use meaningful names for variables, functions, classes, and files.
- Remove unused imports and dead code.

## Error Handling

- Raise domain-specific exceptions when appropriate.
- Avoid generic exceptions unless absolutely necessary.
- Handle HTTP errors in the API layer.

## Documentation

- Update the documentation when changing the project structure or architecture.
- Keep documentation synchronized with the implementation.

## Testing

- New features should include tests whenever practical.
- Bug fixes should include regression tests when applicable.