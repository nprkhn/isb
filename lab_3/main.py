from info import get_info
from hybrid_crypto_system import HybridCryptoSystem

def main():
    args = get_info()

    try:
        if args.command == 'generate':
            HybridCryptoSystem.generate_keys(args.encrypted_key, args.public_key, args.private_key, args.key_size)
        elif args.command == 'encrypt':
            HybridCryptoSystem.encrypt_data(args.input, args.private_key, args.encrypted_key, args.output)
        elif args.command == 'decrypt':
            HybridCryptoSystem.decrypt_data(args.input, args.private_key, args.encrypted_key, args.output)
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()