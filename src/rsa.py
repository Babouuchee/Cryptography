#!/usr/bin/python3

from sys import argv

import math

class RSA():
    def __init__(self):
        self._mode = ""
        self._primeP = ""
        self._primeQ = ""
        self._message = ""
        self._keyFirstPart = ""
        self._keySecondPart = ""

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
            if isHex(primeQ) is False or isHex(primeP) is False or len(primeP) % 2 != 0 or len(primeQ) % 2 != 0:
                print("Prime numbers must be in hexadecimal")
                exit(84)
            self._primeP = int.from_bytes(bytes.fromhex(primeP), 'little')
            self._primeQ = int.from_bytes(bytes.fromhex(primeQ), 'little')
        else:
            if len(argv) < 4:
                print("Key is missing")
            keyParts = argv[3].split('-')
            if len(keyParts) != 2:
                print("The key is invalid")
                exit(84)
            keyFirstPart, keySecondPart = keyParts
            if isHex(keyFirstPart) is False or len(keyFirstPart) % 2 != 0 or isHex(keySecondPart) is False or len(keySecondPart) % 2 != 0:
                print("Key must be in hexadecimal")
                exit(84)
            self._keyFirstPart = int.from_bytes(bytes.fromhex(keyFirstPart), 'little')
            self._keySecondPart = int.from_bytes(bytes.fromhex(keySecondPart), 'little')
            self._message = input("")

    def run(self):
        if self._mode == "-c":
            print(f"{self.cipher()}")
        elif self._mode == "-d":
            print(f"{self.decipher()}")
        elif self._mode == "-g":
            public_key, private_key = self.generate()
            print(f"public key: {public_key}")
            print(f"private key: {private_key}")
        else:
            print("Invalid mode")
            exit(84)

    def cipher(self):
        e = self._keyFirstPart
        n = self._keySecondPart
        messageInt = int.from_bytes(self._message.encode(), 'little')
        encryptedMessage = pow(messageInt, e, n)
        return littleEndianToHex(encryptedMessage)

    def decipher(self):
        d = self._keyFirstPart
        n = self._keySecondPart
        encryptedBytes = bytes.fromhex(self._message)
        encryptedInt = int.from_bytes(encryptedBytes, 'little')
        decryptedInt = pow(encryptedInt, d, n)
        return hexToText(decryptedInt)

    def generate(self):
        p = self._primeP
        q = self._primeQ
        n = p * q
        lambdaN = math.lcm(p - 1, q - 1)
        e = findBiggestFermatPrime(lambdaN)
        d = pow(e, -1, lambdaN)
        publicKey = f"{littleEndianToHex(e)}-{littleEndianToHex(n)}"
        privateKey = f"{littleEndianToHex(d)}-{littleEndianToHex(n)}"

        return [publicKey, privateKey]

def findBiggestFermatPrime(maxValue):
    result = 3
    iteration = 0
    while True:
        fermat = 2 ** (2 ** iteration) + 1
        if fermat > maxValue or fermat > 65537:
            return result
        if math.gcd(fermat, maxValue):
            result = fermat
        iteration += 1

def isHex(input):
    hexValues = "0123456789abcdef"
    for letter in input:
        if letter not in hexValues:
            return False
    return True

def isPrime(value):
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def littleEndianToHex(number):
    return number.to_bytes((number.bit_length() + 7) // 8, 'little').hex()

def hexToText(number):
    return number.to_bytes((number.bit_length() + 7) // 8, 'little').decode()
