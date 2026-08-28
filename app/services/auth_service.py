from app.database.connection import get_connection
from datetime import datetime
from app.auth.security import hash_password
from app.schemas import UserResponse
from app.auth.jwt import create_access_token


def create_user(email, password):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        password_hash = hash_password(password)
        created_at = datetime.now().isoformat()

        cursor.execute(
            """
            INSERT INTO users (
                email,
                password_hash,
                created_at
            )
            VALUES (?, ?, ?)
            RETURNING id, email
            """,
            (
                email,
                password_hash,
                created_at
            )
        )

        user = cursor.fetchone()

        connection.commit()

        return UserResponse(
            id=user["id"],
            email=user["email"]
        )

    finally:
        connection.close()


def login_user(email, password):

    connetion = get_connection()
    
    try:
        cursor = connetion.cursor()

        cursor.execute(""" 
        SELECT * FROM users 
        WHERE email = ?
        """, (email))

        cursor.fetchone()

        if not email:
            print("User not found")
            return

        password_hash = hash_password(password)

        if password_hash != password:
            print("Invalid credencials")
            return

        token = create_access_token(password)

        connetion.commit()

        return token

    finally:
        connetion.close()


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