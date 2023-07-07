from src.phone import Phone
import pytest


def test_phone():
    phone1 = Phone("Honor", 20000, 12, 1)
    assert phone1.name == "Honor"
    assert phone1.number_of_sim == 1
    assert repr(phone1) == "Phone('Honor', 20000, 12, 1)"
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 1.5
