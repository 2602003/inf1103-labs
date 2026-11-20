from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount

supplier = Supplier("S001", "ABC Supplies", "abc@email.com")
product = PhysicalProduct("P001", "Desk Lamp", 250.0, 10, 1.0, supplier)

order = Order("O001")
order.add_order_line(product, 1)

print(f"No Discount: ${order.calculate_total():.2f}")

order.set_discount(BulkDiscount(200, 20))
print(f"Bulk Discount: ${order.calculate_total():.2f}")
assert order.calculate_total() == 230.0

order.set_discount(PercentageDiscount(10))
print(f"Percentage Discount: ${order.calculate_total():.2f}")
assert order.calculate_total() == 225.0

order.set_discount(StudentDiscount())
print(f"Student Discount: ${order.calculate_total():.2f}")
assert order.calculate_total() == 237.50