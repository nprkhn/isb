def read_file(file: str) -> str:
    """
    Function, which reading files

    :param file: path to file
    :return readed file as string
    :raises FileNotFoundError if file not found
    :raises Exception if error with reading file
    """
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
    
        return text
    except FileNotFoundError as fnfe:
        raise(f"File not found: {fnfe}")
    except Exception as exc:
        raise(f"Error with reading file: {exc}")
