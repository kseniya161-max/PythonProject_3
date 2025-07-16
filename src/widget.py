from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_data: str) -> str:
    """Функция возвращает маску номера карты или счета"""
    prefix = ""
    number = ""
    for char in account_card_data:
        if char.isdigit():
            number += char
        elif char.isalpha():
            prefix += char
    if (
        "счет" in prefix.lower()
        or "счёт" in prefix.lower()
        or "account" in prefix.lower()
    ) or len(number.strip()) != 16:
        masked_number = get_mask_card_number(number.strip())
    else:  # Обрабатываем как карту
        masked_number = get_mask_account(number.strip())
    return f"{prefix.strip()} {masked_number}"


def get_date(date: str) -> str:
    """Функция возвращает строку с датой"""
    new_date = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    return new_date


if __name__ == "__main__":
    print(mask_account_card("Счет 70007922896063612056"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(get_date("2024-03-11T02:26:18.671407"))
