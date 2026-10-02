import json
# inventory = [
#     {
#         "product_id" : "P001",
#         "product_name" : "Laptop",
#         "price" : 1200.00,
#         "stock_quantity" : 15,
#     },
#     {
#         "product_id" : "P002",
#         "product_name" : "Mouse",
#         "price" : 25.50,
#         "stock_quantity" : 40,
#     },
#     {
#         "product_id" : "P003",
#         "product_name" : "Keyboard",
#         "price" : 45.00,
#         "stock_quantity" : 25,
#     }
# ]

def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
            print("inventory.json found.")
            print("Inventory loaded succuessfully.")
            return inventory_data

    except FileNotFoundError:
            return []

def add_products(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_product)
    print("Product added successfully!")

def update_stock():
    print("Update Stock")
    product_id = input("Enter Product ID to update: ")
    for product in inventory:
        if product["product_id"] == product_id:
            print(f"Product Found:\nName: {product['product_name']}\nCurrent Stock: {product['stock_quantity']}")
            new_stock_quantity = int(input("Enter new stock quantity: "))
            product["stock_quantity"] = new_stock_quantity
            print("Stock updated successfully!")
            return
    print("Product not found.")

def search_product():
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["product_id"] == product_id:
            print("Product Found")
            print("-"*25)
            print(f"ID: {product['product_id']}\nName: {product['product_name']}\nPrice: ${product['price']:.2f}\nStock: {product['stock_quantity']}")
            print("-"*25)
            return

    print("Product not found.")

def display_all(inventory):
    if not inventory:
        print("No products in the inventory.")
        return

    print("Current Inventory:")
    for product in inventory:
        print(f"Product ID: {product['product_id']}| Name: {product['product_name']}| Price: ${product['price']:.2f}| Stock Quantity: {product['stock_quantity']}")

inventory = load_inventory()