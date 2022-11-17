maiordeidade = 0
homem = 0
mulher = 0
while True:
    print('=-=' * 9)
    print('   CADASTRE UMA PESSOA   ')
    print('=-=' * 9)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    proximo = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
    if idade > 18:
        maiordeidade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if proximo == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiordeidade}')
print(f'Ao todo temos {homem} homen(s) cadastrado(s)')
print(f'E temos {mulher} mulher(es) com menos de 20 anos.')