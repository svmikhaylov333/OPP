import pytest

from src.category import Category
from src.product import Product


def test_category_creation(first_product, second_product) -> None:
    """Тест создания категории с продуктами"""
    category = Category(
        "Смартфоны", "Описание смартфонов", [first_product, second_product]
    )

    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert isinstance(category.products, str)
    assert "First Product" in category.products
    assert "Second Product" in category.products
    assert "руб. Остаток:" in category.products

    assert Category.category_count == 1
    assert Category.product_count == 2
    assert category.category_count == 1
    assert category.product_count == 2


def test_category_add(first_product, second_product) -> None:
    """Тест - проверка складывания метод add"""
    assert first_product + second_product == 5


def test_category_str(category: Category) -> None:
    """Тест - метод __str__"""
    assert "Смартфоны, количество продуктов:" in str(category)
