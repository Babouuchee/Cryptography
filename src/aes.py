#!/usr/bin/python3

from sys import argv

class AES():
    sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]
    inv_sbox = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
    ]
    rcon = [
        0x01, 0x02, 0x04, 0x08, 0x10,
        0x20, 0x40, 0x80, 0x1B, 0x36,
        0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E
    ]
    def __init__(self):
        self._mode = ""
        self._bOptionEnable = False
        self._key = None
        self._round_keys = None
        self._rounds = 10
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
            key_arg = argv[4]
            if self.isHex(key_arg) is False:
                print("Key must be in hexadecimal")
                exit(84)
            self._key = bytes.fromhex(key_arg)
            self._message = input()
        else:
            if len(argv) < 4:
                print("Key is missing")
                exit(84)
            key_arg = argv[3]
            if self.isHex(key_arg) is False:
                print("Key must be in hexadecimal")
                exit(84)
            self._key = bytes.fromhex(key_arg)
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

    def convertLittleEndian(self, data):
        little_endian_bytes = bytearray()
        for i in range(0, len(data), 4):
            chunk = data[i: i+4]
            little_endian_bytes.extend(chunk[::-1])
        return little_endian_bytes

    def validate_key(self):
        if len(self._key) != 16:
            print("Invalid key length. AES-128 requires a 16-byte key.")
            exit(84)
        self._key = self.convertLittleEndian(self._key)

    def validate_message(self):
        block_size = 16
        if isinstance(self._message, str) and self._mode == "-c":
            self._message = self._message.encode('utf-8')
        if isinstance(self._message, str) and self._mode == "-d":
            self._message = bytes.fromhex(self._message)
            self._message = self.convertLittleEndian(self._message)
        if len(self._message) < block_size:
            padding_length = block_size - (len(self._message) % block_size)
            padding = bytes([padding_length] * padding_length)
            self._message += padding

    def cipher(self):
        self.validate_key()
        self.validate_message()
        self.generate_round_key()

        state = self.add_round_key(self._message, self._key)

        for round in range(9):
            state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, self._round_keys[round + 1])

        state = self.sub_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, self._round_keys[10])
        result = self.convertLittleEndian(state)
        return result.hex()

    def decipher(self):
        self.validate_key()
        self.validate_message()
        self.generate_round_key()

        state = self.add_round_key(self._message, self._round_keys[10])

        for round in range(9, 0, -1):
            state = self.inv_shift_rows(state)
            state = self.inv_sub_bytes(state)
            state = self.add_round_key(state, self._round_keys[round])
            state = self.inv_mix_columns(state)
        state = self.inv_shift_rows(state)
        state = self.inv_sub_bytes(state)
        state = self.add_round_key(state, self._round_keys[0])
        return state.decode('ascii')

    def generate_round_key(self):
        key = self._key
        expanded_key = list(key)
        key_size = 16
        expanded_size = 176
        expanded_keys = [key]
        i = key_size
        while i < expanded_size:
            temp = expanded_key[i-4:i]
            if i % key_size == 0:
                temp = temp[1:] + temp[:1]
                temp = [self.sbox[b] for b in temp]
                temp[0] ^= self.rcon[(i // key_size) - 1]
            for j in range(4):
                expanded_key.append(expanded_key[i - key_size + j] ^ temp[j])
            if len(expanded_key) % 16 == 0:
                expanded_keys.append(bytes(expanded_key[-16:]))
            i += 4
        self._round_keys = expanded_keys

    def sub_bytes(self, state):
        result = bytearray(len(state))
        for i in range(len(state)):
            result[i] = self.sbox[state[i]]
        return bytes(result)

    def shift_rows(self, state):
        newState = bytearray(len(state))

        newState[0], newState[1], newState[2], newState[3] = state[0], state[5], state[10], state[15]
        newState[4], newState[5], newState[6], newState[7] = state[4], state[9], state[14], state[3]
        newState[8], newState[9], newState[10], newState[11] = state[8], state[13], state[2], state[7]
        newState[12], newState[13], newState[14], newState[15] = state[12], state[1], state[6], state[11]
        return bytes(newState)

    def mix_columns(self, state):
        mixed_state = bytearray(len(state))

        for col in range(4):
            s0, s1, s2, s3 = state[col * 4: col * 4 + 4]

            mixed_state[0 + col * 4] = self.gmul(s0, 2) ^ self.gmul(s1, 3) ^ s2 ^ s3
            mixed_state[1 + col * 4] = s0 ^ self.gmul(s1, 2) ^ self.gmul(s2, 3) ^ s3
            mixed_state[2 + col * 4] = s0 ^ s1 ^ self.gmul(s2, 2) ^ self.gmul(s3, 3)
            mixed_state[3 + col * 4] = self.gmul(s0, 3) ^ s1 ^ s2 ^ self.gmul(s3, 2)

        return bytes(mixed_state)

    def add_round_key(self, state, old_key):
        newBlock = bytearray()
        for i in range(len(state)):
            newBlock.append(state[i] ^ old_key[i])
        return bytes.fromhex(newBlock.hex())

    def gmul(self, a, b):
        result = 0
        for i in range(8):
            if b & 1:
                result ^= a
            temp = a & 0x80
            a <<= 1
            if temp:
                a ^= 0x1b
            b >>= 1
        return result & 0xff
    
    def inv_sub_bytes(self, state):
        result = bytearray(len(state))
        for i in range(len(state)):
            result[i] = self.inv_sbox[state[i]]
        return bytes(result)

    def inv_shift_rows(self, state):
        newState = bytearray(len(state))

        newState[0], newState[1], newState[2], newState[3] = state[0], state[13], state[10], state[7]
        newState[4], newState[5], newState[6], newState[7] = state[4], state[1], state[14], state[11]
        newState[8], newState[9], newState[10], newState[11] = state[8], state[5], state[2], state[15]
        newState[12], newState[13], newState[14], newState[15] = state[12], state[9], state[6], state[3]
        return bytes(newState)

    def inv_mix_columns(self, state):
        mixed_state = bytearray(len(state))

        for col in range(4):
            s0, s1, s2, s3 = state[col * 4: col * 4 + 4]

            mixed_state[0 + col * 4] = self.gmul(s0, 0x0e) ^ self.gmul(s1, 0x0b) ^ self.gmul(s2, 0x0d) ^ self.gmul(s3, 0x09)
            mixed_state[1 + col * 4] = self.gmul(s0, 0x09) ^ self.gmul(s1, 0x0e) ^ self.gmul(s2, 0x0b) ^ self.gmul(s3, 0x0d)
            mixed_state[2 + col * 4] = self.gmul(s0, 0x0d) ^ self.gmul(s1, 0x09) ^ self.gmul(s2, 0x0e) ^ self.gmul(s3, 0x0b)
            mixed_state[3 + col * 4] = self.gmul(s0, 0x0b) ^ self.gmul(s1, 0x0d) ^ self.gmul(s2, 0x09) ^ self.gmul(s3, 0x0e)

        return bytes(mixed_state)