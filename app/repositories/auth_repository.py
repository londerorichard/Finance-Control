from datetime import datetime
from app.database.connection import get_connection
from app.schemas import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserResponse,
    PasswordChange,
)


def email_exists(email: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 1
        FROM users
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    connection.close()

    return user is not None


def get_user_by_email(email: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    connection.close()

    return user


def insert_user(user: UserCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (
            email,
            password_hash,
            created_at
        )
        VALUES (?, ?, ?)
    """, (
        user.email,
        user.password,      # Later: hashed password
        datetime.now().isoformat()
    ))

    connection.commit()

    new_id = cursor.lastrowid

    connection.close()

    return UserResponse(
        id=new_id,
        email=user.email
    )
    

# def update_user(...):
#     ...

# def delete_user(...):
#     ...