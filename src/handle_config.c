/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** handle_config
*/

#include <stdio.h>

#include "structs.h"
#include "macros.h"

static int check_config(config_t *config)
{
    if (config->mode == NO_MODE || config->system == NO_SYSTEM
        || config->prime_P == -1 || config->prime_Q == -1
        || (config->key != NULL && config->mode == GENERATE_RSA)
        || (config->mode == GENERATE_RSA && config->system != RSA)) {
            return FAILURE;
    }
    return SUCCESS;
}

int handle_config(config_t *config)
{
    if (check_config(config) == FAILURE) {
        printf("Arguments aren't valid\n");
        return FAILURE;
    }
    return SUCCESS;
}
