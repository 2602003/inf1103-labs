from product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
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
        return self.__products