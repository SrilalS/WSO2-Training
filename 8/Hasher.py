import hashlib
import secrets
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python Hasher.py <string>")
        sys.exit(1)
    else:
        string = sys.argv[1]
        salt = secrets.token_hex()
        
        print(hashlib.sha512( salt + string ).hexdigest())
main()