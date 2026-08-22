import pytest
from pytest import CaptureFixture

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


def test_middle_price(category: Category) -> None:
    """Тест - метод middle_price"""
    assert category.middle_price() == 140333.33333333334


def test_custom_exception(
    category: Category, first_product: Product, capsys: CaptureFixture
) -> None:
    assert len(category.get_product_list()) == 3
    first_product.quantity = 0
    category.add_product(first_product)
    message = capsys.readouterr().out
    assert "Нельзя добавлять товар с нулевым кол-вом" in message
    assert "Обработка операции 'Добавление товара' завершена" in message
    assert (
        len(category.get_product_list()) == 3
    )  # проверка, что first_product не добавился
