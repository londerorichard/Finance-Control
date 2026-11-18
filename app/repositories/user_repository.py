from app.database.connection import get_connection
from datetime import datetime
from app.schemas import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserResponse,
    PasswordChange,
)

def email_exists(email: str) -> bool:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 1
            FROM users
            WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        return user is not None

    finally:
        connection.close()

    
def get_user_by_email(email: str) -> dict | None:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM users
            WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        return user

    finally:
        connection.close()


def create_user(email: str, password_hash: str) -> UserResponse:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO users (
                email,
                password_hash,
                created_at
            )
            VALUES (?, ?, ?)
            RETURNING id, email
        """, (
            email,
            password_hash,
            datetime.now().isoformat()
        ))

        user = cursor.fetchone()
        connection.commit()

        return UserResponse(
            id=user["id"],
            email=user["email"]
        )

    finally:
        connection.close()
    

# def update_user(...):
#     ...

# def delete_user(...):
#     ...


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


def get_user_by_google_id(google_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM users
            WHERE google_id = ?
        """, (google_id,))

        return cursor.fetchone()

    finally:
        connection.close()


def create_google_user(email, google_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        created_at = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO users (email, google_id, created_at)
            VALUES (?, ?, ?)
            RETURNING id, email, google_id, created_at
        """, (email, google_id, created_at))

        user = cursor.fetchone()
        connection.commit()

        return user

    finally:
        connection.close()


def get_user_by_id(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
        SELECT * FROM users
        WHERE id = ?
        """, (user_id,))

        user = cursor.fetchone()

        return user

    finally:
        connection.close()


def update_user_profile(user_id, email):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE users
            SET email = ?
            WHERE id = ?
        """, (email, user_id))

        connection.commit()

        cursor.execute("""
            SELECT *
            FROM users
            WHERE id = ?
        """, (user_id,))

        user = cursor.fetchone()

        return user

    finally:
        connection.close()
    

def delete_user_account(user_id):

    connection = get_connection()
    
    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM users
            WHERE id = ?
        """, (user_id,))

        connection.commit()

    finally:
        connection.close()












    