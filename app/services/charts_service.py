from app.database.connection import get_connection


def income_vs_expense_chart(user_id):
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
            
        """, (user_id,))

        result = cursor.fetchall()

        return result

    finally:
        connection.close()




# 2. /charts/category-expenses

# Purpose: Show which categories consume the most money.

# For example:

# Food: R$ 800
# Transportation: R$ 300
# Entertainment: R$ 200

# You could display this information as a bar chart or pie chart.

# SQL concepts you'll practice:

# SUM()
# GROUP BY
# LEFT JOIN or INNER JOIN, depending on how you want to handle uncategorized transactions.
# ORDER BY

# I'd recommend sorting the results by total expenses in descending order so the largest spending categories appear first.

# 3. /charts/monthly-balance

# Purpose: Show whether the user's financial position is improving or deteriorating over time.

# The monthly balance is:

# Monthly balance = Monthly income − Monthly expenses

# For example:

# Month	Income	Expenses	Balance
# January	R$ 3,000	R$ 2,400	R$ 600
# February	R$ 3,200	R$ 2,700	R$ 500
# March	R$ 3,500	R$ 2,300	R$ 1,200

# A line chart would work well for visualizing the balance over time.

# SQL concepts you'll practice:

# SUM()
# CASE WHEN
# GROUP BY
# Date functions.
# Combining calculated values.

# Important distinction: Monthly balance is not the same as the user's total account balance. A monthly balance represents the difference between income and expenses during that month.

# 4. /charts/savings

# Purpose: Show how the user's savings change over time.

# This endpoint needs a little more thought because savings can mean different things.

# For example, you could define savings as:

# Monthly savings: income minus expenses for each month.
# Cumulative savings: the running total of monthly surpluses and deficits.
# Goal progress: how much the user has saved toward specific financial goals.

# These are different metrics.

# If you define savings as income minus expenses, this endpoint could overlap significantly with your monthly-balance endpoint.

# If you want to track actual savings goals, your existing goals table could support goal-progress statistics instead.

# My recommendation: Don't implement this endpoint until you've decided what the chart should represent.

# 2. Should these be separate endpoints?

# Yes, they can be. Each endpoint provides a different dataset for a particular chart.

# However, there's an architectural detail worth understanding.

# Suppose both /charts/income-vs-expenses and /charts/monthly-balance need monthly income and expenses.

# You don't necessarily need to write two completely independent, duplicated SQL queries.

# You could organize your database logic so that the monthly aggregation is reusable, with each endpoint returning the specific data it needs.

# This is a good opportunity to apply what you've learned about CTEs, query organization, and reusable database functions.

# Just avoid introducing unnecessary abstraction before you need it.