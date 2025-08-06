import json
import csv
import pandas as pd
import datetime
from datetime import datetime


def main_greating():
    greating = "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
    print(greating)

def open_json():
    """ Функция для открытия файла json"""
    with open("../logs/operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for operation in data:
            if 'date' in operation:  # Проверяем, есть ли ключ 'date'
                try:
                    operation['date'] = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    print(f"Ошибка при разборе даты: {operation['date']}")
                    operation['date'] = None  # или установите значение по умолчанию
            else:
                print("Запись не содержит ключ 'date':", operation)  # Выводим сообщение для отладки
                operation['date'] = None  # или установите значение по умолчанию


        return data


def open_csv():
    """Функция для открытия файла CSV"""
    with open("trans_file/transactions.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")  # Используем DictReader вместо reader
        data_json = list(reader)  # Преобразуем в список словарей
        for operation in data_json:
            operation["date"] = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
        return data_json


def open_excel():
    """ Функция для открытия файла Excel"""
    data_excel = pd.read_excel("trans_file/transactions_excel.xlsx", engine="openpyxl")
    data_records = data_excel.to_dict(orient='records')
    for operation in data_records:
        operation['date'] = pd.to_datetime(operation['date']).to_pydatetime()
    return data_records


def filtered_by_status(data, status):
    """Функция фильтрует по статусу Нр: Executed, Canceled"""
    return [
        operation for operation in data
        if isinstance(operation.get('state'), str) and operation['state'].strip().lower() == status
    ]

def filtered_by_date(data, ascending):
    """Функция фильтрует операции по дате."""
    return sorted(data, key=lambda x: x.get('date') or datetime.min, reverse=not ascending)


def sort_currency(data, code):
    """Функция фильтрует по валюте"""
    return [operation for operation in data if operation.get("operationAmount", {}).get("currency", {}).get("code") == code]

def filtered_by_word(data, word):
    """Функция фильтрует по ключевому слову"""
    # return [operation for operation in data if word.lower() in operation.get("description", "").lower()]
    return [operation for operation in data if word.lower() in operation['description'].lower()]

def main_user_input():
    users_input = input("Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла \n"
          "2. Получить информацию о транзакциях из CSV-файла \n"
          "3. Получить информацию о транзакциях из XLSX-файла \n")

    if users_input == "1":
                return "Для обработки выбран JSON-файл", open_json()
    elif users_input == "2":
            return "Для обработки выбран CSV-файл", open_csv()
    elif users_input == "3":
        return "Для обработки выбран XLSX-файл", open_excel()
    else:
        return "Неверный ввод, введите 1, 2, или 3", None


def status_input(data):
    status = input("Введите статус, по которому необходимо выполнить фильтрацию."
                         "EXECUTED, CANCELED, PENDING").strip().lower()
    filtered_data = filtered_by_status(data, status)
    if filtered_data:
        print(f"Операции отфильтрованы по статусу \"{status}\":")
        for operation in filtered_data:
            print(operation)
    else:
        print(f"Нет операций со статусом \"{status}\". Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")


def curr_input(data):
    code = input("Выводить только рублевые транзакции? Да/Нет").strip().lower()
    if code.strip().lower() == "да":
        filtered_code = sort_currency(data, "RUB")
        print("Отфильтрованные транзакции:")

        for operation in filtered_code:
            print(operation)
        print(f"Всего банковских операций в выборке: {len(filtered_code)}")

        user_input_2 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").strip().lower()
        if user_input_2 == "да":
            word = input("Введите слово, по которому нужно отфильтровать: ")
            filtered_word = filtered_by_word(filtered_code, word)
            print("Отфильтрованные операции по слову:")
            if filtered_word:  # Проверяем, есть ли отфильтрованные операции
                for operation in filtered_word:
                    print(operation)
                print(f"Всего банковских операций в выборке: {len(filtered_code)}")
            else:
                print("Нет операций, соответствующих указанному слову.")



def sort_operation(data):
    user_input_sort = input ("Отсортировать операции по дате? Да/Нет")
    if user_input_sort.strip().lower() == "да":
        user_input_sort_1 = input("Отсортировать по возрастанию или по убыванию? Возрастание/Убывание").strip().lower()
        ascending = user_input_sort_1 == "возрастание"
        sorted_data = filtered_by_date(data, ascending)
        print("Отсортированные операции:")
        for operation in sorted_data:
            print(operation)




if __name__ == "__main__":
    main_greating()
    result, data = main_user_input()
    print(result)
    if data is not None:
        print(data)
    status_input(data)
    sort_operation(data)
    curr_input(data)





    # def main():
    #     transactions = load_transactions()
    #     status = input("Введите статус транзакций для фильтрации: ")
    #     filtered_transactions = filter_by_status(transactions, status)
    #     order = input("Отсортировать по возрастанию или убыванию? ")
    #     sorted_transactions = sort_transactions(filtered_transactions, order)
    #     print("Отфильтрованные и отсортированные транзакции:", sorted_transactions)




