from random import randint

maquina = randint(0, 5)
voce = int(input("Escolha um númeor de 0 a 5: "))

if voce == maquina:
    print("Você venceu!!!")
    print('Maquina: {}.'.format(maquina))
else:
    print("Você errou!")
    print('Maquina: {}.'.format(maquina))

