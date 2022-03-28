from retweeted import retweeted

lista = []


def main():
    numero = input("Ingrese un número del 1 al 4")
    if numero == 1 or numero == "1":
        lista1 = retweeted()
        for i in lista1:
            lista.append(i['content'])

    return lista
