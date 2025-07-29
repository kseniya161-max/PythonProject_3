from src.utils import read_file
import json
import requests
import os
from dotenv import load_dotenv

# переменные из окружения .env
load_dotenv()

# Доступ к переменным окружения
api_key = os.getenv('API_KEY')

print(f"Токен доступа: {api_key}")


def get_currency(currency_code):
    """Получает курс валют и конвертирует его в рубли"""

    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency_code}"
    headers = {
        "apikey": "1XqmGMhWlHPfZgIWn9q6DU3bTlflFCt5"  # Мой Api ключ
    }

    try:
        response = requests.get(url, headers=headers)
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


currency_code = 'USD'
try:
    rate = get_currency(currency_code)
    print(f"Курс {currency_code} в рублях: {rate}")
except Exception as e:
    print(e)


def convert_currency(amount, currency_code):
    """ Конвертируем в рубли"""
    if currency_code in ['USD', 'EUR']:
        rate = get_currency(currency_code)
        return amount * rate
    return amount


def get_transaction_amount_in_rub(transaction):
    """Возвращает сумму транзакции в рублях."""
    operation_amount = transaction.get('operationAmount', {})
    amount = float(operation_amount.get('amount', 0))
    currency = operation_amount.get('currency', {}).get('code', 'RUB')  # По умолчанию считаем RUB
    print(f"Транзакция: {transaction}")
    print(f"Сумма: {amount}, Валюта: {currency}")

    if amount <= 0:
        return 0  # Возвращаем 0, если сумма отсутствует или меньше 0

    return convert_currency(amount, currency)  # Конвертируем сумму в рубли
    print(convert_currency)


data = read_file("C:/Users/bahar/PycharmProjects/PythonProject3/data/operations.json")

for transaction in data:
    amount_in_rub = get_transaction_amount_in_rub(transaction)
    print(f"Сумма транзакции в рублях: {amount_in_rub}")




