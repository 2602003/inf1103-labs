from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(
            self, 
            product_id: str, 
            product_name: str, 
            price: float, 
            stock_quantity: int,  
            download_size: float,
            supplier: Supplier
        ):
        super().__init__(
            product_id, 
            product_name,
            price, 
            stock_quantity, 
            supplier
        )
        if download_size < 0:
            raise ValueError("Download size cannot be negative.")
        self.__download_size = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        print(super().get_display_text() + f" | Type: Digital | Download Size: {self.__download_size} MB")
        self.get_supplier().display_information()

    def get_fulfilment_info(self) -> str:
        return "Delivered via download link."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Digital"
        data["download_size"] = self.__download_size
        return data