from app.database.connection import get_connection

# def ():

#     connection = get_connection()

#     try:
#         cursor = connection.cursor()

#         cursor.execute("""

#         """)


#         return cursor.fetchall()

#     finally:
#         connection.close()


def get_users(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
        SELECT
            u.email,
            c.name AS category_name
        FROM users u
        LEFT JOIN categories c
            ON c.user
        WHERE c.user.id = u.id
        """, (user_id))


        return cursor.fetchall()

    finally:
        connection.close()


def get_user_transactions(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                u.email,
                c.name AS category_name,
                t.amount
            FROM users u
            LEFT JOIN categories c
                ON c.user_id = u.id
            LEFT JOIN transactions t
                ON t.category_id = c.id
            WHERE u.id = ?
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


def get_all_categories(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                c.name AS category_name,
                COUNT(t.id) AS transaction_count
            FROM categories c
            LEFT JOIN transactions t
                ON t.category_id = c.id
            WHERE c.user_id = ?
            GROUP BY c.id, c.name
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


def get_category_spent(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                c.name AS category_name,
                SUM(t.amount) AS total_spent
            FROM categories c
            LEFT JOIN transactions t
                ON c.id = t.category_id
            WHERE c.user_id = ?
            GROUP BY c.id, c.name
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


def get_user_transaction_amount(user_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                u.email,
                SUM(t.amount) AS total_amount
            FROM users u
            LEFT JOIN transactions t
                ON u.id = t.user_id
            WHERE u.id = ?
            GROUP BY u.id, u.email
        """, (user_id,))

        return cursor.fetchone()

    finally:
        connection.close()




# 1. Users with transactions

# Return:

# email | transaction_id | amount

# Only return users who actually have transactions.

# Use:

# INNER JOIN

def get_user_transaction(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                u.email,
                t.id AS transaction_id,
                t.amount
            FROM users u
            JOIN transactions t
                ON u.id = t.user_id
            WHERE u.id = ?
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


# 2. Categories with transactions

# Return:

# category_name | transaction_id | amount

# Only categories that have at least one transaction should appear.

# Use:

# categories
#     ↓ INNER JOIN
# transactions

def get_category_transactions(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                c.name AS category_name,
                t.id AS transaction_id,
                t.amount
            FROM categories c
            JOIN transactions t
                ON c.id = t.category_id
            WHERE c.user_id = ?
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


# 3. Users and their goals

# Return:

# email | goal_name | target_amount

# Only users who have at least one goal should appear.

# Use:

# users
#     ↓ INNER JOIN
# goals

def get_users_goals(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                u.email,
                g.goal_name,
                g.target_amount
            FROM users u
            JOIN goals g
                ON u.id = g.user_id
        """, (user_id,))

        return cursor.fetchall()

    finally:
        connection.close()


# 4. Users + categories + transactions

# Return:

# email | category_name | amount

# Only return transactions that have a category.

# Use:

# users
#     ↓
# categories
#     ↓
# transactions

# with INNER JOIN for both relationships.

def get_users_categories_transactions():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                u.email,
                c.name AS category_name,
                t.amount
            FROM users u
            JOIN categories c
                ON u.id = c.user_id
            JOIN transactions t
                ON c.id = t.category_id
        """)

        return cursor.fetchall()

    finally:
        connection.close()


# 5. All transactions, even if the user doesn't exist

# Return:

# transaction_id | email | amount

# Start with users, but use:

# RIGHT JOIN

# so that every transaction is preserved.

# Think about:

# users
#    RIGHT JOIN
# transactions

# Ask yourself:

# Which table am I trying to preserve?

def get_users_categories_transactions():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                t.id AS transaction_id,
                u.email,
                t.amount
            FROM users u
            RIGHT JOIN transactions t
                ON u.id = t.user_id
        """)

        return cursor.fetchall()

    finally:
        connection.close()


# 6. All transactions and their categories

# Return:

# transaction_id | category_name | amount

# Make sure transactions without a category still appear.

# Try solving it using:

# categories
#     RIGHT JOIN
# transactions

def get_users_categories_transactions():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                t.id AS transaction_id,
                c.name AS category_name,
                t.amount
            FROM categories c
            RIGHT JOIN transactions t
                ON c.id = t.category_id
        """)

        return cursor.fetchall()

    finally:
        connection.close()


# 7. Users and transactions

# Return:

# email | transaction_id | amount

# Show:

# users with transactions
# users without transactions
# transactions without a matching user

# Use:

# FULL OUTER JOIN

def get_users_categories_transactions():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                u.email,
                t.id,
                t.amount
            FROM users u
            FULL OUTER JOIN transactions t
                ON u.id = t.user_id
        """)

        return cursor.fetchall()

    finally:
        connection.close()


# 8. Categories and transactions

# Return:

# category_name | transaction_id | amount

# Include:

# categories with transactions
# categories without transactions
# transactions without a category

# Use:

# FULL OUTER JOIN

# This one is particularly useful because your transactions.category_id can be NULL.

def get_users_categories_transactions():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                c.name,
                t.id,
                t.amount
            FROM categories c
            FULL OUTER JOIN transactions t
                ON c.id = t.category_id
        """)

        return cursor.fetchall()

    finally:
        connection.close()

