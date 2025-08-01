import pandas as pd
import csv
from typing import List, Dict


def trans_csv_reader(file_csv: str) -> List[Dict]:
    """Функция читает CSV файл"""
    df = pd.read_csv(file_csv)
    return df.to_dict(orient='records')



def trans_excel_reader(file_excel: str) -> List[Dict]:
    """ Функция читает EXCEL файл"""
    excel_df = pd.read_excel(file_excel)
    return excel_df.to_dict(orient='records')


if __name__=="__main__":
    transactions = trans_csv_reader("trans_file/transactions.csv")
    print(transactions)

    transactions_excel = trans_excel_reader("transactions_excel.xlsx")
    print(transactions_excel)
