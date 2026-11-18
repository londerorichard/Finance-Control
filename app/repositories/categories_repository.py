from app.database.connection import get_connection

def create_category(name, user_id):
    
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO categories (
                name,
                user_id
            )
            VALUES (?, ?)
        """, (name, user_id))

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


def update_category(category):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE categories
            SET name = ?
            WHERE id = ?
        """, (category.name, category.id))

        connection.commit()

    finally:
        connection.close()


def delete_category(category_id):

    connection = get_connection()
    
    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM categories
            WHERE id = ?
        """, (category_id,))

        connection.commit()

    finally:
        connection.close()


def list_categories(user_id, page=1, limit=20):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        offset = (page - 1) * limit

        cursor.execute(
            """
            SELECT *
            FROM categories
            WHERE user_id = ?
            ORDER BY name
            LIMIT ?
            OFFSET ?
            """,
            (user_id, limit, offset)
        )

        return cursor.fetchall()

    finally:
        connection.close()


def get_category_by_id(category_id):
    
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM categories
            WHERE id = ?
        """, (category_id,))

        category = cursor.fetchone()

        return category

    finally:
        connection.close()


def get_category_by_name(category_name):
    
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM categories
            WHERE name = ?
        """, (category_name,))

        category = cursor.fetchone()

        return category

    finally:
        connection.close()


def get_category_for_user(category_id, user_id):
    
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM categories
            WHERE id = ?
            AND user_id = ?
        """, (category_id, user_id))

        category = cursor.fetchone()

        return category

    finally:
        connection.close()


def get_categories_above_amount(user_id, amount):
    
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            WITH category_amount AS (
                SELECT
                    c.id AS category_id,
                    COALESCE(c.name, 'Uncategorized') AS category_name,
                    SUM(t.amount) AS total_expenses
                FROM transactions t
                LEFT JOIN categories c
                    ON c.id = t.category_id
                    AND c.user_id = t.user_id
                WHERE t.user_id = ?
                    AND t.transaction_type = 'expense'
                GROUP BY c.id, c.name
            )
            
            SELECT
                category_id,
                category_name,
                total_expenses
            FROM category_amount
            WHERE total_expenses >= ?
            ORDER BY total_expenses DESC
        """, (user_id, amount))

        result = cursor.fetchall()

        return result

    finally:
        connection.close()


def get_category_spending_overtime(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                strftime('%Y-%m', t.created_at) AS month,
                COALESCE(c.name, 'Uncategorized') AS category_name,
                SUM(t.amount) AS monthly_amount
            FROM transactions t
            LEFT JOIN categories c
                ON c.id = t.category_id
                AND c.user_id = t.user_id
            WHERE t.user_id = ?
                AND t.transaction_type = 'expense'
            GROUP BY
                month,
                c.id,
                c.name
            ORDER BY
                month DESC,
                monthly_amount DESC
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()
