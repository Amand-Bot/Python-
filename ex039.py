from datetime import date
#idade para se alistar = 18
#idade limite = 45
ano = int(input('Seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    alistamento = (18-idade) + date.today().year
    print('Seu alistamento será em {}. Falta(m) {} ano(s).'.format(alistamento, 18 - idade))
elif 18 <= idade <= 45 :
    print('Você já está na hora de se alistar no exército. Cuida que é obrigatório.')
elif idade > 45:
    print('Você passou da idade para se alistar no exército. Você passou do prazo {} anos atrás.'.format(idade - 45))
