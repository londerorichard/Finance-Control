
# 📁 Project Structure

This structure follows a common organization for **FastAPI** applications, making the project easier to maintain, scale, and understand.

---

# 📂 Folder and File Responsibilities

| Folder/File     | Responsibility                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| **main.py**     | Entry point of the application. Initializes the FastAPI app, registers routers, and starts the server. |
| **routers/**    | Defines API endpoints and organizes routes by feature or resource.                                     |
| **models.py**   | Contains SQLAlchemy models that represent the database tables.                                         |
| **schemas.py**  | Defines Pydantic models used for request validation and API responses.                                 |
| **crud.py**     | Implements database operations such as Create, Read, Update, and Delete.                               |
| **database.py** | Configures the database connection, engine, and session management.                                    |
| **auth.py**     | Handles authentication, authorization, JWT tokens, and password hashing.                               |
| **templates/**  | Stores HTML templates rendered by Jinja2.                                                              |
| **static/**     | Contains static assets such as CSS, JavaScript, images, and fonts.                                     |
| **utils/**      | Stores reusable helper functions, utilities, and common logic shared across the project.               |
| **tests/**      | Contains automated tests for the application.                                                          |

---

# 🚀 Recommended Development Order

Follow this order to build the project incrementally.

* [x] Create the project structure
* [x] Configure the virtual environment
* [x] Install dependencies
* [x] Configure the database connection (`database.py`)
* [x] Create the database models (`models.py`)
* [x] Create the Pydantic schemas (`schemas.py`)
* [x] Implement CRUD operations (`crud.py`)
* [x] Build the API routes (`routers/`)
* [x] Implement authentication (`auth.py`)
* [x] Create the HTML templates (`templates/`)
* [ ] Add CSS, JavaScript, and images (`static/`)
* [ ] Write automated tests (`tests/`)
* [ ] Refactor and improve the code
* [ ] Update the documentation (`README.md`)
* [ ] Deploy the application

---

# FastAPI Backend Learning Roadmap

## 2. Authentication & Authorization ⭐⭐⭐

1. [ ] **Authentication vs Authorization**
   ↓
2. [ ] **Password hashing & verification**
   ↓
3. [ ] **OAuth2 basics**
   ↓
4. [ ] **Bearer tokens**
   ↓
5. [ ] **JWT structure & claims**
   ↓
6. [ ] **Token expiration**
   ↓
7. [ ] **Access vs Refresh tokens**
   ↓
8. [ ] **`get_current_user` + `Depends()`**
   ↓
9. [ ] **Resource ownership** ⭐
   ↓
10. [ ] **401 vs 403**
    ↓
11. [ ] **Roles / permissions**
    ↓
12. [ ] **Cookies vs `localStorage`**
    ↓
13. [ ] **XSS**
    ↓
14. [ ] **CSRF**
    ↓
15. [ ] **CORS**
    ↓
16. [ ] **OAuth2 scopes**

---

# 7. Pagination ⭐⭐⭐

## Fundamentals

* [ ] What pagination is
* [ ] `page` and `limit`
* [ ] SQL `LIMIT`
* [ ] SQL `OFFSET`
* [ ] Understand the formula:

```text
offset = (page - 1) * limit
```

## FastAPI Pagination

* [ ] Pagination validation with `Query`
* [ ] Set minimum/maximum values for `page` and `limit`
* [ ] Return pagination metadata
* [ ] Calculate `total` count
* [ ] Calculate `has_next`
* [ ] Calculate `has_previous`

## SQL Pagination

* [ ] Pagination with SQL
* [ ] Combine `LIMIT` and `OFFSET`
* [ ] Order results before pagination
* [ ] Understand how pagination interacts with filtering and sorting

---

# 8. Testing ⭐⭐⭐

## Testing Fundamentals

1. [ ] **pytest**
   ↓
2. [ ] **`assert`**
   ↓
3. [ ] **Basic unit tests**
   ↓
4. [ ] **FastAPI `TestClient`**
   ↓
5. [ ] **Testing GET / POST / PATCH / DELETE**
   ↓
6. [ ] **Testing status codes + response JSON**
   ↓
7. [ ] **Testing validation errors**
   ↓
8. [ ] **Testing authentication**
   ↓
9. [ ] **Testing authorization / ownership**
   ↓
10. [ ] **Fixtures**
    ↓
11. [ ] **Test database**
    ↓
12. [ ] **Setup / cleanup**
    ↓
13. [ ] **Integration tests**
    ↓
14. [ ] **Mocking**
    ↓
15. [ ] **Coverage**

---

## Authentication Tests

* [ ] Register valid user
* [ ] Register duplicate email
* [ ] Login with valid credentials
* [ ] Login with wrong password
* [ ] Access protected endpoint without token
* [ ] Access protected endpoint with invalid token

---

## Transaction Tests

* [ ] Create transaction
* [ ] List transactions
* [ ] Get transaction
* [ ] Update transaction
* [ ] Delete transaction
* [ ] Invalid transaction
* [ ] Nonexistent transaction
* [ ] Cannot access another user's transaction

---

## Category Tests

* [ ] Create category
* [ ] List categories
* [ ] Update category
* [ ] Delete category
* [ ] Cannot access another user's category

---

## Database Tests

* [ ] Insert
* [ ] Select
* [ ] Update
* [ ] Delete
* [ ] Rollback on failure

---

# 9. Middleware ⭐⭐

## Fundamentals

* [ ] What middleware is
* [ ] Understand the request/response flow:

```text
Request
   ↓
Middleware
   ↓
Endpoint
   ↓
Middleware
   ↓
Response
```

## FastAPI Middleware

* [ ] `@app.middleware("http")`
* [ ] `call_next(request)`
* [ ] Read request information
* [ ] Modify responses
* [ ] Add response headers

## Practical Middleware

* [ ] Logging middleware
* [ ] Timing middleware
* [ ] CORS middleware

## Middleware Architecture

* [ ] Middleware vs dependencies
* [ ] Middleware vs router dependencies
* [ ] Middleware ordering
* [ ] Understand when middleware is appropriate
* [ ] Understand when **not** to use middleware

---

# 10. SQLAlchemy ⭐

* [ ] SQLAlchemy fundamentals
* [ ] Models
* [ ] Engine
* [ ] Sessions
* [ ] CRUD operations
* [ ] `select()`
* [ ] `where()`
* [ ] Filtering
* [ ] Ordering
* [ ] `LIMIT` / `OFFSET`
* [ ] Relationships
* [ ] Foreign keys
* [ ] Joins
* [ ] Transactions
* [ ] Commit / rollback
* [ ] Session management
* [ ] SQLAlchemy with FastAPI
* [ ] SQLAlchemy with Pydantic schemas

---

# 11. Lifespan / Background Tasks / File Uploads

## Lifespan

* [ ] Understand application lifespan
* [ ] Startup logic
* [ ] Shutdown logic
* [ ] `lifespan`
* [ ] When to use lifespan

## Background Tasks

* [ ] What background tasks are
* [ ] FastAPI `BackgroundTasks`
* [ ] Run non-critical work after a response
* [ ] Understand when background tasks are appropriate
* [ ] Understand their limitations

## File Uploads

* [ ] `UploadFile`
* [ ] `File`
* [ ] Upload validation
* [ ] File size validation
* [ ] File type validation
* [ ] Saving uploaded files
* [ ] File paths and storage
* [ ] Security considerations for uploaded files

---

# 12. Security + Configuration

## Security

* [ ] Secure password hashing
* [ ] JWT security
* [ ] Token expiration
* [ ] Access vs refresh tokens
* [ ] Authentication vs authorization
* [ ] Resource ownership
* [ ] Roles / permissions
* [ ] Input validation
* [ ] SQL injection prevention
* [ ] XSS
* [ ] CSRF
* [ ] CORS
* [ ] Secure cookies
* [ ] Secret management
* [ ] Environment variables
* [ ] HTTPS
* [ ] Rate limiting
* [ ] Secure error handling
* [ ] Avoid exposing sensitive information

## Configuration

* [ ] Environment variables
* [ ] `.env`
* [ ] Separate development / production configuration
* [ ] Configuration management
* [ ] Secrets
* [ ] Database configuration
* [ ] JWT configuration
* [ ] CORS configuration
* [ ] Logging configuration
* [ ] Debug vs production mode
* [ ] Never commit secrets to Git

