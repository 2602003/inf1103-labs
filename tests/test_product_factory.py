from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

supplier = Supplier("S001", "ABC Supplies", "abc@email.com")

# Test 1: Create a PhysicalProduct
physical = ProductFactory.create(
    "Physical", "P001", "Laptop", 1200.0, 20,
    supplier, weight=2.1
)

print("Test 1: Physical Product")
print(isinstance(physical, PhysicalProduct))
physical.display_information()

# Test 2: Create a DigitalProduct
digital = ProductFactory.create(
    "Digital", "P002", "Photo Editor", 49.90, 100,
    supplier, download_size=450.0
)

print("\nTest 2: Digital Product")
print(isinstance(digital, DigitalProduct))
digital.display_information()

# Test 3: Unknown product type
print("\nTest 3: Unknown Product Type")

try:
    ProductFactory.create(
        "Service", "S001", "Installation", 30.0, 5,
        supplier
    )
except ValueError as e:
    print(f"Expected error: {e}")
