from datetime import datetime, timedelta, timezone
from jose import jwt

from app.auth.security import hash_password, verify_password
from app.auth.jwt import (
    ALGORITHM,
    SECRET_KEY,
    create_access_token,
    decode_token,
)


# PASSWORD HASHING

def test_password_hashing():
    password = "MyPassword123"

    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("WrongPassword", hashed) is False


def test_same_password_generates_different_hashes():
    password = "MyPassword123"

    first_hash = hash_password(password)
    second_hash = hash_password(password)

    assert first_hash != second_hash
    assert verify_password(password, first_hash) is True
    assert verify_password(password, second_hash) is True


# JWT TOKENS

def test_create_and_decode_token():
    user_id = 15

    token = create_access_token(user_id)
    payload = decode_token(token)

    assert isinstance(token, str)
    assert payload is not None
    assert payload["sub"] == str(user_id)
    assert "exp" in payload


def test_invalid_token():
    token = "this-is-not-a-valid-jwt"

    payload = decode_token(token)

    assert payload is None


def test_expired_token():
    expire = datetime.now(timezone.utc) - timedelta(minutes=1)

    token = jwt.encode(
        {
            "sub": "15",
            "exp": expire,
        },
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    payload = decode_token(token)

    assert payload is None


def test_invalid_signature():
    token = create_access_token(15)

    parts = token.split(".")

    # Change the signature without changing the header or payload.
    parts[2] = ("A" if parts[2][0] != "A" else "B") + parts[2][1:]

    tampered_token = ".".join(parts)

    payload = decode_token(tampered_token)

    assert payload is None


def test_token_missing_subject():
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    token = jwt.encode(
        {
            "exp": expire,
        },
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    payload = decode_token(token)

    assert payload is None






# [ ] create user
# [ ] find user by email
# [ ] create category
# [ ] find categories for user
# [ ] create transaction
# [ ] find transaction
# [ ] update transaction
# [ ] delete transaction




# Authentication
# POST /auth/register

#     [ ] valid registration
#     [ ] invalid email
#     [ ] invalid password
#     [ ] duplicate email

# Then:

# POST /auth/login

#     [ ] correct credentials
#     [ ] wrong password
#     [ ] nonexistent user

# Then:

# GET /users/me

#     [ ] valid token
#     [ ] missing token
#     [ ] invalid token
#     [ ] nonexistent user from token


# 3. Categories

# Then:

# POST /categories

#     [ ] authenticated user can create
#     [ ] unauthenticated request rejected
#     [ ] invalid data rejected
# GET /categories

#     [ ] returns user's categories
#     [ ] doesn't return another user's categories

# Then:

# PUT /categories/{id}

#     [ ] owner can update
#     [ ] nonexistent category
#     [ ] another user cannot update it
#     [ ] invalid data

# And:

# DELETE /categories/{id}

#     [ ] owner can delete
#     [ ] nonexistent category
#     [ ] another user cannot delete it

# Notice something important here:

# Authorization tests are extremely important in your project.

# For example:

# User A
#    │
#    └── Transaction 15

# User B
#    │
#    └── tries DELETE /transactions/15

# You want a test proving that B cannot delete A's transaction.

# 4. Transactions

# This will probably become your biggest test group.

# POST /transactions
# GET /transactions
# GET /transactions/{id}
# PUT /transactions/{id}
# DELETE /transactions/{id}

# For each, think about:

# happy path
# invalid input
# not found
# authentication
# authorization
# edge cases

# Then your filtering:

# GET /transactions?category_id=3
# GET /transactions?transaction_type=expense
# GET /transactions?min_amount=100
# GET /transactions?max_amount=500
# GET /transactions?page=2&limit=10

# You don't necessarily need a separate test for every possible combination. Test the important combinations and the logic behind them.

# 5. Goals

# Same approach:

# POST /goals
# GET /goals
# GET /goals/{id}
# PUT /goals/{id}
# DELETE /goals/{id}

# Test:

# valid
# invalid
# not found
# unauthenticated
# wrong owner

# And any financial rules you implement.

# 6. Statistics

# Finally:

# GET /dashboard/statistics

# Test things such as:

# [ ] authenticated user gets statistics
# [ ] statistics only use that user's data
# [ ] empty database produces sensible result
# [ ] income totals are correct
# [ ] expense totals are correct
# [ ] balance is correct
# [ ] category totals are correct


# 7. Integration tests

# After you've built a reasonable amount of your API, start testing complete workflows.

# For example:

# Registration → login → protected resource
# register
#    ↓
# login
#    ↓
# receive JWT
#    ↓
# GET /users/me
#    ↓
# verify returned user
# Category → transaction
# register
#    ↓
# login
#    ↓
# create category
#    ↓
# create transaction using category
#    ↓
# retrieve transaction
#    ↓
# verify category information
# User isolation

# This one is very important for your finance application:

# Create User A
#        ↓
# Create User B
#        ↓
# A creates transaction
#        ↓
# B tries to access transaction
#        ↓
# B must not receive A's transaction
# Complete financial workflow

# Eventually:

# register
#    ↓
# login
#    ↓
# create categories
#    ↓
# create income
#    ↓
# create expenses
#    ↓
# retrieve statistics
#    ↓
# verify totals