a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))

def menu():

    print('----- MENU -----'),
    print('[1] SOMAR'),
    print('[2] MULTIPLICAR'),
    print('[3] MAIOR'),
    print('[4] NOVOS NÚMEROS'),
    print('[5] SAIR DO PROGRAMA'),
    print('-' * 20)

menu()
opcao = int(input('Escolha uma opção do menu: '))

while opcao != 5:
    if opcao == 1:
        print(a + b)
        menu()
        opcao = int(input('Escolha uma opção do menu: '))
    elif opcao == 2:
        print(a * b)
        menu()
        opcao = int(input('Escolha uma opção do menu: '))
    elif opcao == 3:
        if a > b:
            print('{} é maior que {}.'.format(a, b))
            menu()
            opcao = int(input('Escolha uma opção do menu: '))
        else:
            print('{} é maior que {}.'.format(b, a))
            menu()
            opcao = int(input('Escolha uma opção do menu: '))
    elif opcao == 4:
        a = float(input('Primeiro valor: '))
        b = float(input('Segundo valor: '))
        menu()
        opcao = int(input('Escolha uma opção do menu: '))
    else:
        print('Valores Inválidos!')
print('SAIU DO PROGRAMA')


