#!/usr/bin/python3

from parser import Parser

from xor import XOR
from rsa import RSA

class PGP_XOR():
    def __init__(self, parser):
        self._parser : Parser = parser

    def isHex(self, input):
        hexValues = "0123456789abcdef"
        for letter in input:
            if letter not in hexValues:
                return False
        return True

    def run(self):
        if self._parser.getMode() == "-c":
            result = self.cipher(bytes.fromhex(self._parser.getPGPKey()), self._parser.getRSAKeys()[0], self._parser.getRSAKeys()[1], self._parser.getMessage())
            print(f"{result[0]}")
            print(f"{result[1]}")
        elif self._parser.getMode() == "-d":
            result = self.decipher(self._parser.getPGPKey(), self._parser.getRSAKeys()[0], self._parser.getRSAKeys()[1], self._parser.getMessage())
            print(f"{result}")
        else:
            print("Invalid mode")
            exit(84)

    def cipher(self, symKey, rsaKeyFirstPart, rsaKeySecondPart, message):
        xorHandler = XOR(self._parser)
        rsaHandler = RSA(self._parser)
        cipheredKey = rsaHandler.cipher(symKey.decode('ascii'), rsaKeyFirstPart, rsaKeySecondPart)
        cipheredMessage = xorHandler.cipher(symKey, message)
        return [cipheredKey, cipheredMessage]

    def decipher(self, symKey, rsaKeyFirstPart, rsaKeySecondPart, message):
        xorHandler = XOR(self._parser)
        rsaHandler = RSA(self._parser)
        decipheredKey = rsaHandler.decipher(symKey, rsaKeyFirstPart, rsaKeySecondPart)
        decipheredMessage = xorHandler.decipher(decipheredKey.encode('ascii'), message)
        return decipheredMessage
