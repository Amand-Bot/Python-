lista = []
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    lista.append(peso)
print('O maior número encontrado foi de {} Kg.'.format(max(lista)))
print('O menor número encontrado foi de {} Kg.'.format(min(lista)))
