from .connection import get_connection

def create_tables(db_path="finance.db"):
    connection = get_connection(db_path)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT,
        google_id TEXT UNIQUE,
        created_at TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        user_id INTEGER NOT NULL,

        FOREIGN KEY (user_id) REFERENCES users(id),
        UNIQUE (name, user_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL CHECK (amount > 0),
        transaction_type TEXT NOT NULL,
        description TEXT,
        created_at TEXT NOT NULL,
        category_id INTEGER,
        account TEXT,

        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (category_id)
            REFERENCES categories(id)
            ON DELETE SET NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        goal_name TEXT NOT NULL,
        target_amount REAL NOT NULL,
        current_amount REAL DEFAULT 0,
        deadline TEXT,

        FOREIGN KEY (user_id) REFERENCES users(id),
        UNIQUE (goal_name, user_id)
    )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()




