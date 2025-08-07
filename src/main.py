import json
import csv
import pandas as pd
import datetime
from datetime import datetime


def main_greating():
    greating = "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
    print(greating)


def open_json():
    with open("../logs/operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for operation in data:
            if 'date' in operation:
                try:
                    operation['date'] = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    print(f"Ошибка при разборе даты: {operation['date']}")
                    operation['date'] = None
        return data


def open_csv():
    with open("trans_file/transactions.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        data_json = list(reader)
        for operation in data_json:
            date_string = operation['date']
            if date_string:
                try:
                    operation["date"] = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
                except ValueError:
                    print(f"Ошибка при разборе даты: {date_string}")
                    operation["date"] = None
            else:
                operation["date"] = None
        return data_json


def open_excel():
    data_excel = pd.read_excel("trans_file/transactions_excel.xlsx", engine="openpyxl")
    data_records = data_excel.to_dict(orient='records')
    for operation in data_records:
        if pd.notnull(operation['date']):
            operation['date'] = pd.to_datetime(operation['date']).to_pydatetime()
        else:
            operation['date'] = None
    return data_records


def filtered_by_status(data, status):
    # return [operation for operation in data if operation.get('state', '').strip().lower() == status]
    return [
        operation for operation in data
        if isinstance(operation.get('state'), str) and operation['state'].strip().lower() == status
    ]


def filtered_by_date(data, ascending):
    """Функция фильтрует операции по дате."""
    return sorted(data, key=lambda x: x['date'] if isinstance(x['date'], datetime) else datetime.min, reverse=not ascending)


def sort_currency(data, code):
    """Функция фильтрует по валюте"""
    return [operation for operation in data if operation.get("operationAmount", {}).get("currency", {}).get("code") == code]


def filtered_by_word(data, word):
    return [operation for operation in data if word.lower() in operation.get('description', '').lower()]


def main_user_input():
    while True:
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
            print("Неверный ввод, введите 1, 2, или 3")


def status_input(data):
    valid_statuses = ['executed', 'canceled', 'pending']
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию." "EXECUTED, CANCELED, PENDING\n").strip().lower()
        if status in valid_statuses:
            filtered_data = filtered_by_status(data, status)
            print(f"Операции отфильтрованы по статусу \"{status}\":")
            for operation in filtered_data:
                print(operation)
            return filtered_data
        else:
            print(f"Статус операции \"{status}\" недоступен.")


def curr_input(data):
    code = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if code.strip().lower() == "да":
        filtered_code = sort_currency(data, "RUB")
        print("Отфильтрованные транзакции:")
        if filtered_code:
            for operation in filtered_code:
                print(operation)
            print(f"Всего банковских операций в выборке: {len(filtered_code)}")
        else:
            print("Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации.")

        user_input_2 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
        if user_input_2 == "да":
            word = input("Введите слово, по которому нужно отфильтровать: ")
            filtered_word = filtered_by_word(filtered_code, word)
            print("Распечатываю итоговый список транзакций...")
            print("Отфильтрованные операции по слову:")
            if filtered_word:  # Проверяем, есть ли отфильтрованные операции
                for operation in filtered_word:
                    print(operation)
                print(f"Всего банковских операций в выборке: {len(filtered_code)}")
            else:
                print("Нет операций, соответствующих указанному слову.")


def sort_operation(data):
    user_input_sort = input ("Отсортировать операции по дате? Да/Нет\n")
    if user_input_sort.strip().lower() == "да":
        user_input_sort_1 = input("Отсортировать по возрастанию или по убыванию? Возрастание/Убывание\n").strip().lower()
        ascending = user_input_sort_1 == "возрастание"
        sorted_data = filtered_by_date(data, ascending)
        print("Отсортированные операции:")
        for operation in sorted_data:
            print(operation)


# def format_and_print_operations(data):
#     """Функция выводит отфильтрованные операции в корректном виде"""
#     print(f"Всего банковских операций в выборке: {len(data)}\n")
#     for operation in data:
#         if isinstance(operation["date"], datetime):
#             date_str = operation["date"].strftime("%d.%m.%Y")
#         else:
#             date_str = "Дата не указана"
#         description = operation.get('description', 'Описание не указано')
#         operation_amount = operation.get('operationAmount')
#         if operation_amount:
#             amount = operation_amount.get('amount', 'Сумма не указана')
#             currency = operation_amount.get('currency', {}).get('name', 'Валюта не указана')
#         else:
#             amount = 'Сумма не указана'
#             currency = 'Валюта не указана'
#
#         from_account = operation.get('from', 'Счет не указан')
#         to_account = operation.get('to', 'Счет не указан')
#
#         #Сама маскировка
#         if isinstance(from_account, str):
#             if "Счет" in from_account:
#                 from_account = from_account.replace(from_account[6:10], "**")
#             elif  "Mastercard" in from_account or "Visa" in from_account:
#                 from_account = from_account[:-4] + "** ****" + from_account[0:7]
#         if isinstance(to_account, str):
#             if "Счет" in to_account:
#                 to_account = to_account.replace(to_account[6:10], '**')
#             elif 'MasterCard' in to_account or 'Visa' in to_account:
#                 to_account = to_account[:-4] + '**** **** ' + to_account[0:7]
#
#
#         print(f"{date_str} {description}")
#         print(f"{from_account} -> {to_account}")
#         print(f"Сумма: {amount} {currency}\n")


def format_and_print_operations(data):
    """Функция выводит отфильтрованные операции в корректном виде"""
    print(f"Всего банковских операций в выборке: {len(data)}\n")
    for operation in data:
        if isinstance(operation["date"], datetime):
            date_str = operation["date"].strftime("%d.%m.%Y")
        else:
            date_str = "Дата не указана"
        description = operation.get('description', 'Описание не указано')
        operation_amount = operation.get('operationAmount')
        if operation_amount:
            amount = operation_amount.get('amount', 'Сумма не указана')
            currency = operation_amount.get('currency', {}).get('name', 'Валюта не указана')
        else:
            amount = 'Сумма не указана'
            currency = 'Валюта не указана'

        from_account = operation.get('from', 'Счет не указан')
        to_account = operation.get('to', 'Счет не указан')

        # Маскировка
        def mask_account(account):
            if isinstance(account, str):
                if "Счет" in account:
                    return f"Счет **{account[-4:]}"
                elif "MasterCard" in account or "Visa" in account:

                    return account[:-4] + "** **** " + account[-4:0]
            return account

        from_account = mask_account(from_account)
        to_account = mask_account(to_account)


        print(f"{date_str} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}\n")



if __name__ == "__main__":
    main_greating()
    result, data = main_user_input()
    print(result)
    if data is not None:
        status_data = status_input(data)
        sort_operation(status_data)
        curr_input(status_data)
        format_and_print_operations(status_data)




