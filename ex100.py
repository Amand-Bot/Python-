from random import randint
numeros = list()

def sorteia():

    for c in range(5):
        numeros.append(randint(0, 9))
        c += 1
    print(f'Sorteando {len(numeros)} valores da lista: {numeros} PRONTO!')


def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, tempos: {soma}')

sorteia()
somaPar()