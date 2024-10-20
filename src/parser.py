#!/usr/bin/python3

from sys import argv

class Parser():
    def __init__(self, system):
        self._system = system
        self._mode = self.setMode()
        self._option = self.setOption()
        self._basic_key, self._rsa_key_first, self._rsa_key_second, self._pgp_key = self.setKeys(system)
        self._rsa_prime_q, self._rsa_prime_p = self.setPrimes(system)
        self._message = self.setMessage()

    def setMode(self):
        return argv[2]

    def setOption(self):
        if argv[3] == "-b":
            return True
        return False

    def setKeys(self, system):
        basicKey, rsaKeyFirstPart, rsaKeySecondPart, pgpKey = "", "", "", ""
        if system == "rsa" and self._mode != "-g":
            keyBuf = argv[3]
            keyParts = keyBuf.split('-')
            rsaKeyFirstPart = keyParts[0]
            rsaKeySecondPart = keyParts[1]
        if system == "pgp-aes" or system == "pgp-xor":
            if self._option == True:
                keyBuf = argv[4]
                keyParts = keyBuf.split(':')
                pgpKey = keyParts[0]
                rsaKeyFirstPart, rsaKeySecondPart = keyParts[1].split('-')
            else:
                keyBuf = argv[3]
                keyParts = keyBuf.split(':')
                pgpKey = keyParts[0]
                rsaKeyFirstPart, rsaKeySecondPart = keyParts[1].split('-')
        if system == "aes" or system == "xor":
            if self._option == True:
                basicKey = argv[4]
            else:
                basicKey = argv[3]
        return [basicKey, rsaKeyFirstPart, rsaKeySecondPart, pgpKey]

    def setPrimes(self, system):
        if system == "rsa":
            if self._mode == "-g":
                return [int.from_bytes(bytes.fromhex(argv[3])), int.from_bytes(bytes.fromhex(argv[4]))]
            else:
                return [-1, -1]
        else:
            return [-1, -1]

    def setMessage(self):
        if self._system == "rsa" and self._mode == "-g":
            return ""
        return input()

    def getSystem(self):
        return self._system

    def getMode(self):
        return self._mode

    def getOption(self):
        return self._option

    def getBasicKey(self):
        return self._basic_key

    def getRSAKeys(self):
        return [self._rsa_key_first, self._rsa_key_second]

    def getPGPKey(self):
        return self._pgp_key

    def getRSAPrime(self):
        return [self._rsa_prime_p, self._rsa_prime_q]

    def getMessage(self):
        return self._message