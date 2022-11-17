a1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
t = 1
while  t <= 10:
    print('{} → '.format(a1), end='')
    a1 += razao
    t += 1
print('FIM',end='')