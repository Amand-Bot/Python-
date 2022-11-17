#Pega uma lista de palavras e mostra as vogais de cada uma

palavras = ('aprender', 'amarrar', 'gratis', 'praticar', 'estudar', 'pular',
            'curso', 'mercado')
for p in palavras:
    print(f'\n Na palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')