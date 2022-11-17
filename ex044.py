valor = float(input('Valor do produto: R$'))
print('Escolha uma opção:')
print('[1] À vista [2] Parcelado')
escolha = int(input('Opção: '))

if escolha == 1:
    escolha2 = int(input('[1] Dinheiro/Cheque [2] Cartão'))
    if escolha2 == 1:
        print('Valor a pagar: {} com desconto de 10% inserido.'.format((valor*0.9)))
    elif escolha2 == 2:
        print('Valor a pagar: {} com desconto de 5% inserido.'.format(valor*0.95))
elif escolha == 2:
    parcelas = int(input('Quantidade de parcelas: '))
    if parcelas <= 2:
        print('Valor a pagar: {} de {} vezes sem juros.'.format(valor, parcelas))
    elif parcelas >= 3:
        print('Valor total á pagar: {} ; {} vezes de {} com 20% de juros.'.format(valor*1.20, parcelas, (valor*1.20)/parcelas))