##
## EPITECH PROJECT, 2024
## CNA
## File description:
## Makefile
##

NAME		=	my_pgp

SRC			=	main.c							\

OBJ			=	$(addprefix src/, $(SRC:.c=.o))

CPPFLAGS	=	-Wall -Wextra -Werror

CFLAGS		=	-I./include/

$(NAME):	$(OBJ)
	gcc -o $(NAME) $(OBJ) $(CPPFLAGS) $(CFLAGS) $(LIBS)

all:	$(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all
