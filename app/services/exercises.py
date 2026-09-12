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
# 2. Categories with transactions

# Return:

# category_name | transaction_id | amount

# Only categories that have at least one transaction should appear.

# Use:

# categories
#     ↓ INNER JOIN
# transactions
# 3. Users and their goals

# Return:

# email | goal_name | target_amount

# Only users who have at least one goal should appear.

# Use:

# users
#     ↓ INNER JOIN
# goals
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

# RIGHT JOIN exercises

# These are mainly to understand the direction of a JOIN.

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

# 6. All transactions and their categories

# Return:

# transaction_id | category_name | amount

# Make sure transactions without a category still appear.

# Try solving it using:

# categories
#     RIGHT JOIN
# transactions

# This is basically a good exercise for understanding how RIGHT JOIN can be equivalent to changing the order of the tables and using LEFT JOIN.

# FULL OUTER JOIN exercises

# These are particularly useful for understanding the difference between LEFT, RIGHT, and FULL.

# 7. Users and transactions

# Return:

# email | transaction_id | amount

# Show:

# users with transactions
# users without transactions
# transactions without a matching user

# Use:

# FULL OUTER JOIN

# This is the easiest way to see what FULL OUTER JOIN actually does.

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

# 9. Users and goals

# Return:

# email | goal_name | target_amount

# Include:

# users with goals
# users without goals
# goals without a matching user

# Use:

# FULL OUTER JOIN
# JOIN comparison exercises

# These are probably the most valuable exercises after you've learned all the types.

# 10. Compare INNER vs LEFT

# Write two queries using users and transactions.

# Query A:

# INNER JOIN

# Query B:

# LEFT JOIN

# Return:

# email | transaction_id

# Then compare the results.

# Ask:

# Which users disappeared with INNER JOIN?

# 11. Compare LEFT vs RIGHT

# Write:

# users
# LEFT JOIN transactions

# Then:

# transactions
# RIGHT JOIN users

# Try to make both queries produce the same result.

# This teaches you that:

# A LEFT JOIN B

# is conceptually equivalent to:

# B RIGHT JOIN A
# 12. FULL JOIN vs LEFT JOIN

# First:

# users
# LEFT JOIN transactions

# Then:

# users
# FULL OUTER JOIN transactions

# Compare the results.

# Ask:

# What additional rows can FULL OUTER JOIN return that LEFT JOIN cannot?

# Recommended order

# I'd practice them like this:

# 1 → 2 → 3 → 4
#         ↓
# 5 → 6
#         ↓
# 7 → 8 → 9
#         ↓
# 10 → 11 → 12

# The key concept you should get from these isn't memorizing syntax. It's understanding which table's rows you want to preserve:

# INNER JOIN
# → only matching rows

# LEFT JOIN
# → everything from the left table

# RIGHT JOIN
# → everything from the right table

# FULL OUTER JOIN
# → everything from both tables