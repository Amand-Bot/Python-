nome = str(input('Qual seu nome?: ')).strip().title()
palavra = nome.split()
print('Seu primeiro nome: {}'.format(palavra[0]))
print('Seu último nome: {}'.format(palavra[-1]))