from app.database.connection import get_connection

def get_dashboard_summary(user_id):

    connection = get_connection()
    
    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                COALESCE(
                    SUM(
                        CASE
                            WHEN transaction_type = 'expense'
                            THEN amount
                            ELSE 0
                        END
                    ), 0
                ) AS total_expenses,

                COALESCE(
                    SUM(
                        CASE
                            WHEN transaction_type = 'income'
                            THEN amount
                            ELSE 0
                        END
                    ), 0
                ) AS total_income,

                COUNT(id) AS transaction_count

            FROM transactions
            WHERE user_id = ?
        """, (user_id,))

        summary = cursor.fetchone()

        return summary

    finally:
        connection.close()


def get_recent_transactions(user_id):

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
                t.account,
                COALESCE(c.name, 'Uncategorized') AS category_name
            FROM transactions AS t
            LEFT JOIN categories AS c
                ON t.category_id = c.id
            WHERE t.user_id = ?
            ORDER BY t.created_at DESC
            LIMIT 5
        """, (user_id,))

        recent_transactions = cursor.fetchall()

        return recent_transactions

    finally:
        connection.close()


def dashboard_statistics(user_id):

    connection = get_connection()
        
    try:
        cursor = connection.cursor()

        cursor.execute("""
            
        """, (user_id,))


    finally:
        connection.close()



