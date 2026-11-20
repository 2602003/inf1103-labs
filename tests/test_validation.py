from product_factory import ProductFactory
from order_line import OrderLine
from supplier import Supplier

supplier = Supplier("S001", "ABC Supplies", "abc@email.com")

# Test 1: Invalid price
try:
    ProductFactory.create(
        "Physical", "P001", "Laptop", -100.0, 10,
        supplier, weight=2.1
    )
except ValueError as e:
    print(f"Test 1 passed: {e}")
else:
    raise AssertionError("Negative price should raise ValueError.")

# Test 2: Invalid stock
try:
    ProductFactory.create(
        "Digital", "D001", "Photo Editor", 49.90, -5,
        supplier, download_size=450.0
    )
except ValueError as e:
    print(f"Test 2 passed: {e}")
else:
    raise AssertionError("Negative stock should raise ValueError.")

# Test 3: Invalid OrderLine quantity
product = ProductFactory.create(
    "Physical", "P002", "Mouse", 25.50, 20,
    supplier, weight=0.1
)

try:
    OrderLine(product, 0)
except ValueError as e:
    print(f"Test 3 passed: {e}")
else:
    raise AssertionError("Zero order quantity should raise ValueError.")