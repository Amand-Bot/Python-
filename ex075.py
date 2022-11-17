palavra = ('um', 'outro', 'mais um', 'o último')
tupla = ()
pares = ()
i = 0
for c in palavra:
    num = int(input(f'Digite {c} valor: '))
    tupla += tuple([num])
    if num == 9:
      i += 1
    if num % 2 == 0:
        pares += tuple([num])
print(f'Você digitou os numeros {tupla}.')
print(f'O numero 9 apareceu {i} vezes.')
if 3 in tupla:
    print(f'O número três foi digitado pela primeira vez na {(tupla.index(3))+1}° posição.')
else:
    print(f'O número três não foi inserido.')
print(f'O números pares inseridos foram: {pares}', end=' ')