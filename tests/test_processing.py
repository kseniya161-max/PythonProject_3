import pytest

from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def test_filter_by_state(operation):
    """Тестирование функции filter_by_state"""

    assert (filter_by_state(operation, "EXECUTED") == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
    assert (filter_by_state(operation, "CANCELED") == [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])


def test_filter_by_state_none_list(operation):
    assert filter_by_state(operation, None) == []


def test_sort_by_date(operation):
    """ Тестирование функции sort_by_date"""
    assert sort_by_date(operation) == [{'id': 41428829, 'state': 'EXECUTED',
                                        'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 615064591, 'state': 'CANCELED',
                                        'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 594226727, 'state': 'CANCELED',
                                        'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 939719570, 'state': 'EXECUTED',
                                        'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_invalid_date():
    invalid_operation = [{'id': 41428829, 'state': 'EXECUTED', 'date': 2}]
    with pytest.raises(ValueError):
        sort_by_date(invalid_operation)


def test_sort_by_date_same_date():
    same_date_operation = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    result = sort_by_date(same_date_operation)
    assert result == [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


def test_mask_account_card(card, account):

    """Тестирование mask_account_card """
    assert mask_account_card(card[0]) == card[1]
    assert mask_account_card(account[0]) == account[1]


@pytest.mark.parametrize("number, expected", [
    ("Счет 70007922896063612056", "Счет 7000 79** **** 2056"),
    ("Maestro 1596837868705199", "Maestro ** 5199")
])
def tests_multiple_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


def test_get_date():
    """ Тестирование функции get_date"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
