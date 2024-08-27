import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, ����� ����, 200MP ������", price=180000.0, quantity=5
    )


@pytest.fixture
def product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product_3():
    return Product(name="Nokia", description="Yellow", price=90000.0, quantity=0)


@pytest.fixture
def category_1():
    return Category(
        name="���������",
        description="���������, ��� �������� �� ������ ������������, "
        "�� � ��������� �������������� ������� ��� �������� �����",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, ����� ����, 200MP ������", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="����������",
        description="����������� ���������, ������� ��������� ������������ ����������, "
        "������ ����� ������ � ����������",
        products=[Product('55" QLED 4K', "������� ���������", 123000.0, 7)],
    )


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, ����� ����, 200MP ������", 180000.0, 5, 95.5, "S23 Ultra", 256, "�����"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("�������� �����", "������� ����� ��� ������", 500.0, 20, "������", "7 ����", "�������")


@pytest.fixture
def grass2():
    return LawnGrass("�������� ����� 2", "���������� �����", 450.0, 15, "���", "5 ����", "�����-�������")


@pytest.fixture
def products_json():
    return [
        {
            "name": "���������",
            "description": "����������� ���������",
            "products": [
                {"name": "Samsung", "description": "�����", "price": 180000.0, "quantity": 5},
                {"name": "Iphone 15", "description": "Gray", "price": 210000.0, "quantity": 8},
            ],
        },
        {
            "name": "����������",
            "description": "����������� ���������",
            "products": [{"name": '55"', "description": "������� ���������", "price": 123000.0, "quantity": 7}],
        },
    ]
