#!/usr/bin/python3

from sys import argv

import math

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
        print("Generate")
        p = int.from_bytes(self._primeP)
        q = int.from_bytes(self._primeQ)
        n = p * q
        lambdaN = self.leastCommonMultiple(p - 1, q - 1)
        e = 65537
        if self.greatestCommonMultiple(e, lambdaN) != 1:
            raise Exception("e and lambda are not coprime")
        d = self.mod_inverse(e, lambdaN)

        public_key = f"{hex(e)}-{hex(n)}"
        private_key = f"{hex(d)}-{hex(n)}"

        print(f"Public key : {public_key}")
        print(f"Private key : {private_key}")

    def leastCommonMultiple(self, a, b):
        return abs(a * b) // self.greatestCommonMultiple(a, b)

    def greatestCommonMultiple(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def mod_inverse(self, e, phi):
        gcd_val, x, y = self.extended_gcd(e, phi)
        if gcd_val != 1:
            raise Exception("Modular inverse does not exist")
        return x % phi

    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = self.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y