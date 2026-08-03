import json
import os

from src.category import Category, Product


def read_json(path: str) -> list:
    full_path = os.path.abspath(path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"файл не найден: {full_path}")

    with open(full_path, "r", encoding="UTF-8") as f:
        json_data = json.load(f)
        return json_data


def create_products_from_json(categories_data: list) -> list[Product]:
    """Создает спискок объектов Product из json файла"""
    products = []
    for category_data in categories_data:
        for product_data in category_data.get("products", []):
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=float(product_data["price"]),
                quantity=int(product_data["quantity"]),
            )
            products.append(product)
    return products


def create_categories_from_json(categories_data: list) -> list:
    """Создает список объектов Category ииз json файла"""
    categories = []

    for category_data in categories_data:

        products = []
        for product_data in category_data.get("products", []):
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=float(product_data["price"]),
                quantity=int(product_data["quantity"]),
            )
            products.append(product)

        # Создаем категорию
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories


# if __name__ == "__main__":
#     data = read_json("../data/products.json")
#     print(data)
#     print("=" * 10 + "\nданные из json\n")
#     for cat in create_categories_from_json(data):
#         print(f"\nКатегория: {cat.name}")
#         print(f"\nОписание: {cat.description}")
#         print(f"\nкол-во товаров {len(cat.products)}")
#         for prod in cat.products:
#             print(f"Наименование {prod.name}")
#             print(f"Цена: {prod.price} руб.")
#             print(f"В наличии: {prod.quantity} шт.")
