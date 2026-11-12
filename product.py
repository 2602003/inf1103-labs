from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(
            self, 
            product_id: str, 
            product_name: str, 
            price: float, 
            stock_quantity: int, 
            supplier: Supplier
    ):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        self.__stock_quantity = stock_quantity
        self.__supplier: Supplier = supplier

    def get_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__product_name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock_quantity

    def get_supplier(self) -> Supplier:
        return self.__supplier
    
    def update_stock(self, new_stock_quantity: int) -> None:
        if new_stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.__stock_quantity = new_stock_quantity

    def get_display_text(self) -> str:
        return f"ID: {self.__product_id} | Name: {self.__product_name} | Price: ${self.__price:.2f} | Stock: {self.__stock_quantity}"

    def display_information(self) -> None:
        print(self.get_display_text())
        self.__supplier.display_information()

    def to_dict(self) -> dict:
        return {
            "product_id": self.__product_id,
            "product_name": self.__product_name,
            "price": self.__price,
            "stock_quantity": self.__stock_quantity,
            "supplier_id": self.__supplier.get_supplier_id(),
            "supplier_name": self.__supplier.get_name(),
            "supplier_email": self.__supplier.get_contact_email()
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass