#!/usr/bin/python3

from sys import argv

class XOR():
    def __init__(self):
        self._mode = ""
        self._bOptionEnable = False
        self._key = ""
        self._message = input("Enter message: ")

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
            self._key = argv[4]
        else:
            if len(argv) < 4:
                print("Key is missing")
                exit(84)
            self._key = argv[3]

    def run(self):
        # print(f"XOR  mode: '{self._mode}'  bOption: '{self._bOptionEnable}'  key: '{self._key}'  message: '{self._message}'")
        if self._mode == "-c":
            self.cipher()
        elif self._mode == "-d":
            self.decipher()
        else:
            print("Invalid mode")
            exit(84)

    def cipher(self):
        key_bytes = bytes.fromhex(self._key)
        reversed_message = self._message[::-1]
        xor = bytes([a ^ key_bytes[i % len(key_bytes)] for i, a in enumerate(reversed_message.encode())])
        little_endian = "".join([f"{x:02x}" for x in xor])
        print(little_endian)

    def decipher(self):
        key_bytes = bytes.fromhex(self._key)
        xor_bytes = bytes([a ^ key_bytes[i % len(key_bytes)] for i, a in enumerate(bytes.fromhex(self._message))])
        print(xor_bytes.decode()[::-1])
