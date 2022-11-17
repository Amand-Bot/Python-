from datetime import date
i = 0
t = 0
for c in range(1,8):
    ano = int(input('Ano de nascimento:'))
    t += 1
    idade = date.today().year - ano
    if idade < 20:
        i += 1
print('{} pessoas ainda não atingiram a maior idade.'.format(t-i))
print('Já atingiram a maioridade {} pessoas.'.format(i))