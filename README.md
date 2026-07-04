# 💰 Financial Management System

A web application for personal financial management, developed to strengthen **Full Stack** development skills using **Python, FastAPI, SQLite, HTML, CSS, and JavaScript**.

The project simulates a real-world application, allowing users to manage income, expenses, categories, and financial goals, as well as generate reports and charts.

---

## 📖 About the Project

This project was designed as a complete learning application, covering everything from building a REST API to developing the web interface and integrating it with a database.

Throughout the development process, the following concepts will be practiced:

* Project architecture
* Code organization
* Full CRUD operations
* REST APIs
* Relational databases
* Authentication
* API consumption
* DOM manipulation
* Responsive design
* Deployment

---

# 🚀 Technologies

## Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

## Frontend

* HTML5
* CSS3
* JavaScript

## Tools

* Git
* GitHub
* Uvicorn
* Swagger
* Postman
* VS Code

---

# 📁 Project Structure

```text
finance-control/
│
├── app/
│   ├── main.py              # Application entry point
│   ├── database.py          # Database connection
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   ├── auth.py              # Authentication logic
│   ├── dependencies.py      # FastAPI dependencies
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── categories.py
│   │   ├── incomes.py
│   │   ├── expenses.py
│   │   ├── goals.py
│   │   └── reports.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── incomes.html
│   │   ├── expenses.html
│   │   ├── categories.html
│   │   ├── goals.html
│   │   └── reports.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── variables.css
│   │   │
│   │   ├── js/
│   │   │   ├── api.js
│   │   │   ├── dashboard.js
│   │   │   ├── forms.js
│   │   │   └── utils.js
│   │   │
│   │   └── images/
│   │
│   └── utils/
│       ├── validators.py
│       ├── helpers.py
│       └── constants.py
│
├── database/
│   └── finance.db
│
├── tests/
│   ├── test_auth.py
│   ├── test_categories.py
│   ├── test_incomes.py
│   ├── test_expenses.py
│   └── test_reports.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── ROADMAP.md
└── LICENSE
```

---

# ✨ Features

## 👤 Authentication

Handles user authentication and account management.

### Features

* User registration
* Login
* Logout
* Password hashing
* Route protection

### Concepts Practiced

* Password hashing
* JWT
* FastAPI dependencies
* Authentication

---

## 📊 Dashboard

Home page displaying a financial overview.

### Displayed Information

* Current balance
* Total income
* Total expenses
* Monthly savings
* Recent transactions
* Financial goals
* Charts

### Concepts Practiced

* SQL queries
* Aggregations
* User interface organization

---

## 💵 Income

Manage financial income records.

### Operations

* Create income
* Edit income
* Delete income
* List income

### Fields

* Description
* Amount
* Category
* Date
* Notes

### Concepts Practiced

* CRUD operations
* Validation
* Forms

---

## 💳 Expenses

Manage financial expense records.

### Operations

* Create expense
* Edit expense
* Delete expense
* List expenses

### Fields

* Description
* Amount
* Category
* Payment method
* Date
* Notes

### Extras

* Installment payments
* Recurring expenses

---

## 🏷 Categories

Organize income and expenses into categories.

### Features

* Create category
* Edit category
* Delete category

### Examples

* Food
* Transportation
* Healthcare
* Education
* Housing
* Investments
* Entertainment

### Concepts Practiced

* Relationships
* Foreign Keys

---

## 🎯 Financial Goals

Track personal financial goals.

### Features

* Create goal
* Update progress
* Delete goal

### Information

* Name
* Target amount
* Current amount
* Completion percentage
* Deadline

---

## 📈 Reports

Generate customized financial reports.

### Filters

* Today
* This week
* This month
* This year
* Custom date range

### Available Reports

* Income
* Expenses
* Balance
* Expenses by category

### Concepts Practiced

* Queries
* Filters
* Statistics

---

## 🔍 Search

Search financial transactions by:

* Name
* Category
* Date
* Amount

