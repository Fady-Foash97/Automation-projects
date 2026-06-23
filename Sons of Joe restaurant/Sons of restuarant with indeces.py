import json
from pathlib import Path
import time
print("Welcome to Sons of Joe restaurant, home to the most tasty food in the world:")
print("menu:")
food_menu = {"Cheese burger": [3, "Sandwich"],
            "Chicken burger": [3,"Sandwich"],
            "Margarita Pizza": [8, "Pizza"],
            "Shrimp": [6, "Seafood"],
            "Pepperoni pizza": [10, "Pizza"],
            "Pasta": [10, "Pasta"],
            "Pasta with sauce": [6, "Pasta"],
            "Koshary": [2, "Vegetarian"],
            "Fava beans": [10, "Vegetarian"],
            "Basmati rice": [2, "Rice"],
            "Molokhia": [4, "Vegetarian"],
            "Greek salad": [10, "Vegetarian"],
            "Tacos": [6, "Tacos"],
            "Sardine fish": [4, "Seafood"]}
menu_extra = {"Cola": [2.50, "Drink"],
                  "Bottle of Water": [3, "Drink"],
                  "French fries": [3, "Snacks"]}
total_price = 0
food_item = ""
extra_item = ""
delivery_fee = 2
choice = ""
def menu():
   for i, (food, values) in enumerate(food_menu.items(), 1):
        print(f"{i}- {food}: ${values[0]}, type: {values[1]}")
def order():
    global total_price, food_item, extra_item, choice
    while True:
      food_index = list(food_menu.keys())  
      choice = int(input("What would you like to order? "))
      if 1 <= choice <= len(food_index):
          food_item = food_index[choice - 1]
          price = food_menu[food_item][0]
          print(f"You have ordered: {food_item}")
          print(f"Price: ${price}")
          total_price += food_menu[food_item][0]
          time.sleep(3)
          break
      else:
           print("This item is not avaliable.")
           time.sleep(3)
           print("Choose from the following")
           menu() 
    request = input("Do you want something with it? yes or no? ")
    if request == "yes":
         while True:
          for i, (key, values) in enumerate(menu_extra.items(), 1):
              print(f"{i}- {key}: ${values[0]}, {values[1]}")
          extra_index = list(menu_extra.keys())
          choice = int(input("What would you like to order? "))
          if 1 <= choice <= len(extra_index):
               extra_item = extra_index[choice - 1]
               price = menu_extra[extra_item][0]
               print(f"You have ordered: {extra_item}")
               print(f"Price: {menu_extra[extra_item][0]}")
               time.sleep(3)
               total_price += menu_extra[extra_item][0]
               print(f"total price is ${total_price}")
               time.sleep(3)
               break
          else:
               print("This item is not avaliable")
               print("Choose from the following")
               print(f"{key}: price: ${values[0]}, {values[1]}")
               time.sleep(3)
    choice = input("pickup or delivery? ")
    if choice == "delivery":
         total_price += delivery_fee
         print(f"total price is ${total_price}\n")
         time.sleep(3)
    elif choice == "pickup":
          print(f"total price is ${total_price}\n")
          time.sleep(3)
    return True

def save_data():
    global food_item
    data_entries = []
    if Path("Restaurant_data.json").is_file():
      with open("Restaurant_data.json", "r") as file:
       data_entries = json.load(file)
    else:
      data_entries = []
    data = {"Food": food_item,
           "Delivery": True if choice == "delivery" else False,
           "Delivery_fee": f"${delivery_fee}" if choice == "delivery" else 0, 
           "Food price": f"${food_menu[food_item][0]}",
           "Extra": extra_item if extra_item in menu_extra else "null",
           "Extra price": f"${menu_extra[extra_item][0]}" if extra_item in menu_extra else "null",
           "Total Price": f"${total_price}"}
    data_entries.append(data)
    with open("Restaurant_data.json", "w") as data_list:
       json.dump(data_entries, data_list, indent=3)
def receipt():
    print("Sons of Joe restaurant")
    print("-----------------")
    time.sleep(3)
    print(f"Food: {food_item}")
    print(f"Price: ${food_menu[food_item][0]}")
    time.sleep(3)
    if extra_item in menu_extra:
     print(f"Extra: {extra_item}")      
     print(f"Price: ${menu_extra[extra_item][0]}")
     time.sleep(3) 
    if choice == "delivery":
        print(f"Delivery fee: ${delivery_fee}")
        print("-----------------")
        print(f"Total price: ${total_price}")
        time.sleep(3)
    else:
        print("-----------------")
        print(f"Total price: ${total_price}")
        time.sleep(3) 
menu()
if order():
 save_data()
 receipt()