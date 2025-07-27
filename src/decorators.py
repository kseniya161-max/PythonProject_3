import logging
import datetime
from functools import wraps
help(logging)


import logging
import functools


def setup_logging(filename=None):
    """Создание и настройка логирования."""
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format='%(asctime)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def log(filename=None):
    """Декоратор для логирования выполнения функции."""
    setup_logging(filename)

    def decorator(func):
        # Создаем логгер для текущей функции
        logger = logging.getLogger(func.__name__)

        # Настройка индивидуального обработчика для этой функции
        handler = logging.StreamHandler() if filename is None else logging.FileHandler(filename)
        handler.setLevel(logging.INFO)

        # Форматирование логов
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)


        logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f'Starting function: {func.__name__}, args: {args}, kwargs: {kwargs}')
            try:
                result = func(*args, **kwargs)
                logger.info(f'Function: {func.__name__} completed successfully with result: {result}')
                return result
            except Exception as e:
                logger.error(
                    f'Error in function: {func.__name__}, error type: {type(e).__name__}, args: {args}, kwargs: {kwargs}')
                raise
            finally:
                logger.info(f'Ending function: {func.__name__}')

        return wrapper

    return decorator


# "my_filename_log.txt"
@log()
def get_mask_card_number(card_num: str) -> str:
    """Функция возвращает маску номера карты"""
    if card_num is None:
        return ""
    else:
        mask_card = f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[-4:]}"
        return mask_card


@log()
def get_mask_account(num_count: str) -> str:
    """Функция возвращает маску счета"""
    mask_count = f"**{num_count[-4:]}"
    return mask_count


@log("my_filename_log.txt")
def faulty_function():
    raise ValueError("This is a test exception")

if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_card_number(None))

if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
