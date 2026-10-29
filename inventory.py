class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_id()) is not None:
            raise ValueError(f"Product ID {product.get_id()} already exists.")
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("No products in the inventory.")
            return

        print("Current Inventory")
        for product in self.__products:
            product.display_information()

    def get_products(self):
        return list(self.__products)