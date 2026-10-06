# 💰 Financial Management System — Backend Function Roadmap

A checklist of the main functions and responsibilities for each part of the financial management system.

---

# 🔐 Auth

* [x] **Register user** — Create a new user account and securely store their password.
* [x] **Login user** — Verify credentials and authenticate the user.
* [x] **Create access token** — Generate a JWT for an authenticated user.
* [x] **Decode / verify token** — Validate a JWT and retrieve the user's identity.
* [x] **Get current user** — Retrieve the authenticated user from the token.
* [x] **Change password** — Verify the current password and replace it with a new one.
* [ ] **Refresh token** — Generate a new access token when the existing one expires. *(Later)*

---

# 🏷️ Categories

* [x] **Create category** — Create a category belonging to a specific user.
* [x] **Get categories** — Retrieve all categories belonging to the current user.
* [x] **Get single category** — Retrieve one category belonging to the current user.
* [x] **Update category** — Change a category's information.
* [x] **Delete category** — Remove a category belonging to the current user.
* [x] **Check category ownership** — Verify that a category belongs to the authenticated user.

---

# 📊 Charts

These are mostly data and calculation functions rather than database CRUD operations.

* [ ] **Get spending by category** — Calculate how much the user spent in each category.
* [ ] **Get income vs expenses** — Calculate income and expenses for comparison.
* [ ] **Get monthly spending** — Calculate expenses for each month.
* [ ] **Get monthly income** — Calculate income for each month.
* [ ] **Get balance evolution** — Calculate how the user's balance changes over time.

---

# 📋 Dashboard

The dashboard should aggregate information from other services instead of duplicating database logic.

* [ ] **Get dashboard summary** — Retrieve the main financial metrics for the dashboard.
* [ ] **Get current balance** — Calculate the user's current balance.
* [ ] **Get total income** — Calculate total income for a specified period.
* [ ] **Get total expenses** — Calculate total expenses for a specified period.
* [ ] **Get savings** — Calculate the difference between income and expenses.
* [ ] **Get recent transactions** — Retrieve the user's latest financial movements.
* [ ] **Get active goals** — Retrieve the user's current goals and progress.

> **Tip:** Dashboard functions should usually reuse functions from other services instead of duplicating database queries.

---

# 💸 Expenses

You don't necessarily need a completely separate database system for expenses because the `transactions` table can store both income and expense records.

* [ ] **Create expense** — Create an expense transaction.
* [ ] **Get expenses** — Retrieve the user's expenses.
* [ ] **Get single expense** — Retrieve one expense.
* [ ] **Update expense** — Modify an existing expense.
* [ ] **Delete expense** — Delete an expense.
* [ ] **Get expenses by period** — Retrieve expenses within a specific date range.
* [ ] **Get expenses by category** — Retrieve expenses belonging to a specific category.

---

# 🎯 Goals

* [ ] **Create goal** — Create a financial goal for the user.
* [ ] **Get goals** — Retrieve the user's goals.
* [ ] **Get single goal** — Retrieve one goal.
* [ ] **Update goal** — Modify a goal's information.
* [ ] **Delete goal** — Remove a goal.
* [ ] **Add money to goal** — Increase the current amount saved toward a goal.
* [ ] **Calculate goal progress** — Calculate how close the user is to reaching a goal.
* [ ] **Get completed goals** — Retrieve goals that have reached their target.
* [ ] **Get active goals** — Retrieve goals that haven't been completed.

---

# 💰 Income

Income can use the same `transactions` table as expenses.

* [ ] **Create income** — Create an income transaction.
* [ ] **Get income** — Retrieve the user's income transactions.
* [ ] **Get single income** — Retrieve one income transaction.
* [ ] **Update income** — Modify an existing income transaction.
* [ ] **Delete income** — Delete an income transaction.
* [ ] **Get income by period** — Retrieve income within a specific date range.
* [ ] **Get income by category** — Retrieve income grouped or filtered by category.

---

# 👤 Profile

* [ ] **Get profile** — Retrieve the authenticated user's profile information.
* [ ] **Update profile** — Update editable user information such as email.
* [ ] **Change password** — Change the user's password. *(Could live entirely under Auth instead.)*
* [ ] **Delete account** — Permanently delete the user's account and associated data.

---

# 📈 Statistics

This section contains more analytical queries.

