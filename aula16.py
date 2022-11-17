#Tuplas
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#print(lanche[3])
#print(len(lanche)) #== 4
#for comida in lanche:
#    print(f'Eu vou comer {comida}')

a = list(range(10))
print(a)

b = tuple(range(6))
print(b)

from random import randint

tupla = ()
for c in range(5):
    maquina = randint(0,9)
    tupla = tupla + tuple([maquina])
print(tupla)
