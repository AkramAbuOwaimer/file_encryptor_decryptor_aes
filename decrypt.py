import argparse as ap
import pyAesCrypt

parser = ap.ArgumentParser(description='Command-Line tool to encrypt and decrypt a file, using AES-256.')
parser.add_argument('--encrypted-file-path', '-f', required=True, type=str, help='path to the encrypted file.')
parser.add_argument('--output-file-path', '-o', default="./decrypted", type=str, help='path to output file.')
parser.add_argument('--key', '-k', required=True, type=str, help='encryption key.')

args = parser.parse_args()

pyAesCrypt.decryptFile(args.encrypted_file_path, args.output_file_path, args.key, 64 * 1024)
