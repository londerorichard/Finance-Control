from database.connection import get_connection
from datetime import datetime


def create_transaction(
    user_id,
    amount,
    transaction_type,
    description,
    created_at,
    category_id,
    account
):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        created_at = datetime.now()

        cursor.execute(
            """
            INSERT INTO transactions 
            (
                user_id,
                amount,
                type,
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
                transaction_type,
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


def list_transactions():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM transactions")

        return cursor.fetchall()

    finally:
        connection.close()


def calculate_balance(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
        SELECT * FROM transactions
        WHERE user_id = ?
        """,(user_id,))

        transactions = cursor.fetchall()

        balance = 0

        for transaction in transactions:

            if transaction["type"] == "income":
                balance += transaction["amount"]

            elif transaction["type"] == "expense":
                balance -= transaction["amount"]

        return balance

    finally:
        connection.close()
