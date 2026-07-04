# 🗺 Development Roadmap

This roadmap follows a realistic development flow used in many professional projects. Each milestone builds on the previous one, helping you avoid unnecessary refactoring while gradually increasing the project's complexity.

> **Rule:** Never move to the next phase until the current one is stable and tested.

---

# Phase 1 — Project Setup

## Repository

- [x] Create GitHub repository
- [x] Add `.gitignore`
- [x] Create `README.md`
- [x] Create project license (optional)

## Environment

- [x] Create virtual environment
- [x] Install dependencies
- [x] Create `requirements.txt`
- [x] Configure project structure

---

# Phase 2 — Project Architecture

## Folder Structure

- [x] Create `routers/`
- [x] Create `models.py`
- [x] Create `schemas.py`
- [x] Create `crud.py`
- [x] Create `database.py`
- [x] Create `dependencies.py`
- [x] Create `auth.py`
- [x] Create `utils/`
- [x] Create `templates/`
- [x] Create `static/`

## Static Files

- [x] CSS folder
- [x] JavaScript folder
- [x] Images folder

---

# Phase 3 — Database

## SQLite

- [ ] Configure SQLite connection
- [ ] Create SQLAlchemy engine
- [ ] Configure SessionLocal
- [ ] Configure Base class

## Models

### User

- [ ] Create User model

### Category

- [ ] Create Category model

### Income

- [ ] Create Income model

### Expense

- [ ] Create Expense model

### Goal

- [ ] Create Goal model

## Relationships

- [ ] User → Income
- [ ] User → Expense
- [ ] User → Goal
- [ ] Category → Income
- [ ] Category → Expense

---

# Phase 4 — Schemas

## User Schemas

- [ ] UserCreate
- [ ] UserLogin
- [ ] UserResponse

## Category Schemas

- [ ] CategoryCreate
- [ ] CategoryUpdate
- [ ] CategoryResponse

## Income Schemas

- [ ] IncomeCreate
- [ ] IncomeUpdate
- [ ] IncomeResponse

## Expense Schemas

- [ ] ExpenseCreate
- [ ] ExpenseUpdate
- [ ] ExpenseResponse

## Goal Schemas

- [ ] GoalCreate
- [ ] GoalUpdate
- [ ] GoalResponse

---

# Phase 5 — Authentication

## Registration

- [ ] Create register endpoint
- [ ] Validate email
- [ ] Hash password
- [ ] Save user

## Login

- [ ] Verify credentials
- [ ] Generate JWT token
- [ ] Return token

## Protected Routes

- [ ] Authentication dependency
- [ ] Current user dependency
- [ ] Protect private endpoints

---

# Phase 6 — Categories CRUD

## Backend

- [ ] Create category
- [ ] Get all categories
- [ ] Get category by ID
- [ ] Update category
- [ ] Delete category

## Frontend

- [ ] Category page
- [ ] Create form
- [ ] Edit form
- [ ] Delete confirmation

---

# Phase 7 — Income CRUD

## Backend

- [ ] Create income
- [ ] List incomes
- [ ] Get income
- [ ] Update income
- [ ] Delete income

## Frontend

- [ ] Income page
- [ ] Create form
- [ ] Edit form
- [ ] Delete confirmation
- [ ] Fetch API integration

---

# Phase 8 — Expense CRUD

## Backend

- [ ] Create expense
- [ ] List expenses
- [ ] Get expense
- [ ] Update expense
- [ ] Delete expense

## Frontend

- [ ] Expense page
- [ ] Create form
- [ ] Edit form
- [ ] Delete confirmation
- [ ] Fetch API integration

---

# Phase 9 — Financial Goals

## Backend

- [ ] Create goal
- [ ] Update goal
- [ ] Delete goal
- [ ] List goals

## Frontend

- [ ] Goal page
- [ ] Progress bar
- [ ] Goal cards

---

# Phase 10 — Dashboard

## Backend

- [ ] Current balance
- [ ] Total income
- [ ] Total expenses
- [ ] Monthly savings
- [ ] Recent transactions

## Frontend

- [ ] Dashboard layout
- [ ] Summary cards
- [ ] Responsive layout

---

# Phase 11 — Reports

## Reports

- [ ] Income report
- [ ] Expense report
- [ ] Balance report
- [ ] Category report

## Filters

- [ ] Today
- [ ] Week
- [ ] Month
- [ ] Year
- [ ] Custom range

---

# Phase 12 — Search

- [ ] Search by description
- [ ] Search by category
- [ ] Search by date
- [ ] Search by amount

---

# Phase 13 — Sorting

- [ ] Sort by date
- [ ] Sort by amount
- [ ] Sort by category
- [ ] Ascending order
- [ ] Descending order

---

# Phase 14 — Pagination

- [ ] LIMIT
- [ ] OFFSET
- [ ] Previous page
- [ ] Next page

---

# Phase 15 — User Profile

- [ ] Update name
- [ ] Update email
- [ ] Update password

---

# Phase 16 — Settings

- [ ] Dark mode
- [ ] Light mode
- [ ] Currency selection

---

# Phase 17 — Charts

## Dashboard Charts

- [ ] Expenses by category
- [ ] Income vs Expenses
- [ ] Monthly balance
- [ ] Financial evolution

---

# Phase 18 — Export

- [ ] Export CSV
- [ ] Export PDF *(optional)*

---

# Phase 19 — Frontend Improvements

## HTML

- [ ] Semantic structure
- [ ] Accessibility improvements

## CSS

- [ ] Responsive design
- [ ] Mobile layout
- [ ] Animations
- [ ] Reusable components

## JavaScript

- [ ] Form validation
- [ ] Error handling
- [ ] Loading states
- [ ] Toast notifications

---

# Phase 20 — Testing

## Backend

- [ ] Test authentication
- [ ] Test CRUD endpoints
- [ ] Test reports

## Frontend

- [ ] Validate forms
- [ ] Test API integration
- [ ] Test responsiveness

---

# Phase 21 — Refactoring

- [ ] Remove duplicated code
- [ ] Improve folder organization
- [ ] Improve naming
- [ ] Add comments where necessary
- [ ] Improve type hints

---

# Phase 22 — Documentation

- [ ] Update README
- [ ] Add installation guide
- [ ] Add project screenshots
- [ ] Add API documentation
- [ ] Document project structure

---

# Phase 23 — Deployment

## Backend

- [ ] Configure environment variables
- [ ] Production settings

## Database

- [ ] Prepare production database

## Deployment

- [ ] Deploy backend
- [ ] Deploy frontend
- [ ] Final testing

---

# ⭐ Bonus Features

## Finance

- [ ] Recurring expenses
- [ ] Installments
- [ ] Multiple bank accounts
- [ ] Monthly budget
- [ ] Savings goals
- [ ] Investment tracking

## User Experience

- [ ] Notifications
- [ ] Profile picture
- [ ] Password recovery
- [ ] Email verification

## Technical

- [ ] Docker
- [ ] Alembic migrations
- [ ] Logging
- [ ] Environment configuration
- [ ] CI/CD
- [ ] Unit tests
- [ ] Integration tests
- [ ] Docker Compose

---

# 🎯 Project Completion Checklist

## Backend

- [ ] REST API completed
- [ ] Authentication implemented
- [ ] Database modeled
- [ ] CRUD completed
- [ ] Reports implemented

## Frontend

- [ ] Responsive interface
- [ ] API integration completed
- [ ] Forms validated
- [ ] Dashboard completed

## Quality

- [ ] Clean code
- [ ] Organized project structure
- [ ] Updated documentation
- [ ] Fully tested
- [ ] Ready for portfolio