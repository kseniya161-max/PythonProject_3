from src. transactions import trans_csv_reader,trans_excel_reader
import pytest
import pandas as pd
from unittest.mock import patch


def test_trans_csv_reader():
    """Тестируем возвращает ли функция список словарей корректно"""
    mock_data = pd.DataFrame({
        'id': [650703],
        'state': ['EXECUTED'],
        'date': ['2023-09-05T11:30:32Z'],
        'amount': [16210],
        'currency_name': ['Sol'],
        'currency_code': ['PEN'],
        'from': ['Счет 58803664561298323391'],
        'to': ['Счет 39745660563456619397'],
        'description': ['Перевод организации']
    })

    # Настройка mock для pd.read_csv
    with patch('pandas.read_csv', return_value=mock_data) as mock_read_csv:
        result = trans_csv_reader('fake_file.csv')  # Имя файла не имеет значения

        expected_result = [{
            'id': 650703,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210,
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }]
        assert result == expected_result

        # Проверяем, что mock_read_csv был вызван с правильным аргументом
        mock_read_csv.assert_called_once_with('fake_file.csv')


def test_trans_csv_reader_empty_data():
    # Создаем пустой DataFrame
    mock_data = pd.DataFrame(columns=['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'])

    with patch('pandas.read_csv', return_value=mock_data):
        result = trans_csv_reader('fake_file.csv')
        expected_result = []  # Ожидаем пустой список
        assert result == expected_result


def test_trans_csv_reader_file_not_found():
    # Тестируем случай, когда файл не найден
    with patch('pandas.read_csv', side_effect=FileNotFoundError) as mock_read_csv:
        with pytest.raises(FileNotFoundError):
            trans_csv_reader('non_existent_file.csv')
        mock_read_csv.assert_called_once_with('non_existent_file.csv')


def test_trans_excel_reader():
    """Создание теста с фиктивными данными Excel"""
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

    # Начтройка mock
    with patch('pandas.read_excel', return_value=mock_data) as mock_read_excel:
        result = trans_excel_reader('fake_file.xlsx')  # имя файла не имеет значения


        mock_read_excel.assert_called_once_with('fake_file.xlsx')
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


def test_trans_excel_reader_file_not_found():
    """Тестирует случвй если файл не найден"""
    with patch('pandas.read_excel', side_effect=FileNotFoundError) as mock_read_excel:
        with pytest.raises(FileNotFoundError):
            trans_excel_reader('non_existent_file.xlsx')
        mock_read_excel.assert_called_once_with('non_existent_file.xlsx')

def test_trans_excel_reader_empty_file():
    """Тестирует случвй если файл пустой"""
    mock_data = pd.DataFrame(columns=['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'])

    with patch('pandas.read_excel', return_value=mock_data) as mock_read_excel:
        result = trans_excel_reader('fake_empty_file.xlsx')
        expected_result = []
        assert result == expected_result
        mock_read_excel.assert_called_once_with('fake_empty_file.xlsx')






