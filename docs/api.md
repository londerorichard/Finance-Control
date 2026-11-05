
# 8. Testing ⭐⭐⭐

## Testing Fundamentals

1. [x] **pytest**
   ↓
2. [x] **`assert`**
   ↓
3. [x] **Basic unit tests**
   ↓
4. [x] **FastAPI `TestClient`**
   ↓
5. [x] **Testing GET / POST / PATCH / DELETE**
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

### Unit tests

* [x] Password hashing.
* [x] Password verification.
* [x] Different hashes for identical passwords.
* [x] JWT creation and decoding.
* [x] Invalid token.
* [x] Expired token.
* [x] Invalid signature.
* [x] Missing subject.
* [x] Invalid subject format.

### Service/database integration tests

* [x] Register valid user.
* [x] Login with valid credentials.
* [x] Reject incorrect password.
* [x] Reject nonexistent email.
* [x] Reject token for nonexistent user.
* [x] Reject token for deleted user.

### API route tests

* [x] Register valid user.
* [ ] Register duplicate email.
* [ ] Login with valid credentials.
* [ ] Login with incorrect password.
* [ ] Login with nonexistent email.
* [ ] Access protected endpoint without token.
* [ ] Access protected endpoint with invalid token.
* [ ] Access protected endpoint with valid token.

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

