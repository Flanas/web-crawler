import sqlite3

DB_NAME = 'crawler.db'

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS crawl_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            filter_type TEXT,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_data(entries, timestamp, filter_type):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    data_str = str(entries)
    c.execute('''
        INSERT INTO crawl_data (timestamp, filter_type, data)
        VALUES (?, ?, ?)
    ''', (timestamp, filter_type, data_str))
    conn.commit()
    conn.close()
