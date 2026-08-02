import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def fist_product() -> Product:
    return Product("Fist Product", "description first product", 1.0, 1)

@pytest.fixture
def second_product() -> Product:
    return Product("Second Product", "description second product", 2.0, 2)