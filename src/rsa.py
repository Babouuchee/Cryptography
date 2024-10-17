#!/usr/bin/python3

from sys import argv

class RSA():
    def __init__(self):
        self._mode = ""
        self._primeP = -1
        self._primeQ = -1
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
            self._primeP = int(argv[3])
            self._primeQ = int(argv[4])
        else:
            if len(argv) < 4:
                print("Key is missing")
            self._key = argv[3]
        self._message = input("Enter message: ")

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