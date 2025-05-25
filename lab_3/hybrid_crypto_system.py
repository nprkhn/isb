from assymetric import AsymmetricCrypto
from filework import write_in_binary_file, read_binary_file, read_binary_private_key_file
from extra import encrypt_key, decrypt_key
from symmetric import SymmetricCrypto

class HybridCryptoSystem:
    def generate_keys(encrypted_key_path, public_key_path, private_key_path, key_size):
        """
        Function, which generates keys of hybrid crypto system

        :param encrypted_key_path: path to file with encrypted key
        :param public_key_path: path to file with public key
        :param private_key_path: path to file with private key 
        """
        print("\n=== Generation keys ===")
    
        sym_crypto = SymmetricCrypto()
        sym_key = sym_crypto.generate__key(key_size)
        print("Symmetric key succesfully generated!")
    
        asym_crypto = AsymmetricCrypto()
        public_key, private_key = asym_crypto.generate_keys()
        asym_crypto.serialization_keys(public_key_path, private_key_path)
        print(f"Asymmetric keys saved in:\n- {public_key_path}\n- {private_key_path}")
    
        encrypted_sym_key = encrypt_key(public_key, sym_key)
        write_in_binary_file(encrypted_key_path, encrypted_sym_key)

        print(f"Encrypted key saved in: {encrypted_key_path}")

    def encrypt_data(text_path, private_key_path, encrypted_key_path, output_path):
        """
        Function, which encrypts data of hybrid crypto system

        :param text_path: path to txt file
        :param private_key_path: path to file with private key
        :param encrypted_key_path: path to file with encrypted key
        :param output_path: path to output file
        """
        print("\n=== Encryption data ===")
    
        asym_crypto = AsymmetricCrypto()
        private_key=read_binary_private_key_file(private_key_path)

        encrypted_sym_key = read_binary_file(encrypted_key_path)
    
        sym_key = decrypt_key(private_key, encrypted_sym_key)
    
        sym_crypto = SymmetricCrypto()
        sym_crypto.key = sym_key
    
        encrypted_data = sym_crypto.encrypt_text(text_path)
        write_in_binary_file(output_path, encrypted_data)
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
    
        asym_crypto = AsymmetricCrypto()
        private_key = read_binary_private_key_file(private_key_path)

        encrypted_sym_key = read_binary_file(encrypted_key_path)
    
        sym_key = decrypt_key(private_key, encrypted_sym_key)
    
        sym_crypto = SymmetricCrypto()
        sym_crypto.key = sym_key

        sym_crypto.encrypted_text = read_binary_file(encrypted_path)
    
        decrypted_data = sym_crypto.decrypt_text()

        write_in_binary_file(output_path, decrypted_data)

        print(f"Decrypted data saved in: {output_path}")
        print("\nDecrypted data:")
        print(decrypted_data.decode('utf-8'))
