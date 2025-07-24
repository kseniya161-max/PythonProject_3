import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_not_existing_currency(transactions):
    """ Функция тестирует корректность фильтрации транзакции по заданной валюте."""
    iterator = filter_by_currency(transactions, "USD")
    assert next(iterator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }


def test_filter_by_currency(transactions):
    """ Тестирует когда транзакции в заданной валюте отсутствуют"""
    assert list(filter_by_currency(transactions, "EUR")) == []


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


def test_card_number_generator():
    """ Тестирует что генератор выдает правильные номера карт в заданном диапазоне."""
    start = 1
    stop = 6
    expected_list = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]
    assert list(card_number_generator(start, stop)) == expected_list


def test_card_number_generator_incorrect():
    """ Тестирует что генератор не возвращает значения при неправильном диапазоне"""
    start = 1
    with pytest.raises(TypeError):
        list(card_number_generator(start, None))
    assert list(card_number_generator(3, 2)) == []


def test_card_number_generator_correct_formating():
    """ Проверяет корректность форматирования номеров карт"""
    start = 1
    stop = 6
    expected_list = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004",
                     "0000 0000 0000 0005"]

    format_card = list(card_number_generator(start, stop))

    for actual, expected in zip(format_card, expected_list):
        assert actual == expected


@pytest.mark.parametrize("transactions, expected_descriptions", [
    (
        [
            {"description": "Перевод организации"},
            {"description": "Перевод со счета на счет"},
            {"description": "Перевод со счета на счет"},
            {"description": "Перевод с карты на карту"}
        ],
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту"
        ]
    ),
    (
        [
            {"description": "Оплата товара"},
            {"description": "Перевод организации"},
            {"description": "Перевод со счета на счет"},
            {"description": None}
        ],
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Оплата товара"
        ]
    ),
    (
        [
            {"description": None},
            {"description": None}
        ],
        []
    ),
])
def test_transaction_descriptions(transactions, expected_descriptions):
    """ Тестирует, что все ожидаемые описания присутствуют в результатах """
    descriptions = list(transaction_descriptions(transactions))
    for description in expected_descriptions:
        assert description in descriptions


