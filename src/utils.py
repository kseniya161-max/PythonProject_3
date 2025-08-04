import json
import os
from typing import List, Dict, Any
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('../logs/application.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_file(file_path: str) -> List[Dict[str, Any]]:
    logger.info("Приложение запущено")
    """Чтение json файла и возвращение списка словарей с данными о транзакциях."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        logger.info("Чтения файла")
        try:
            data = json.load(f)
            logger.debug("Данные загружены: %s", data)
            if not isinstance(data, list):
                logger.error("Некорректный формат")
                return []
            return data
        except json.JSONDecodeError:
            logger.error("Некорректный json файл")
            return []


if __name__ == "__main__":
    data = read_file("C:/Users/bahar/PycharmProjects/PythonProject3/data/operations.json")
    print(data)
