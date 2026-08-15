from fastapi import APIRouter, HTTPException
# from app.schemas import ()


router = APIRouter(prefix="/dashboard", tags=["Dashboard"])




# GET /dashboard

# This should return the main summary the dashboard needs at once.

# For example:

# Current balance
# Total income
# Total expenses
# Number of transactions
# Maybe savings/progress toward goals

# Think of it as the overview.

# GET /dashboard/recent-transactions

# This should return the most recent transactions, probably limited to something like the last 5–10.

# For each transaction, you might return:

# Transaction ID
# Amount
# Type (income/expense)
# Description
# Category
# Date

# You don't want this endpoint returning thousands of transactions. That's what a dedicated transactions endpoint would be for.

# GET /dashboard/statistics

# This should return calculated financial information, rather than individual transactions.

# For example:

# Income vs. expenses
# Expenses by category
# Monthly income
# Monthly expenses
# Spending trends
# Savings rate

# This is the data your frontend could use to create charts.