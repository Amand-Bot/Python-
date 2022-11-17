#Cadastrar varios valores numéricos não repetidos em uma lista.
#Mostrar todos os valores unicos digitados, em ordem crescente.
lista = []
while True:
    num = int(input('Digite uma valor: '))
    if num not in lista:
        print('Valor adcionado com sucesso!')
    if num in lista:
        print('Valor duplicado não adcionado.')
        lista.remove(num)
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    lista.append(num)
    if pergunta in 'Nn':
        break
print(sorted(lista))

