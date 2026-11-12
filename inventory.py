from product import Product

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if self.search_product(product.get_id()) is not None:
            raise ValueError(f"Product ID {product.get_id()} already exists.")
        self.__products.append(product)

    def search_product(self, product_id: str)-> Product | None:
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None

    def remove_product(self, product_id: str) -> Product:
        product = self.search_product(product_id)
        if product is None:
            raise ValueError(f"Product ID {product_id} not found.")
        self.__products.remove(product)
        return product

    def display_all(self) -> None:
        if not self.__products:
            print("No products in the inventory.")
            return

        print("Current Inventory")
        for product in self.__products:
            product.display_information()

    def get_products(self) -> list[Product]:
        return list(self.__products)