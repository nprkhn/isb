from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from filework import read_text_file
import os

class SymmetricCrypto:
    def __init__(self):
        """
        Class attributes
        """
        self.key = None
        self.encrypted_key = None
        self.decrypted_key = None
        self.encrypted_text = None
        self.decrypted_text = None
    
    def generate__key(self, key_size: int):
        """
        Function, which generates symmetric key

        :return: symmetric key
        """
        if key_size in [16, 24, 32]:
            key = os.urandom(key_size)

            self.key = key

            return key
        else:
            print(key_size)
            raise ValueError("Key length must be 16, 24 or 32 bytes")
    
    def encrypt_text(self, text_path: str):
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

        self.encrypted_text = c_text

        return c_text
    
    def decrypt_text(self) -> bytes:
        """
        Function, which decrypts encrypted text

        :return: decrypted text
        """
        iv = self.encrypted_text[:16]
        cipher = Cipher(algorithms.Camellia(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(self.encrypted_text[16:]) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_text = unpadder.update(decrypted_padded) + unpadder.finalize()

        self.decrypted_text = decrypted_text

        return decrypted_text
