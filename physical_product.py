from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, product_name: str, price: float, stock_quantity: int, weight: float):
        super().__init__(product_id, product_name, price, stock_quantity)
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def get_display_text(self):
        return super().get_display_text() + f" | Type: Physical | Weight: {self.__weight} kg"

    def get_information(self):
        return self.get_display_text()

    def get_fufilment_info(self):
        return "Requires physical shipping from warehouse."

    def calculate_shipping_cost(self):
        base_cost = 5.0  
        weight_cost = 2.0 * self.__weight  # Cost per kg
        total_cost = base_cost + weight_cost
        return total_cost

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Physical"
        data["weight"] = self.__weight
        return data
