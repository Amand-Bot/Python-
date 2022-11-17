num = int(input('Digite o número: '))

print('=-=' * 15)
print('Escolha uma opção:')
print('=-=' * 15)
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
print('=-=' * 15)

base = int(input('Base de conversão: '))

if base == 1:
    bin = '{0:b}'.format(num)
    print('O número {} fica {} em binário.'.format(num,bin))
elif base == 2:
    oct = '{0:o}'.format(num)
    print('O número {} fica {} em octal.'.format(num,oct))
elif base == 3:
    hexa = '{0:x}'.format(num)
    print('O número {} fica {} em hexadecimal.'.format(num,hexa))
else:
    print('Digite uma opção válida.')
