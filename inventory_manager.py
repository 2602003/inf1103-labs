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
            
    return inventory

inventory = load_inventory()