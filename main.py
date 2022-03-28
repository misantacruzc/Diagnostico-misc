from retweeted import retweeted
from users import users
from days import date
from hashtags import hashtag


def main():
    lista = []
    numero = input("Ingrese un número del 1 al 4")
    if numero == 1 or numero == "1":
        lista1 = retweeted()
        for i in lista1:
            lista.append(i['content'])
    elif numero == 2 or numero == "2":
        lista = users()
    elif numero == 3 or numero == "3":
        lista = date()
    elif numero == 4 or numero == "4":
        lista = hashtag()
    else:
        lista = "Número inválido"

    return lista
