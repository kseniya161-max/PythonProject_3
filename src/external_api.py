from src.utils import read_file
import json
import requests


def get_currency(currency_code):
    """Получает курс валют и конвертирует его в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency_code}"
    headers = {
        "apikey": "1XqmGMhWlHPfZgIWn9q6DU3bTlflFCt5"  # АПИ КЛЮЧ
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Возвращаем курс для указанной валюты
        return data['rates']['RUB']  # Получаем курс RUB для данной валюты
    else:
        raise Exception("Ошибка при получении курса валюты.")


def convert_currency(amount, currency_code):
    """ Конвертируем в рубли"""
    if currency_code in ['USD', 'EUR']:
        rate = get_currency(currency_code)
        return amount * rate # Конвертируем сумму в рубли
    return amount





def get_transaction_amount_in_rub(transaction):
    """Возвращает сумму транзакции в рублях."""
    operation_amount = transaction.get('operationAmount', {})
    amount = float(operation_amount.get('amount', 0))
    currency = operation_amount.get('currency', {}).get('code', 'RUB')  # По умолчанию считаем, что валюта RUB
    print(f"Транзакция: {transaction}")  # Выводим всю транзакцию
    print(f"Сумма: {amount}, Валюта: {currency}")  # Выводим сумму и валюту

    if amount <= 0:
        return 0  # Возвращаем 0, если сумма отсутствует или отрицательная

    return convert_currency(amount, currency)  # Конвертируем сумму в рубли
    print(convert_currency)


# Пример использования
data = read_file("C:/Users/bahar/PycharmProjects/PythonProject3/data/operations.json")

for transaction in data:
    amount_in_rub = get_transaction_amount_in_rub(transaction)
    print(f"Сумма транзакции в рублях: {amount_in_rub}")




