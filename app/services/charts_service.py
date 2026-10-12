from app.database.connection import get_connection


def income_expense_chart(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                strftime('%Y-%m', created_at) AS month,
                SUM(
                    CASE
                        WHEN transaction_type = 'income' THEN amount
                        ELSE 0
                    END
                ) AS total_income,
                SUM(
                    CASE
                        WHEN transaction_type = 'expense' THEN amount
                        ELSE 0
                    END
                ) AS total_expenses

            FROM transactions
            WHERE user_id = ?
            GROUP BY strftime('%Y-%m', created_at)
            ORDER BY month DESC
        """, (user_id,))

        result = cursor.fetchall()

        return result

    finally:
        connection.close()


def category_expenses_chart(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                c.name AS category_name,
                COALESCE(
                    SUM(
                        CASE
                            WHEN t.transaction_type = 'expense' THEN t.amount
                            ELSE 0
                        END
                    ),
                    0
                ) AS category_amount_total

            FROM categories c
            LEFT JOIN transactions t
                ON c.id = t.category_id
                AND t.user_id = ?
            WHERE c.user_id = ?
            GROUP BY c.id, c.name
            ORDER BY category_amount_total DESC
        """, (user_id, user_id))

        result = cursor.fetchall()

        return result

    finally:
        connection.close()


def monthly_balance_chart(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            WITH balance AS (
                SELECT 
                    strftime('%Y-%m', created_at) AS month,
                    SUM(
                        CASE
                            WHEN transaction_type = 'expense' THEN amount
                            ELSE 0
                        END
                    ) AS monthly_expense,
                    SUM(
                        CASE
                            WHEN transaction_type = 'income' THEN amount
                            ELSE 0
                        END
                    ) AS monthly_income
                FROM transactions
                WHERE user_id = ?
                GROUP BY month
            )

            SELECT 
                month,
                monthly_income,
                monthly_expense,
                monthly_income - monthly_expense AS balance
            FROM balance
            ORDER BY month DESC 
        """, (user_id,))

        result = cursor.fetchall()

        return result

    finally:
        connection.close()


# 4. /charts/savings

