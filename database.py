import sqlite3

def create_table():
    conn=sqlite3.connect("event.db")
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS registrations (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          email TEXT NOT NULL,
                          department TEXT NOT NULL
                         )
                     """)
    conn.commit()
    conn.close()
create_table()