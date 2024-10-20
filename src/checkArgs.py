#!/usr/bin/python3

from sys import argv

class checkArgv():
    def __init__(self, system):
        self._system = system

    def check(self):
        if self._system == "aes":
            return self.checkAES()
        if self._system == "rsa":
            return self.checkRSA()
        if self._system == "xor":
            return self.checkXOR()
        if self._system == "pgp-xor":
            return self.checkPGP_XOR()
        if self._system == "pgp-aes":
            return self.checkPGP_AES()
        print("System unknown")
        return False

    def checkAES(self):
        if len(argv) < 3:
            print("Missing arguments")
            return False
        if len(argv) > 5:
            print("Too many arguments")
            return False
        mode = argv[2]
        if "-c" not in mode and "-d" not in mode:
            print("Invalid mode")
            return False
        if len(argv) > 3 and argv[3] == "-b":
            bOptionEnable = True
        if bOptionEnable is True:
            if len(argv) < 5:
                print("Key is missing")
                return False
            key_arg = argv[4]
            if isHex(key_arg) is False:
                print("Key must be in hexadecimal")
                return False
        else:
            if len(argv) < 4:
                print("Key is missing")
                return False
            key_arg = argv[3]
            if isHex(key_arg) is False:
                print("Key must be in hexadecimal")
                return False
        return True

    def checkRSA(self):
        if len(argv) < 3:
            print("Missing arguments")
            return False
        if len(argv) > 6:
            print("Too many arguments")
            return False
        mode = argv[2]
        if "-c" not in mode and "-d" not in mode and "-g" not in mode:
            print("Invalid mode")
            return False
        if mode == "-g":
            if len(argv) < 5:
                print("Prime numbers are missing")
                return False
            if len(argv) > 5:
                print("Key is not supposed to be with -g")
                return False
            primeP = argv[3]
            primeQ = argv[4]
            if isHex(primeQ) is False or isHex(primeP) is False or len(primeP) % 2 != 0 or len(primeQ) % 2 != 0:
                print("Prime numbers must be in hexadecimal")
                return False
        else:
            if len(argv) < 4:
                print("Key is missing")
                return False
            keyParts = argv[3].split('-')
            if len(keyParts) != 2:
                print("The key is invalid")
                return False
            keyFirstPart, keySecondPart = keyParts
            if isHex(keyFirstPart) is False or len(keyFirstPart) % 2 != 0 or isHex(keySecondPart) is False or len(keySecondPart) % 2 != 0:
                print("Key must be in hexadecimal")
                return False
        return True
    
    def checkXOR(self):
        if len(argv) < 3:
            print("Missing arguments")
            return False
        if len(argv) > 5:
            print("Too many arguments")
            return False
        mode = argv[2]
        if "-c" not in mode and "-d" not in mode:
            print("Invalid mode")
            return False
        if len(argv) > 3 and argv[3] == "-b":
            bOptionEnable = True
        if bOptionEnable is True:
            if len(argv) < 5:
                print("Key is missing")
                return False
            key = argv[4]
        else:
            if len(argv) < 4:
                print("Key is missing")
                return False
            key = argv[3]
        if isHex(key) is False or len(key) % 2 != 0:
            print("Key must be in hexadecimal")
            return False
        return True

    def checkPGP_AES(self):
        if len(argv) < 3:
            print("Missing arguments")
            return False
        if len(argv) > 5:
            print("Too many arguments")
            return False
        mode = argv[2]
        if "-c" not in mode and "-d" not in mode:
            print("Invalid mode")
            return False
        if len(argv) > 3 and argv[3] == "-b":
            bOptionEnable = True
        if bOptionEnable is True:
            if len(argv) < 5:
                print("Key is missing")
                return False
            keyParts = argv[4].split(':')
            if len(keyParts) != 2 or len(keyParts[0]) % 2 != 0 or isHex(keyParts[0]) is False:
                print("Keys are not valid 3")
                return False
            rsaKeyParts = keyParts[1].split('-')
            if len(rsaKeyParts) != 2 or len(rsaKeyParts[0]) % 2 != 0 or isHex(rsaKeyParts[0]) is False or len(rsaKeyParts[1]) % 2 != 0 or isHex(rsaKeyParts[1]) is False:
                print("RSA key is not valid 2")
                return False
        else:
            if len(argv) < 4:
                print("Key is missing")
                return False
            keyParts = argv[3].split(':')
            if len(keyParts) != 2 or len(keyParts[0]) % 2 != 0 or isHex(keyParts[0]) is False:
                print("Keys are not valid 1")
                return False
            rsaKeyParts = keyParts[1].split('-')
            if len(rsaKeyParts) != 2 or len(rsaKeyParts[0]) % 2 != 0 or isHex(rsaKeyParts[0]) is False or len(rsaKeyParts[1]) % 2 != 0 or isHex(rsaKeyParts[1]) is False:
                print("RSA key is not valid 2")
                return False
        return True

    def checkPGP_XOR(self):
        if len(argv) < 3:
            print("Missing arguments")
            return False
        if len(argv) > 5:
            print("Too many arguments")
            return False
        mode = argv[2]
        if "-c" not in mode and "-d" not in mode:
            print("Invalid mode")
            return False
        if len(argv) > 3 and argv[3] == "-b":
            bOptionEnable = True
        if bOptionEnable is True:
            if len(argv) < 5:
                print("Key is missing")
                return False
            keyParts = argv[4].split(':')
            if len(keyParts) != 2 or len(keyParts[0]) % 2 != 0 or isHex(keyParts[0]) is False:
                print("Keys are not valid 3")
                return False
            rsaKeyParts = keyParts[1].split('-')
            if len(rsaKeyParts) != 2 or len(rsaKeyParts[0]) % 2 != 0 or isHex(rsaKeyParts[0]) is False or len(rsaKeyParts[1]) % 2 != 0 or isHex(rsaKeyParts[1]) is False:
                print("RSA key is not valid 2")
                return False
        else:
            if len(argv) < 4:
                print("Key is missing")
                return False
            keyParts = argv[3].split(':')
            if len(keyParts) != 2 or len(keyParts[0]) % 2 != 0 or isHex(keyParts[0]) is False:
                print("Keys are not valid 1")
                return False
            rsaKeyParts = keyParts[1].split('-')
            if len(rsaKeyParts) != 2 or len(rsaKeyParts[0]) % 2 != 0 or isHex(rsaKeyParts[0]) is False or len(rsaKeyParts[1]) % 2 != 0 or isHex(rsaKeyParts[1]) is False:
                print("RSA key is not valid 2")
                return False
        return True

def isHex(input):
    hexValues = "0123456789abcdef"
    for letter in input:
        if letter not in hexValues:
            return False
    return True