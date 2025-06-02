from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from filework import read_text_file, write_in_binary_file, read_binary_file
import os

class SymmetricCrypto:
    def __init__(self):
        """
        Class attributes
        """
        self.key = None
    
    def generate_random_key(self, key_size: int, rand_key_path: str):
        """
        Function, which generates random key

        :return: symmetric key
        """
        if key_size in [16, 24, 32]:
            key = os.urandom(key_size)

            self.key = key
            write_in_binary_file(rand_key_path, key)

        else:
            print(key_size)
            raise ValueError("Key length must be 16, 24 or 32 bytes")
    
    def encrypt_text(self, text_path: str, encrypted_text_path: str):
        """
        Function, which encrypts text file

        :param text_path: path to txt file

        :return: encrypted_text
        """
        padder = padding.PKCS7(algorithms.Camellia.block_size).padder()
        text = read_text_file(text_path)
        text = text.encode('utf-8')
        padded_text = padder.update(text)+padder.finalize()

        iv = os.urandom(16)
        cipher = Cipher(algorithms.Camellia(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = iv + encryptor.update(padded_text) + encryptor.finalize()

        write_in_binary_file(encrypted_text_path, c_text)

    def decrypt_text(self, encrypted_text_path: str, decrypted_text_path: str):
        """
        Function, which decrypts encrypted text

        :return: decrypted text
        """
        encrypted_text = read_binary_file(encrypted_text_path)
        iv = encrypted_text[:16]
        cipher = Cipher(algorithms.Camellia(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(encrypted_text[16:]) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_text = unpadder.update(decrypted_padded) + unpadder.finalize()

        write_in_binary_file(decrypted_text_path, decrypted_text)
