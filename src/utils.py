import json
import os
from src.external_api import convert_currency



def read_file(file_path):
    """Чтение json файла и возвращение списка словарей с данными о транзакциях."""
    if not os.path.exists(file_path):  # Проверяем, существует ли файл
        return []  # Если файл не найден, возвращаем пустой список

    with open(file_path, 'r', encoding='utf-8') as f:  # Указываем кодировку UTF-8
        try:
            data = json.load(f)  # Загружаем данные из файла
            if not isinstance(data, list):  # Проверяем, является ли data списком
                return []  # Если нет, возвращаем пустой список
            return data  # Возвращаем список словарей
        except json.JSONDecodeError:  # Обрабатываем ошибку, если файл не является корректным JSON
            return []  # Если ошибка, возвращаем пустой список

# Пример использования
data = read_file("C:/Users/bahar/PycharmProjects/PythonProject3/data/operations.json")

# Теперь data будет содержать список словарей с транзакциями или пустой список
print(data)  # Выводим данные для проверки



def get_transaction_amount_in_rub(transaction):
    """Возвращает сумму транзакции в рублях."""
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB')  # По умолчанию считаем, что валюта RUB
    return convert_currency(amount, currency)  # Конвертируем сумму в рубли
