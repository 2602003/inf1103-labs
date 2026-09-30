def load_inventory():
    orders = []

    try:
        with open("inventory.txt", "r") as f:
            for line in f:
                order_id, product_name, quantity = line.strip().split(",")
                orders.append([
                    int(order_id),
                    product_name,
                    int(quantity)
                ])

    except FileNotFoundError:
        pass

    return orders

def save_inventory(orders):
    with open("inventory.txt", "a") as f:
        for order in orders:
            f.write(f"{order[0]},{order[1]},{order[2]}\n")

def get_valid_input():
    product_name = input("\nEnter Product Name (or type 'quit'): ")

    if product_name.lower() == "quit":
        return "quit"

    quantity = input("Enter Quantity: ")

    if not quantity.isdigit():
        print("Error: Invalid quantity, must be a number.")
        return None

    quantity = int(quantity)

    return product_name, quantity

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(orders, failed_attempts):
    print("\n==========Audit Report==========")
    print(f"Total Transactions Recorded: {len(orders)}")
    print(f"Total Units Processed: {sum(order[2] for order in orders)}")
    print(f"Total Tax Collected: ${sum(calculate_tax(order[2]) for order in orders):.2f}")
    print(f"Failed/Rejected Entries: {failed_attempts}")

orders = load_inventory()
print("Current Orders:\n")
if orders:
    for order in orders:
        print(f"{order[0]}, {order[1]}, {order[2]}")
else:
    print("(No previous orders found)")

inventory = 0

for order in orders:
    inventory += order[2]

failed_entries = 0
history = []
new_orders = []

while True:
    value = get_valid_input()

    if value == "quit":
        save_inventory(new_orders)
        print("Order successfully saved to inventory.txt.\n")
        break

    if value is None:
        failed_entries += 1
        continue

    product_name, quantity = value

    if orders:
        next_order_id = orders[-1][0] + 1
    else:
        next_order_id = 1001

    new_order = [next_order_id, product_name, quantity]
    orders.append(new_order)
    new_orders.append(new_order)

    history.append(quantity)

    inventory = process_delivery(inventory, quantity)
    tax = calculate_tax(quantity)

    print("\nNew Order Added:")
    print(f"{new_order[0]}, {new_order[1]}, {new_order[2]}")
    print(f"Tax: ${tax:.2f} | Total Inventory: {inventory}")
    
generate_report(orders, failed_entries)
