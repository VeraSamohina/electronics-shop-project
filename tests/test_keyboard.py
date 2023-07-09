from src.keyboard import Keyboard
import pytest


@pytest.fixture
def kb1():
    return Keyboard("testkeyboard", 13000, 2)


def test_keyboard_init(kb1):
    assert kb1.name == "testkeyboard"
    assert kb1.price == 13000
    assert kb1.quantity == 2
    assert kb1.language == "EN"


def test_change_lang(kb1):
    kb1.change_lang()
    assert kb1.language == "RU"
    kb1.change_lang()
    assert kb1.language == "EN"
