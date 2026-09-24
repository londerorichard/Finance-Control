# Income

| Method | Endpoint        | Description             |
| ------ | --------------- | ----------------------- |
| GET    | `/incomes`      | List all income records |
| GET    | `/incomes/{id}` | Get income details      |
| POST   | `/incomes`      | Create income           |
| PUT    | `/incomes/{id}` | Update income           |
| DELETE | `/incomes/{id}` | Delete income           |

---

# Expenses

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| GET    | `/expenses`      | List all expenses   |
| GET    | `/expenses/{id}` | Get expense details |
| POST   | `/expenses`      | Create expense      |
| PUT    | `/expenses/{id}` | Update expense      |
| DELETE | `/expenses/{id}` | Delete expense      |

---

# Categories

| Method | Endpoint           | Description     |
| ------ | ------------------ | --------------- |
| GET    | `/categories`      | List categories |
| GET    | `/categories/{id}` | Get category    |
| POST   | `/categories`      | Create category |
| PUT    | `/categories/{id}` | Update category |
| DELETE | `/categories/{id}` | Delete category |

---

# Financial Goals

| Method | Endpoint      | Description          |
| ------ | ------------- | -------------------- |
| GET    | `/goals`      | List financial goals |
| GET    | `/goals/{id}` | Get goal details     |
| POST   | `/goals`      | Create goal          |
| PUT    | `/goals/{id}` | Update goal          |
| DELETE | `/goals/{id}` | Delete goal          |

---

# Reports

| Method | Endpoint              | Description                 |
| ------ | --------------------- | --------------------------- |
| GET    | `/reports/income`     | Income report               |
| GET    | `/reports/expenses`   | Expense report              |
| GET    | `/reports/balance`    | Balance report              |
| GET    | `/reports/categories` | Expenses by category        |
| GET    | `/reports/monthly`    | Monthly report              |
| GET    | `/reports/yearly`     | Yearly report               |
| GET    | `/reports/custom`     | Report by custom date range |

---

# Search

| Method | Endpoint  | Description         |
| ------ | --------- | ------------------- |
| GET    | `/search` | Search transactions |

### Supported filters

* Description
* Category
* Date
* Amount
* Transaction type

---

# Statistics

| Method | Endpoint                 | Description                  |
| ------ | ------------------------ | ---------------------------- |
| GET    | `/statistics/monthly`    | Monthly financial statistics |
| GET    | `/statistics/yearly`     | Yearly financial statistics  |
| GET    | `/statistics/categories` | Statistics by category       |
| GET    | `/statistics/goals`      | Goal progress statistics     |

---

# Charts

| Method | Endpoint                     | Description               |
| ------ | ---------------------------- | ------------------------- |
| GET    | `/charts/income-vs-expenses` | Income vs. expenses chart |
| GET    | `/charts/category-expenses`  | Expenses by category      |
| GET    | `/charts/monthly-balance`    | Monthly balance           |
| GET    | `/charts/savings`            | Savings history           |

---

# Profile

| Method | Endpoint            | Description                         |
| ------ | ------------------- | ----------------------------------- |
| GET    | `/profile`          | Get profile                         |
| PUT    | `/profile`          | Update profile                      |
| PUT    | `/profile/password` | Update password                     |
| PUT    | `/profile/avatar`   | Update profile picture *(optional)* |

---

# Settings

| Method | Endpoint    | Description          |
| ------ | ----------- | -------------------- |
| GET    | `/settings` | Get user settings    |
| PUT    | `/settings` | Update user settings |

---

# Export

| Method | Endpoint      | Description                       |
| ------ | ------------- | --------------------------------- |
| GET    | `/export/csv` | Export transactions as CSV        |
| GET    | `/export/pdf` | Export report as PDF *(optional)* |

---

# Health Check

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | `/health` | Check API status |

---

# Future Endpoints

## Notifications

| Method | Endpoint                   | Description               |
| ------ | -------------------------- | ------------------------- |
| GET    | `/notifications`           | List notifications        |
| PUT    | `/notifications/{id}/read` | Mark notification as read |

---

## Budgets

| Method | Endpoint        | Description   |
| ------ | --------------- | ------------- |
| GET    | `/budgets`      | List budgets  |
| POST   | `/budgets`      | Create budget |
| PUT    | `/budgets/{id}` | Update budget |
| DELETE | `/budgets/{id}` | Delete budget |

---

## Credit Cards

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/cards`      | List credit cards |
| POST   | `/cards`      | Add credit card   |
| PUT    | `/cards/{id}` | Update card       |
| DELETE | `/cards/{id}` | Delete card       |

---

## Bank Accounts

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| GET    | `/accounts`      | List bank accounts |
| POST   | `/accounts`      | Create account     |
| PUT    | `/accounts/{id}` | Update account     |
| DELETE | `/accounts/{id}` | Delete account     |
