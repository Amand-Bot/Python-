vel = float(input('velocidade do carro: '))
conta = (vel-80)*7
if vel > 80:
    print('Você foi multado!')
    print('Valor da multa: R$ {:.2f} .'.format(conta))