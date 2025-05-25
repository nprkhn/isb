from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives import serialization

def read_text_file(file_path: str) -> str:
    """
    Function, which reads text files

    :param file_path: path to file

    :return: readed text
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    return text

def read_binary_file(file_path: str):
    """
    Function, which reads binary files

    :param file_path: path to file

    :return: readed data
    """
    with open(file_path, 'rb') as file:
        data = file.read()
    
    return data

def read_binary_private_key_file(file_path: str):
    """
    Function, which reads file with binary private key

    :param file_path: path to file

    :return: private key
    """
    with open(file_path, 'rb') as file:
        private_key = load_pem_private_key(file.read(), password=None)
    
    return private_key

def write_in_text_file(file_path: str, text: str) -> None:
    """
    Function, which writes data in text files

    :param file_path: path to file
    :param text: data
    """
    with open(file_path, 'w') as file:
        file.write(text)

def write_in_binary_file(file_path: str, data) -> None:
    """
    Function, which writes data in binary files

    :param file_path: path to file
    :param data: data
    """
    with open(file_path, 'wb') as file:
        file.write(data)

def serialization_public_key(public_key, public_key_path: str):
    """
    Function, which writes serializated public key in file

    :param public_key: public key
    :param public_key_path: path to file
    """
    with open(public_key_path, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))

def serialization_private_key(private_key, private_key_path: str):
    """
    Function, which writes serializated private key in file

    :param private_key: private_key
    :param private_key_path: path to file
    """
    with open(private_key_path, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))

def deserialization_public_key(public_key_path: str):
    """
    Function, which deserializates public key

    :param public_key_path: path to file with public key

    :return deserializated public key
    """
    with open(public_key_path, 'rb') as pem_in:
        public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)

    return d_public_key

def deserialization_private_key(private_key_path: str):
    """
    Function, which deserializates private key

    :param private_key_path: path to file with private key

    :return deserializated private key
    """
    with open(private_key_path, 'rb') as pem_in:
        private_bytes = pem_in.read()
        d_private_key = load_pem_private_key(private_bytes)

    return d_private_key
