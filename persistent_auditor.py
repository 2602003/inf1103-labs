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

def generate_report(total_deliveries, failed_attempts):
    print("==========Audit Report==========")
    print(f"Total Deliveries Processed: {total_deliveries}")
    print(f"Failed/Rejected Entries: {failed_attempts}")

orders = load_inventory()
print("Current Orders:\n")
for order in orders:
    print(f"{order[0]}, {order[1]}, {order[2]}")

inventory = 0

for order in orders:
    inventory += order[2]

failed_entries = 0
deliveries_processed = 0
history = []

while True:
    value = get_valid_input()

    if value == "quit":
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

    history.append(quantity)

    inventory = process_delivery(inventory, quantity)
    tax = calculate_tax(quantity)
    deliveries_processed += 1

    print("\nNew Order Added:")
    print(f"{new_order[0]}, {new_order[1]}, {new_order[2]}")
    print(f"Current inventory: {inventory}.")
    print(f"Tax: {tax:.2f}")
    
generate_report(deliveries_processed, failed_entries)
