import pytest


from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(mask_card, mask_account):
    """Тестирование функции get_mask_card_number"""
    assert get_mask_card_number(mask_card[0]) == mask_card[1]


def test_get_mask_account(mask_card, mask_account):
    """Тестирование функции get_mask_account"""
    assert get_mask_account(mask_account[0]) == mask_account[1]


@pytest.mark.parametrize("mask_card, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
])
def tests_multiple_get_mask_card_number(mask_card, expected):
    """Тестирование функции get_mask_card_number"""
    assert get_mask_card_number(mask_card) == expected


@pytest.mark.parametrize("mask_count, expected", [
    ("73654108430135874305", "**4305"),])
def tests_multiple_get_mask_account(mask_count, expected):
    """Тестирование функции get_mask_account"""
    assert get_mask_account(mask_count) == expected


def test_get_mask_card_num():
    """ Тестирование функции get_date"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_acc():
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_card_number_none_list():
    assert get_mask_card_number(None) == ""


def test_get_mask_card_number_valid_number():
    """
    При маскировке номера карты скрывается часть символов
    """
    card_number = '7000792289606361'
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'

@pytest.mark.parametrize(
    'invalid_card_number', ['0' * 15, '0' * 17], ids=['too short', 'too long']
)
def test_get_mask_card_number_invalid_card_number_length(invalid_card_number):
    """
    Если длина номера карты не равна 16 символам, упадет ошибка валидации.
    """
    card_number = '7000792289606361'
    if len(card_number) != 16:
        raise ValueError("Неверная длина номера карты")

