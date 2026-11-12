from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(
            self, 
            product_id: str, 
            product_name: str, 
            price: float, 
            stock_quantity: int, 
            weight: float,
            supplier: Supplier
        ):
        super().__init__(
            product_id, 
            product_name, 
            price, 
            stock_quantity, 
            supplier
        )
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        print(super().get_display_text() + f" | Type: Physical | Weight: {self.__weight} kg")
        self.get_supplier().display_information()

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping from warehouse."

    def calculate_shipping_cost(self) -> float:
        base_cost = 5.0  
        weight_cost = 2.0 * self.__weight  # Cost per kg
        total_cost = base_cost + weight_cost
        return total_cost

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Physical"
        data["weight"] = self.__weight
        return data
