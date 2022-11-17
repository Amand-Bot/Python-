a1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = a1 + (10 - 1) * razao
for c in range(a1, termo + razao, razao):
    print('{} '.format(c), end=' → ')
print('FIM')

