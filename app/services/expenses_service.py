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


def get_largest_expense_by_category(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                c.id AS category_id,
                c.name AS category_name,
                MAX(t.amount) AS largest_category_expense
            FROM categories c
            INNER JOIN transactions t
                ON c.id = t.category_id
                AND c.user_id = t.user_id
            WHERE c.user_id = ?
                AND t.transaction_type = 'expense'
            GROUP BY c.id, c.name
            ORDER BY largest_category_expense DESC
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()