from app.database.connection import get_connection


def get_expenses_by_months(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                strftime('%Y-%m', created_at) AS month,
                SUM(amount) AS total_expenses
            FROM transactions
            WHERE transaction_type = 'expense'
            AND user_id = ?
            GROUP BY strftime('%Y-%m', created_at)
            ORDER BY month;
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()