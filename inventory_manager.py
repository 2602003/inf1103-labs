import json
# inventory = [
#     {
#         "product_id": "P001",
#         "product_name": "Laptop",
#         "price": 1200.00,
#         "stock_quantity": 15,
#     },
#     {
#         "product_id": "P002",
#         "product_name": "Mouse",
#         "price": 25.50,
#         "stock_quantity": 40,
#     },
#     {
#         "product_id": "P003",
#         "product_name": "Keyboard",
#         "price": 45.00,
#         "stock_quantity": 25,
#     }
# ]

def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inventory_data

    except FileNotFoundError:
        return []

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "product_id": product_id,
        "product_name": product_name,
        "price": price,
        "stock_quantity": stock
    }
    inventory.append(new_product)
    print("\nProduct added successfully!")

def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID to update: ")
    for product in inventory:
        if product["product_id"] == product_id:
            print(f"Product Found:\nName: {product["product_name"]}\nCurrent Stock: {product["stock_quantity"]}")
            new_stock_quantity = int(input("\nEnter new stock quantity: "))
            product["stock_quantity"] = new_stock_quantity
            print("\nStock updated successfully!")
            return
    print("Product not found.")

def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["product_id"] == product_id:
            print("Product Found")
            print("-" * 26)
            print(f"ID: {product["product_id"]}\nName: {product["product_name"]}\nPrice: ${product["price"]:.2f}\nStock: {product["stock_quantity"]}")
            print("-" * 26)
            return

    print("Product not found.")

def display_all(inventory):
    if not inventory:
        print("No products in the inventory.")
        return

    print("Current Inventory:")
    for product in inventory:
        print(f"Product ID: {product["product_id"]}| Name: {product["product_name"]}| Price: ${product["price"]:.2f}| Stock Quantity: {product["stock_quantity"]}")

def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

def main():
    print("\nINVENTORY MANAGEMENT SYSTEM\n")
    inventory = load_inventory()
    while True:
        print("\n-----------MENU-----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("-" * 26)

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            print("-" * 26)
            display_all(inventory)
            print("-" * 26)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

main()