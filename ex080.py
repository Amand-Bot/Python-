#Colocar 5 valores em uma lista e mostrar ela ordenada na tela sem usar o sort.
lista = []
menor = 0
while True:
    num = int(input('Digite um valor:'))
    if num > menor:
        menor = num
    lista.append(num)
