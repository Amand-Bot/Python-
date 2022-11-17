soma = 0
i = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    i += 1
    soma += num
print(f'A quantidade de números inseridos foi {i} e a soma deles foi de {soma}. ')