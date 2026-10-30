def test_analyze_recent_transactions(test_auth_db, db_connection):
    cursor = db_connection.cursor()

    user_id = 1

    cursor.execute("""
        EXPLAIN QUERY PLAN
        SELECT *
        FROM transactions
        WHERE created_at >= date('now', '-7 days')
          AND user_id = ?
        ORDER BY created_at DESC
    """, (user_id,))

    query_plan = cursor.fetchall()

    print("\nSQLite Query Execution Plan:")

    for row in query_plan:
        print(tuple(row))

    assert len(query_plan) > 0