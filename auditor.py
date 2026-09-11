inventory = 0
failed_entries = 0

while True:
    entry = input("Enter stock quantity (or type 'quit'): ")

    if entry.lower() == "quit":
        break

    if not entry.isdigit():
        print("Error: Invalid input, must be a number.")
        failed_entries += 1
        continue

    quantity = int(entry)

    if quantity < 0:
        print("Error: Negative values not allowed.")
        failed_entries += 1
        continue

    inventory += quantity

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeded 500 units.")
        break

print(f"Total Units Processed: {inventory}")
print(f"Failed/Rejected Entries: {failed_entries}")