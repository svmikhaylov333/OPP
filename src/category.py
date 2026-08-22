from typing import List
from src.product import Product


class Category:
    name: str  # название
    description: str
    __products: List[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):

        # return f"{self.name}, количество продуктов: {len(self.__products)} шт."
        total_quantity = sum(prod.quantity for prod in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


    @property
    def products(self):
        """Геттер для приватного атрибута __products"""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str


    def add_product(self, product: Product) -> None:
        """метод добавления товаров в категорию"""
        if not isinstance(product, Product):
            raise TypeError(
                " в список нельзя добавить ничего другого кроме Product и его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1


    def get_product_list(self):
        """метод получения списка продуктов в категории"""
        return self.__products

    def middle_price(self):
        """метод получения среднего ценника всех товаров"""
        try:
            return sum([product.price for product in self.__products])/len(self.__products)
        except ZeroDivisionError:
            return 0