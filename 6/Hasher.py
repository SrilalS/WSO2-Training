import hashlib
import secrets
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python Hasher.py <string>")
        sys.exit(1)
    else:
        string = sys.argv[1]
        salt = b''+secrets.token_hex()
        iterations = 200000
        hash = hashlib.pbkdf2_hmac('sha256',string.encode(), salt, iterations)
        print(hash)
main()