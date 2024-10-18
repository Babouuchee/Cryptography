#!/usr/bin/python3

from sys import argv

from aes import AES
from rsa import RSA
from xor import XOR
from pgpAes import PGP_AES
from pgpXor import PGP_XOR

class My_PGP():
    def __init__(self):
        if len(argv) < 2:
            print("No system given")
            exit(84)

        self._system = argv[1]
        self._systems = {
            "aes": AES,
            "rsa": RSA,
            "xor": XOR,
            "pgp-xor": PGP_XOR,
            "pgp-aes": PGP_AES
        }

    def run(self):
        systemWanted = self._systems.get(self._system)

        if systemWanted:
            instance = systemWanted()
            instance.run()
        else:
            print(f"No system found for '{self._system}'")
            exit(84)