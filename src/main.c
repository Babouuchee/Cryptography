/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** main
*/

#include <string.h>

#include "structs.h"
#include "include.h"

int main(int argc, char const *const *argv)
{
    config_t *config = NULL;
    generate_aes("2b7e151628aed2a6");
    return 0;

    if (argc == 2 && (strcmp(argv[1], "-h") == 0
        || strcmp(argv[1], "--help") == 0))
            return print_usage();
    config = get_config(argc, argv);
    return handle_config(config);
}
