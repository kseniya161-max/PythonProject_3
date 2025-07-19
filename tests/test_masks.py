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
    ("73654108430135874305", "** 4305"),])
def tests_multiple_get_mask_account(mask_count, expected):
    """Тестирование функции get_mask_account"""
    assert get_mask_account(mask_count) == expected
