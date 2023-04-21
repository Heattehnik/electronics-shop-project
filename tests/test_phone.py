import pytest

from src.phone import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item('Лопата', 200, 40)


@pytest.fixture
def phone():
    return Phone("Pixel 6 pro", 500, 20, 2)


def test_calculate_total_price(phone):
    assert phone.calculate_total_price() == 10000


def test_apply_discount(phone):
    Phone.apply_discount(phone)
    assert phone.price == 425


def test_string_to_digit(phone):
    assert Phone.string_to_number('6.2') == 6


def test_repr(phone):
    assert repr(phone) == "Phone('Pixel 6 pro', 500, 20, 2)"


def test_str(phone):
    assert str(phone) == 'Pixel 6 pro'


def test_add(phone, item):
    assert phone + item == 60


def test_number_of_sims(phone):
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
