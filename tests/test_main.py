import pytest
import unittest
import json
from datetime import datetime
from src. main import open_json, open_csv, open_excel, main_user_input, filtered_by_status,status_input, format_and_print_operations
from unittest.mock import mock_open, patch
import csv
from unittest.mock import patch, MagicMock
import pandas as pd


def test_open_json(mocker):
    # Подготовим данные для теста
    mock_data = [
        {"id": 1, "date": "2019-07-03T18:35:29.512364", "description": "Тестовая операция"},
        {"id": 2, "date": "2020-08-04T12:00:00.000000", "description": "Еще одна операция"},
        {"id": 3, "date": "invalid-date", "description": "Некорректная дата"}
    ]

    # Замокируем json.load
    mock_json_load = mocker.patch("json.load", return_value=mock_data)

    # Создаем мок для open
    mock_open_func = mock_open(read_data=json.dumps(mock_data))
    with patch("builtins.open", mock_open_func):
        result = open_json()  # Путь не важен, так как мы замокировали open

    # Проверяем, что json.load был вызван
    mock_json_load.assert_called_once()

    # Проверяем результат
    assert len(result) == 3  # Убедимся, что мы получили 3 операции
    assert result[0]['date'] == datetime.strptime("2019-07-03T18:35:29.512364", '%Y-%m-%dT%H:%M:%S.%f')
    assert result[1]['date'] == datetime.strptime("2020-08-04T12:00:00.000000", '%Y-%m-%dT%H:%M:%S.%f')
    assert result[2]['date'] is None  # Для некорректной даты должно быть None


def test_open_csv():
    mock_csv_data = "date;description\n2019-07-03T18:35:29Z;Тестовая операция\n2020-08-04T12:00:00Z;Еще одна операция"

    # Патчим open и csv.DictReader
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        with patch("csv.DictReader", return_value=csv.DictReader(mock_csv_data.splitlines(), delimiter=';')):
            result = open_csv()

    # Проверяем результат
    assert len(result) == 2  # Проверка количества операций
    assert result[0]['date'] == datetime(2019, 7, 3, 18, 35, 29)  # Проверка первой даты
    assert result[1]['date'] == datetime(2020, 8, 4, 12, 0, 0)  # Проверка второй даты
    assert result[0]['description'] == 'Тестовая операция'  # Проверка описания первой операции
    assert result[1]['description'] == 'Еще одна операция'  # Проверка описания второй


def test_open_excel():
    # Создаем тестовые данные
    mock_data = pd.DataFrame({
        'date': ['2023-01-01', None, '2023-01-03'],
        'description': ['Операция 1', 'Операция 2', 'Операция 3']
    })
    with patch('pandas.read_excel', return_value=mock_data):
        result = open_excel()


    expected_result = [
        {'date': pd.to_datetime('2023-01-01').to_pydatetime(), 'description': 'Операция 1'},
        {'date': None, 'description': 'Операция 2'},
        {'date': pd.to_datetime('2023-01-03').to_pydatetime(), 'description': 'Операция 3'}
    ]

    assert result == expected_result


def test_status_input_valid_status():
    test_data = [
        {'id': 1, 'state': 'executed', 'description': 'Операция 1'},
        {'id': 2, 'state': 'canceled', 'description': 'Операция 2'},
        {'id': 3, 'state': 'pending', 'description': 'Операция 3'},
    ]

    with patch('builtins.input', side_effect=['executed']):
        filtered_data = status_input(test_data)

    assert len(filtered_data) == 1
    assert filtered_data[0]['state'] == 'executed'


def test_status_input_invalid_status():
    test_data = [
        {'id': 1, 'state': 'executed', 'description': 'Операция 1'},
        {'id': 2, 'state': 'canceled', 'description': 'Операция 2'},
    ]

    with patch('builtins.input', side_effect=['invalid_status', 'canceled']):
        with patch('builtins.print') as mock_print:  # Патчим print для проверки вывода
            filtered_data = status_input(test_data)

    mock_print.assert_any_call('Статус операции "invalid_status" недоступен.')
    assert len(filtered_data) == 1
    assert filtered_data[0]['state'] == 'canceled'


def test_format_and_print_operations():
    test_data = [
        {
            'date': datetime(2023, 1, 1, 12, 0, 0),
            'description': 'Перевод со счета на счет',
            'operationAmount': {'amount': '1000', 'currency': {'name': 'руб.'}},
            'from': 'Счет 1234567890123456',
            'to': 'Счет 6543210987654321'
        },
        {
            'date': None,
            'description': 'Перевод с карты на счет',
            'operationAmount': {'amount': '500', 'currency': {'name': 'USD'}},
            'from': 'Visa 1234 5678 9012 3456',
            'to': 'Счет 9876543210123456'
        }
    ]

    expected_output = [
        "Всего банковских операций в выборке: 2\n",  # Исправлено
        "01.01.2023 Перевод со счета на счет",
        "Счет **3456 -> Счет **4321",
        "Сумма: 1000 руб.\n",
        "Дата не указана Перевод с карты на счет",
        "Visa 1234 5678 **** **** -> Счет **3456",
        "Сумма: 500 USD\n"
    ]

    with patch('builtins.print') as mock_print:
        format_and_print_operations(test_data)

    actual_calls = [call[0][0] for call in mock_print.call_args_list]

    for expected, actual in zip(expected_output, actual_calls):
        assert expected.strip() == actual.strip()


