import json

def read_file(path: str) -> dict:
    """
    Function, which reading json files

    :param path: path to file
    :return dictionary
    :raises FileNotFoundError if file not found
    :raises Exception if error with reading file
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            dictionary = json.load(file)
    
        return dictionary
    except FileNotFoundError as fnfe:
        raise(f"File not found: {fnfe}")
    except Exception as exc:
        raise(f"Error with reading file: {exc}")

def read_text(path: str) -> str:
    """
    Function, which reading files

    :param path: path to file
    :return file's text as string
    :raises FileNotFoundError if file not found
    :raises Exception if error with reading file
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
    
        return text
    except FileNotFoundError as fnfe:
        raise(f"File not found: {fnfe}")
    except Exception as exc:
        raise(f"Error with reading file: {fnfe}")

def write_in_file(freq_count: dict, path: str) -> None:
    """
    Function, which writing char's frequency in json file

    :param freq_count: dictionary with char's frequency
    :return None
    :raises Exception if dictionary is not found or error with writing in file
    """
    try:
        with open(path, 'w', encoding="utf-8") as file:
            json.dump(freq_count, file)
    except Exception as exc:
        raise(f"Dictionary is not found or error with writing in file: {exc}")
