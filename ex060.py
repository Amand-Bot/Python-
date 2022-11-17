num = int(input('Digite um número: '))
c = num - 1

print('{}! = '.format(num), end='')

while c > 1:
    print("{} X ".format(c), end='')
    num = num * c
    c -= 1
print('1 = {}'.format(num), end='')

#n = int(input('Digite um número para calcular seu Fatorial: ')
#c = n
#f = 1
#print('Calculando {}! = '.format(n), end='')
#while c > 0:
#   print('{}'.format(c), end='')
#   print(' x ' if c > 1 else ' = ', end='')
#   f*= c
#   c -= 1
#print('{}'.format(f))