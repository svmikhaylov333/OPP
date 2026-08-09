import pytest

from src.product_iterator import ProductIterator


def test_product_iterator(category):
    """Тест - итерации по продуктам"""
    product_iterator = ProductIterator(category)
    products = list(product_iterator)
    iter(product_iterator)
    assert len(products) == 3
    assert products[0].name == "Samsung Galaxy C23 Ultra"
    assert products[1].name == "Iphone 15"
    assert products[2].name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        next(product_iterator)
