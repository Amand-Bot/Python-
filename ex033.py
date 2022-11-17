a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

if a > b > c:
    print(f'{a} é o maior número e {c} é o menor');
if a > c > b:
    print(f'{a} é o maior número e {b} é o menor');
if b > a > c:
    print(f'{b} é o maior número e {c} é o menor');
if b > c > a:
    print(f'{b} é o maior número e {a} é o menor');
if c > a > b:
    print(f'{c} é o maior número e {b} é o menor');
if c > b > a:
    print(f'{c} é o maior número e {a} é o menor');

