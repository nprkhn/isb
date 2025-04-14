import filework

def changed_text(text: str) -> str:
    """
    Function, which lowercase the text

    :param text: original text
    :return changed text
    """
    changed_text = text.lower()

    return changed_text

def vigeneres_algorithm(text: str, key: str, alphabet: str) -> str:
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
        if char in alphabet.lower():
            char_index = alphabet.index(char.upper())
            key_index = alphabet.index(key[mark % len(key)].upper())

            encr_idx = (char_index + key_index) % alphabet_length
            encrypted_text.append(alphabet[encr_idx])
            mark += 1
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def decryption_task1(text: str, key: str, alphabet: str) -> str:
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
        if char in alphabet:
            char_index = alphabet.index(char)
            key_index = alphabet.index(key[mark % len(key)].upper())

            decr_idx = (char_index - key_index) % alphabet_length
            decrypted_text.append(alphabet[decr_idx])
            mark += 1
        else:
            decrypted_text.append(char)
    
    return "".join(decrypted_text)

def frequency_counter(text: str, freq_path: str) -> None:
    """
    Function, which counting frequencies of chars in encrypted text

    :param text: encrypted text
    :return None
    """
    char_count = {}
    char_frequency = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char, count in char_count.items():
        char_frequency[char] = count / len(text)
    
    sorted_dict = dict(sorted(char_frequency.items(), key=lambda item: item[1], reverse=True))
    
    filework.write_in_file(sorted_dict, freq_path)

def decryption_task2(encrypted_text: str, key: dict) -> str:
    """
    Function, which decrypting text

    :param encrypted_text: encrypted text
    :param key: decryption key
    :return decrypted text
    """
    decrypted_text = ""

    for char in encrypted_text:
        if char in key.keys():
            decrypt_char = key[char]
            decrypted_text += decrypt_char
        else:
            decrypted_text += char
    
    return decrypted_text