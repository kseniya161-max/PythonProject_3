import pytest

from src.generators import filter_by_currency, transaction_descriptions


def test_filter_not_existing_currency(transactions):
    """ Функция тестирует корректность фильтрации транзакции по заданной валюте."""
    assert filter_by_currency(transactions, "USD") == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
    {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
    {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}]



def test_filter_by_currency(transactions):
    """ Тестирует когда транзакции в заданной валюте отсутствуют"""
    assert filter_by_currency(transactions, "EUR") == []


def test_transaction_descriptions(transactions):
    """ Тестирует что все ожидаемые описания присутствуют в результатах"""
    descriptions = list(transaction_descriptions(transactions))


    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту"
    ]


    for description in expected_descriptions:
        assert description in descriptions



def test_transaction_descriptions_empty():
    """ Тест проверяет устойчивость функции к пустым входным данным."""
    assert list(transaction_descriptions([])) == []

