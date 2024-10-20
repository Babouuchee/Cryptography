#!/usr/bin/python3

from sys import argv

class XOR():
    def __init__(self):
        self._mode = ""
        self._bOptionEnable = False
        self._key = ""
        self._message = ""

        if len(argv) < 3:
            print("Missing arguments")
            exit(84)
        if len(argv) > 5:
            print("Too many arguments")
            exit(84)
        self._mode = argv[2]
        if "-c" not in self._mode and "-d" not in self._mode:
            print("Invalid mode")
            exit(84)
        if len(argv) > 3 and argv[3] == "-b":
            self._bOptionEnable = True
        if self._bOptionEnable is True:
            if len(argv) < 5:
                print("Key is missing")
                exit(84)
            key = argv[4]
        else:
            if len(argv) < 4:
                print("Key is missing")
                exit(84)
            key = argv[3]
        if self.isHex(key) is False or len(key) % 2 != 0:
            print("Key must be in hexadecimal")
            exit(84)
        self._key = bytes.fromhex(key)
        self._message = input()

    def isHex(self, input):
        hexValues = "0123456789abcdef"
        for letter in input:
            if letter not in hexValues:
                return False
        return True

    def run(self):
        if self._mode == "-c":
            print(f"{self.cipher()}")
        elif self._mode == "-d":
            print(f"{self.decipher()}")
        else:
            print("Invalid mode")
            exit(84)

    def cipher(self):
        reversed_message = self._message[::-1]
        xor = bytes([a ^ self._key[i % len(self._key)] for i, a in enumerate(reversed_message.encode())])
        little_endian = "".join([f"{x:02x}" for x in xor])
        return little_endian

    def decipher(self):
        xor_bytes = bytes([a ^ self._key[i % len(self._key)] for i, a in enumerate(bytes.fromhex(self._message))])
        return xor_bytes.decode()[::-1]
