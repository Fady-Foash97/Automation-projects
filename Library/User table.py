import sqlite3 
conn = sqlite3.connect("D:\Programming\python\Automation\Library\Library program.db")
cursor = conn.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL
        )
        """)
conn.commit()
conn.close()