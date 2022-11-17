#Programa que le 5 valores e guarda em uma lista.
#No final mostra o maior e o menor valor digitado e suas respectivas osições.
lista = []

for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
print(f'O maior valor da lista é: {max(lista)} na {lista.index(max(lista))+1}° posição.')
print(f'O menor valor da lista é: {min(lista)} na {lista.index(min(lista))+1}° posição.')