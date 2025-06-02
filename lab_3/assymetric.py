from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from filework import deserialization_private_key, deserialization_public_key, serialization_private_key, serialization_public_key
import symmetric

class AsymmetricCrypto:
    def __init__(self):
        """
        Class attributes
        """
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        """
        Function, which generates private and public keys

        :return: public and private keys
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        self.public_key = public_key
        self.private_key = private_key

    def serialization_keys(self, s_public_key_path: str, s_private_key_path: str):
        """
        Function, which serializates public and private keys

        :param s_public_key_path: path to file with public key
        :param s_private_key_path: path to file with private key
        """
        serialization_public_key(self.public_key, s_public_key_path)
        serialization_private_key(self.private_key, s_private_key_path)

    def deserialization_keys(self, s_public_key_path: str, s_private_key_path: str, d_public_key_path: str, d_private_key_path: str):
        """
        Function, which deserializates public and private keys

        :param: s_public_key_path: path to file with serializated public key
        :param: s_private_key_path: path to file with serializated private key

        :return: deserializated public and private keys
        """
        d_public_key = deserialization_public_key(s_public_key_path)
        d_private_key = deserialization_private_key(s_private_key_path)

        symmetric.write_in_binary_file(d_public_key_path, d_public_key)
        symmetric.write_in_binary_file(d_private_key_path, d_private_key)
