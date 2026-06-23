import json
from pathlib import Path
print("أهلا بكم في محل البلاستيك")
products = {
      "كيلو شنطة أبيض أو أسود" : 45, "كيلو شنطة شفاف": 85, "بيور أسود": 85, "كياس لبن": 90, "كيلو بدلة": 80, "كيلو قميص": 80, "كيلو زبالة": 55,
      "مناديل": 85, "عمود قهوة": 20, "عمود شاي": 25, "عمود مياه صغير": 22, "عمود مياه وسط": 27, "عمود مياه كبير": 35, "شاليموه زيج زاج": 10,
      "شاليموه مانجة": 30, "شاليموه عادي": 17, "شاليموه حركات جملة": 15, "شاليموه حركات قطاعي": 20, "تمن فوم": 25, "ميني تمن فوم": 25,
      "ربع فوم": 35, "ميني ربع فوم": 35, "نص فوم": 45, "كيلو فوم": 65, "مفرش سفرة": 30, "ورق زبدة": 10, "مفرش ألمونيا": 32,
      "طبق جاتوه بلاستيك صغير": 2, "طبق جاتوه بلاستيك كبير": 2.50, "100 تمن فوم بلاستيك 530 جم": 62, "100 ربع فوم بلاستيك 900 جم": 98,
      "100 نص فوم بلاستيك 1200 جم": 148, "ألمونيوم 20 متر": 75, "ألمونيوم 10 متر": 52, "فويل 700 جم": 150, "فويل 100 جم": 405,
      "كيس فرن حراري": 10, "جوانتي": 10, "معلقة صغيرة شفاف": 10, "شوك شفاف بيور": 15, "شوك ملون": 20,  "طبق جاتوه عيد ميلاد عادي": 1,
      "طبق جاتوه عيد ميلاد مربع": 2, "نيلون تخزين": 10, "سلوفان": 85, "سلوفان بلزق": 150, "شيش": 10
   }
def menu():   
 print("\n قائمة المنتجات: \n")
 for product, price in products.items():
     print(f"-{product}: {price} جنيه")
def order():
 while True:
      product_input = input("\nأضف منتج:  ")
      if product_input in products: 
          product_price = products[product_input]
          total_cost += product_price
          print(f"تمت اضافة منتج {product_input} بسعر {product_price} جنيه")
          print(f"اجمالي السعر: {total_cost} جنيه ")
      else:
          print("المنتج غير موجود")
      repeat = input("هل تريد اضافة منتج جديد؟ نعم أم لا؟")
      if repeat != "نعم":
          break
def save_data():
 global product_input, product_price, total_cost
 Cart = []
 if Path("محل بلاستيك.json").is_file():
      with open("محل بلاستيك.json", "r") as file:
       Cart = json.load(file)
 else:
      Cart = []
 data = {" المنتجات": product_input,
         "اجمالي السعر": total_cost}
 Cart.append(data)
 with open("محل بلاستيك.json", "w") as data_list:
       json.dump(Cart, data_list, indent=3)
menu()
order()
save_data()