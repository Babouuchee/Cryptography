#!/usr/bin/python3

from sys import argv

class AES():
    sbox = [
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01,   0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
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
        #print(f"AES  mode: '{self._mode}'  bOption: '{self._bOptionEnable}'  key: '{self._key.hex}'  message: '{self._message}'")
        if self._mode == "-c":
            self.cipher()
        elif self._mode == "-d":
            self.decipher()
        else:
            print("Invalid mode")
            exit(84)

    def validate_key(self):
        if len(self._key) != 16:
            raise ValueError("Invalid key length. AES-128 requires a 16-byte key.")

    def validate_message(self):
        block_size = 16
        if isinstance(self._message, str):
            self._message = self._message.encode('utf-8')

        padding_length = block_size - (len(self._message) % block_size)
        padding = bytes([padding_length] * padding_length)
        self._message += padding

    def bytes_to_words(self, data):
        words = []
        for i in range(0, len(data), 4):
            word = int.from_bytes(data[i:i + 4])
            words.append(word)
        return words

    def words_to_bytes(self, words):
        byte_array = []
        for word in words:
            byte_array.append(word.to_bytes(4))
        return b''.join(byte_array)

    def key_expansion(self, word, round_number):
        if isinstance(word, int):
            word = [(word >> (i * 8)) & 0xFF for i in reversed(range(4))]
            #print(f"Converted word to bytes: {[hex(byte) for byte in word]}")

        rotated_word = word[1:] + word[:1]
        #print(f"Rotated word: {[hex(byte) for byte in rotated_word]}")

        substituted_word = []
        for b in rotated_word:
            substituted_value = self.sbox[b]
            substituted_word.append(substituted_value)
            #print(f"Substituted {b:#04x} -> {substituted_value:#04x}")

        #print(f"Before XOR with Rcon: {substituted_word}")
        substituted_word[0] ^= self.rcon[round_number]
        #print(f"After XOR with Rcon[{round_number}]: {substituted_word}")

        result = 0
        for i in range(4):
            result |= substituted_word[i] << ((3 - i) * 8)
            #print(f"Step {i+1}: result = {hex(result)} (after adding byte {hex(substituted_word[i])})")
        return result


    def generate_round_key(self):
        self._key = self.bytes_to_words(self._key)
        key_size = len(self._key) // 4
        round_keys = []
        round_keys.append(self._key)

        for i in range(0, self._rounds):
            temp = self.key_expansion(round_keys[-1][-1], i)
            #print("Temp after key expansion is : ", temp.to_bytes(4).hex())

            new_key_block = []
            new_key_block.append(round_keys[-1][0] ^ temp)
            xor_result = round_keys[-1][0] ^ temp
            #print("First octet : ", xor_result.to_bytes(4).hex())
            for k in range(1, 4):
                result = new_key_block[k - 1] ^ round_keys[-1][k]
                new_key_block.append(new_key_block[k - 1] ^ round_keys[-1][k])
                #print(f"Octet {k}: {result.to_bytes(4).hex()}")
            #print(f"Round {i}: {self.words_to_bytes(new_key_block).hex()}")
            #print("\n")
            round_keys.append(new_key_block)

        self._round_keys = round_keys

    def sub_bytes(self, state):
        substituted_state = []
        for word in state:
            for i in range(4):
                byte = (word >> (i * 8)) & 0xFF
                substituted_byte = self.sbox[byte]
                substituted_state.append(substituted_byte)
        grouped_state = []
        for i in range(0, len(substituted_state), 4):
            word = (substituted_state[i] << 24) | (substituted_state[i + 1] << 16) | (substituted_state[i + 2] << 8) | substituted_state[i + 3]
            grouped_state.append(word)
        return grouped_state

    def inv_sub_bytes(self, state):
        return [
            sum((self.inv_sbox[(word >> (i * 8)) & 0xFF] << (i * 8)) for i in range(4))
            for word in state
        ]

    def shift_rows(self, state):
        state_bytes = [word.to_bytes(4, byteorder='little') for word in state]

        shifted_state = []
        shifted_state.append(state_bytes[0][0:1] + state_bytes[1][1:2] + state_bytes[2][2:3] + state_bytes[3][3:4])
        shifted_state.append(state_bytes[1][0:1] + state_bytes[2][1:2] + state_bytes[3][2:3] + state_bytes[0][3:4])
        shifted_state.append(state_bytes[2][0:1] + state_bytes[3][1:2] + state_bytes[0][2:3] + state_bytes[1][3:4])
        shifted_state.append(state_bytes[3][0:1] + state_bytes[0][1:2] + state_bytes[1][2:3] + state_bytes[2][3:4])

        result = []
        for i in range(len(shifted_state)):
            result.append(int.from_bytes(shifted_state[i]))
        return result

    def inv_shift_rows(self, state):
        return [
            state[0],
            (state[1] >> 8) | (state[1] << 24),
            (state[2] >> 16) | (state[2] << 16),
            (state[3] >> 24) | (state[3] << 8),
        ]

    def mix_columns(self, state):
        mixed = []
        for col in range(4):
            bytes_col = state[col].to_bytes(4)
            s0, s1, s2, s3 = bytes_col
            #print(f"Column {col}: s0 = {hex(s0)}, s1 = {hex(s1)}, s2 = {hex(s2)}, s3 = {hex(s3)}")

            first_col = self.gmul(s0, 2) ^ self.gmul(s1, 3) ^ s2 ^ s3
            second_col = s0 ^ self.gmul(s1, 2) ^ self.gmul(s2, 3) ^ s3
            third_col = s0 ^ s1 ^ self.gmul(s2, 2) ^ self.gmul(s3, 3)
            fourth_col = self.gmul(s0, 3) ^ s1 ^ s2 ^ self.gmul(s3, 2)
            #print(f"Row 1 : {first_col.to_bytes(1).hex()}")
            #print(f"Row 1 : {second_col.to_bytes(1).hex()}")
            #print(f"Row 3 : {third_col.to_bytes(1).hex()}")
            #print(f"Row 4 : {fourth_col.to_bytes(1).hex()}")

            mixed.append(first_col)
            mixed.append(second_col)
            mixed.append(third_col)
            mixed.append(fourth_col)


            result = []
            for i in range(0, len(mixed), 4):
                word = (mixed[i] << 24) | (mixed[i + 1] << 16) | (mixed[i + 2] << 8) | mixed[i + 3]
                result.append(word)
        return result

    def inv_mix_columns(self, state):
        for i in range(4):
            s0 = (state[i] >> 24) & 0xFF
            s1 = (state[i] >> 16) & 0xFF
            s2 = (state[i] >> 8) & 0xFF
            s3 = state[i] & 0xFF
            new_s0 = self.gmul(s0, 0x0e) ^ self.gmul(s1, 0x0b) ^ self.gmul(s2, 0x0d) ^ self.gmul(s3, 0x09)
            new_s1 = self.gmul(s0, 0x09) ^ self.gmul(s1, 0x0e) ^ self.gmul(s2, 0x0b) ^ self.gmul(s3, 0x0d)
            new_s2 = self.gmul(s0, 0x0d) ^ self.gmul(s1, 0x09) ^ self.gmul(s2, 0x0e) ^ self.gmul(s3, 0x0b)
            new_s3 = self.gmul(s0, 0x0b) ^ self.gmul(s1, 0x0d) ^ self.gmul(s2, 0x09) ^ self.gmul(s3, 0x0e)
            state[i] = (new_s0 << 24) | (new_s1 << 16) | (new_s2 << 8) | new_s3

        return state

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
        return result & 0xFF

    def cipher(self):
        print("Cipher")
        print("Key : ", self._key.hex())
        print("Message : ", self._message)

        self.validate_key()
        self.validate_message()
        self.generate_round_key()
        print("Round Keys:")
        for i, round_key in enumerate(self._round_keys):
            round_key_bytes = b''.join(word.to_bytes(4) for word in round_key)
            print(f"Round {i}: {round_key_bytes.hex()}")

        print("Message : ", self._message)

        state = self.bytes_to_words(self._message)

        print("Initial State:", [hex(word) for word in state])

        state = [state[i] ^ self._round_keys[0][i] for i in range(4)]
        print("After AddRoundKey (Round 0):", [hex(word) for word in state])

        for round in range(0, self._rounds):
            state = self.sub_bytes(state)
            print(f"After SubBytes (Round {round}):", [hex(byte) for byte in state])

            state = self.shift_rows(state)
            print(f"After ShiftRows (Round {round}):", [hex(byte) for byte in state])

            if round < (self._rounds - 1):
                state = self.mix_columns(state)
                print(f"After MixColumns (Round {round}):", [hex(byte) for byte in state])

            state = [state[i] ^ self._round_keys[round + 1][i] for i in range(4)]
            print(f"After AddRoundKey (Round {round} with round_key {round + 1}):", [hex(byte) for byte in state])

        #self._message = self.words_to_bytes(state)
        #print("Final Ciphertext:", self._message.hex())

    def decipher(self):
        print("Decipher")
        print("Key : ", self._key.hex())
        print("Message : ", self._message)

        self.validate_key()
        self.validate_message()
        if self._round_keys is None:
            self.generate_round_key()

        state = self.bytes_to_words(self._message)

        print("Initial State:", [hex(word) for word in state])

        for round in range(self._rounds - 1, -1, -1):
            state = [state[i] ^ self._round_keys[round + 1][i] for i in range(4)]
            print(f"After InvAddRoundKey (Round {round + 1}):", [hex(byte) for byte in state])

            if round > 0:
                state = self.inv_mix_columns(state)
                print(f"After InvMixColumns (Round {round + 1}):", [hex(byte) for byte in state])

            state = self.inv_shift_rows(state)
            print(f"After InvShiftRows (Round {round + 1}):", [hex(byte) for byte in state])

            state = self.inv_sub_bytes(state)
            print(f"After InvSubBytes (Round {round + 1}):", [hex(byte) for byte in state])

        state = [state[i] ^ self._round_keys[0][i] for i in range(4)]
        print("After InvAddRoundKey (Round 0):", [hex(word) for word in state])

        self._message = self.words_to_bytes(state)
        print("Final Deciphered Message:", self._message.hex())
