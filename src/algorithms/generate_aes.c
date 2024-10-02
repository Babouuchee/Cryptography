/*
** EPITECH PROJECT, 2024
** my_PGP
** File description:
** generate_aes_algorithm
*/

/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** main
*/

#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

#include "macros.h"

uint8_t sbox[256];

void generate_sbox() {
    uint8_t p = 1, q = 1;

    while (p != 1) {
        p = p ^ (p << 1) ^ (p & 0x80 ? 0x1B : 0);

        q ^= (q << 1);
        q ^= (q << 2);
        q ^= (q << 4);
        q ^= 0x63;

        sbox[p] = q;
    }

    sbox[0] = 0x63;
}

const uint8_t rcon[10] = {
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36
};

void key_expansion(uint8_t* RoundKey, const uint8_t* Key) {
    int i, j;
    uint8_t temp[4];

    generate_sbox();
    for (i = 0; i < AES_KEYLEN; i++) {
        RoundKey[i] = Key[i];
    }

    for (i = AES_KEYLEN; i < AES_KEYEXP_SIZE; i += 4) {
        for (j = 0; j < 4; j++) {
            temp[j] = RoundKey[(i - 4) + j];
        }

        if (i % AES_KEYLEN == 0) {
            // Rotation (RotWord)
            uint8_t k = temp[0];
            temp[0] = temp[1];
            temp[1] = temp[2];
            temp[2] = temp[3];
            temp[3] = k;

            // SubBytes (SubWord)
            temp[0] = sbox[temp[0]];
            temp[1] = sbox[temp[1]];
            temp[2] = sbox[temp[2]];
            temp[3] = sbox[temp[3]];

            // XOR avec une constante rcon (seulement sur le premier octet)
            temp[0] ^= rcon[(i / AES_KEYLEN) - 1];
        }

        // XOR avec les 4 octets 16 positions avant dans RoundKey
        for (j = 0; j < 4; j++) {
            RoundKey[i + j] = RoundKey[i - AES_KEYLEN + j] ^ temp[j];
        }
    }
}

void print_state(const uint8_t* state)
{
    for (int i = 0; i < AES_BLOCKLEN; i++) {
        printf("%02x ", state[i]);
    }
    printf("\n");
}

uint8_t* add_padding(const uint8_t* message, int length, int* padded_length)
{
    int padding = AES_BLOCKLEN - (length % AES_BLOCKLEN);
    *padded_length = length + padding;

    uint8_t* padded_message = malloc(sizeof(uint8_t) * *padded_length);
    memcpy(padded_message, message, length);
    for (int i = length; i < *padded_length; i++) {
        padded_message[i] = padding;
    }

    printf("Original message with padding: %s\n", padded_message);

    return padded_message;
}

uint8_t* read_message(int* length)
{
    char* buffer;
    size_t bufsize = 0;
    printf("Entrez le message à chiffrer : ");
    *length = getline(&buffer, &bufsize, stdin);

    if (*length == -1) {
        exit(ERROR);
    }

    if (buffer[*length - 1] == '\n') {
        buffer[*length - 1] = '\0';
        (*length)--;
    }
    printf("Original message : %s\n", buffer);
    uint8_t* message = malloc(sizeof(uint8_t) * *length);
    memcpy(message, buffer, *length);

    free(buffer);
    return message;
}

int generate_aes(char *client_key)
{
    int message_length, padded_length;
    uint8_t key[AES_BLOCKLEN];
    uint8_t round_key[AES_KEYEXP_SIZE];

    for (int i = 0; i < AES_BLOCKLEN; i++) {
        sscanf(&client_key[2*i], "%2hhx", &key[i]);
    }
    printf("Key : ");
    print_state(key);

    uint8_t* message = read_message(&message_length);
    printf("Message: ");
    print_state(message);

    uint8_t* padded_message = add_padding(message, message_length, &padded_length);
    printf("Padded message: ");
    print_state(padded_message);

    key_expansion(round_key, key);
    printf("Clé étendue :\n");
    for (int i = 0; i < AES_KEYEXP_SIZE; i++) {
        printf("%02x ", round_key[i]);
        if ((i + 1) % 16 == 0) {
            printf("\n");
        }
    }

    free(message);
    free(padded_message);
    return SUCCESS;
}
