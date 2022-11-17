a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if abs(b - c) < a < b + c:
    print('O triângulo existe e é3 ', end='');
    if a == b == c:
        print('Equilátero')
    elif a == b or a == c or b == c:
        print('Isóceles')
    elif a != b and a!= c and b!= c:
        print('Escaleno')
else:
    print('O triângulo não existe');
