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

const uint8_t rcon[10] = {
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36
};

void print_state(const uint8_t* state)
{
    for (int i = 0; i < AES_BLOCKLEN; i++) {
        printf("%02x", state[i]);
    }
    printf("\n");
}

uint8_t* read_message(int* length)
{
    char* buffer;
    size_t bufsize = 0;

    printf("Entrez le message à chiffrer : ");
    *length = getline(&buffer, &bufsize, stdin);
    if (*length == -1)
        exit(ERROR);
    if (buffer[*length - 1] == '\n') {
        buffer[*length - 1] = '\0';
        (*length)--;
    }
    uint8_t* message = malloc(sizeof(uint8_t) * *length);
    memcpy(message, buffer, *length);
    free(buffer);
    return message;
}

uint8_t* add_padding(const uint8_t* message, int length, int* padded_length)
{
    int padding = AES_BLOCKLEN - (length % AES_BLOCKLEN);
    uint8_t* padded_message = malloc(sizeof(uint8_t) * *padded_length);

    *padded_length = length + padding;
    memcpy(padded_message, message, length);
    for (int i = length; i < *padded_length; i++) {
        padded_message[i] = padding;
    }

    return padded_message;
}

static uint8_t rotl8(uint8_t x, uint8_t shift)
{
    return ((x) << (shift)) | ((x) >> (8 - shift));
}

static void generate_sbox(uint8_t *sbox)
{
    uint8_t p = 1;
    uint8_t q = 1;
    uint8_t xformed = 0;

    do {
        p = p ^ (p << 1) ^ (p & 0x80 ? 0x1B : 0);

        q ^= q << 1;
        q ^= q << 2;
        q ^= q << 4;
        q ^= q & 0x80 ? 0x09 : 0;

        xformed = q ^ rotl8
        (q, 1) ^ rotl8(q, 2) ^ rotl8(q, 3) ^ rotl8(q, 4);
        sbox[p] = xformed ^ 0x63;
    } while (p != 1);
    sbox[0] = 0x63;
}

void sub_bytes(uint8_t *block, uint8_t *sbox) {
    for (int i = 0; i < AES_BLOCKLEN; i++) {
        block[i] = sbox[block[i]];
    }
}

void key_expansion(uint8_t* RoundKey, const uint8_t* Key, uint8_t *sbox) {
    int i, j;
    uint8_t *temp = malloc(sizeof(uint8_t) * 4);

    for (i = 0; i < AES_KEYLEN; i++)
        RoundKey[i] = Key[i];
    for (i = AES_KEYLEN; i < AES_KEYEXP_SIZE; i += 4) {
        for (j = 0; j < 4; j++)
            temp[j] = RoundKey[(i - 4) + j];

        if (i % AES_KEYLEN == 0) {
            uint8_t k = temp[0];
            temp[0] = temp[1];
            temp[1] = temp[2];
            temp[2] = temp[3];
            temp[3] = k;

            sub_bytes(temp, sbox);

            temp[0] ^= rcon[(i / AES_KEYLEN) - 1];
        }
        for (j = 0; j < 4; j++)
            RoundKey[i + j] = RoundKey[i - AES_KEYLEN + j] ^ temp[j];
    }
    free(temp);
}

void add_round_key(uint8_t* block, uint8_t* round_key) {
    for (int i = 0; i < AES_BLOCKLEN; i++) {
        block[i] ^= round_key[i];
    }
}

void shift_rows(uint8_t* state) {
    uint8_t temp;

    temp = state[1];
    state[1] = state[5];
    state[5] = state[9];
    state[9] = state[13];
    state[13] = temp;
    temp = state[2];
    state[2] = state[10];
    state[10] = temp;
    temp = state[3];
    state[3] = state[7];
    state[7] = state[11];
    state[11] = state[15];
    state[15] = temp;
}

uint8_t gmul(uint8_t a, uint8_t b) {
    uint8_t p = 0;
    uint8_t hi_bit_set;

    for (int i = 0; i < 8; i++) {
        if (b & 1) {
            p ^= a;
        }
        hi_bit_set = (a & 0x80);
        a <<= 1;
        if (hi_bit_set) {
            a ^= 0x1B;
        }
        b >>= 1;
    }
    return p;
}

void mix_columns(uint8_t* state) {
    for (int i = 0; i < 4; i++) {
        uint8_t a[4];
        for (int j = 0; j < 4; j++) {
            a[j] = state[j * 4 + i];
        }
        state[i * 4 + 0] = gmul(a[0], 2) ^ gmul(a[3], 1) ^ gmul(a[2], 1) ^ gmul(a[1], 3);
        state[i * 4 + 1] = gmul(a[1], 2) ^ gmul(a[0], 1) ^ gmul(a[3], 1) ^ gmul(a[2], 3);
        state[i * 4 + 2] = gmul(a[2], 2) ^ gmul(a[1], 1) ^ gmul(a[0], 1) ^ gmul(a[3], 3);
        state[i * 4 + 3] = gmul(a[3], 2) ^ gmul(a[2], 1) ^ gmul(a[1], 1) ^ gmul(a[0], 3);
    }
}

void aes_encrypt_block(uint8_t* block, uint8_t* round_key, uint8_t *sbox) {
    int i;

    add_round_key(block, round_key);
    for (i = 1; i < 10; i++) {
        printf("\n\n%d\n", i);
        print_state(block);
        sub_bytes(block, sbox);
        shift_rows(block);
        mix_columns(block);
        add_round_key(block, round_key + (i * AES_BLOCKLEN));
    }
    sub_bytes(block, sbox);
    shift_rows(block);
    add_round_key(block, round_key + (10 * AES_BLOCKLEN));
}

int generate_aes(char *client_key) {
    int message_length, padded_length;
    uint8_t key[AES_BLOCKLEN];
    uint8_t round_key[AES_KEYEXP_SIZE];
    uint8_t *sbox = malloc(sizeof(uint8_t) * 256);

    generate_sbox(sbox);
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

    key_expansion(round_key, key, sbox);

    for (int i = 0; i < padded_length; i += AES_BLOCKLEN) {
        aes_encrypt_block(&padded_message[i], round_key, sbox);
    }

    printf("Encrypted message: ");
    print_state(padded_message);

    free(message);
    free(padded_message);
    free(sbox);
    return SUCCESS;
}
