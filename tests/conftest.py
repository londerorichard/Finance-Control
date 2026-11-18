import sqlite3
import pytest

from fastapi.testclient import TestClient

import app.repositories.auth_repository as auth_repository
import app.repositories.transaction_repository as transaction_repository

from app.database.connection import get_connection
from app.database.setup import create_tables

from app.main import app


@pytest.fixture
def test_db(tmp_path):
    db_path = tmp_path / "test_finance.db"

    create_tables(str(db_path))

    return str(db_path)


@pytest.fixture
def db_connection(test_db):
    connection = get_connection(test_db)

    yield connection

    connection.close()


@pytest.fixture
def test_auth_db(test_db, monkeypatch):
    def get_test_connection():
        return get_connection(test_db)

    monkeypatch.setattr(
        auth_repository,
        "get_connection",
        get_test_connection
    )


@pytest.fixture
def test_transaction_db(test_db, monkeypatch):
    def get_test_connection():
        return get_connection(test_db)

    monkeypatch.setattr(
        transaction_repository,
        "get_connection",
        get_test_connection
    )


@pytest.fixture
def client(test_db, monkeypatch):
    def get_test_connection():
        return get_connection(test_db)

    monkeypatch.setattr(
        auth_repository,
        "get_connection",
        get_test_connection
    )

    monkeypatch.setattr(
        transaction_repository,
        "get_connection",
        get_test_connection
    )

    with TestClient(app) as test_client:
        yield test_client