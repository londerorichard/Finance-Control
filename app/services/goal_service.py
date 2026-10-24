from app.database.connection import get_connection


def get_goal_process(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                goal_name,
                target_amount,
                current_amount,
                deadline,
                (CAST(current_amount AS REAL) / NULLIF(target_amount, 0)) * 100
                    AS completion_percentage
            FROM goals
            WHERE user_id = ?
            ORDER BY completion_percentage DESC
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


def get_completed_goals(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                goal_name,
                target_amount,
                current_amount,
                deadline
            FROM goals
            WHERE user_id = ?
            AND current_amount >= target_amount
            ORDER BY current_amount DESC
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


def get_ongoing_goals(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                id,
                goal_name,
                target_amount,
                current_amount,
                deadline
            FROM goals
            WHERE user_id = ?
                AND current_amount < target_amount
            ORDER BY
                deadline IS NULL ASC,
                deadline DESC
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()



