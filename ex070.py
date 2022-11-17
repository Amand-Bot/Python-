barato = 0
nomebarato = 0
mil = 0
soma = 0
while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? R$'))
    cont = + 1
    soma += preco
    p = str(input('Dejesa continuar? [S/N] ')).strip().upper()[0]
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < barato:
        barato = preco
        nomebarato = nome
    if p == 'N':
        break
print(f'O gato total da compra foi de {soma}.')
print(f'A quantidade de produtos que custam mais de 1000,00 foi  {mil}.')
print(f'O nome do produto mais barato é {nomebarato} que custa {barato}.')