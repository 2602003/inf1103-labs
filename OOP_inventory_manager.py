import json
from product import Product
from inventory import Inventory

def load_inventory(inventory: Inventory):
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
            for item in inventory_data:
                product_id = item["product_id"]
                product_name = item["product_name"]
                price = float(item["price"])
                stock = int(item["stock_quantity"])
                product = Product(product_id, product_name, price, stock)
                inventory.add_product(product)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
    except FileNotFoundError:
        with open("inventory.json", "w") as f:
            json.dump([], f, indent=4)
        print("inventory.json not found. Created a new inventory.json file.")

    except (json.JSONDecodeError, KeyError):
        with open("inventory.json", "w") as f:
            json.dump([], f, indent=4)
        print("inventory.json is empty or corrupted. Reset with empty inventory.")

def save_inventory(inventory: Inventory):
    inventory_data = []
    for product in inventory.get_products():
        inventory_data.append(product.to_dict())
    with open("inventory.json", "w") as f:
        json.dump(inventory_data, f, indent=4)

def add_product_menu(inventory: Inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    product = Product(product_id, product_name, price, stock)
    inventory.add_product(product)
    print("\nProduct added successfully!")

def update_stock_menu(inventory: Inventory):
    print("Update Stock")
    product_id = input("Enter Product ID to update: ")
    product = inventory.search_product(product_id)
    if product:
        print(f"\nProduct Found:\nName: {product.get_name()}\nCurrent Stock: {product.get_stock()}")
        new_stock_quantity = int(input("\nEnter new stock quantity: "))
        product.update_stock(new_stock_quantity)
        print("\nStock updated successfully!")
        return
    else:
        print("Product not found.")

def search_product_menu(inventory: Inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product:
        print("Product Found")
        print("-" * 26)
        product.display_information()
        print("-" * 26)
    else:
        print("Product not found.")



def main():
    print("\nINVENTORY MANAGEMENT SYSTEM\n")
    inventory = Inventory()
    load_inventory(inventory)
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
            inventory.display_all()
            print("-" * 26)
        elif choice == "2":
            add_product_menu(inventory)
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
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

if __name__ == "__main__":
    main()