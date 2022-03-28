from retweeted import retweeted


def main():
    numero = input("Ingrese un número del 1 al 4")
    if numero == 1 or numero == "1":
        lista = retweeted()

    return lista
