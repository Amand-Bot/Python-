from random import randint
from time import sleep
print('Escolha um número: '),
print('0 - PEDRA | 1 - PAPEL | 2 - TESOURA'),
print('---' * 12)

valor = int(input('Sua opção:'))

objetos = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = randint(0, 2)
print('Você escolheu: {}'.format(objetos[valor]))
print('A máquina escolheu: {}'.format(objetos[maquina]))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if maquina == valor:
    print('Empate')
elif maquina == 0:  # Se ela escolher Pedra
    if valor == 1:
        print('Você ganhou!')
    elif valor == 2:
        print('Máquina ganhou!')
    else:
        print('Jogada inválida')
elif maquina == 1:  # Se ela escolher Papel
    if valor == 0:
        print('Máquina ganhou!')
    elif valor == 2:
        print('Você ganhou!')
    else:
        print('Jogada inválida')
elif maquina == 2:  # Se ela escolher Tesoura
    if valor == 0:
        print('Você ganhou!')
    elif valor == 1:
        print('Máquina ganhou!')
    else:
        print('Jogada inválida')