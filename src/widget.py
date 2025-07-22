from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_data: str) -> str:
    """Функция возвращает маску номера карты или счета"""
    name, number = account_card_data.rsplit(' ', maxsplit=1)
    if name.lower() in {'счет', 'счёт'}:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f'{name} {masked_number}'


def get_date(date: str) -> str:
    """Функция возвращает строку с датой"""
    day = date[8:10]
    month = date[5:7]
    year = date[0:4]
    new_date = f"{day}.{month}.{year}"
    return new_date


if __name__ == "__main__":
    print(mask_account_card("Счет 70007922896063612056"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(get_date("2024-03-11T02:26:18.671407"))
