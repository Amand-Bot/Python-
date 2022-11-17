#Criar uma lista com varios números depois mostra-la na forma decrescente
#e dizer se o 5 está ou não na lista.
i = 0
lista = []
while True:
    num = int(input('Digite um número: '))
    i += 1
    lista.append(num)
    lista.sort(reverse= True)
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    while pergunta not in 'NS':
       pergunta = str(input('Tente novamente.Quer continuar? [S/N] ')).strip().upper()
    if pergunta in 'Nn':
        print('=-='*18)
        lista.sort(reverse=True)
        if i == 1:
            print(f'Foi digitado apenas 1 número')
        print(f'Foram digitados {i} números.')
        print(f'Lista em ordem decrescente: {lista}')
        if 5 in lista:
            print(f'O número 5 foi digitado e está na lista.')
        else:
            print('O número 5 não foi digitado e não está na lista.')
        print('=-='*18)
        break