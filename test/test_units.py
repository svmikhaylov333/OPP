import json
from unittest.mock import mock_open, patch

import pytest

from src.product import Product
from src.utils import create_categories_from_json, create_products_from_json, read_json


def test_read_json_success():
    """Тест - чтения JSON файла"""
    mock_data = [{"name": "Test", "description": "Desc", "products": []}]

    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("os.path.exists", return_value=True):
            with patch("os.path.abspath", return_value="/fake/path.json"):
                result = read_json("/fake/path.json")

    assert result == mock_data


def test_read_json_file_not_found():
    """Тест - ошибки при отсутствии файла"""
    with patch("os.path.exists", return_value=False):
        with patch("os.path.abspath", return_value="/fake/path.json"):
            with pytest.raises(FileNotFoundError):
                read_json("/fake/path.json")


def test_create_products_from_json(test_data):
    """Тест - создания ВСЕХ продуктов из JSON данных"""

    all_products = create_products_from_json(test_data)

    # Общее кол-во продуктов
    assert len(all_products) == 4

    for product in all_products:
        assert isinstance(product, Product)

    # Категория - Смартфоны
    assert all_products[0].name == "Samsung Galaxy C23 Ultra"
    assert all_products[1].name == "Iphone 15"
    assert all_products[2].name == "Xiaomi Redmi Note 11"

    # Категория -Телевизоров
    assert all_products[3].name == '55" QLED 4K'
    assert all_products[3].price == 123000.0
    assert all_products[3].quantity == 7


def test_create_categories_from_json():
    """Тест - создания категорий с продуктами"""
    categories_data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    categories = create_categories_from_json(categories_data)

    assert len(categories) == 1
    assert categories[0].name == "Смартфоны"
    assert isinstance(categories[0].products, str)
    assert "Samsung Galaxy C23 Ultra" in categories[0].products
