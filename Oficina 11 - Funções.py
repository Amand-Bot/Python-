agenda = [
  ((2020, 1, 13), (11, 50), 'Renovar identidade'),
  ((2020, 1, 15), (16, 30), 'Fazer compras'),
  ((2020, 1, 25), (8, 45), 'Autenticar documentos'),
  ((2020, 2, 29), (14, 15), 'Prestar concurso'),
  ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),
  ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista')
]

meses = ['jan', 'fev', 'mar', 'abr','mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
def formatar_data(ano,mes,dia):
  for x in range(len(meses)+1):
    if mes == x:
      mes = meses[x]
      print(f'{dia}/{mes}/{ano}')

formatar_data(2020, 1, 15)
def formatar_hora(hora, minuto):
  print(f'{hora}:{minuto}')



#def imprimir_eventos(eventos, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):