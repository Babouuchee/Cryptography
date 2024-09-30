/*
** EPITECH PROJECT, 2024
** VlaLaThune
** File description:
** print_usage
*/

#include <stdio.h>

static void print_crypto_system(void)
{
    printf("\tCRYPTO_SYSTEM\n");
    printf("\t\t\"xor\"\t    computation using XOR algorithm\n");
    printf("\t\t\"aes\"\t    computation using 128-bit AES algorithm\n");
    printf("\t\t\"rsa\"\t    computation using RSA algorithm\n");
    printf("\t\t\"pgp-xor\"   computation using both RSA and XOR algorithm\n");
    printf("\t\t\"pgp-aes\"   computation using both RSA ");
    printf("and 128-bit AES algorithm\n");
}

static void print_mode_options_and_key(void)
{
    printf("\n\tMODE\n");
    printf("\t\t-c\t    MESSAGE is clear and we want to cipher it\n");
    printf("\t\t-d\t    MESSAGE is ciphered and we want to decipher it\n");
    printf("\t\t-g P Q      for RSA only: Don't read a MESSAGE, but ");
    printf("instead generate a public and private key pair from the prime ");
    printf("number P and Q\n");
    printf("\n\tOPTIONS\n");
    printf("\t\t-b\t    for XOR, AES and PGP, only works on one block. ");
    printf("The MESSAGE and the symmetric key must be the same size\n");
    printf("\n\tkey \t\t    Key used to cipher/decipher MESSAGE ");
    printf("(incompatible with -g MODE)\n");
}

void print_usage(void)
{
    printf("USAGE\n");
    printf("./my_pgp CRYPTO_SYSTEM MODE [OPTIONS] [key]\n\n");
    printf("DESCRIPTION\n");
    printf("The MESSAGE is read from standard input\n\n");
    print_crypto_system();
    print_mode_options_and_key();
}
