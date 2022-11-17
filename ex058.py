from random import randint

maquina = randint(0, 10)
voce = int(input('Escolha um número de 0 a 10: '))
tentativas = 0

while maquina != voce:
    if maquina > voce:
        print('Mais... Tente novamente.')
    elif maquina < voce:
        print('Menos... Tente novamente.')
    voce = int(input('Qual é seu palpite: : '))
    tentativas += 1

print('Você acertou!')
print('A Màquina escolheu {}!'.format(maquina))
print('Números de tentativas: {}.'.format(tentativas))