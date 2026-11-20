import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0

    try:
        file = open(path, newline="")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                try:
                    product_type, product_id, name, price, stock = row

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        float(price),
                        int(stock),
                        supplier
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as e:
                    print(f"Skipped invalid row {row}: {e}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")


# Test 1: Existing CSV file
supplier = Supplier("S001", "ABC Supplies", "abc@email.com")
inventory = Inventory()

print("Test 1: Loading products.csv")
load_products("tests/products.csv", inventory, supplier)

assert len(inventory.get_products()) == 3

# Test 2: Missing CSV file
inventory = Inventory()

print("\nTest 2: Renamed CSV file")
load_products("tests/missing_products.csv", inventory, supplier)

assert len(inventory.get_products()) == 0