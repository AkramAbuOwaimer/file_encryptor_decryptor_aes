# file_encryptor_decryptor_aes
Script to encrypt and decrypt a file using AES-256, and a key Generator scrypt

usage:
python key_generator.py -p yourpassword -s -o key.txt

python decrypt.py -f encrypted.bin -o decrypted.rar -k 89f7512e2ca6ed711ac156618c14bed42ff4cb645b77a860b0669384e050f117

python encrypt.py -f file.rar -o encrypted.bin -k 89f7512e2ca6ed711ac156618c14bed42ff4cb645b77a860b0669384e050f117