import json
import os
from typing import List, Dict, Any
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('src/utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_file(file_path: str) -> List[Dict[str, Any]]:
    logging.info("Приложение запущено")
    """Чтение json файла и возвращение списка словарей с данными о транзакциях."""
    if not os.path.exists(file_path):  # Проверяем, существует ли файл
        return []  # Если файл не найден, возвращаем пустой список

    with open(file_path, 'r', encoding='utf-8') as f:  # Указываем кодировку UTF-8
        logging.info("Чтения файла")
        try:
            data = json.load(f)  # Загружаем данные из файла
            if not isinstance(data, list):  # Проверяем, является ли data списком
                logging.error("Некорректный формат")
                return []  # Если нет, возвращаем пустой список
            return data  # Возвращаем список словарей
        except json.JSONDecodeError:  # Обрабатываем ошибку, если файл не является корректным JSON
            logging.error("Некорректный json файл")
            return []  # Если ошибка, возвращаем пустой список
