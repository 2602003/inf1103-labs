import json
from inventory import Inventory
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from supplier import Supplier
from order import Order

def build_product_from_dict(item: dict) -> Product:
    supplier_data = item["supplier"]

    supplier = Supplier(
        supplier_data["supplier_id"],
        supplier_data["name"],
        supplier_data["contact_email"]
    )
    product_type = item["type"]
    product_id = item["product_id"]
    product_name = item["product_name"]
    price = float(item["price"])
    stock = int(item["stock_quantity"])
    
    if product_type == "Physical":
        weight = float(item["weight"])
        return PhysicalProduct(product_id, product_name, price, stock, weight, supplier)
    elif product_type == "Digital":
        download_size = float(item["download_size"])
        return DigitalProduct(product_id, product_name, price, stock, download_size, supplier)
    else:
        raise ValueError("Invalid product type.")

def load_inventory(inventory: Inventory) -> None:
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
            for item in inventory_data:
                product = build_product_from_dict(item)
                inventory.add_product(product)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
    except FileNotFoundError:
        with open("inventory.json", "w") as f:
            json.dump([], f, indent=4)
        print("inventory.json not found. Created a new inventory.json file.")

    except (json.JSONDecodeError, KeyError, ValueError):
        with open("inventory.json", "w") as f:
            json.dump([], f, indent=4)
        print("inventory.json is empty or corrupted. Reset with empty inventory.")

def save_inventory(inventory: Inventory) -> None:
    inventory_data = []
    for product in inventory.get_products():
        inventory_data.append(product.to_dict())
    with open("inventory.json", "w") as f:
        json.dump(inventory_data, f, indent=4)

def add_product_menu(inventory: Inventory) -> None:
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    supplier_id = input("Supplier ID: ")
    supplier_name = input("Supplier Name: ")
    supplier_email = input("Supplier Contact Email: ")
    supplier = Supplier(supplier_id, supplier_name, supplier_email)
    if inventory.search_product(product_id) is not None:
        print(f"\nProduct ID {product_id} already exists.")
        return
    print("Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")
    product_type = input("Enter your choice (1 or 2): ")
    if product_type not in ("1", "2"):
        print("\nInvalid product type.")
        return
    
    product_name = input("Product Name: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        if product_type == "1":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(product_id, product_name, price, stock, weight, supplier)
        else:
            download_size = float(input("Download Size (MB): "))
            product = DigitalProduct(product_id, product_name, price, stock, download_size, supplier)
        inventory.add_product(product)
        print("\nProduct added successfully!")
    except ValueError as e:
        print(f"\nCould not add product: {e}")

def update_stock_menu(inventory: Inventory) -> None:
    print("\nUpdate Stock")
    product_id = input("Enter Product ID to update: ")
    product = inventory.search_product(product_id)
    if product:
        print(f"\nProduct Found:\nName: {product.get_name()}\nCurrent Stock: {product.get_stock()}")
        try:
            new_stock_quantity = int(input("\nEnter new stock quantity: "))
            product.update_stock(new_stock_quantity)
            print("\nStock updated successfully!")
        except ValueError as e:
            print(f"\nCould not update stock: {e}")
        return
    else:
        print("Product not found.")

def search_product_menu(inventory: Inventory) -> None:
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product:
        print("Product Found")
        print("-" * 26)
        product.display_information()
        print(f"Fulfillment: {product.get_fulfilment_info()}")
        if isinstance(product, CanBeShipped):
            print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
        print("-" * 26)
    else:
        print("Product not found.")

def create_order_menu(inventory: Inventory) -> None:
    print("\nCreate New Order")
    order_id = input("Order ID: ")
    order = Order(order_id)
    while True:
        product_id = input("\nEnter Product ID: ")
        product = inventory.search_product(product_id)
        if product is None:
            print("Product not found.")
            continue
        print(f"Product: {product.get_name()}")
        print(f"Price: ${product.get_price():.2f}")
        try:
            quantity = int(input("Quantity: "))
            order.add_order_line(product, quantity)
            print("Product added to order.")
        except ValueError as e:
            print(f"Could not add product to order: {e}")
        another = input("Add another product? (y/n): ")
        if another.lower() == "n":
            break
    print(f"\nOrder ID: {order_id}")
    print(f"Order Total: ${order.calculate_total():.2f}")

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
        print("6. Create New Order")
        print("7. Exit")
        print("-" * 26)

        choice = input("\nEnter your choice (1-7): ")

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
            create_order_menu(inventory)
        elif choice == "7":
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