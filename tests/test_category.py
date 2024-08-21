def test_category_init(category_1, category_2, category_3):
    assert category_1.name == "Бытовая техника"
    assert category_1.description == "Техника для дома и быта"
    assert len(category_1.products_list) == 3
    assert category_1.category_count == 3
    assert category_2.category_count == 3
    assert category_3.category_count == 3
    assert len(category_3.products_list) == 1


def test_category_str(category_3):
    assert category_3.products == "Насос, 3000 руб. Остаток: 25 шт.\n"


def test_add_product(category_3, product_3):
    category_3.add_product(product_3)


def test_str_category(category_1):
    assert str(category_1) == "Бытовая техника, количество продуктов: 30 шт."
