import pytest
from app.database.connection import get_connection

@pytest.fixture
def db_connection():
    connection = get_connection()

    yield connection

    connection.close()