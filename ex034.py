sal = float(input('Digite seu salário: '))

if sal > 1250:
    print('Seu salário aumentou para: R$ {:.2f} '.format(sal*1.1));
else:
    print('Seu salário aumentou para: R$ {:.2f}'.format(sal*1.15));