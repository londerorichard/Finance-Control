# 🌿 Git Branching Strategy

A clean branching strategy makes your project easier to develop, review, and maintain.

---

# ❌ Avoid Organizing Branches by Layer

Instead of creating branches based on project layers like this:

```text id="7x4nqm"
main
├── frontend
├── backend
├── database
└── api
```

This approach makes features difficult to integrate because changes related to a single feature become scattered across multiple branches.

---

# ✅ Organize Branches by Feature

Create one branch for each feature you develop.

```text id="o31bho"
main
├── feature/authentication
├── feature/dashboard
├── feature/transactions
├── feature/categories
├── feature/reports
├── feature/goals
├── feature/settings
└── feature/home-page
```

Each branch contains **everything needed** for that feature.

---

# 📦 Example: `feature/authentication`

A feature branch should include every part of the application required to complete that feature.

### Frontend

* ✅ Login page
* ✅ Registration page

### Backend

* ✅ Authentication endpoints
* ✅ JWT implementation

### Database

* ✅ Users table
* ✅ Authentication-related migrations

### Tests

* ✅ Authentication unit tests
* ✅ Authentication integration tests

Once the feature is complete:

```text id="8i8g0x"
feature/authentication
          │
          ▼
        main
```

---

# 🎯 Organize by Work, Not by Files

Imagine you're implementing **Categories**.

Instead of splitting the work into multiple branches:

```text id="6vbv3t"
frontend
    └── Edit Category Page

database
    └── Categories Table

api
    └── CRUD Endpoints

logic
    └── Validation
```

Create a single feature branch:

```text id="tx3lxa"
feature/categories
```

Everything related to categories belongs in that branch.

This keeps the feature isolated and easy to review.

---

# 🌱 Temporary Branches

Sometimes a feature becomes large enough that it's helpful to split it into smaller temporary branches.

Example:

```text id="2mtdyy"
feature/dashboard
        │
        ├── fix/dashboard-css
        ├── refactor/dashboard-service
        └── test/dashboard
```

These branches usually:

* Live for only a few hours or days.
* Are merged back into the parent feature branch.
* Are deleted afterward.

> 💡 For most personal projects, you won't need this unless a feature grows significantly.

---

# 💰 Suggested Structure for a Financial Management System

```text id="h9rtrh"
main

├── feature/home-page
├── feature/authentication
├── feature/dashboard
├── feature/transactions
├── feature/categories
├── feature/accounts
├── feature/goals
├── feature/reports
├── feature/charts
├── feature/settings
└── feature/deployment
```

---

# 🐞 Bug Fix Branches

Create dedicated branches for bug fixes.

Examples:

```text id="4v2n84"
fix/login-validation
fix/dashboard-css
fix/api-timezone
```

---

# ♻️ Refactoring Branches

Use separate branches when improving code without adding new features.

Examples:

```text id="7g30v8"
refactor/project-structure
refactor/database-layer
refactor/services
```

---

# 🚀 Suggested Workflow

```text id="kllzws"
main
   │
   ├── feature/dashboard
   │          │
   │          ▼
   │       Merge → main
   │
   ├── feature/api
   │          │
   │          ▼
   │       Merge → main
   │
   ├── feature/reports
   │          │
   │          ▼
   │       Merge → main
```

For every feature:

* [ ] Create a new feature branch.
* [ ] Make small, meaningful commits.
* [ ] Push the branch to GitHub.
* [ ] Open a Pull Request (even if you're working alone, for practice).
* [ ] Review your changes.
* [ ] Merge into `main`.
* [ ] Delete the feature branch.

---

# 🌍 What About Long-Lived Branches?

Many professional teams keep only **one permanent branch** (`main`) and create short-lived feature branches whenever new work begins.

Some teams also maintain a `develop` branch, but many modern workflows (such as **GitHub Flow**) work directly from `main`.

For a personal project, keep it simple:

```text id="i7n6g0"
main
   │
   ▼
feature/something
   │
   ▼
Pull Request
   │
   ▼
main
```

---

# ✅ Benefits of a Feature Branch Workflow

* Easier code reviews.
* Cleaner Git history.
* Features remain isolated until they're complete.
* Lower risk of introducing bugs into `main`.
* Simple rollback if a feature causes problems.
* Encourages small, focused commits.
* Mirrors the workflow used by many professional development teams.

---

# 💡 Best Practices

* Create one branch per feature.
* Keep branches focused on a single purpose.
* Commit frequently with descriptive commit messages.
* Open Pull Requests for every feature, even when working solo.
* Delete feature branches after merging.
* Use `fix/` for bug fixes and `refactor/` for code improvements.
* Keep `main` stable and deployable whenever possible.
