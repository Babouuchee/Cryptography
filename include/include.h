/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** include
*/

#ifndef INCLUDE_H_
    #define INCLUDE_H_

    #include "structs.h"

void print_usage(void);
config_t *get_config(char const *const *argv);
int handle_config(config_t *config);

#endif /* !INCLUDE_H_ */
