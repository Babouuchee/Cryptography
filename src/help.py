def print_crypto_system():
    print("  CRYPTO_SYSTEM")
    print("    \"xor\"        computation using XOR algorithm")
    print("    \"aes\"        computation using 128-bit AES algorithm")
    print("    \"rsa\"        computation using RSA algorithm")
    print("    \"pgp-xor\"    computation using both RSA and XOR algorithm")
    print("    \"pgp-aes\"    computation using both RSA and 128-bit AES algorithm")

def print_mode_options_and_key():
    print("\n  MODE")
    print("    -c           MESSAGE is clear and we want to cipher it")
    print("    -d           MESSAGE is ciphered and we want to decipher it")
    print("    -g P Q       for RSA only: Don't read a MESSAGE, but instead generate a public and private key pair from the prime numbers P and Q")

    print("\n  OPTIONS")
    print("    -b           for XOR, AES, and PGP, only works on one block. The MESSAGE and the symmetric key must be the same size")
    print("\n  key            Key used to cipher/decipher MESSAGE (incompatible with -g MODE)")

def print_usage():
    print("USAGE")
    print("    ./my_pgp CRYPTO_SYSTEM MODE [OPTIONS] [key]\n")

def print_description():
    print("DESCRIPTION")
    print("The MESSAGE is read from standard input\n")

def printHelp():
    print_usage()
    print_description()
    print_crypto_system()
    print_mode_options_and_key()