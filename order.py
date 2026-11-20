from discount_strategy import DiscountStrategy
from no_discount import NoDiscount
from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
        self.__order_id = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount = discount if discount is not None else NoDiscount()

    def get_order_id(self) -> str:
        return self.__order_id

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(total)