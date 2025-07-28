from src.utils import read_file, get_transaction_amount_in_rub
import json
import requests


def get_currency(currency_code):
    """Получает курс валют и конвертирует его в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base=USD"
    headers = {
        "apikey": "1XqmGMhWlHPfZgIWn9q6DU3bTlflFCt5"  # АПИ КЛЮЧ
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return ['rates'],['RUB']
    else:
        raise Exception("Ошибка при получении курса валюты.")

def convert_currency(amount, currency_code):
    """ Конвертируем в рубли"""
    if currency_code in ['USD', 'EUR']:
        rate = get_currency(currency_code)
        return amount * rate # Конвертируем сумму в рубли
    return amount

# Пример использования
data = read_file("C:/Users/bahar/PycharmProjects/PythonProject3/data/operations.json")

for transaction in data:
    amount_in_rub = get_transaction_amount_in_rub(transaction)
    print(f"Сумма транзакции в рублях: {amount_in_rub}")



