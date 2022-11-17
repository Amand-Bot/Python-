lista = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    while pergunta not in 'NS':
        pergunta = str(input('Tente novamente.Quer continuar? [S/N] ')).strip().upper()
    if num % 2 == 0:
        pares.append(num)
    if num % 2 != 0:
        impares.append(num)
    if pergunta in 'Nn':
        print(f'Lista: {sorted(lista)}.')
        print(f'Números pares digitados: {pares}.')
        print(f'Números impáres digitados {impares}.')
        break