from app.database.connection import get_connection


def get_user_by_id(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
        SELECT * FROM users
        WHERE id = ?
        """, (user_id,))

        user = cursor.fetchone()

        return user

    finally:
        connection.close()


def update_user_profile(user_id, email):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE users
            SET email = ?
            WHERE id = ?
        """, (email, user_id))

        connection.commit()

        cursor.execute("""
            SELECT *
            FROM users
            WHERE id = ?
        """, (user_id,))

        user = cursor.fetchone()

        return user

    finally:
        connection.close()
    

def delete_user_account(user_id):

    connection = get_connection()
    
    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM users
            WHERE id = ?
        """, (user_id,))

        connection.commit()

    finally:
        connection.close()












    