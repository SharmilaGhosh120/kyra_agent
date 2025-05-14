
import sqlite3

DB_NAME = "kyra_queries.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            apaar_id TEXT,
            query TEXT,
            response TEXT,
            timestamp TEXT,
            feedback TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(apaar_id, query, response, timestamp, feedback=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO student_queries (apaar_id, query, response, timestamp, feedback)
        VALUES (?, ?, ?, ?, ?)
    ''', (apaar_id, query, response, timestamp, feedback))
    conn.commit()
    conn.close()

init_db()
