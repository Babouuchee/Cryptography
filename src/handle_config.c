/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** handle_config
*/

#include <stdio.h>

#include "structs.h"
#include "macros.h"

static int error_message(char const *message)
{
    printf("%s\n", message);
    return FAILURE;
}

static int check_config(config_t *config)
{
    if (config->mode == NO_MODE)
        return error_message("No mode given.");
    if (config->system == NO_SYSTEM)
        return error_message("No system given.");
    if (config->mode == GENERATE_RSA
        && (config->prime_P == -1 || config->prime_Q == -1))
            return error_message("Prime numbers are invalid.");
    if (config->key != NULL && config->mode == GENERATE_RSA)
        return error_message("Key incompatible with -g MODE.");
    if (config->mode == GENERATE_RSA && config->system != RSA)
        return error_message("-g MODE can only be used with RSA.");
    if (config->b_option_used == true && config->system == RSA)
        return error_message("-b options cannot be used in RSA system.");
    return SUCCESS;
}

int handle_config(config_t *config)
{
    if (!config || check_config(config) == FAILURE)
        return FAILURE;
    return SUCCESS;
}
