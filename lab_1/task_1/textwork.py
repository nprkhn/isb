ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ"

def changed_text(text: str) -> str:
    """
    Function, which lowercase the text

    :param text: original text
    :return changed text
    """
    changed_text = text.lower()

    return changed_text

def vigeneres_algorithm(text: str, key: str) -> str:
    """
    Vigenere's algorithm

    :param text: text, which we will encrypt
    :param key: encryption key
    :return encrypted text
    """
    encrypted_text = []
    text = changed_text(text)
    alphabet_length = 31
    mark = 0

    for char in text:
        if char in ALPHABET.lower():
            char_index = ALPHABET.index(char.upper())
            key_index = ALPHABET.index(key[mark % len(key)].upper())

            encr_idx = (char_index + key_index) % alphabet_length
            encrypted_text.append(ALPHABET[encr_idx])
            mark += 1
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def decrypted_text(text: str, key: str) -> str:
    """
    Function, which decrypting text by vigenere's algorithm

    :param text: decrypted text
    :param key: encryption key
    :return decrypted text
    """
    decrypted_text = []
    alphabet_length = 31
    mark = 0

    for char in text:
        if char in ALPHABET:
            char_index = ALPHABET.index(char)
            key_index = ALPHABET.index(key[mark % len(key)].upper())

            decr_idx = (char_index - key_index) % alphabet_length
            decrypted_text.append(ALPHABET[decr_idx])
            mark += 1
        else:
            decrypted_text.append(char)
    
    return "".join(decrypted_text)
