from tkinter import *
from tkinter import messagebox

class Product:
    def __init__(self, pid, name, category, price, quantity):
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

products = []

def add_product():
    try:
        pid = entry_pid.get()
        name = entry_name.get()
        category = entry_category.get()

        if pid == "" or name == "":
            raise ValueError("Product ID and Name cannot be empty")

        price = float(entry_price.get())
        quantity = int(entry_quantity.get())

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        for p in products:
            if p.pid == pid:
                raise Exception("Product ID already exists")

        products.append(Product(pid, name, category, price, quantity))

        messagebox.showinfo("Success", "Product Added Successfully")
        clear_fields()

    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_products():
    listbox.delete(0, END)

    if len(products) == 0:
        listbox.insert(END, "No Products Available")
        return

    listbox.insert(END, "ID | Name | Category | Price | Quantity")
    listbox.insert(END, "-" * 70)

    for p in products:
        listbox.insert(
            END,
            f"{p.pid} | {p.name} | {p.category} | ₹{p.price} | {p.quantity}"
        )

def search_product():
    pid = entry_pid.get()

    try:
        if pid == "":
            raise Exception("Enter Product ID")

        for p in products:
            if p.pid == pid:
                messagebox.showinfo(
                    "Product Found",
                    f"ID : {p.pid}\n"
                    f"Name : {p.name}\n"
                    f"Category : {p.category}\n"
                    f"Price : ₹{p.price}\n"
                    f"Quantity : {p.quantity}"
                )
                return

        raise Exception("Product Not Found")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_product():
    pid = entry_pid.get()

    try:
        for p in products:
            if p.pid == pid:
                products.remove(p)
                messagebox.showinfo("Success", "Product Deleted")
                view_products()
                clear_fields()
                return

        raise Exception("Product Not Found")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def extract_product():
    try:
        pid = entry_pid.get()

        # Quantity field should be empty during extraction
        if entry_quantity.get() != "":
            raise Exception(
                "Invalid Option!\nUse Extract Quantity only."
            )

        qty = int(entry_extract.get())

        if qty <= 0:
            raise ValueError("Extract quantity must be greater than 0")

        for p in products:

            if p.pid == pid:

                if qty > p.quantity:
                    raise Exception(
                        f"Only {p.quantity} item(s) available in stock"
                    )

                p.quantity -= qty

                messagebox.showinfo(
                    "Success",
                    f"{qty} item(s) extracted successfully.\nRemaining Stock = {p.quantity}"
                )

                view_products()
                clear_fields()
                return

        raise Exception("Product Not Found")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

    except Exception as e:
        messagebox.showerror("Error", str(e))

def count_products():
    messagebox.showinfo(
        "Total Products",
        f"Total Products = {len(products)}"
    )

def clear_fields():
    entry_pid.delete(0, END)
    entry_name.delete(0, END)
    entry_category.delete(0, END)
    entry_price.delete(0, END)
    entry_quantity.delete(0, END)
    entry_extract.delete(0, END)

# Main Window
root = Tk()
root.title("Inventory Management System")
root.geometry("850x600")

Label(
    root,
    text="INVENTORY MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
).grid(row=0, column=0, columnspan=3, pady=15)

Label(root, text="Product ID").grid(row=1, column=0, padx=10, pady=5)
entry_pid = Entry(root, width=30)
entry_pid.grid(row=1, column=1)

Label(root, text="Product Name").grid(row=2, column=0, padx=10, pady=5)
entry_name = Entry(root, width=30)
entry_name.grid(row=2, column=1)

Label(root, text="Category").grid(row=3, column=0, padx=10, pady=5)
entry_category = Entry(root, width=30)
entry_category.grid(row=3, column=1)

Label(root, text="Price").grid(row=4, column=0, padx=10, pady=5)
entry_price = Entry(root, width=30)
entry_price.grid(row=4, column=1)

Label(root, text="Quantity").grid(row=5, column=0, padx=10, pady=5)
entry_quantity = Entry(root, width=30)
entry_quantity.grid(row=5, column=1)

Label(root, text="Extract Quantity").grid(row=6, column=0, padx=10, pady=5)
entry_extract = Entry(root, width=30)
entry_extract.grid(row=6, column=1)

Button(root, text="Add Product", width=15,
       command=add_product).grid(row=7, column=0, pady=10)

Button(root, text="View Products", width=15,
       command=view_products).grid(row=7, column=1)

Button(root, text="Search Product", width=15,
       command=search_product).grid(row=7, column=2)

Button(root, text="Delete Product", width=15,
       command=delete_product).grid(row=8, column=0, pady=10)

Button(root, text="Extract Item", width=15,
       command=extract_product).grid(row=8, column=1)

Button(root, text="Clear Fields", width=15,
       command=clear_fields).grid(row=8, column=2)

Button(root, text="Count Products", width=15,
       command=count_products).grid(row=9, column=1, pady=10)

listbox = Listbox(root, width=120, height=15)
listbox.grid(row=10, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()