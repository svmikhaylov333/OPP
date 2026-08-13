from src.base_product import BaseProduct
from src.print_mixin import PrintMixin



class Product(BaseProduct,PrintMixin):
    name: str  # название
    description: str  # описание
    # price: float  # цена
    quantity: int  # количество в наличии

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__(name, description, price, quantity)


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is type(self):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError(
            "можно складывать товары только из одинаковых классов продуктов"
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            answer = input(f"Понизить цену с {self.__price} до {price}? (y/n): ")
            if answer.lower() == "y":
                self.__price = price
        else:
            self.__price = price

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=float(product_data["price"]),
            quantity=int(product_data["quantity"]),
        )
