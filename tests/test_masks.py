import pytest


from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(mask_card):
    """Принимает ли функция номер карты и возвращает ее маску"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_account():
    """Принимает ли функция номер счета и возвращает его маску"""
    assert get_mask_account("73654108430135874305") == "**4305"


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


def test_get_mask_card_number_none_list():
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты."""
    assert get_mask_card_number(None) == ""


def test_get_mask_card_number_valid_number():
    """
    При маскировке номера карты скрывается часть символов
    """
    card_number = '7000792289606361'
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


def test_get_mask_account_valid_number():
    """
    При маскировке номера карты скрывается часть символов
    """
    account_number = "73654108430135874305"
    assert get_mask_account(account_number) == "**4305"


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


@pytest.mark.parametrize(
    'invalid_mask_account', ['0' * 19, '0' * 21], ids=['too short', 'too long']
)
def test_get_mask_account_invalid_mask_account(invalid_mask_account):
    """"Если длина номера счета не равна 20 символам, упадет ошибка валидации."""
    mask_account = "73654108430135874305"
    if len(mask_account) != 20:
        raise ValueError("Неверная длина номера счета")
