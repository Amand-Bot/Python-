dist = int(input("Distância da viagem em Km: "))

if 1 < dist <= 200:
    print('O valor da viagem é: R$ {} .'.format(dist*0.5))
elif dist > 200:
    print('O valor da viagem é: R$ {} .'.format(dist * 0.45))
else:
    print('Digite um valor positivo maior que 0.')