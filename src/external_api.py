from src.utils import read_file
import requests
import os
from dotenv import load_dotenv
from typing import Any


load_dotenv()
api_key = os.getenv('API_KEY')
""" Если Api нет в окружении то это вызовет ошибку"""
if api_key is None:
    raise ValueError("API_KEY не найден в переменных окружения.")


def get_currency(currency_code: str) -> float:
    """Получает курс валют и конвертирует его в рубли"""
    api_key = os.getenv('API_KEY')

    url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {
        "apikey": api_key
    }
    params = {'symbols': 'RUB', 'base': currency_code}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        if 'rates' in data and 'RUB' in data['rates']:
            return data['rates']['RUB']  # Возвращается курс рубля
        else:
            raise Exception("Курс рубля не найден в ответе API.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка при обращении к API: {e}")
    except Exception as e:
        raise Exception(f"Общая ошибка: {e}")


def convert_currency(amount: float, currency_code: str) -> float:
    """ Конвертируем в рубли"""
    if currency_code == 'RUB':
        return amount
    rates = get_currency(currency_code)
    return amount * rates


def get_transaction_amount_in_rub(transaction: dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    operation_amount = transaction.get('operationAmount', {})
    amount = float(operation_amount.get('amount', 0))
    currency = operation_amount.get('currency', {}).get('code', 'RUB')
    print(f"Сумма: {amount}, Валюта: {currency}")

    if amount <= 0:
        return 0

    return convert_currency(amount, currency)  # Конвертируем сумму в рубли

if __name__ == "__main__":
    data = read_file("C:/Users/bahar/PycharmProjects/PythonProject3/data/operations.json")
    print(data)
