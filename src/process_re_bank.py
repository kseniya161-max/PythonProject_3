import re
from collections import Counter


def process_bank_search(trans_bank: list[dict], search_bank: str) -> list[dict]:
    """Функция принимает список словарей и строку поиска и возвращает список словарей у которых есть данная строка"""
    pattern = re.compile(search_bank, re.IGNORECASE)
    filtered_operation = [trans for trans in trans_bank if "description" in trans and pattern.search(trans["description"])]
    return filtered_operation


def process_bank_operations(bank_operation: list[dict], list_operation: list) -> dict:
    """Функция считает количество банковские операции на основе поля description"""
    description_operation = [operate["description"] for operate in bank_operation if "description" in operate]
    count_descriptions = Counter(description_operation)  # список для хранения описаний операций
    result = {category: count_descriptions.get(category, 0) for category in list_operation}
    return result


if __name__ == "__main__":
    transactions_categories = [
        {'description': 'Перевод на карту', 'amount': 100, 'state': "EXECUTED", "currency": "USD"},
        {'description': 'Оплата ЖКХ', 'amount': 200, 'state': "EXECUTED", "currency": "USD"},
        {'description': 'Покупка в магазине', 'amount': 50, 'state': "EXECUTED", "currency": "USD"}
    ]


categories = ['Перевод на карту', 'Оплата ЖКХ', 'Покупка в магазине', 'Неизвестная категория']
result = process_bank_operations(transactions_categories, categories)
print(result)


if __name__ == "__main__":
    transactions = [
        {'description': 'Перевод на карту', 'amount': 100, 'state': "EXECUTED", "currency": "USD"},
        {'description': 'Оплата ЖКХ', 'amount': 200, 'state': "EXECUTED", "currency": "USD"},
        {'description': 'Покупка в магазине', 'amount': 50, 'state': "EXECUTED", "currency": "USD"}
    ]

search_term = "Перевод на карту"
result = process_bank_search(transactions, search_term)


print("Результаты поиска:")
for operation in result:
    print(operation)
