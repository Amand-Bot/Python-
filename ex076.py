listagem = ('Pão', 1,
            'Leite', 3.50,
            'Frango', 10.90,
            'Café', 5)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}',end='')
    else:
        print(f'R${listagem[item]:>5.2f}')

