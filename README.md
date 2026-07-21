# FastAPI Template

A professional FastAPI project template built with modern Python development practices.

This template provides a solid foundation for building scalable REST APIs using FastAPI, SQLAlchemy 2.0, Pydantic Settings, and uv.

---

## Features

- Layered project architecture
- FastAPI
- SQLAlchemy 2.0
- Pydantic Settings
- Environment configuration
- Database session management
- SQLite support
- Ready to evolve to PostgreSQL
- uv package manager
- Type hint friendly

---

## Technology Stack

- Python 3.13+
- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- Pydantic Settings
- SQLite
- uv

---

## Project Structure

```text
app/
├── core/
├── database/
├── models/
├── routers/
├── schemas/
├── services/
└── main.py

data/
docs/
```

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/csodcaceres/fastapi-template.git
```

Install dependencies:

```bash
uv sync
```

Run the application:

```bash
uv run uvicorn app.main:app --reload
```

---

## Roadmap

- [x] Project structure
- [x] Configuration management
- [x] Database session management
- [ ] SQLAlchemy models
- [ ] Alembic migrations
- [ ] Docker support
- [ ] Pytest
- [ ] GitHub Actions

---

## License

MIT