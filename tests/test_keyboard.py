import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
