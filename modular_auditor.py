inventory = 0
failed_entries = 0
deliveries_processed = 0

def get_valid_input():
    entry = input("Enter stock quantity (or type 'quit'): ")

    if entry.lower() == "quit":
        return "quit"

    if not entry.isdigit():
        print("Error: Invalid input, must be a number.")
        return None
    quantity = int(entry)

    if quantity < 0:
        print("Error: Negative values not allowed.")
        return None
    return quantity

def process_delivery(current_total, new_value):
    return current_total + new_value

while True:
    value = get_valid_input()

    if value == "quit":
        break

    if value is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, value)
    deliveries_processed += 1
    print(f"Added {value} units. Current inventory: {inventory}")

print("==========Audit Report==========")
print(f"Total Deliveries Processed: {deliveries_processed}")
print(f"Failed/Rejected Entries: {failed_entries}")