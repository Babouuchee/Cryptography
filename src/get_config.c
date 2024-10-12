/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** get_config
*/

#include <stdlib.h>
#include <string.h>

#include "structs.h"
#include "macros.h"

static int check_num(char const *str)
{
    if (!str)
        return FAILURE;
    for (int index = 0; str[index] != '\0'; index++) {
        if (str[index] < '0' || str[index] > '9')
            return FAILURE;
    }
    return SUCCESS;
}

static crypto_system_t get_crypto_system(int ac, char const *const *av)
{
    if (ac < 2)
        return NO_SYSTEM;
    if (strcmp(av[1], "xor") == 0)
        return XOR;
    if (strcmp(av[1], "aes") == 0)
        return AES;
    if (strcmp(av[1], "rsa") == 0)
        return RSA;
    if (strcmp(av[1], "pgp-xor") == 0)
        return PGP_XOR;
    if (strcmp(av[1], "pgp-aes") == 0)
        return PGP_AES;
    return NO_SYSTEM;
}

static crypto_mode_t get_crypto_mode
(int ac, char const *const *av, config_t *config)
{
    config->prime_P = -1;
    config->prime_Q = -1;
    if (ac < 3)
        return NO_MODE;
    if (strcmp(av[2], "-c") == 0)
        return CIPHER;
    if (strcmp(av[2], "-d") == 0)
        return DECIPHER;
    if (strcmp(av[2], "-g") == 0) {
        if (ac > 3 && av[3] != NULL && check_num(av[3]) != FAILURE)
            config->prime_P = atoi(av[3]);
        if (ac > 4 && av[4] != NULL && check_num(av[4]) != FAILURE)
            config->prime_Q = atoi(av[4]);
        return GENERATE_RSA;
    }
    return NO_MODE;
}

static bool get_b_option(int ac, char const *const *av, config_t *config)
{
    if (config->mode != GENERATE_RSA && ac > 3 && strcmp(av[3], "-b") == 0)
        return true;
    if (config->mode == GENERATE_RSA && ac > 6 && strcmp(av[6], "-b") == 0)
        return true;
    return false;
}

static char *get_key(int ac, char const *const *av, config_t *config)
{
    if (config->b_option_used == true) {
        if (config->mode == GENERATE_RSA && ac > 4)
            return strdup(av[4]);
        if (config->mode != GENERATE_RSA && ac > 7)
            return strdup(av[7]);
    } else {
        if (config->mode == GENERATE_RSA && ac > 3)
            return strdup(av[3]);
        if (config->mode != GENERATE_RSA && ac > 6)
            return strdup(av[6]);
    }
    return NULL;
}

config_t *get_config(int ac, char const *const *av)
{
    config_t *result = malloc(sizeof(config_t));

    if (!result)
        return NULL;
    if (ac < 3 || ac > 7) {
        free(result);
        return NULL;
    }
    result->system = get_crypto_system(ac, av);
    result->mode = get_crypto_mode(ac, av, result);
    result->b_option_used = get_b_option(ac, av, result);
    result->key = get_key(ac, av, result);
    return result;
}
