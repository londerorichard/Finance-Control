# 1. Authentication (`auth`)

Authentication is one of the most important areas because mistakes can expose users' financial information.

## Password Hashing

Test the functions responsible for hashing and verifying passwords.

- [x] A password is hashed successfully.
- [x] The generated hash is different from the original password.
- [x] The correct password matches its hash.
- [x] An incorrect password doesn't match the hash.
- [x] Two hashes generated for the same password can differ but both verify successfully.

## JWT Tokens

Test the functions responsible for creating and decoding tokens.

- [x] A token is generated successfully for a valid user.
- [x] The token contains the expected user identifier in its `sub` claim.
- [x] A valid token can be decoded successfully.
- [x] An invalid token is rejected.
- [x] A token with an invalid signature is rejected.
- [x] An expired token is rejected.
- [x] A token without the required claims is rejected.

## Authentication Logic

Test the logic that authenticates users and resolves the current user.

- [ ] Valid credentials authenticate successfully.
- [ ] An incorrect password is rejected.
- [ ] An email that doesn't exist is rejected.
- [ ] A token referring to a nonexistent user is rejected.
- [ ] A user who has been deleted cannot authenticate using an old token.

---

# 2. User Management (`users`)

These tests cover user creation, retrieval, and modification.

## User Creation

- [ ] A user is created with valid information.
- [ ] The password is stored as a hash, never as plaintext.
- [ ] The email is stored correctly.
- [ ] The creation timestamp is generated correctly.
- [ ] A duplicate email is rejected.
- [ ] Invalid email input is rejected if your schema enforces email validation.
- [ ] Missing required fields are rejected by the schema.

## User Retrieval

- [ ] An existing user can be retrieved by ID.
- [ ] A nonexistent user returns the expected result.
- [ ] Retrieving a user doesn't expose their password hash through a public response schema.

## Password Changes

- [ ] A user can change their password with valid input.
- [ ] The new password is stored as a hash.
- [ ] The new password can be verified successfully.
- [ ] The old password no longer matches the updated hash.
- [ ] An incorrect current password prevents the change, if your application requires current-password verification.

**Priority:** Duplicate-email handling and password hashing are particularly important for your project.

---

# 3. Transaction Schemas (`schemas`)

These tests validate the data entering your application before it reaches the business logic.

For your `TransactionCreate` schema, you've already started working with Pydantic's `Field(gt=0)`.

## Amount Validation

- [ ] A positive amount, such as `31.90`, is accepted.
- [ ] A small positive amount, such as `0.01`, is accepted.
- [ ] Zero is rejected.
- [ ] A negative amount is rejected.
- [ ] A nonnumeric value, such as `"invalid"`, is rejected.

## Transaction Type Validation

- [ ] A valid income type is accepted.
- [ ] A valid expense type is accepted.
- [ ] An unsupported transaction type is rejected.

## Other Transaction Fields

- [ ] Missing required fields are rejected.
- [ ] Optional fields can be omitted.
- [ ] Invalid values for fields with constraints are rejected.
- [ ] A valid transaction can be represented by the appropriate response schema.

**One important distinction:** These are schema tests. They verify Pydantic's validation behavior, not whether the database successfully saves the transaction.

Also, if your project uses `float` for monetary amounts, consider `Decimal` or integer cents to avoid floating-point precision issues.

---

# 4. Transaction Business Logic (`transactions`)

These tests cover your CRUD functions and any calculations or rules that operate on transactions.

## Create

- [ ] A transaction is created with valid data.
- [ ] The transaction is associated with the correct user.
- [ ] The transaction is associated with the correct category, if provided.
- [ ] An invalid category is rejected.
- [ ] A category belonging to another user is rejected.

## Read

- [ ] A transaction can be retrieved by ID.
- [ ] A nonexistent transaction returns the expected result.
- [ ] A user's transactions are filtered by their user ID.
- [ ] A transaction belonging to another user isn't returned by a user-scoped query.
- [ ] A transaction can be retrieved with its category name if you support enriched queries using a `JOIN`.

## Update

- [ ] A transaction can be updated with valid data.
- [ ] Updating a transaction changes only the intended fields.
- [ ] Updating a nonexistent transaction produces the expected result.
- [ ] A user cannot update another user's transaction.
- [ ] An update with an invalid amount is rejected.
- [ ] Changing a transaction's category to another user's category is rejected.

## Delete

- [ ] An existing transaction can be deleted.
- [ ] Deleting a nonexistent transaction produces the expected result.
- [ ] A user cannot delete another user's transaction.

## Financial Calculations

- [ ] The current balance is calculated correctly.
- [ ] Income totals are calculated correctly.
- [ ] Expense totals are calculated correctly.
- [ ] Income and expense transactions affect the balance in the correct direction.
- [ ] An empty transaction list produces the expected balance.
- [ ] Monthly totals include only transactions from the relevant month.
- [ ] Transactions from different users aren't mixed in calculations.

For your financial application, these calculations deserve particular attention. A small error in a query or calculation could produce an incorrect balance even when all the CRUD operations work correctly.

---

# 5. Categories (`categories`)

