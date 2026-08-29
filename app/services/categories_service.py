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


def list_categories():

    connection = get_connection()

    try: 
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM categories")

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