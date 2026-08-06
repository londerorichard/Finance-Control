from app.database.connection import get_connection
from datetime import datetime
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(email, password):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id FROM users
            WHERE email = ?
            """,(email,))

        existing_user = cursor.fetchone()

        if existing_user:
            connection.close()
            return None

        password_hash = hash_password(password)

        created_at = datetime.now()

        cursor.execute(
            """
            INSERT INTO users (email, password_hash, created_at)
            VALUES (?, ?, ?)
            """,
            (
                email,
                password_hash,
                created_at
            )
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


def get_user_by_id(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM users
            WHERE id = ?
            """,(user_id,))

        return cursor.fetchone()

    finally:
        connection.close()


def list_users():

    connection = get_connection()
    
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")

        return cursor.fetchall()

    finally:
        connection.close()








    