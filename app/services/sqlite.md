

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