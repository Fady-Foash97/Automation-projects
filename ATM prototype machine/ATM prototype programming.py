import sqlite3
import time

conn = sqlite3.connect("D:\Programming\python\Automation\ATM machine\ATM.db")
cursor = conn.cursor()
def login():
  print("Welcome to the bank: ")
  time.sleep(3)
  while True:
   account_number = input("Enter account number: ")
   pin = input("Enter PIN: ")
   
   cursor.execute("""
   SELECT * 
   FROM Accounts
   WHERE account_number = ? and PIN = ?
   """, (account_number, pin))
   
   account = cursor.fetchone()
   
   if account:
       print("Login successful!")
       print(f"Welcome {account[2]}") 
       time.sleep(3)
       return account
   else:
       print("Invalid account number or PIN")
       print("Try again")
       time.sleep(3)
       continue
account = login()
def message():
 print("====== ATM MENU ======\n")
 print("1-Withdraw\n2-Deposit\n3-Balance Inquiry\n4-Exit\n")
 print("======================")
 time.sleep(3)
while True:
 try:
  message()
  choice = int(input("Choose: "))
 except ValueError:
  print("Please enter a valid number")
  time.sleep(2)
  continue
 if choice == 1:
     print("Withdraw Money")
     while True:
      amount = float(input("Amount to withdraw: "))
      if amount > account[3]:
          print("Insufficient funds")
          time.sleep(3)
          continue
      else:
         new_balance = account[3] - amount 
         
         cursor.execute("""
         UPDATE Accounts
         SET balance = ?
         WHERE ID = ?
         """, (new_balance, account[0]))
         
         cursor.execute("""
         INSERT INTO Transactions
         (account_id, transaction_type, amount)
         VALUES (?, ?, ?)
         """, (account[0], "Withdraw", amount))
         
         conn.commit()
         
         account = (
             account[0],
             account[1],
             account[2],
             new_balance,
             account[4],
             account[5]
         )
         
         print(f"Withdrawl successful. New balance: {new_balance}")
         time.sleep(3)
         print("Thank you for using our system")
         time.sleep(3)
         break
 elif choice == 2:
     while True:
      print("Deposit Money")
      amount = float(input("Amount to deposit: "))
      
      new_balance = account[3] + amount
      
      cursor.execute("""
             UPDATE Accounts
             SET balance = ?
             WHERE ID = ?
             """, (new_balance, account[0]))
      
      cursor.execute("""
             INSERT INTO Transactions
             (account_id, transaction_type, amount)
             VALUES (?, ?, ?)
             """, (account[0], "Deposit", amount))
      
      conn.commit()
      
      account = (
              account[0],
              account[1],
              account[2],
              new_balance,
              account[4],
              account[5]
          )
      
      print(f"Deposit successful. New balance: {new_balance}")
      time.sleep(3)
      print("Thank you for using our system")
      time.sleep(3)
      break
 elif choice == 3:
     print(f"Current balance: {account[3]}")
     time.sleep(4)
 elif choice == 4:
     print("Goodbye")
     time.sleep(3)
     break
 else:
     print("Invalid number, try again")
     time.sleep(3)
     continue
 