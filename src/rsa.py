#!/usr/bin/python3

from parser import Parser

import math

class RSA():
    def __init__(self, parser):
        self._parser : Parser = parser

    def run(self):
        if self._parser.getMode() == "-c":
            print(f"{self.cipher(self._parser.getMessage(), self._parser.getRSAKeys()[0], self._parser.getRSAKeys()[1])}")
        elif self._parser.getMode() == "-d":
            print(f"{self.decipher(self._parser.getMessage(), self._parser.getRSAKeys()[0], self._parser.getRSAKeys()[1])}")
        elif self._parser.getMode() == "-g":
            public_key, private_key = self.generate(self._parser.getRSAPrime()[0], self._parser.getRSAPrime()[1])
            print(f"public key: {public_key}")
            print(f"private key: {private_key}")
        else:
            print("Invalid mode")
            exit(84)

    def cipher(self, message, keyFirstPart, keySecondPart):
        e = int.from_bytes(bytes.fromhex(keyFirstPart), 'little')
        n = int.from_bytes(bytes.fromhex(keySecondPart), 'little')
        messageInt = int.from_bytes(message.encode(), 'little')
        encryptedMessage = pow(messageInt, e, n)
        return littleEndianToHex(encryptedMessage)

    def decipher(self, message, keyFirstPart, keySecondPart):
        d = int.from_bytes(bytes.fromhex(keyFirstPart), 'little')
        n = int.from_bytes(bytes.fromhex(keySecondPart), 'little')
        encryptedBytes = bytes.fromhex(message)
        encryptedInt = int.from_bytes(encryptedBytes, 'little')
        decryptedInt = pow(encryptedInt, d, n)
        return hexToText(decryptedInt)

    def generate(self, primeP, primeQ):
        p = primeP
        q = primeQ
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

def isPrime(value):
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def littleEndianToHex(number):
    return number.to_bytes((number.bit_length() + 7) // 8, 'little').hex()

def hexToText(number):
    return number.to_bytes((number.bit_length() + 7) // 8, 'little').decode()
