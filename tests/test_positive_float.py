from OOP_part2_inventory_manager import get_positive_float

print("Test: Positive Float Input")
print("Enter abc, then -5, then 12.50")

result = get_positive_float("Price: ")

print(f"Returned value: {result}")