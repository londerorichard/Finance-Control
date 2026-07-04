# 📦 Project Dependencies

This document lists the main dependencies used in the project and their purposes.

---

# 🚀 Production Dependencies

Install the required packages with:

```bash
pip install fastapi uvicorn sqlalchemy pydantic python-jose passlib[bcrypt] python-multipart jinja2
```

| Package              | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| **FastAPI**          | Web framework for building high-performance APIs.          |
| **Uvicorn**          | ASGI server used to run FastAPI applications.              |
| **SQLAlchemy**       | ORM for interacting with relational databases.             |
| **Pydantic**         | Data validation and serialization using Python type hints. |
| **python-jose**      | JWT authentication and token handling.                     |
| **passlib[bcrypt]**  | Password hashing using the bcrypt algorithm.               |
| **python-multipart** | Handles form data, file uploads, and login forms.          |
| **Jinja2**           | Template engine for rendering dynamic HTML pages.          |

---

# 🛠️ Development Dependencies

Install the development tools with:

```bash
pip install pytest httpx black isort ruff mypy
```

| Package    | Purpose                                                           |
| ---------- | ----------------------------------------------------------------- |
| **pytest** | Framework for writing and running unit tests.                     |
| **httpx**  | HTTP client used to test FastAPI endpoints.                       |
| **black**  | Automatically formats Python code following a consistent style.   |
| **isort**  | Organizes and sorts Python imports.                               |
| **ruff**   | Fast linter that replaces Flake8 and several other linting tools. |
| **mypy**   | Static type checker for Python.                                   |

---

# 📋 Summary

### Production

* FastAPI
* Uvicorn
* SQLAlchemy
* Pydantic
* python-jose
* passlib[bcrypt]
* python-multipart
* Jinja2

### Development

* pytest
* httpx
* black
* isort
* ruff
* mypy

```

This setup provides everything needed to build, test, format, lint, and maintain a modern FastAPI application.
```
