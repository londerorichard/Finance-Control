
. Transactions
This table has the greatest potential for performance improvements.
A. Retrieve transactions by user and date
You've used queries similar to:
SELECT *
FROM transactions
WHERE user_id = ?
ORDER BY created_at DESC;

Recommended index:
CREATE INDEX idx_transactions_user_created
ON transactions(user_id, created_at);

Why:
- Finds transactions belonging to a specific user.
- Helps with date ordering.
- Useful for recent transactions and pagination.
Priority: High.
B. Retrieve a specific transaction
Your ownership-sensitive queries follow this pattern:
SELECT *
FROM transactions
WHERE id = ?
  AND user_id = ?;

Your id column is already a primary key, so SQLite automatically creates an index for it.

You probably don't need another index here. SQLite can locate the transaction by id and then check user_id.
C. Filter transactions by type
For example:
SELECT *
FROM transactions
WHERE user_id = ?
  AND transaction_type = ?;

Potential index:
CREATE INDEX idx_transactions_user_type
ON transactions(user_id, transaction_type);

Useful for:
- Listing only expenses.
- Listing only income.
- Filtering transaction history.
Priority: Medium.
D. Filter transactions by category
For example:
SELECT *
FROM transactions
WHERE user_id = ?
  AND category_id = ?;

Potential index:
CREATE INDEX idx_transactions_user_category
ON transactions(user_id, category_id);

Useful for category-specific transaction lists and reports.

Priority: Medium.
E. Filter transactions by date range
For example:
SELECT *
FROM transactions
WHERE user_id = ?
  AND created_at BETWEEN ? AND ?
ORDER BY created_at DESC;

Your existing (user_id, created_at) index already supports this query pattern.

You don't need another index specifically for this query.
2. Categories
Your categories table has:
UNIQUE (name, user_id)

This automatically creates an index on the combination of name and user_id.

It can help with queries such as:
SELECT *
FROM categories
WHERE name = ?
  AND user_id = ?;

However, you also retrieve categories by user:
SELECT *
FROM categories
WHERE user_id = ?;

The existing composite index (name, user_id) generally cannot efficiently support filtering by user_id alone because user_id isn't the leftmost column.

Potential additional index:
CREATE INDEX idx_categories_user
ON categories(user_id);

Priority: Medium.
3. Goals
Your goals queries include patterns similar to:
SELECT *
FROM goals
WHERE user_id = ?;

And:
SELECT *
FROM goals
WHERE user_id = ?
  AND current_amount >= target_amount;

Potential index:
CREATE INDEX idx_goals_user
ON goals(user_id);

This helps locate goals belonging to a particular user.

The completion condition compares two columns, current_amount and target_amount. An ordinary index on one of those columns won't necessarily optimize that comparison.

Priority: Medium to low, depending on the number of goals per user.
4. Authentication
Your authentication service uses a query similar to:
SELECT *
FROM users
WHERE email = ?;

Your email column already has:
email TEXT UNIQUE NOT NULL

SQLite automatically creates an index to enforce that uniqueness.

Therefore, you don't need another index for email lookups.

The same applies to google_id if it has a UNIQUE constraint.
5. My recommended indexes
Here is the shortlist I'd consider for your project:
Table	Index	Priority	Reason
transactions	(user_id, created_at)	High	Recent transactions, pagination, date filtering
transactions	(user_id, transaction_type)	Medium	Filter income and expenses
transactions	(user_id, category_id)	Medium	Filter transactions by category
categories	(user_id)	Medium	Retrieve categories belonging to a user
goals	(user_id)	Low	Retrieve goals belonging to a user


These are candidates, not a recommendation to create all of them immediately.
6. What I'd actually implement now
I'd start with just this:
CREATE INDEX idx_transactions_user_created
ON transactions(user_id, created_at);

Then investigate the other queries using EXPLAIN QUERY PLAN.

One important consideration: indexes can overlap.

For example, (user_id, created_at) already supports searches using user_id alone. Therefore, creating a separate index on user_id in the transactions table would probably be redundant for those queries.

Also, your transactions table has a foreign key on category_id. SQLite does not automatically create an index on foreign-key columns, so indexing that column can be useful for joins and foreign-key operations.
My advice
Don't create indexes based only on this list. Look at the actual SQL queries in your services, identify their filtering and sorting patterns, and choose indexes accordingly.

That's a much better habit than indexing every column in your database.