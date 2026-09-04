from app.database.connection import get_connection
from datetime import datetime


def create_transaction(
    user_id,
    amount,
    transaction_type,
    description,
    category_id,
    account
):
    
    connection = get_connection()

    try:
        cursor = connection.cursor()

        created_at = datetime.now().isoformat()

        cursor.execute(
            """
            INSERT INTO transactions (
                user_id,
                amount,
                transaction_type,
                description,
                created_at,
                category_id,
                account
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                amount,
                transaction_type.value,
                description,
                created_at,
                category_id,
                account
            )
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


def list_transactions(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM transactions
            WHERE user_id = ?
            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


def calculate_balance(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                COALESCE(
                    SUM(
                        CASE
                            WHEN transaction_type = 'income'
                                THEN amount

                            WHEN transaction_type = 'expense'
                                THEN -amount

                            ELSE 0
                        END
                    ),
                    0
                ) AS balance
            FROM transactions
            WHERE user_id = ?
            """,
            (user_id,)
        )

        result = cursor.fetchone()

        return result["balance"]

    finally:
        connection.close()


def get_single_transaction(user_id, transaction_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM transactions
            WHERE user_id = ?
            AND id = ?
        """, (user_id, transaction_id))

        return cursor.fetchone()

    finally:
        connection.close()


def update_transaction(
    user_id,
    transaction_id,
    amount,
    transaction_type,
    description,
    category_id,
    account
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE transactions
            SET
                amount = ?,
                transaction_type = ?,
                description = ?,
                category_id = ?,
                account = ?
            WHERE user_id = ?
            AND id = ?
        """, (
            amount,
            transaction_type.value,
            description,
            category_id,
            account,
            user_id,
            transaction_id
        ))

        connection.commit()

        cursor.execute("""
            SELECT *
            FROM transactions
            WHERE user_id = ?
            AND id = ?
        """, (user_id, transaction_id))

        return cursor.fetchone()

    finally:
        connection.close()


def delete_transaction(user_id, transaction_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM transactions
            WHERE user_id = ?
            AND id = ?
        """, (user_id, transaction_id))

        connection.commit()

    finally:
        connection.close()




def get_transaction_by_type(user_id, transaction_type):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM transactions
            WHERE user_id = ?
            AND transaction_type = ?
        """, (user_id, transaction_type))

        result = cursor.fetchall()

        return result

    finally:
        connection.close()


def get_transaction_by_category(user_id, transaction_type):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM 
            JOIN transaction
        """, (user_id, transaction_type))

        result = cursor.fetchall()

        return result

    finally:
        connection.close()