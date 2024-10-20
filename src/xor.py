#!/usr/bin/python3

from parser import Parser

class XOR():
    def __init__(self, parser):
        self._parser : Parser = parser

    def run(self):
        if self._parser.getMode() == "-c":
            print(f"{self.cipher(bytes.fromhex(self._parser.getBasicKey()), self._parser.getMessage())}")
        elif self._parser.getMode() == "-d":
            print(f"{self.decipher(bytes.fromhex(self._parser.getBasicKey()), self._parser.getMessage())}")
        else:
            print("Invalid mode")
            exit(84)

    def cipher(self, key, message):
        reversed_message = message[::-1]
        xor = bytes([a ^ key[i % len(key)] for i, a in enumerate(reversed_message.encode())])
        little_endian = "".join([f"{x:02x}" for x in xor])
        return little_endian

    def decipher(self, key, message):
        xor_bytes = bytes([a ^ key[i % len(key)] for i, a in enumerate(bytes.fromhex(message))])
        return xor_bytes.decode()[::-1]
