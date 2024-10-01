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
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

#include "macros.h"

uint8_t sbox[256] = {
    // Table S-box d'AES
    // (à compléter avec les valeurs correctes)
};

void key_expansion(uint8_t* RoundKey, const uint8_t* Key)
{
    int i, j;
    uint8_t temp[4];

    // Les 16 premiers octets du RoundKey sont la clé initiale
    for (i = 0; i < AES_KEYLEN; i++) {
        RoundKey[i] = Key[i];
    }

    // Générer les sous-clés restantes
    for (i = AES_KEYLEN; i < AES_KEYEXP_SIZE; i += 4) {
        // Stocker les 4 derniers octets de RoundKey dans temp
        for (j = 0; j < 4; j++) {
            temp[j] = RoundKey[(i - 4) + j];
        }

        // Appliquer la transformation à temp tous les 16 octets (1 tour complet)
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

            // XOR avec une constante rcon
            temp[0] ^= (1 << ((i / AES_KEYLEN) - 1));  // Simplifié pour l'exemple
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

// Fonction de chiffrement (à implémenter)
void encrypt_block(const uint8_t* block, uint8_t* encrypted_block)
{
    (void) block;
    (void) encrypted_block;
    // Fonction à compléter avec ton algorithme AES
    // Exemple : AES_Encrypt(block, encrypted_block);
    // Ici tu dois appliquer les transformations AES à chaque bloc
    // encrypted_block = AES_Encrypt(block);
}

void print_uint8(const uint8_t* message, int message_length)
{
    for (int i = 0; i < message_length; i++) {
        printf("%02x ", message[i]);
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

    printf("Padded message: %s\n", padded_message);

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

    uint8_t* message = malloc(sizeof(uint8_t) * *length);
    memcpy(message, buffer, *length);

    free(buffer);
    return message;
}

int generate_aes(char *client_key)
{
    int message_length, padded_length;

    uint8_t key[AES_BLOCKLEN];
    for (int i = 0; i < AES_BLOCKLEN; i++) {
        sscanf(&client_key[2*i], "%2hhx", &key[i]);
    }

    uint8_t* message = read_message(&message_length);
    printf("Message: ");
    print_uint8(message, message_length);

    uint8_t* padded_message = add_padding(message, message_length, &padded_length);
    printf("Padded message: ");
    print_uint8(padded_message, padded_length);


    // Chiffrement bloc par bloc
    //for (int i = 0; i < padded_length; i += AES_BLOCKLEN) {
    //    uint8_t encrypted_block[AES_BLOCKLEN];
    //    EncryptBlock(&padded_message[i], encrypted_block);
//
    //    // Afficher le bloc chiffré (facultatif)
    //    printf("Bloc chiffré %d : ", i / AES_BLOCKLEN);
    //    for (int j = 0; j < AES_BLOCKLEN; j++) {
    //        printf("%02x ", encrypted_block[j]);
    //    }
    //    printf("\n");
    //}

    free(message);
    free(padded_message);
    return SUCCESS;
}
