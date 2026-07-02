import sqlite3

conn = sqlite3.connect("D:\Programming\python\Automation\Library\Library program.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Purchased_Books(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    User_ID INTEGER NOT NULL,
    Book_ID INTEGER NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES Users(ID),
    FOREIGN KEY (Book_ID) REFERENCES Books(ID)
)
""")
conn.commit()
conn.close()