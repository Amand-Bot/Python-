nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('REPROVADO')
elif 5 >= media <= 6.9:
    print('RECUPERAÇÂO')
elif media >= 7:
    print('APROVADO!')
print('Média : {:.2f}'.format(media))
