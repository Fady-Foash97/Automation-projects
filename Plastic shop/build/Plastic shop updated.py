import json
from pathlib import Path
from arprint import arprint, arinput
arprint("أهلا بكم في محل البلاستيك")
products = {
    "شنط و كياس": {
        "كيلو أبيض و أسود": 45,
        "كيلو شفاف": 85,
        "كيلو بيور أسود": 85,
        "كيلو زبالة": 55
    },
    "كوبايات": {
        "عمود قهوة": 20,
        "عمود شاي": 25,
        "عمود مياه صغير": 22,
        "عمود مياه وسط": 27,
        "عمود مياه كبير": 35
    },
    "شاليموه": {
        "شاليموه زيج زاج": 10,
        "شاليموه مانجة": 30,
        "شاليموه جركات": 20 ,
        "شاليموه عادي": 17
    },
    "أطباق": {
        "تمن فوم": 25,
        "ربع فوم": 35,
        "نص فوم": 45,
        "كيلو فوم": 65,
        "طبق جاتوه بلاستيك صغير": 2,
        "طبق جاتوه بلاستيك كبير": 2.50,
        "طبق جاتوه عيد ميلاد عادي": 1,
        "طبق جاتوه عيد ميلاد مربع": 2
    },
    "أدوات طعام": {
        "مفرش سفرة": 30,
        "ورق زبدة": 10,
        "مفرش ألمونيا": 35,
        "شيش": 10,
        "جوانتي": 10
    },
    "أطباق خاصة": {
        "100 تمن فوم بلاستيك 530 جم": 62,
        "100 ربع فوم بلاستيك 900 جم": 98
    }
}
products_list = []
prices_list = []
total_cost = 0
def category():
    arprint("أنواع المنتجات:\n")
    category = list(products.keys())
    for i, types in enumerate(category, 1):
        arprint(f"{i}- {types}")
    return category
def order():
    global total_cost, products_list, prices_list
    while True:
       categories = category()
       type_choice = int(arinput("ما هو نوع المنتج الذي تريده؟\n").strip())
       arprint("")
       if type_choice == 0:
            break
       else:
           category_name = categories[type_choice - 1]
           arprint("أسامي المنتجات:")
           items = list(products[category_name].items())
           for i, (product, price) in enumerate(items, 1):
                 arprint(f"{i}- {product}: {price}")
           product_choice = int(arinput("اختر المنتج:\n").strip())
           if product_choice == 0:
               break
           else:
               product_name, price = items[product_choice - 1]
               arprint(f"لقد اخترت: {product_name} بسعر {price}")
               products_list.append(product_name)
               prices_list.append(price)
               total_cost += price
               arprint(f"اجمالي السعر: {total_cost}")
           question = arinput("هل تريد اضافة منتج جديد؟ نعم أم لا؟\n").strip()
           if question == "لا":
               break
def save_data():
    global products_list, prices_list, total_cost
    cart = []
    if Path("محل البلاستيك.Json").is_file():
      try:
         with open("محل البلاستيك.Json", "r", encoding="utf-8") as file:
           cart = json.load(file)
      except json.JSONDecodeError:
          cart = []
    else:
        cart = []
    data = {"أسامي المنتجات": products_list,
           "الأسعار": prices_list,
           "اجمالي السعر": total_cost}
    cart.append(data)
    with open("محل البلاستيك.Json", "w", encoding="utf-8") as file:
        json.dump(cart, file, ensure_ascii = False, indent=4)
order()
save_data()
