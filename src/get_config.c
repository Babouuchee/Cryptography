/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** get_config
*/

#include <stdlib.h>

#include "structs.h"

config_t *get_config(char const *const *argv)
{
    config_t *result = malloc(sizeof(config_t));

    (void)argv;
    result->key = NULL;
    return result;
}
