import argparse as ap
import pyAesCrypt

parser = ap.ArgumentParser(description='Command-Line tool to encrypt and decrypt a file, using AES-256.')
parser.add_argument('--file-path', '-f', required=True, type=str, help='path to the file to be encrypted.')
parser.add_argument('--encrypted-file-path', '-o', default="./encrypted.bin", type=str, help='path to output file.')
parser.add_argument('--key', '-k', required=True, type=str, help='encryption key.')

args = parser.parse_args()

pyAesCrypt.encryptFile(args.file_path, args.encrypted_file_path, args.key, 64 * 1024)
