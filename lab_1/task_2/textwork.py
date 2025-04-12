import filework

def frequency_counter(text: str) -> None:
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
    
    filework.write_in_file(sorted_dict, 'frequency_in_text.json')

def decryption(encrypted_text: str, key: dict) -> str:
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
