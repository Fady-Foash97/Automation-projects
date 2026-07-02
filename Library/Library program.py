import sqlite3
import time 
conn = sqlite3.connect("D:\Programming\python\Automation\Library\Library program.db")
cursor = conn.cursor()
def login():
    print("Welcome to our library: ")
    time.sleep(3)
    name = input("Enter account name: ").strip()
    cursor.execute("""
    SELECT ID 
    FROM Users
    WHERE User_name = ?
    """, (name,))
    user = cursor.fetchone()
    if user:
     print(f"\nWelcome back {name}")
     time.sleep(3)
    else:
        cursor.execute("""
        INSERT INTO users(User_name)
        VALUES (?)               
        """, (name,))
        conn.commit()
        print(f"\nWelcome, {name}!")
        time.sleep(3)
    return name
def category():
    cursor.execute("""
        SELECT DISTINCT TYPE
        FROM Books 
        """)
    
    types = cursor.fetchall()
    while True:
     try:
      for i, t in enumerate(types, start=1):
          print(f"{i}. {t[0]}")
      choice = int(input("Choose a type: "))
      selected_type = types[choice - 1][0]
      print(f"Selected type: {selected_type}")
      time.sleep(3)
      return selected_type
     except IndexError:
      print("Invalid number.")
      time.sleep(3)
def book():
    name = login()
    selected_books = []
    while True:
     selected_type = category()
     cursor.execute("""
         SELECT Book_name 
         FROM Books
         WHERE Type = ?
         """, (selected_type,))
     
     books = cursor.fetchall()
     while True:
      try:
       for i, book in enumerate(books, start=1):
             print(f"{i}- {book[0]}")
       time.sleep(3)       
       choice = int(input("What book do you want to buy?\n"))
       selected_book = books[choice - 1][0]
       selected_books.append(selected_book)
      except IndexError:
          print("Invalid number.")
          time.sleep(3)
          continue
      cursor.execute("""
             SELECT ID 
             FROM users
             WHERE user_name = ?
             """, (name,))
      user_id = cursor.fetchone()[0]
      cursor.execute("""
             SELECT ID
             FROM Books
             WHERE Book_name = ?        
             """, (selected_book,))
      book_id = cursor.fetchone()[0]
      cursor.execute("""
             INSERT INTO Purchased_books 
             (User_ID, Book_ID) 
             VALUES (?, ?)
             """, (user_id, book_id))
      conn.commit()
      print(f"Customer: {name}\nSelected book:{selected_book}")
      time.sleep(3)
      conn.close()
      question = input("Do you want to buy another book? yes or no?\n")
      if question == "yes":
          continue
      elif question == "no":
          print("Thank you for visiting our library")
          time.sleep(3)
          break
     return name, selected_books
book()