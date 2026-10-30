from app.database.connection import get_connection
from datetime import datetime
from app.auth.security import hash_password, verify_password
from app.schemas import UserResponse
from fastapi import HTTPException
import sqlite3

connection = sqlite3.connect("name_file")
cursor = connection.cursor()

def create_user(email, password):
    connection = get_connection()

    try:
        with connection:
            cursor = connection.cursor()

            password_hash = hash_password(password)
            created_at = datetime.now().isoformat()

            print(f"Attempting to create user with email: {email}")

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
                (email, password_hash, created_at)
            )

            user = cursor.fetchone()

            return UserResponse(
                id=user["id"],
                email=user["email"]
            )

    finally:
        connection.close()


def login_user(email, password):

    connection = get_connection()
    
    try:
        cursor = connection.cursor()

        cursor.execute(""" 
        SELECT * FROM users 
        WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        if not user:
            raise HTTPException( 
                status_code=401, 
                detail="Invalid credentials"
                )

        password_hash = user['password_hash']

        if not verify_password(password, password_hash): 
            raise HTTPException(
                status_code=401, 
                detail="Invalid credentials" 
                )

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


def change_password(user_id, current_password, new_password):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, password_hash
            FROM users
            WHERE id = ?
        """, (user_id,))

        user = cursor.fetchone()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        stored_password_hash = user["password_hash"]

        if not verify_password(
            current_password,
            stored_password_hash
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        new_password_hash = hash_password(new_password)

        cursor.execute("""
            UPDATE users
            SET password_hash = ?
            WHERE id = ?
        """, (new_password_hash, user_id))

        connection.commit()

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
