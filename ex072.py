numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco')

while True:
    c = int(input('Escolha um número de 0 a 5: '))
    if c > len(numeros) or c < 0:
        c = int(input('Tente novamente.Escolha um número de 0 a 5: '))
    print(f'Voce escolheu o número {numeros[c]}')
    pergunta = str(input('Você quer continuar? [S/N] ')).strip().upper()
    if pergunta == 'N':
        break

