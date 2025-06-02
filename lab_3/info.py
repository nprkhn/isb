import argparse

def get_info():
    """
    Function, which reads data from console
    """
    parser = argparse.ArgumentParser(description="Hybrid crypto system")
    subparsers = parser.add_subparsers(dest='command', required=True)

    gen_rand_parser = subparsers.add_parser('generate_random_key', help='Random key generation')
    gen_rand_parser.add_argument('--key_size', type=int, required=True, help='Key size')
    gen_rand_parser.add_argument('--rand_key_path', required=True, help='Random key path')

    gen_parser = subparsers.add_parser('generate', help='Keys generation')
    gen_parser.add_argument('--encrypted_key', required=True, help='Encrypted key path')
    gen_parser.add_argument('--public_key', required=True, help='Public key path')
    gen_parser.add_argument('--private_key', required=True, help='Private key path')
    gen_parser.add_argument('--key_path', required=True, help='Key path')

    enc_parser = subparsers.add_parser('encrypt', help='Data encryption')
    enc_parser.add_argument('--input', required=True, help='Text path')
    enc_parser.add_argument('--private_key', required=True, help='Private key path')
    enc_parser.add_argument('--encrypted_key', required=True, help='Encrypted key path')
    enc_parser.add_argument('--output', required=True, help='Finally data path')

    dec_parser = subparsers.add_parser('decrypt', help='Decryption data')
    dec_parser.add_argument('--encrypted_file', required=True, help='Encrypted file')
    dec_parser.add_argument('--private_key', required=True, help='Private key path')
    dec_parser.add_argument('--encrypted_key', required=True, help='Encrypted key path')
    dec_parser.add_argument('--decrypted_file', required=True, help='Decryption data path')

    args = parser.parse_args()

    return args 