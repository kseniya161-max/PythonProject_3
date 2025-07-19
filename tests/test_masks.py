import pytest

from src. masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number(mask_card, mask_account):
    """Тестирование функции get_mask_card_number """
    assert get_mask_card_number(mask_card[0]) == mask_card[1]


def test_get_mask_account(mask_card, mask_account):
    assert get_mask_account(mask_account[0]) == mask_account[1]

