import json
import csv
import pandas as pd


def main_greating():
    greating = "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
    print(greating)

def open_json():
    """ Функция для открытия файла json"""
    with open("../logs/operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def open_csv():
    with open("trans_file/transactions.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")  # Используем DictReader вместо reader
        data_json = list(reader)  # Преобразуем в список словарей
        return data_json


def open_excel():
    data_excel = pd.read_excel("trans_file/transactions_excel.xlsx", engine="openpyxl")
    return data_excel.to_dict(orient='records')


def filtered_by_status(data, status):
    """Функция фильтрует по статусу"""
    return [
        operation for operation in data
        if isinstance(operation.get('state'), str) and operation['state'].strip().lower() == status
    ]

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




if __name__ == "__main__":
    main_greating()
    result, data = main_user_input()
    print(result)
    if data is not None:
        print(data)
    status_input(data)



    # def main():
    #     transactions = load_transactions()
    #     status = input("Введите статус транзакций для фильтрации: ")
    #     filtered_transactions = filter_by_status(transactions, status)
    #     order = input("Отсортировать по возрастанию или убыванию? ")
    #     sorted_transactions = sort_transactions(filtered_transactions, order)
    #     print("Отфильтрованные и отсортированные транзакции:", sorted_transactions)




