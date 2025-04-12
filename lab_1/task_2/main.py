import textwork

def main():
    """
    The main function
    """
    try:
        text = textwork.filework.read_text("cod12.txt")
        textwork.frequency_counter(text)
        key = textwork.filework.read_file("key.json")
        decrypted_text = textwork.decryption(text, key)

        print(decrypted_text)
    except Exception as exc:
        raise(f"Error: {exc}")

if __name__ == '__main__':
    main()
