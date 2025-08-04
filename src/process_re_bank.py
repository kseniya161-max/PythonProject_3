import re


def process_bank_search(trans_bank: list[dict], search_bank: str) -> list[dict]:
    pattern = re.compile(search_bank, re.IGNORECASE)
    filtered_operation = [trans for trans in trans_bank if "description" in trans and pattern.search(trans["description"])]
    return filtered_operation




if __name__=="__main__":
    transactions = [
        {'description': 'Перевод на карту', 'amount': 100, 'state': "EXECUTED", "currency": "USD"},
        {'description': 'Оплата ЖКХ', 'amount': 200, 'state': "EXECUTED", "currency": "USD"},
        {'description': 'Покупка в магазине', 'amount': 50, 'state': "EXECUTED","currency": "USD"}
    ]

search_term = "Перевод на карту"
result = process_bank_search(transactions, search_term)


print("Результаты поиска:")
for operation in result:
    print(operation)
