/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** structs
*/

#ifndef STRUCTS_H_
    #define STRUCTS_H_

    #include "stdbool.h"

typedef enum crypto_system_e {
    XOR,
    AES,
    RSA,
    PGP_XOR,
    PGP_AES,
    NO_SYSTEM
} crypto_system_t;

typedef enum crypto_mode_e {
    CIPHER,
    DECIPHER,
    GENERATE_RSA,
    NO_MODE
} crypto_mode_t;

typedef struct config_s {
    crypto_system_t system;
    crypto_mode_t mode;
    bool b_option_used;
    char *key;
    int prime_P;
    int prime_Q;
} config_t;

#endif /* !STRUCTS_H_ */
