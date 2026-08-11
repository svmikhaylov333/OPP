ООП проект

![Python Version](https://img.shields.io/badge/python-3.12+-blue)
![Status](https://img.shields.io/badge/status-development-blue)
![Style](https://img.shields.io/badge/code%20style-black-blue)
![Version](https://img.shields.io/badge/version-0.0.1-blue)

Проект для работы с категориями и товарами. Реализована загрузка данных из JSON, 
создание объектов классов Category и Product с автоматическим подсчетом количества 
категорий и товаров.

---

## Содержание

- [Технологии](#технологии)
- [Установка](#установка)
- [Использование](#использование)
- [Разработка](#разработка)
- [Тестирование](#тестирование)
- [To do](#to-do)

---

## Технологии

- Python 3.12+
- Poetry - управление зависимостями
- Black - форматирование кода
- Isort - сортировка импортов
- Flake8 - проверка стиля
- Mypy - проверка типов
- Pytest - тестирование

---

## Установка

```bash
# Клонировать репозиторий
git clone <repository-url>
cd OPP
# Установить зависимости через poetry
poetry install
# Активировать виртуальное окружение
eval $(poetry env activate)
```
## Использование

### Запуск программы
```bash
python main.py
```

### Создание объектов
```python
from src.product import Product
from src.category import Category

# Создание продуктов

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

# Создание категории
category = Category("Смартфоны", "Описание смартфонов", [product1, product2])

#Просмотр счетчиков
print(f"Всего категорий: {Category.category_count}")  # 1
print(f"Всего товаров: {Category.product_count}")     # 2
```
Создание подклассов Product
```python

from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
 )
 

```
Загрузка данных из JSON
```python
from src.utils import read_json, create_categories_from_json
```
### Чтение JSON файла
```python
data = read_json("data/products.json") # noqa
```
### Создание категорий и товаров из JSON
```python
categories = create_categories_from_json(data) # noqa
```

### Пример JSON файла
```json
[
  {
    "name": "Смартфоны",
    "description": "Описание категории",
    "products": [
      {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет",
        "price": 180000.0,
        "quantity": 5
      }
    ]
  }
]
```
## Разработка

### Требования

- Python 3.12+
- Poetry

### Проверка качества кода

```bash
flake8 .
black .
isort .
mypy .
```

---

## Тестирование

Для запуска проверки функций:

```bash
pytest
```
Дополнительные проверки
```bash
python tests/test.py
```
Для анализа покрытия кода тестами использовать

```bash
pytest --cov
```

Сформировать отчет, см. htmlcov/index.html
 ```bash
pytest --cov=src --cov-report=html
```
Сформировать отчет "без .gitignore", см. htmlcov/index.html
 ```bash
pytest --cov=src --cov-report=html; Remove-Item htmlcov/.gitignore
```
Если папка (не пустая) 'htmlcov' существует и в ней удален .gitignore. 
При повторных генерациях .gitignore не создается
---

## Deploy и CI/CD

На текущем этапе CI/CD отсутствует.

## Contributing

По вопросам и предложениям писать на почту.

---
## FAQ

Ответы на вопросы...

---
### Для чего нужен проект?

Проект нужен

---

## To do
 - [x] классы Product, Category
 - [x] работа с json
 - [x] Классы-наследники Smartphone и LawnGrass
 - [x] Итератор для продуктов
 - [x] Защита сложения товаров
 - [x] Защита добавления в категорию
 - [ ] ...
---

## Команда проекта

MC

---
## Источники

---