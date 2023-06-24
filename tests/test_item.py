"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


def test_calculate_total_price():
    assert Item('Диск', 100, 3).calculate_total_price() == 300


def test_apply_discount():
    Item.pay_rate = 0.5
    item3 = Item('Книга', 400, 1)
    item3.apply_discount()
    assert item3.price == 200


def test_string_to_number():
    item5 = Item("Устройство", '90', '8')
    item6 = Item("Блок", '90.3', '8')
    assert item5.string_to_number(item5.price) == 90
    assert item6.string_to_number(item6.price) == 90


def test_item_name():
    item = Item('Телефон', 10000, 5)
    item.name = "Монитор"
    assert item.name == "Монитор"
    item.name = "Жидкокристаллический"
    with pytest.raises(AssertionError):
        assert item.name == "Жидкокристаллический"
    assert item.name == "Жидкокрист"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
