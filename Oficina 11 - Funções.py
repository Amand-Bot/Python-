agenda = [
  ((2020, 1, 13), (11, 50), 'Renovar identidade'),
  ((2020, 1, 15), (16, 30), 'Fazer compras'),
  ((2020, 1, 25), (8, 45), 'Autenticar documentos'),
  ((2020, 2, 29), (14, 15), 'Prestar concurso'),
  ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),
  ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista')
]

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

def formatar_data(data):
  for x in range(1, len(meses)):
    if data[1] == x:
      return f'{data[2]}/{meses[x-1]}/{data[0]}'


def formatar_hora(hora):
  return f'{hora[0]}:{hora[1]}'


def imprimir_eventos(agenda, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):
  for x in range(len(agenda)):
    if de_data[1] <= agenda[x][0][1] and de_data[2] <= agenda[x][0][2]:
        print(f'{formatar_data(agenda[x][0])} - '
              f'{formatar_hora(agenda[x][1])}\t:'
              f' {agenda[x][2]}')
  


imprimir_eventos(agenda, (2020, 1, 25), (2020, 3, 15))
