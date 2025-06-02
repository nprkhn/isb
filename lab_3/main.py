from info import get_info
from hybrid_crypto_system import HybridCryptoSystem

def main():
    args = get_info()

    try:
        match args.command:
            case 'generate_random_key':
                HybridCryptoSystem.generate_random_key(args.key_size, args.rand_key_path)
            case 'generate':
                HybridCryptoSystem.generate_keys(args.encrypted_key, args.public_key, args.private_key, args.key_path)
            case 'encrypt':
                HybridCryptoSystem.encrypt_data(args.input, args.private_key, args.encrypted_key, args.output)
            case 'decrypt':
                HybridCryptoSystem.decrypt_data(args.encrypted_file, args.private_key, args.encrypted_key, args.decrypted_file)

    except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()
