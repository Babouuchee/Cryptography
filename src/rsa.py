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
            self._primeP = int(''.join([primeP[i:i + 2] for i in range(0, len(primeP), 2)][::-1]), 16)
            self._primeQ = int(''.join([primeQ[i:i + 2] for i in range(0, len(primeQ), 2)][::-1]), 16)
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
        p = self._primeP
        q = self._primeQ
        n = p * q
        lambdaN = math.lcm(p - 1, q - 1)
        e = findBiggestFermatPrime(lambdaN)
        d = pow(e, -1, lambdaN)
        public_key = f"{e.to_bytes((e.bit_length() + 7) // 8, 'little').hex()}-{n.to_bytes((n.bit_length() + 7) // 8, 'little').hex()}"
        private_key = f"{d.to_bytes((d.bit_length() + 7) // 8, 'little').hex()}-{n.to_bytes((n.bit_length() + 7) // 8, 'little').hex()}"

        print(f"public key: {public_key}")
        print(f"private key: {private_key}")

def findBiggestFermatPrime(maxValue):
    result = 0
    iteration = 0
    while True:
        fermat = 2 ** (2 ** iteration) + 1
        if fermat > maxValue or fermat > 65537:
            return result
        if math.gcd(fermat, maxValue):
            result = fermat
        iteration += 1