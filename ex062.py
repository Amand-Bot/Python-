a1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while  cont <= total:
        print('{} → '.format(a1), end=' ')
        a1 += razao
        cont += 1
    print('PAUSA',)
    mais = int(input('Quantos termos a mais quer ver?: '))
print('FIM')