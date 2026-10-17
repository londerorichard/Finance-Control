Exercise 7.3 — Income and expense counts ⭐

Create a query that returns:

Number of income transactions.
Number of expense transactions.
Total transaction count.

All three values should be returned in a single row.

Concepts: COUNT, CASE, conditional aggregation.

Exercise 7.4 — Category spending over time ⭐⭐

Create a query that returns the total expenses for each category for each month.

Example:

month	category_name	total_expenses
2026-01	Food	400
2026-01	Housing	1200
2026-02	Food	500
2026-02	Housing	1200

Concepts: JOIN, strftime, GROUP BY.

Where to use it: A chart comparing category spending across months.

Exercise 7.5 — Identify unusual spending ⭐⭐⭐

Retrieve expenses that are significantly larger than the user's average expense amount.

For this exercise, define "significantly larger" as more than twice the average expense amount.

Concepts: Subqueries, AVG, comparison operators.

Challenge: Make sure the average is based on expenses only, not on income and expenses combined.

8. Financial Goals

Your goals table makes these exercises directly applicable to your project.

Exercise 8.1 — Goal progress ⭐

Retrieve all goals belonging to a user and calculate the percentage completed for each goal.

Return:

Goal name.
Target amount.
Current amount.
Completion percentage.

Concepts: Calculated columns, WHERE, division by zero.

Exercise 8.2 — Completed goals ⭐

Retrieve all goals where the current amount has reached or exceeded the target amount.

Concepts: Comparison operators, WHERE.

Exercise 8.3 — Goals still in progress ⭐⭐

Retrieve goals that haven't been completed, sorted by their deadlines.

Consider how to handle goals without a deadline.

Concepts: WHERE, ORDER BY, NULL handling.

Exercise 8.4 — Total amount remaining ⭐⭐

Calculate the total amount a user still needs to save across all their goals.

For each goal, calculate the amount remaining as:

target_amount − current_amount

However, don't allow completed goals to contribute a negative amount.

Concepts: CASE, SUM, MAX or equivalent conditional logic.

Exercise 8.5 — Goals with the greatest remaining amount ⭐⭐

Retrieve the three goals that require the most additional savings.

Return:

Goal name.
Target amount.
Current amount.
Remaining amount.

Concepts: Calculated columns, ORDER BY, LIMIT.

9. Constraints, Transactions, and Data Integrity

Not every useful database task is a SELECT query. These exercises help you avoid corrupt or inconsistent financial data.

Exercise 9.1 — Prevent invalid transaction amounts

Design a table constraint that prevents a transaction from having an amount less than or equal to zero.

Concepts: CHECK.

Question: Should the constraint live only in the application, or also in the database?

Exercise 9.2 — Protect against duplicate categories

Your application allows users to create categories.

Consider whether a user should be able to create two categories with the same name.

If not, design a database constraint that prevents duplicate category names for the same user while still allowing different users to have a category with that name.

Concepts: UNIQUE, composite constraints.

Exercise 9.3 — Transaction rollback

Imagine a financial operation requires two database changes:

Insert a transaction.
Update the corresponding goal's current amount.

If the second operation fails, the first operation shouldn't remain committed on its own.

Describe how you would use a database transaction to keep these operations consistent.

Concepts: BEGIN, COMMIT, ROLLBACK.

Exercise 9.4 — Delete a category safely

A user wants to delete a category that has transactions associated with it.

Consider three possible behaviors:

Reject the deletion.
Delete the category and its associated transactions.
Delete the category while preserving its transactions without a category.

Which behavior would you choose for a finance application, and how would your foreign-key design support that choice?

Concepts: Foreign keys, ON DELETE, NULL, data integrity.

My recommendation: For a finance application, preserving historical transactions is usually important. Avoid cascading deletion of financial records unless you have a specific, well-designed reason to do so.

🔵 Level 4 — Query Optimization and Performance

You already studied indexes, so now apply that knowledge to the project.

10. Indexes and Query Plans
Exercise 10.1 — Optimize recent transactions

Your dashboard frequently runs a query that filters transactions by user_id and sorts them by created_at.

Consider which index could support that access pattern.

Question: Would an index on user_id alone necessarily be as useful as a composite index on user_id and created_at?

Exercise 10.2 — Analyze a query plan

Use SQLite's EXPLAIN QUERY PLAN to examine the execution plan for your recent-transactions query.

Then compare the plan before and after adding an appropriate index.

Look for differences in how SQLite accesses the table and whether it needs an additional sorting step.

Exercise 10.3 — Understand index trade-offs

Consider a database that receives:

Many transaction reads.
Frequent transaction inserts.
Occasional transaction updates and deletions.

Explain why adding an index to every column would be a poor decision.

Think about storage costs and the extra work required to maintain indexes during writes.

Exercise 10.4 — Review your user-scoped queries

Inspect the queries used by your API.

For every query that retrieves or changes a user's data, verify that it restricts the operation to the authenticated user's records.

Consider whether a query involving a category or goal also needs to check ownership of the related record.

This is both a correctness and security exercise.