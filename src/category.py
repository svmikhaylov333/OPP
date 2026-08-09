from typing import List

from src.product import Product


class Category:
    name: str  # название
    description: str
    # products: List[Product] # чтобы не ругался mypy
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."




    # Геттер для приватного атрибута __products
    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    # метод добавления товаров в категорию
    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1
