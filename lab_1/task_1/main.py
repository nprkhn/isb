import filework
import textwork
import keyvalidate

def main():
    """
    The main function
    """
    text = filework.read_file("text.txt")
    key = filework.read_file("key_task1.txt")
    
    text = textwork.changed_text(text)
    if keyvalidate.key_correctly(key):
        encrypted_text = textwork.vigeneres_algorithm(text, key)
    else:
        raise ValueError("Invalid key!")
    
    print(encrypted_text)

if __name__ == "__main__":
    main()
