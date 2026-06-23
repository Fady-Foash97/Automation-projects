import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ==================
# Database
# ==================
conn = sqlite3.connect("Plastic shop database.db")
cursor = conn.cursor()

# ==================
# Variables 
# ==================
cart = []
total_price = 0

# ==================
# Functions
# ==================

def load_categories():
    
    cursor.execute("""
        SELECT DISTINCT النوع
        FROM المنتجات
    """)
    
    categories = [row[0] for row in cursor.fetchall()]
    
    category_combo["values"] = categories

def update_products(event=None):
    
    selected_category = category_var.get()
    
    cursor.execute("""
        SELECT اسم_المنتج
        FROM المنتجات
        WHERE النوع = ?
    """, (selected_category,))
    
    products = [row[0] for row in cursor.fetchall()]
    
    product_combo["values"] = products
    
    product_var.set("")
    price_label.config(text="السعر: --")
    
def show_price(event=None):
    
    product = product_var.get()
    
    cursor.execute("""
            SELECT السعر
            FROM المنتجات
            WHERE اسم_المنتج = ?
            """, (product,))
    
    result = cursor.fetchone()
    
    if result:
        price_label.config(
            text=f"السعر: {result[0]} جنيه"
        )

def add_to_cart():
    global total_price
    product = product_var.get()
    
    if not product:
        messagebox.showwarning(
            "تنبية",
            "اختر منتج أولا"
        )
        
    cursor.execute("""
            SELECT السعر
            FROM المنتجات
            WHERE اسم_المنتج = ?
            """, (product,))
    
    price = cursor.fetchone()[0]
    
    cart.append((product, price))
    
    listbox.insert(
        tk.END,
        f"{product} - {price} جنيه"
    )
    
    total_price += price
    
    total_label.config(
        text=f"الاجمالي: {total_price} جنيه"
    )

def save_order():
    
    if not cart:
        messagebox.showwarning(
            "تنبيه",
            "السلة فارغة"
        )
        return
    products_text = ",  ".join([product for product, _ in cart])
    total = sum([price for _ , price in cart])
    cursor.execute("""
            INSERT INTO الطلبات
            (اسامي_المنتجات, السعر)
            VALUES (?, ?)
        """, (products_text, total))
    conn.commit()
    
    messagebox.showinfo(
        "نجاح",
        "تم حفظ الطلب"
    )

# ==================
# Title and size
# ==================
root = tk.Tk()

root.title("محل البلاستيك")

root.geometry("700x500")
root.configure(bg="#EEF7EE")
root.iconbitmap("D:\Programming\python\Automation\Plastic_bag.ico")
# ==================
# Frame 
# ==================


main_frame = tk.Frame(
    root,
    bg="#FFFFFF",
    width=600,
    height=400
)


main_frame.place(relx=0.5, rely=0.5, anchor="center")
main_frame.pack_propagate(False)
# ==================
# GUI
# ==================

# نوع_المنتج

category_label = tk.Label(
    main_frame,
    text="نوع المنتج"
)

category_label.grid(row=0, column=0, pady=5)

category_var = tk.StringVar()

category_combo = ttk.Combobox(
    main_frame,
    textvariable=category_var,
    state="readonly"
)

category_combo.grid(row=1, column=0, sticky="ew")

category_combo.bind("<<ComboboxSelected>>", update_products)

#  المنتج

product_label = tk.Label(
    main_frame,
    text="المنتج"
)

product_label.grid(row=2, column=0, pady=5)

product_var = tk.StringVar()

product_combo = ttk.Combobox(
    main_frame,
    textvariable=product_var,
    state="readonly"
)

product_combo.grid(row=3, column=0, sticky="ew")

product_combo.bind("<<ComboboxSelected>>", show_price)

#السعر

price_label = tk.Label(
    main_frame,
    text="السعر: --",
    font=("Arial", 12)
)

price_label.grid(row=4, column=0, pady=10)
# زر اضافة

button = tk.Button(
    main_frame,
    text="اضافة للسلة",
    command=add_to_cart
)

button.grid(row=5, column=0, pady=10)
# السلة

listbox = tk.Listbox(
    main_frame,
    width=50,
    height=10
)

listbox.grid(row=6, column=0, sticky="nsew")

# الاجمالي

total_label = tk.Label(
    main_frame,
    text="الاجمالي: 0 جنيه",
    font=("Arial", 12, "bold")
)

total_label.grid(row=7, column=0, pady=10)

# حفظ

save = tk.Button(
    main_frame,
    text="حفظ الطلب",
    command=save_order
)

save.grid(row=8, column=0, pady=10)

load_categories()



root.mainloop()

conn.close()