* [ ] **Get total transactions** — Count the user's transactions.
* [ ] **Get total income** — Calculate total income.
* [ ] **Get total expenses** — Calculate total expenses.
* [ ] **Get average expense** — Calculate the user's average expense.
* [ ] **Get average income** — Calculate the user's average income.
* [ ] **Get largest expense** — Find the user's largest expense.
* [ ] **Get largest income** — Find the user's largest income.
* [ ] **Get spending by category** — Calculate spending distribution across categories.
* [ ] **Get monthly statistics** — Calculate financial metrics per month.
* [ ] **Get financial summary** — Combine important financial statistics into one response.

---

# 💳 Transactions

This should be the **central financial CRUD**.

* [x] **Create transaction** — Create an income or expense transaction.
* [x] **Get transactions** — Retrieve the user's transactions.
* [x] **Get single transaction** — Retrieve one transaction.
* [x] **Update transaction** — Modify an existing transaction.
* [x] **Delete transaction** — Delete a transaction.
* [ ] **Get transactions by type** — Retrieve only income or only expenses.
* [ ] **Get transactions by category** — Retrieve transactions for a specific category.
* [ ] **Get transactions by date range** — Retrieve transactions between two dates.
* [ ] **Get recent transactions** — Retrieve the newest transactions.
* [ ] **Get paginated transactions** — Retrieve transactions in pages.
* [ ] **Check transaction ownership** — Verify that a transaction belongs to the authenticated user.

> Your `get_single_transaction()` function belongs here.

---

# 👥 Users

Most of these functions are usually admin-oriented in a real application.

* [ ] **Create user** — Create a user account.
* [ ] **Get user** — Retrieve a user's information.
* [ ] **Get user by email** — Find a user using their email.
* [ ] **Get user by ID** — Find a user using their ID.
* [ ] **Update user** — Update user information.
* [ ] **Delete user** — Delete a user.
* [ ] **Check email availability** — Check whether an email is already registered.

> You probably don't need a public `get_users()` endpoint for a personal finance application.

---

# 🏦 Accounts

Since you currently have something like:

```text
transactions.account
```

as a text field, you could eventually turn accounts into their own entity.

* [ ] **Create account** — Create a financial account such as checking, savings, cash, or credit card.
* [ ] **Get accounts** — Retrieve the user's accounts.
* [ ] **Get single account** — Retrieve one account.
* [ ] **Update account** — Modify account information.
* [ ] **Delete account** — Remove an account.
* [ ] **Get account balance** — Calculate the balance of a specific account.
* [ ] **Get account transactions** — Retrieve transactions belonging to an account.

---

# 🔧 Utilities / Validation

Small reusable functions that can make the project cleaner.

* [ ] **Check user ownership** — Verify that a resource belongs to the authenticated user.
* [ ] **Validate date range** — Ensure a requested date range is valid.
* [ ] **Validate transaction type** — Ensure the transaction is either income or expense.
* [ ] **Validate category ownership** — Ensure the selected category belongs to the current user.
* [ ] **Validate goal ownership** — Ensure a goal belongs to the current user.
* [ ] **Validate account ownership** — Ensure an account belongs to the current user.

---

# 🚀 Recommended Priority

Don't implement every function immediately.

For the current stage of the project, focus on the core functionality first.

## 🔐 AUTH

* [x] Register user
* [x] Login user
* [x] Get current user
* [x] Change password

## 🏷️ CATEGORIES

* [x] Create category
* [x] Get categories
* [x] Get single category
* [x] Update category
* [x] Delete category

## 💳 TRANSACTIONS

* [x] Create transaction
* [x] Get transactions
* [x] Get single transaction
* [x] Update transaction
* [x] Delete transaction
* [ ] Filter transactions
* [ ] Pagination

## 🎯 GOALS

* [ ] Create goal
* [ ] Get goals
* [ ] Update goal
* [ ] Delete goal
* [ ] Add money to goal

## 📋 DASHBOARD

* [ ] Get balance
* [ ] Get total income
* [ ] Get total expenses
* [ ] Get recent transactions

## 📈 STATISTICS / CHARTS

* [ ] Get spending by category
* [ ] Get monthly income
* [ ] Get monthly expenses
* [ ] Get income vs expenses

## 👤 PROFILE

* [ ] Get profile
* [ ] Update profile



