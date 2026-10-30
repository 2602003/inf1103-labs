from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id: str, product_name: str, price: float, stock_quantity: int, download_size: float):
        super().__init__(product_id, product_name, price, stock_quantity)
        if download_size < 0:
            raise ValueError("Download size cannot be negative.")
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def get_display_text(self):
        return super().get_display_text() + f" | Type: Digital | Download Size: {self.__download_size} MB"

    def get_information(self):
        return self.get_display_text()

    def get_fufilment_info(self):
        return "Delivered via download link."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Digital"
        data["download_size"] = self.__download_size
        return data