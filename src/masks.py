def get_mask_card_number(card_num: str) -> str:
    """Функция возвращает маску номера карты"""
    if card_num is None:
        return ""
    else:
        mask_card = f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[-4:]}"
        return mask_card


def get_mask_account(num_count: str) -> str:
    """Функция возвращает маску счета"""
    mask_count = f"** {num_count[-4:]}"
    return mask_count


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
