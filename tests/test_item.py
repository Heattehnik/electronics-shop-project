import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item('Лопата', 200, 40)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 8000.0


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 170


def test_string_to_digit(item):
    assert Item.string_to_number('6.2') == 6


def test___repr__(item):
    assert repr(item) == "Item('Лопата', 200, 40)"


def test___str__(item):
    assert str(item) == 'Лопата'


def test_name(item):
    item.name = 'Грабли'
    assert item.name == 'Грабли'
    with pytest.raises(Exception):
        item.name = 'СуперМегаЛопата'


def test__add__(item):
    assert item + item == 80

