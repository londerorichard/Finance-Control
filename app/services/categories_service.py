from app.database.connection import get_connection

def create_category(
    name,
    user_id
):
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


def list_categories():

    connection = get_connection()

    try: 
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM categories")

        return cursor.fetchall()

    finally:
        connection.close()