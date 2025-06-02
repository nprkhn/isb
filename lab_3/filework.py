from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives import serialization

def read_text_file(file_path: str) -> str:
    """
    Function, which reads text files

    :param file_path: path to file

    :return: readed text
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    
        return text
    except FileNotFoundError as fnfe:
        raise(f'File not found: {fnfe}')
    except Exception as exc:
        raise(f'Error with reading text file: {exc}')

def read_binary_file(file_path: str):
    """
    Function, which reads binary files

    :param file_path: path to file

    :return: readed data
    """
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
    
        return data
    except FileNotFoundError as fnfe:
        raise(f'file not found: {fnfe}')
    except Exception as exc:
        raise(f'Error with reading binary file: {exc}')

def read_binary_private_key_file(file_path: str):
    """
    Function, which reads file with binary private key

    :param file_path: path to file

    :return: private key
    """
    try:
        with open(file_path, 'rb') as file:
            private_key = load_pem_private_key(file.read(), password=None)
    
        return private_key
    except FileNotFoundError as fnfe:
        raise(f'File not found: {fnfe}')
    except Exception as exc:
        raise(f'Error with reading private key file: {exc}')

def write_in_text_file(file_path: str, text: str) -> None:
    """
    Function, which writes data in text files

    :param file_path: path to file
    :param text: data
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except Exception as exc:
        raise(f'Error with writing in text file: {exc}')

def write_in_binary_file(file_path: str, data) -> None:
    """
    Function, which writes data in binary files

    :param file_path: path to file
    :param data: data
    """
    try:
        with open(file_path, 'wb') as file:
            file.write(data)
    except Exception as exc:
        raise(f'Error with writing into binary file: {exc}')

def serialization_public_key(public_key, public_key_path: str):
    """
    Function, which writes serializated public key in file

    :param public_key: public key
    :param public_key_path: path to file
    """
    try:
        with open(public_key_path, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except FileNotFoundError as fnfe:
        raise(f'File not found: {fnfe}')
    except Exception as exc:
        raise(f'Error with writing serializated key: {exc}')

def serialization_private_key(private_key, private_key_path: str):
    """
    Function, which writes serializated private key in file

    :param private_key: private_key
    :param private_key_path: path to file
    """
    try:
        with open(private_key_path, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))
    except FileNotFoundError as fnfe:
        raise(f'File not found: {fnfe}')
    except Exception as exc:
        raise(f'Error with writing serializated key: {exc}')

def deserialization_public_key(public_key_path: str):
    """
    Function, which deserializates public key

    :param public_key_path: path to file with public key

    :return deserializated public key
    """
    try:
        with open(public_key_path, 'rb') as pem_in:
            public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)

        return d_public_key
    except FileNotFoundError as fnfe:
        raise(f'File not found: {fnfe}')
    except Exception as exc:
        raise(f'Error with deserializating key: {exc}')

def deserialization_private_key(private_key_path: str):
    """
    Function, which deserializates private key

    :param private_key_path: path to file with private key

    :return deserializated private key
    """
    try:
        with open(private_key_path, 'rb') as pem_in:
            private_bytes = pem_in.read()
            d_private_key = load_pem_private_key(private_bytes)

        return d_private_key
    except FileNotFoundError as fnfe:
        raise(f'File not found: {fnfe}')
    except Exception as exc:
        raise(f'Error with deserializating key: {exc}')
