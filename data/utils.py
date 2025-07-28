import json

def read_file(file_path):
    """ Чтение json  файла"""
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data
    return