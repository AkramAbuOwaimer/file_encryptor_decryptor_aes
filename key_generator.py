import argparse as ap
import hashlib
import pyscrypt

parser = ap.ArgumentParser(description='Command-Line tool to generate a key 32byte key from a password.')
parser.add_argument('--password', '-p', required=True, type=str, help='password to generate key from.')
parser.add_argument('--key-file-path', '-o', default="./key.txt", type=str, help='path to output key file.')
parser.add_argument('--salt', '-s', action='store_true', help='use salt')
parser.add_argument('--sea-salt', '-c', type=str, help='sea salt')

args = parser.parse_args()

password = str(args.password)

if args.salt:
    if args.sea_salt is None:
        salt = hashlib.sha256("sea salt".encode('UTF-8')).hexdigest().encode('UTF-8')
    else:
        salt = args.sea_salt.encode('UTF-8')

    N = 1024
    r = 1
    p = 1

    key_32 = pyscrypt.hash(password.encode('UTF-8'), salt, N, r, p, 32)
    key_32 = key_32.hex()
    file = open(args.key_file_path, 'w').write(key_32)
else:
    hashed = hashlib.sha256(password.encode('UTF-8')).hexdigest()
    key_32 = hashed
    file = open(args.key_file_path, 'w').write(key_32)




