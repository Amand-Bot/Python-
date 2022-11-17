from datetime import date

ano = int(input('Informe sua data de nascimento: '))
idade = date.today().year - ano

print('O atleta tem {} anos. '.format(idade))
print('Classificação: ')
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 20:
    print('Sênior')
elif idade > 20:
    print('Master')