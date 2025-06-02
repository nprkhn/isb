from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def encrypt_key(public_key, key):
        """
        Function, which encrypts symmetric key

        :param public_key: public key
        :param key: symmetric key

        :return: encrypted key
        """
        encrypted_key = public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

        return encrypted_key

def decrypt_key(private_key, encrypted_key):
        """
        Function, which decrypts symmetric key

        :param private_key: private key
        :param encrypted_key: encrypted key

        :return: decrypted key
        """
        decrypted_key = private_key.decrypt(encrypted_key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

        decrypted_key = decrypted_key

        return decrypted_key