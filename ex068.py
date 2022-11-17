from random import randint
i = 0
while True:
    maquina = randint(0, 10)
    voce = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    num = int(input('Escolha um número de 0 a 10: '))
    print(f'A máquina escolheu {maquina} e você {num}. ', end='')
    soma = num + maquina
    i += 1
    if voce == 'P' and soma % 2 == 0:
        print(f'Total de {soma} deu PAR')
        print('Voce ganhou!')
        print('Jogue novamente. ',end='')
    elif voce == 'I' and soma % 2 !=  0:
        print(f'Total de {soma} deu Impar')
        print('Voce ganhou!')
        print('Jogue novamente. ', end='')
    else:
        break
print('Voce perdeu.')
print(f'Você ganhou {i-1} vez(es) seguida(s).')
