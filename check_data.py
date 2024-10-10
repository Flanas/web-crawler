import sqlite3

DB_NAME = 'crawler.db'

def check_data():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Fetch all rows from the crawl_data table
    c.execute('SELECT * FROM crawl_data')
    rows = c.fetchall()

    # Print the fetched rows
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    check_data()
