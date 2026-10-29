class Product:
    def __init__(self, product_id: str, product_name: str, price: float, stock_quantity: int):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        self.__stock_quantity = stock_quantity

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock_quantity
    
    def update_stock(self, new_stock_quantity: int):
        self.__stock_quantity = new_stock_quantity

    def display_information(self):
        print(f"ID: {self.__product_id}| Name: {self.__product_name}| Price: ${self.__price:.2f}| Stock: {self.__stock_quantity}")

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "product_name": self.__product_name,
            "price": self.__price,
            "stock_quantity": self.__stock_quantity
        }