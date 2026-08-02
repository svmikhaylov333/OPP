from src.product import Product
from test.conftest import fist_product


def test_product_creation():
    """Тест - создание класса Product со всеми атрибутами
   (name: str, description: str, price: float, quantity: int)"""
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_product_creation_with_name(fist_product, second_product):
    assert fist_product.name=="Fist Product"
    assert fist_product.description == "description first product"
    assert fist_product.price == 1.0
    assert fist_product.quantity == 1
    assert second_product.name == "Second Product"
    assert second_product.description == "description second product"
    assert second_product.price == 2.0
    assert second_product.quantity == 2
