##
## EPITECH PROJECT, 2024
## CNA
## File description:
## Makefile
##

NAME		=	my_pgp

SRC_MAIN	=	main.c

SRC			=	get_config.c	\
				handle_config.c	\
				print_usage.c	\
				algorithms/generate_aes.c

OBJ_MAIN	=	$(addprefix src/, $(SRC_MAIN:.c=.o))

OBJ			=	$(addprefix src/, $(SRC:.c=.o))

CPPFLAGS	=	-Wall -Wextra -Werror

CFLAGS		=	-I./include/

$(NAME):	$(OBJ_MAIN) $(OBJ)
	gcc -o $(NAME) $(OBJ_MAIN) $(OBJ) $(CPPFLAGS) $(CFLAGS) $(LIBS)

all:	$(NAME)

clean:
	rm -f $(OBJ) $(OBJ_MAIN)

fclean: clean
	rm -f $(NAME)

re: fclean all
