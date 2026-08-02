from src.product import Product
from typing import List


class Category:
    name: str # название
    description: str
    products: List[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count +=1
        Category.product_count += len(self.products)

