import pytest

from src.category import Category
from src.product import Product


def test_category_creation(fist_product, second_product) -> None:
    """Тест создания категории с продуктами"""
    category = Category(
        "Смартфоны", "Описание смартфонов", [fist_product, second_product]
    )

    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert len(category.products) == 2
    assert category.products[0] == fist_product
    assert category.products[1] == second_product

    assert Category.category_count == 1
    assert Category.product_count == 2
    assert category.category_count == 1
    assert category.product_count == 2
