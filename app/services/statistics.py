from app.database.connection import get_connection


def get_spending_by_category(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                c.name AS category_name,
                SUM(t.amount) AS total_spent
            FROM transactions t
            LEFT JOIN categories c
                ON t.category_id = c.id
            WHERE t.user_id = ?
            AND t.transaction_type = 'expense'
            GROUP BY c.name
            ORDER BY total_spent DESC
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


def get_monthly_spending(user_id, year, month):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                SUM(amount) AS total_spent
            FROM transactions
            WHERE user_id = ?
            AND transaction_type = 'expense'
            AND strftime('%Y', created_at) = ?
            AND strftime('%m', created_at) = ?
        """, (user_id, str(year), f"{month:02d}"))

        return cursor.fetchone()

    finally:
        connection.close()


def get_monthly_spending_by_category(user_id, year, month):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                c.name AS category_name,
                SUM(t.amount) AS total_spent
            FROM transactions t
            LEFT JOIN categories c
                ON t.category_id = c.id
            WHERE t.user_id = ?
            AND t.transaction_type = 'expense'
            AND strftime('%Y', t.created_at) = ?
            AND strftime('%m', t.created_at) = ?
            GROUP BY c.name
            ORDER BY total_spent DESC
        """, (user_id, str(year), f"{month:02d}"))

        return cursor.fetchall()

    finally:
        connection.close()