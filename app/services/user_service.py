from app.database.connection import get_connection
from datetime import datetime
from app.auth.security import hash_password
import sqlite3


def create_user(email, name, password):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        password_hash = hash_password(password)
        created_at = datetime.now()

        cursor.execute(
            """
            INSERT INTO users (
                email,
                name,
                password_hash,
                created_at
            )
            VALUES (?, ?, ?, ?)
            RETURNING id, email, name
            """,
            (
                email,
                name,
                password_hash,
                created_at,
            )
        )

        user = cursor.fetchone()

        connection.commit()

        return user

    except sqlite3.IntegrityError:
        return None

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


def get_user_by_email(email):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM users
            WHERE email = ?
            """, (email,))

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









    