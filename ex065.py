num = int(input('Digite um número: '))
r = str(input('Quer continuar? [S/N] ')).strip().upper()
total = 1
soma = num
maiornum = 0
menornum = 0
while r != 'N':
    if total == 1:
        maiornum = menornum = num
    else:
        if num > maiornum:
            maiornum = num
        if num < menornum:
            menornum = num
    if r == 'S':
        num = int(input('Digite um número: '))
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
        soma = soma + num
        total += 1
print('A média dos {} termos inseridos é {}.'.format(total, soma/total))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maiornum, menornum))
