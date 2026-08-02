from src.product import Product
from typing import List


class Category:
    name: str # название
    description: str
    products: List[Product]
    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products