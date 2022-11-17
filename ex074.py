from random import randint
n = (randint(1, 10),randint(1, 10),randint(1, 10),
     randint(1, 10),randint(1, 10))
print(f'Eu sorteei os valores {n}. ')
print(f'O maior valor é {max(n)} e o menor é {min(n)}')
#tupla = ()
#for c in range(5):
#    maquina = randint(0,9)
#    tupla = tupla + tuple([maquina])

#print(f'Os valores foram: {tupla}')
#print(f'O maior valor é {max(tupla)} e o menor é {min(tupla)}')