---

## ↕ Sorting

Sort records by:

* Date
* Amount
* Category
* Most recent
* Highest amount
* Lowest amount


---

## 📄 Pagination

Automatic pagination for large amounts of records.

### Concepts Practiced

* LIMIT
* OFFSET

---

## 👤 Profile

Allows users to manage their personal information.

### Features

* Change name
* Change email
* Change password

---

## ⚙ Settings

Application preferences.

### Features

* Light theme
* Dark theme
* Currency settings

---

## 📤 Export

Export financial transactions.

### Formats

* CSV

### Optional

* PDF

---

## 📊 Charts

Visual representation of financial data.

### Examples

* Expenses by category
* Income vs. Expenses
* Monthly trends
* Monthly savings

---

# 🗄 Database

## users

| Field    | Type    |
| -------- | ------- |
| id       | INTEGER |
| name     | TEXT    |
| email    | TEXT    |
| password | TEXT    |

---

## categories

| Field | Type    |
| ----- | ------- |
| id    | INTEGER |
| name  | TEXT    |

---

## incomes

| Field       | Type    |
| ----------- | ------- |
| id          | INTEGER |
| description | TEXT    |
| value       | REAL    |
| date        | DATE    |
| category_id | INTEGER |
| user_id     | INTEGER |

---

## expenses

| Field       | Type    |
| ----------- | ------- |
| id          | INTEGER |
| description | TEXT    |
| value       | REAL    |
| date        | DATE    |
| category_id | INTEGER |
| user_id     | INTEGER |

---

## goals

| Field         | Type    |
| ------------- | ------- |
| id            | INTEGER |
| name          | TEXT    |
| target_value  | REAL    |
| current_value | REAL    |
| user_id       | INTEGER |

---

# 🌐 API

## Authentication

| Method | Endpoint  |
| ------ | --------- |
| POST   | /register |
| POST   | /login    |
| GET    | /me       |

---

## Income

| Method | Endpoint      |
| ------ | ------------- |
| GET    | /incomes      |
| GET    | /incomes/{id} |
| POST   | /incomes      |
| PUT    | /incomes/{id} |
| DELETE | /incomes/{id} |

---

## Expenses

| Method | Endpoint       |
| ------ | -------------- |
| GET    | /expenses      |
| GET    | /expenses/{id} |
| POST   | /expenses      |
| PUT    | /expenses/{id} |
| DELETE | /expenses/{id} |

---

## Categories

| Method | Endpoint         |
| ------ | ---------------- |
| GET    | /categories      |
| POST   | /categories      |
| PUT    | /categories/{id} |
| DELETE | /categories/{id} |

---

## Financial Goals

| Method | Endpoint    |
| ------ | ----------- |
| GET    | /goals      |
| POST   | /goals      |
| PUT    | /goals/{id} |
| DELETE | /goals/{id} |

---

## Reports

| Method | Endpoint          |
| ------ | ----------------- |
| GET    | /reports/month    |
| GET    | /reports/year     |
| GET    | /reports/category |

---

# 📚 Concepts Practiced

### Python

* Project organization
* Functions
* Classes
* Type hints
* Exception handling

### FastAPI

* Routes
* Path Parameters
* Query Parameters
* Depends
* Pydantic
* Response Models
* Status Codes
* Middleware
* Authentication

### Database

* SQLite
* SQLAlchemy
* CRUD operations
* Relationships
* SQL queries
* Pagination
* Sorting
* Filtering

### HTML

* Semantic structure
* Forms
* Templates

### CSS

* Flexbox
* Grid
* Responsive design
* CSS variables

### JavaScript

* DOM
* Events
* Fetch API
* Async/Await
* Dynamic UI manipulation

---

# 🚧 Future Improvements

* Password recovery
* Profile picture upload
* Notifications
* Credit card management
* Multiple accounts
* Bank statement import
* More advanced dashboard
* Docker
* Automated testing
* Production deployment