import sqlite3

import pytest
from fastapi.testclient import TestClient

import app.services.auth_service as auth_service
from app.database.connection import get_connection
from app.main import app


@pytest.fixture
def test_db(tmp_path):
    db_path = tmp_path / "test_finance.db"

    connection = sqlite3.connect(db_path)

    try:
        connection.execute(
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.commit()
    finally:
        connection.close()

    return str(db_path)


@pytest.fixture
def test_auth_db(test_db, monkeypatch):
    def get_test_connection():
        return get_connection(test_db)

    monkeypatch.setattr(
        auth_service,
        "get_connection",
        get_test_connection
    )


@pytest.fixture
def db_connection(test_db):
    connection = get_connection(test_db)

    yield connection

    connection.close()


@pytest.fixture
def client(test_db, monkeypatch):
    def get_test_connection():
        return get_connection(test_db)

    monkeypatch.setattr(
        auth_service,
        "get_connection",
        get_test_connection
    )

    with TestClient(app) as test_client:
        yield test_client