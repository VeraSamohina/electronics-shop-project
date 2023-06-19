"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    assert Item('Диск', 100, 3).calculate_total_price() == 300


def test_apply_discount():
    Item.pay_rate = 0.5
    item3 = Item('Книга', 400, 1)
    item3.apply_discount()
    assert item3.price == 200
