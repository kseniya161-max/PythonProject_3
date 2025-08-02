from src. transactions import trans_csv_reader,trans_excel_reader
import unittest
import pytest
import pandas as pd
from unittest.mock import patch
from typing import List, Dict


@patch('pandas.read_csv')
def test_trans_csv_reader(mock_read_csv):
    """ Создаем фиктивный список и тестируем функцию"""
    mock_data = pd.DataFrame({'id': ['650703', '3598919'],
        'state': ['EXECUTED', 'EXECUTED'],
        'date': ['2023-09-05T11:30:32Z', '2020-12-06T23:00:58Z'],
        'amount': [16210, 29740],
        'currency_name': ['Sol', 'Peso'],
        'currency_code': ['PEN', 'COP'],
        'from': ['Счет 58803664561298323391', 'Discover 3172601889670065'],
        'to': ['Счет 39745660563456619397', 'Discover 0720428384694643'],
        'description': ['Перевод организации', 'Перевод с карты на карту']

        })
    """ Настройка mock для pd.read_csv"""
    mock_read_csv.return_value = mock_data
    expected_result = [
        {
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210,
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        },
        {
            'id': '3598919',
            'state': 'EXECUTED',
            'date': '2020-12-06T23:00:58Z',
            'amount': 29740,
            'currency_name': 'Peso',
            'currency_code': 'COP',
            'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643',
            'description': 'Перевод с карты на карту'
        }
    ]

    # Вызываем функцию
    result = trans_csv_reader('fake_file.csv')  # Путь к файлу не важен, так как мы подменяем функцию

    # Проверка
    assert result == expected_result


# # Запуск теста
# if __name__ == '__main__':
#     pytest.main()


def test_trans_excel_reader():
    # Создаем фиктивные данные
    mock_data = pd.DataFrame({
        'id': [650703, 3598919, 593027],
        'state': ['EXECUTED', 'EXECUTED', 'CANCELED'],
        'date': ['2023-09-05T11:30:32Z', '2020-12-06T23:00:58Z', '2023-07-22T05:02:01Z'],
        'amount': [16210, 29740, 30368],
        'currency_name': ['Sol', 'Peso', 'Shilling'],
        'currency_code': ['PEN', 'COP', 'TZS'],
        'from': ['Счет 58803664561298323391', 'Discover 3172601889670065', 'Visa 1959232722494097'],
        'to': ['Счет 39745660563456619397', 'Discover 0720428384694643', 'Visa 6804119550473710'],
        'description': ['Перевод организации', 'Перевод с карты на карту', 'Перевод с карты на карту']
    })

    # Замокируем pd.read_excel
    with patch('pandas.read_excel', return_value=mock_data) as mock_read_excel:
        result = trans_excel_reader('fake_file.xlsx')  # имя файла не имеет значения

        # Проверяем, что mock_read_excel был вызван с правильным аргументом
        mock_read_excel.assert_called_once_with('fake_file.xlsx')

        # Проверяем результат
        expected_result = [
            {'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
             'currency_name': 'Sol', 'currency_code': 'PEN',
             'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
             'description': 'Перевод организации'},
            {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
             'currency_name': 'Peso', 'currency_code': 'COP',
             'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
             'description': 'Перевод с карты на карту'},
            {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0,
             'currency_name': 'Shilling', 'currency_code': 'TZS',
             'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710',
             'description': 'Перевод с карты на карту'}
        ]

        assert result == expected_result