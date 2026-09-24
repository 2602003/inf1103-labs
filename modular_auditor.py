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

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_deliveries, failed_attempts):
    print("==========Audit Report==========")
    print(f"Total Deliveries Processed: {total_deliveries}")
    print(f"Failed/Rejected Entries: {failed_attempts}")

while True:
    value = get_valid_input()

    if value == "quit":
        break

    if value is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, value)
    tax = calculate_tax(value)
    deliveries_processed += 1
    print(f"Added {value} units.\nCurrent inventory: {inventory}.\nTax: {tax:.2f}")
    
generate_report(deliveries_processed, failed_entries)
