import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item('Лопата', 200, 40)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 8000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 170


def test_string_to_digit(item):
    assert Item.string_to_number('6.2') == 6

def test_repr(item):
    assert repr(item) == "Item('Лопата', 200, 40)"


def test_str(item):
    assert str(item) == 'Лопата'

