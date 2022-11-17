casa = float(input('O valor da casa: R$'))
sal = float(input('Seu salário: R$'))
anos = int(input('Quantos anos para quitar o empréstimo: '))

parcela = casa/(anos*12)

if parcela <= 0.3*sal:
    print('Parcela da casa: R$ {:.2f} pôr mês durante {} anos'.format(parcela, anos))
else:
    print('Empréstimo não aprovado.')