import sqlite3

DB_NAME = 'credentials.db'

def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   website TEXT,
                   username TEXT,
                   password TEXT,
                   UNIQUE(website, username)
        )
    """)
    
    conn.commit()
    conn.close()
