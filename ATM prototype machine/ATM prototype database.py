import sqlite3

conn = sqlite3.connect("ATM.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Accounts(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number INT,
    owner_name TEXT NOT NULL,
    balance REAL NOT NULL DEFAULT 0,
    PIN TEXT NOT NULL,
    STATUS TEXT NOT NULL 
)       
               """)
cursor.executemany("""
INSERT INTO Accounts
(account_number, owner_name, balance, PIN, STATUS)
VALUES (?, ?, ?, ?, ?)
                   """, [
                       
("2001", "User 1", 20000, "4827", "Active"),
("2002", "User 2", 15000, "9153", "Active"),
("2003", "User 3", 8500, "6704", "Active"),
("2004", "User 4", 50000, "2489", "Active"),
("2005", "User 5", 1200, "7316", "Blocked"),
("2006", "User 6", 750, "5942", "Active"),
("2007", "User 7", 32000, "1867", "Active"),
("2008", "User 8", 0, "8421", "Blocked"),
("2009", "User 9", 9500, "3758", "Active"),
("2010", "User 10", 250000, "6294", "Active"),

("2011", "User 11", 4700, "9071", "Active"),
("2012", "User 12", 18000, "4536", "Active"),
("2013", "User 13", 6200, "7185", "Blocked"),
("2014", "User 14", 41000, "2648", "Active"),
("2015", "User 15", 3500, "8392", "Active"),
("2016", "User 16", 100000, "5714", "Active"),
("2017", "User 17", 50, "9463", "Blocked"),
("2018", "User 18", 87000, "3275", "Active"),
("2019", "User 19", 12500, "6841", "Active"),
("2020", "User 20", 6800, "1957", "Active")

])
cursor.execute("""
CREATE TABLE IF NOT EXISTS Transactions(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(account_id) REFERENCES Accounts(ID)
)
""")

conn.commit()
conn.close()