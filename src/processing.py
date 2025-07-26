operation = [{'id': 41428829, 'state': 'EXECUTED',
              'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED',
              'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED',
              'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED',
              'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(operation: list, state: str = 'EXECUTED') -> list:
    """Сортирует список словарей по значению state"""
    result = []
    for operat in operation:
        if operat.get('state') == state:
            result.append(operat)
    return result


if __name__ == "__main__":
    print(filter_by_state(operation, 'EXECUTED'))
    print(filter_by_state(operation, 'CANCELED'))


def sort_by_date(operation: list) -> list:
    """Сортирует список словарей по дате"""
    if not all(isinstance(x["date"], str) for x in operation):
        raise ValueError

    return sorted(operation, key=lambda x: x["date"], reverse=True)


if __name__ == "__main__":
    print(sort_by_date(operation))
