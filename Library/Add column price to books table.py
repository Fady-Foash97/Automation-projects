import sqlite3

conn = sqlite3.connect("D:\Programming\python\Automation\Library\Library program.db")
cursor = conn.cursor()

cursor.execute("""
        ALTER TABLE Books
        ADD COLUMN 
        Prices FLOAT
                   """)
conn.commit()
conn.close()