Categories require special attention because each user should manage their own categories.

## Create

- [ ] A category is created with valid data.
- [ ] The category is associated with the correct user.
- [ ] Required category fields are validated.
- [ ] A category belonging to another user cannot be created or assigned on that user's behalf.

## Read

- [ ] A user can retrieve their own category.
- [ ] A user can retrieve their own list of categories.
- [ ] Categories belonging to another user aren't returned by user-scoped queries.
- [ ] A nonexistent category returns the expected result.

## Update and Delete

- [ ] A user can update their own category.
- [ ] A user can delete their own category, subject to your deletion rules.
- [ ] A user cannot update another user's category.
- [ ] A user cannot delete another user's category.

## Category-Related Calculations

- [ ] The total expense amount for a category is calculated correctly.
- [ ] The total is calculated only for the intended user.
- [ ] A category with no transactions returns the expected total, usually zero.
- [ ] Category totals respect any monthly date filters your application supports.

**Highest priority:** Test ownership at the database-function or business-logic level. Don't rely on the frontend to prevent users from accessing each other's categories.

---

# 6. Goals (`goals`)

If your application supports financial goals, test their validation and calculations.

## Goal Creation and Validation

- [ ] A goal can be created with valid information.
- [ ] The target amount must be positive.
- [ ] The initial current amount has the correct default, such as zero.
- [ ] Invalid target amounts are rejected.
- [ ] Invalid or missing required fields are handled correctly.

## Goal Calculations

- [ ] Progress is calculated correctly.
- [ ] A goal with no saved amount has zero progress.
- [ ] A partially completed goal shows the correct progress.
- [ ] A completed goal shows 100% progress.
- [ ] Progress doesn't exceed 100% if your application caps it there.
- [ ] Division by zero is avoided if progress is calculated using a target amount.

## Ownership and CRUD

- [ ] A user can retrieve their own goals.
- [ ] A user cannot retrieve another user's goals.
- [ ] A user can update their own goal.
- [ ] A user cannot update another user's goal.
- [ ] A user can delete their own goal.
- [ ] A user cannot delete another user's goal.

---

# 7. Database Operations (`database`)

You should test the database functions that your application relies on, especially when they contain SQL queries or transaction handling.

These are often called *unit tests* informally, although tests that exercise a real database are more precisely integration tests.

## Essential Tests

- [ ] A record is inserted successfully.
- [ ] A record can be retrieved after insertion.
- [ ] A record can be updated successfully.
- [ ] A record can be deleted successfully.
- [ ] A query returns the expected result when no records exist.
- [ ] Foreign-key constraints prevent invalid references, if enabled in your database.
- [ ] Unique constraints prevent duplicate values where required.
- [ ] Database errors are handled as expected.
- [ ] Failed operations don't leave partially applied changes when atomicity is required.

## Important for SQLite

If you use SQLite, remember that foreign-key enforcement must be enabled on the relevant connections. Merely declaring a foreign key in your schema doesn't guarantee that SQLite will enforce it.

**Recommendation:** Use a separate test database so your tests never modify your real financial data.

---

# 8. Reports and Dashboard Calculations

Your dashboard and reports depend on the correctness of your queries and calculations.

You don't need to test every possible chart configuration yet. Focus on the underlying data.

## Essential Tests

- [ ] The total income is calculated correctly.
- [ ] The total expenses are calculated correctly.
- [ ] The current balance is calculated correctly.
- [ ] Monthly balances are returned in the expected format.
- [ ] Monthly reports use the correct date boundaries.
- [ ] Category totals are calculated correctly.
- [ ] An empty database produces sensible results.
- [ ] Reports only include the authenticated user's transactions.
- [ ] Transactions outside the requested date range are excluded.

For example, if your monthly report calculates expenses for October, test that September and November transactions don't accidentally appear in the October result.

You should also test date boundaries, such as a transaction recorded at the beginning or end of a month.

---

# 9. Shared Validation and Utility Functions

If you have helper functions used across multiple features, test them independently.

Examples include date formatting, monetary calculations, and validation helpers.

## Essential Tests

- [ ] Valid dates are handled correctly.
- [ ] Invalid dates are rejected when validation is expected.
- [ ] Currency calculations produce the expected results.
- [ ] Empty collections are handled correctly.
- [ ] Missing or optional values are handled correctly.
- [ ] Boundary values behave as expected.

Only include tests for utilities that actually exist in your project. You don't need to create helper functions just to have something to test.

---

# 10. Error Handling and Business Rules

Finally, test important rules that don't fit neatly into a single CRUD operation.

## Essential Tests

- [ ] Duplicate emails are handled consistently.
- [ ] Missing records produce the expected result.
- [ ] Invalid input is rejected before database modification.
- [ ] A failed update doesn't accidentally modify unrelated records.
- [ ] A user cannot access another user's financial data.
- [ ] Invalid foreign-key references are rejected.
- [ ] Unexpected database failures don't result in partially completed operations.
- [ ] Passwords and other sensitive data aren't exposed in returned user data.

Some of these rules overlap with the earlier sections. That's intentional: the earlier sections organize tests by feature, while this section helps you check for cross-cutting problems.