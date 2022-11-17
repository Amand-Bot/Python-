a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if abs(b - c) < a < b + c:
    print('O triângulo existe');
else:
    print('O triângulo não existe');
