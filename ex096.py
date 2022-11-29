def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} * {c} é de {a}m².')



print(' Controle de Terrenhos')
print('_'* 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)