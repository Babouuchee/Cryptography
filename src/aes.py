#!/usr/bin/python3

from sys import argv

class AES():
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
        print(f"AES  mode: '{self._mode}'  bOption: '{self._bOptionEnable}'  key: '{self._key}'  message: '{self._message}'")
        if self._mode == "-c":
            self.cipher()
        elif self._mode == "-d":
            self.decipher()
        else:
            print("Invalid mode")
            exit(84)

    def cipher(self):
        print("Cipher")
        sbox = self.generate_sbox()
        print("Generated S-Box (Hexadecimal):")

        for i in range(0, 256, 16):
            print(" ".join(f"{x:02x}\n" for x in sbox[i:i+16]))

        message = self.get_message()


    def decipher(self):
        print("Decipher")

    def get_message(self):
        message = input("Enter the message to encrypt: ")
        print(f"Message: {message}")
        return message.encode()

def generate_sbox(self):
    sbox = [0] * 256
    inverse = [0] * 256

    # Générer l'inverse multiplicatif sur le corps de Galois
    for i in range(256):
        if i == 0:
            inverse[i] = 0
        else:
            inverse[i] = self.galois_inverse(i)

    # Appliquer la transformation affine pour créer la S-Box
    for i in range(256):
        x = inverse[i]
        sbox[i] = (x ^ (x << 1) ^ (x << 2) ^ (x << 3) ^ (x << 4)) & 0xFF
        sbox[i] ^= 0x63

    return sbox

def galois_inverse(self, a):
    # Trouver l'inverse multiplicatif de a dans GF(2^8)
    b = 1
    for i in range(1, 8):
        b = (b * a) % 0x11b
    return b
