/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** include
*/

#ifndef INCLUDE_H_
    #define INCLUDE_H_

    #include "structs.h"

int print_usage(void);
config_t *get_config(int ac, char const *const *av);
int handle_config(config_t *config);
int generate_aes(char *client_key);

#endif /* !INCLUDE_H_ */
