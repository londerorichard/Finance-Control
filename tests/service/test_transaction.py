def test_analyze_recent_transactions(test_auth_db, db_connection):
    cursor = db_connection.cursor()

    user_id = 1

    query = """
        SELECT *
        FROM transactions
        WHERE created_at >= date('now', '-7 days')
          AND user_id = ?
        ORDER BY created_at DESC
    """

    # 1. Analyze the query before creating the index
    cursor.execute("EXPLAIN QUERY PLAN " + query, (user_id,))
    plan_before = cursor.fetchall()

    print("\nExecution Plan BEFORE index:")

    for row in plan_before:
        print(tuple(row))

    # 2. Create a composite index
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_transactions_user_created
        ON transactions(user_id, created_at)
    """)

    # 3. Analyze the same query after creating the index
    cursor.execute("EXPLAIN QUERY PLAN " + query, (user_id,))
    plan_after = cursor.fetchall()

    print("\nExecution Plan AFTER index:")

    for row in plan_after:
        print(tuple(row))

    # 4. Verify that both execution plans were returned
    assert len(plan_before) > 0
    assert len(plan_after) > 0