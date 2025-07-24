transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


# def filter_by_currency(transactions, currency_code):
#     """Функция использует генератор для фильтрации транзакций по валюте"""
#     filtered_transactions = [
#         transaction for transaction in transactions if transaction['operationAmount']['currency']['code'] == currency_code]
#     return filtered_transactions
#
#
# if __name__ == "__main__":
#     usd_transactions = filter_by_currency(transactions, 'USD')
#
#     for transaction in usd_transactions:
#         print(transaction)


# def filter_by_currency(transactions, currency_code):
#     """Функция использует генератор для фильтрации транзакций по валюте"""
#     filtered_transactions = (
#     transaction for transaction in transactions if
#     transaction['operationAmount']['currency']['code'] == currency_code)
#     yield filtered_transactions
#
#
# if __name__ == "__main__":
#     usd_transactions = filter_by_currency(transactions, 'USD')
#
# for transaction in usd_transactions:
#     print(next(transaction))


def filter_by_currency(transactions, currency_code):
    """Функция использует генератор для фильтрации транзакций по валюте"""
    filtered_transactions = (
    transaction for transaction in transactions if
    transaction['operationAmount']['currency']['code'] == currency_code)
    return filtered_transactions


def transaction_descriptions(transactions):
    """ Функция реализует генератор который принимает список словарей
     с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        if transaction.get("description"):
            yield transaction.get("description")


def card_number_generator(start: int, stop: int):
    """ Генератор генерирует номера карт в диаппазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for card_num in range(start, stop):
        yield f"{card_num:016d}"[:4] + " " + f"{card_num:016d}"[4:8] + " " + f"{card_num:016d}"[8:12] + " " + f"{card_num:016d}"[12:16]


if __name__ == "__main__":
    start = 1
    stop = 9999_9999_9999_9999
    generator = card_number_generator(start, stop)

    for _ in range(5):
        print(next(generator))


if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, 'USD')

    for transaction in usd_transactions:
        print(transaction)


if __name__ == "__main__":
    result = transaction_descriptions(transactions)
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))