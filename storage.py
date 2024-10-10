import sqlite3

DB_NAME = 'crawler.db'

def initialize_db():
    """Create the crawl_data table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS crawl_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            filter_type TEXT,
            data TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def save_data(entries, timestamp, filter_type):
    """Save the fetched entries into the database."""
 
    initialize_db()
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    data_str = str(entries)  
    
    c.execute('''
        INSERT INTO crawl_data (timestamp, filter_type, data)
        VALUES (?, ?, ?)
    ''', (timestamp, filter_type, data_str))
    
    conn.commit()
    conn.close()
    print(f"Data saved successfully at {timestamp} with filter: {filter_type}")
