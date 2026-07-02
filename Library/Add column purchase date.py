import sqlite3

conn = sqlite3.connect("D:\Programming\python\Automation\Library\Library program.db")
cursor = conn.cursor()

cursor.execute("""
        ALTER TABLE Purchased_Books
        ADD COLUMN 
        Purchase_date TEXT DEFAULT CURRENT_TIMESTAMP 
                   """)
conn.commit()
conn.close()