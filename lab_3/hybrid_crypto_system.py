from assymetric import AsymmetricCrypto, symmetric
from filework import write_in_binary_file, read_binary_file, read_binary_private_key_file
from extra import encrypt_key, decrypt_key

class HybridCryptoSystem:
    def generate_random_key(key_size, rand_key_path):
        """
        Extra function for generating random key

        :param key_size: key size
        :param rand_key_path: path to file with random key
        """
        sym_crypto = symmetric.SymmetricCrypto()
        sym_crypto.generate_random_key(key_size, rand_key_path)
        print("Random key succesfully generated!")

    def generate_keys(encrypted_key_path, public_key_path, private_key_path, key_path):
        """
        Function, which generates keys of hybrid crypto system

        :param encrypted_key_path: path to file with encrypted key
        :param public_key_path: path to file with public key
        :param private_key_path: path to file with private key 
        """
        print("\n=== Generation keys ===")
    
        asym_crypto = AsymmetricCrypto()
        asym_crypto.generate_keys()
        asym_crypto.serialization_keys(public_key_path, private_key_path)
        print(f"Asymmetric keys saved in:\n- {public_key_path}\n- {private_key_path}")

        key = read_binary_file(key_path)
    
        encrypted_sym_key = encrypt_key(asym_crypto.public_key, key)
        write_in_binary_file(encrypted_key_path, encrypted_sym_key)

        print(f"Encrypted symmetric key saved in: {encrypted_key_path}")

    def encrypt_data(text_path, private_key_path, encrypted_key_path, output_path):
        """
        Function, which encrypts data of hybrid crypto system

        :param text_path: path to txt file
        :param private_key_path: path to file with private key
        :param encrypted_key_path: path to file with encrypted key
        :param output_path: path to output file
        """
        print("\n=== Encryption data ===")
    
        private_key=read_binary_private_key_file(private_key_path)

        encrypted_sym_key = read_binary_file(encrypted_key_path)
    
        sym_key = decrypt_key(private_key, encrypted_sym_key)
    
        sym_crypto = symmetric.SymmetricCrypto()
        sym_crypto.key = sym_key
    
        sym_crypto.encrypt_text(text_path, output_path)
        print(f"Encrypted data saved in: {output_path}")

    def decrypt_data(encrypted_path, private_key_path, encrypted_key_path, output_path):
        """
        Function, which decrypts data of hybrid crypto system

        :param encrypted_path: path to encrypted text
        :param private_key_path: path to file with private key
        :param encrypted_key_path: path to file with encrypted key
        :param output_path: path to output file
        """
        print("\n=== Decryption data ===")
    
        private_key = read_binary_private_key_file(private_key_path)

        encrypted_sym_key = read_binary_file(encrypted_key_path)
    
        sym_key = decrypt_key(private_key, encrypted_sym_key)
    
        sym_crypto = symmetric.SymmetricCrypto()
        sym_crypto.key = sym_key
    
        sym_crypto.decrypt_text(encrypted_path, output_path)

        print(f"Decrypted data saved in: {output_path}")
