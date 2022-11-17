tot = -1
soma = num = 0
while num != 999:
    soma = soma + num
    num = int(input('Digite um número: '))
    tot += 1
print('Números digitados: {}.'.format(tot))
print('Soma dos números: {}.'.format(soma))