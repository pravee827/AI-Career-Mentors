import sqlite3

DB_NAME = "chat_history.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        user_message TEXT,
        bot_response TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_chat(username, user_message, bot_response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_history
    (username, user_message, bot_response)
    VALUES (?, ?, ?)
    """, (username, user_message, bot_response))

    conn.commit()
    conn.close()


def get_history(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT user_message, bot_response, timestamp
    FROM chat_history
    WHERE username = ?
    ORDER BY timestamp DESC
    """, (username,))

    data = cursor.fetchall()

    conn.close()

    return data


def clear_history(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM chat_history
    WHERE username = ?
    """, (username,))

    conn.commit()
    conn.close()


create_table()