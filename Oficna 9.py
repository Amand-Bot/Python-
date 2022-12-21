import math
presentes = {
    'cadeira', 'cafeteira', 'caneca', 'escumadeira',
    'espanador', 'espátula', 'estante', 'faqueiro',
    'frigideira', 'funil', 'halter', 'liquidificador',
    'notebook', 'panela', 'peneira', 'playstation',
    'rádio', 'smartphone', 'sofá', 'tablet', 'teclado',
    'televisão', 'vassoura', 'webcam', 'xbox',
}
print(presentes)
loja1 = {
    'cadeira', 'cafeteira', 'caneca', 'escumadeira', 'estante',
    'frigideira', 'funil', 'liquidificador', 'notebook', 'panela',
    'playstation', 'smartphone', 'teclado', 'televisão'}
loja2 = {
    'cafeteira', 'escumadeira', 'espanador', 'frigideira', 'funil',
    'halter', 'peneira', 'playstation', 'sofá', 'tablet', 'televisão',
    'vassoura', 'webcam', 'xbox'}
loja3 = {
    'caneca', 'escumadeira', 'espanador', 'espátula', 'estante',
    'frigideira', 'halter', 'playstation', 'rádio', 'smartphone',
    'sofá', 'teclado', 'televisão', 'vassoura', 'xbox'}
loja4 = {
    'caneca', 'escumadeira', 'espanador', 'espátula', 'estante',
    'frigideira', 'halter', 'playstation', 'rádio', 'smartphone',
    'sofá', 'teclado', 'televisão', 'vassoura', 'xbox'}

todos_produtos = loja1.union(loja2, loja3, loja4)

produtos_distintos = presentes.intersection(todos_produtos)
produtos_comuns = presentes.intersection(loja1, loja2, loja3, loja4)
produtos_diferentes = presentes.difference(todos_produtos)
loja1_diferenca = loja1.difference(loja2, loja3, loja4)
loja2_diferenca = loja2.difference(loja1, loja3, loja4)
loja3_diferenca = loja3.difference(loja2, loja1, loja4)
loja4_diferenca = loja4.difference(loja2, loja3, loja1)
loja1_presentes = loja1.intersection(loja2.union(loja3, loja4))
loja2_presentes = loja2.intersection(loja1.union(loja3, loja4))
loja3_presentes = loja3.intersection(loja1.union(loja2, loja4))
loja4_presentes = loja4.intersection(loja1.union(loja2, loja3))

print(produtos_distintos)
print(produtos_comuns)
print(produtos_diferentes)
print(loja1_diferenca)
print(loja2_diferenca)
print(loja3_diferenca)
print(loja4_diferenca)
print(len(loja1_presentes))
print(len(loja2_presentes))
print(len(loja3_presentes))
print(len(loja4_presentes))

