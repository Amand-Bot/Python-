
sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf' :
    sexo = str(input('Erro!, Escolha uma opção válida [M/F]:')).strip().upper()[0]
print('Sexo {} registrado.'.format(sexo))

