import json

def read_json(path: str) -> dict:
    """
    Function, which read json files

    :param path: path to json file
    :return dictionary with json file's data
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            dictionary = json.load(file)
    
        return dictionary
    except FileNotFoundError as fnfe:
        raise(f"File not found: {fnfe}")
    except Exception as exc:
        raise(f"Error with reading json file: {exc}")

def read_file(path: str) -> str:
    """
    Function, which read txt files

    :param path: path to txt file
    :return readed text
    """
    try:
        text = ""
        with open(path, 'r', encoding = 'utf-8') as file:
            text = file.read()
    
        return text
    except FileNotFoundError as fnfe:
        raise(f"File not found: {fnfe}")
    except Exception as exc:
        raise(f"Error with reading txt file: {exc}")
