from unittest.mock import patch

import pytest

from src.product import Product


def test_product_creation():
    """Тест - создание класса Product со всеми атрибутами
    (name: str, description: str, price: float, quantity: int)"""
    product = Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_creation_with_name(first_product, second_product):
    assert first_product.name == "First Product"
    assert first_product.description == "description first product"
    assert first_product.price == 1.0
    assert first_product.quantity == 1
    assert second_product.name == "Second Product"
    assert second_product.description == "description second product"
    assert second_product.price == 2.0
    assert second_product.quantity == 2


def test_price_setter_with_positive_change():
    """Тест - повышение цены"""
    product = Product("Test", "Desc", 100.0, 10)
    product.price = 200.0
    assert product.price == 200.0
    product.price = 250.0
    assert product.price == 250.0


@pytest.mark.usefixtures("capsys")
@patch("builtins.input", return_value="y")
def test_price_setter_decrease_yes(mock_input):
    """Тест - понижение цены"""
    product = Product("Test", "Desc", 200.0, 10)

    product.price = 100.0
    mock_input.assert_called_once_with("Понизить цену с 200.0 до 100.0? (y/n): ")
    assert product.price == 100.0


def test_product_str(first_product: Product) -> None:
    """Тест - метод __str__"""
    assert str(first_product) == "First Product, 1.0 руб. Остаток: 1 шт."
