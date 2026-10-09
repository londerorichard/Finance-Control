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


def list_transactions(user_id, page=1, limit=20):
    
    connection = get_connection()

    try:
        cursor = connection.cursor()

        offset = (page - 1) * limit

        cursor.execute(
            """
            SELECT *
            FROM transactions
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT ?
            OFFSET ?
            """,
            (user_id, limit, offset)
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
            SELECT
                t.id,
                t.amount,
                t.transaction_type,
                t.description,
                t.created_at,
                t.category_id,
                c.name AS category_name
            FROM transactions t
            LEFT JOIN categories c
                ON t.category_id = c.id
            WHERE t.user_id = ?
            AND t.id = ?
        """, (user_id, transaction_id))

        return cursor.fetchone()

    finally:
        connection.close()


def get_transaction_after_date(user_id, date):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM transactions
            WHERE created_at >= ?
            AND user_id = ?
            ORDER BY created_at ASC
        """, (date, user_id))

        result = cursor.fetchall()
        return result

    finally:
        connection.close()

        
def get_transactions_between_dates(user_id, start_date, end_date):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM transactions
            WHERE created_at >= ?
            AND created_at < ?
            AND user_id = ?
            ORDER BY created_at ASC
        """, (start_date, end_date, user_id))

        result = cursor.fetchall()
        return result

    finally:
        connection.close()

def get_recent_transactions(user_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM transactions
            WHERE created_at >= date('now', '-7 days')
            AND user_id = ?
            ORDER BY created_at DESC
        """, (user_id,))

        result = cursor.fetchall()
        return result

    finally:
        connection.close()


def get_transaction_dates(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                amount,
                created_at,
                strftime('%Y', created_at) AS year,
                strftime('%m', created_at) AS month
            FROM transactions
            WHERE user_id = ?
        """, (user_id,))

        result = cursor.fetchall()
        return result

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


