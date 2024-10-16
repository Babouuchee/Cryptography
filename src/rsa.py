#!/usr/bin/python3

from sys import argv

class RSA():
    def __init__(self):
        self._mode = ""
        self._primeP = ""
        self._primeQ = ""
        self._key = ""
        self._message = ""

        if len(argv) < 3:
            print("Missing arguments")
            exit(84)
        if len(argv) > 6:
            print("Too many arguments")
            exit(84)
        self._mode = argv[2]
        if "-c" not in self._mode and "-d" not in self._mode and "-g" not in self._mode:
            print("Invalid mode")
            exit(84)
        if self._mode == "-g":
            if len(argv) < 5:
                print("Prime numbers are missing")
                exit(84)
            if len(argv) > 5:
                print("Key is not supposed to be with -g")
                exit(84)
            primeP = argv[3]
            primeQ = argv[4]
            if self.isHex(primeQ) is False or self.isHex(primeP) is False or len(primeP) % 2 != 0 or len(primeQ) % 2 != 0:
                print("Prime numbers must be in hexadecimal")
                exit(84)
            self._primeQ = bytes.fromhex(primeP)
            self._primeP = bytes.fromhex(primeQ)
        else:
            if len(argv) < 4:
                print("Key is missing")
            key = argv[3]
            if self.isHex(self._key) is False or len(key) % 2 != 0:
                print("Key must be in hexadecimal")
                exit(84)
            self._key = bytes.fromhex(key)
        self._message = input("Enter message: ")

    def isHex(self, input):
        hexValues = "0123456789abcdef"
        for letter in input:
            if letter not in hexValues:
                return False
        return True

    def run(self):
        print(f"RSA  mode: '{self._mode}'  primes: '{self._primeQ},{self._primeP}'  key: '{self._key}'  message: '{self._message}'" if self._mode == "-g" else f"RSA  mode: '{self._mode}'  key: '{self._key}'  message: '{self._message}'")
        if self._mode == "-c":
            self.cipher()
        elif self._mode == "-d":
            self.decipher()
        elif self._mode == "-g":
            self.generate()
        else:
            print("Invalid mode")
            exit(84)

    def cipher(self):
        print("Cipher")

    def decipher(self):
        print("Decipher")

    def generate(self):
        print("Decipher")