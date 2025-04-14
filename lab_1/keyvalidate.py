ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯЭЮЯ"

def key_correctly(key: str) -> bool:
    """
    Function, which verifies the validity of key

    :param key: encryption key
    :return true if key is valid and false if key is invalid
    """
    if not key:
        return False
    else:
        changed_key = key.lower()

        for char in changed_key:
            if char not in ALPHABET.lower():
                return False
    
    return True