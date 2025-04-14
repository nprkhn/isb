import textwork
import keyvalidate

def task1():
    """
    The main function of task 1
    """
    data = textwork.filework.read_file('settings.json')["task_1"]
    ALPHABET = data["ALPHABET"]
    input_text = data["text_path"]
    key_path = data["key_path"]
    text = textwork.filework.read_text(input_text)
    key = textwork.filework.read_text(key_path)
    
    text = textwork.changed_text(text)
    if keyvalidate.key_correctly(key):
        encrypted_text = textwork.vigeneres_algorithm(text, key, ALPHABET)
    else:
        raise ValueError("Invalid key!")
    
    print(encrypted_text)

def task2():
    """
    The main function of task 2
    """
    try:
        data = textwork.filework.read_file("settings.json")["task_2"]
        enc_text = data["enc_text_path"]
        freq_path = data["freq_path"]
        key = data["key_task2"]
        text = textwork.filework.read_text(enc_text)
        textwork.frequency_counter(text, freq_path)
        decrypted_text = textwork.decryption_task2(text, key)

        print(decrypted_text)
    except Exception as exc:
        raise(f"Error: {exc}")
    
def main():
    task1()
    task2()

    return 0

if __name__ == '__main__':
    main()