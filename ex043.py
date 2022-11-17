peso = float(input('Peso: '));
altura = float(input('Altura: '));

cal = peso  / pow(altura, 2);

if cal < 18.5:
  print(f'{cal:,.2f} Kg/h² - Abaixo do peso');
elif 18.5 < cal < 25:
  print(f'{cal:,.2f} Kg/h² - Peso ideal');
elif 25 < cal < 30:
  print(f'{cal:,.2f} Kg/h² - Sobrepeso');
elif 30 < cal < 40:
  print(f'{cal:,.2f} Kg/h² - Obesidade');
elif cal > 40:
  print(f'{cal:,.2f} Kg/h² - Obesidade Mórbida');