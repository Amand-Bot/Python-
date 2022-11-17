times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'América-MG',
         'Atlético-MG', 'São Paulo', 'Fortaleza', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Atlético-GO', 'Ceará', 'Avaí', 'Juventude')

print('=-='*50)
print('                CAMPEONATO BRASILEIRO DE FUTEBOL ')
print('=-='*50)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print(f'Os últimos 4 colocados da tabela: {times[-5:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'Fortaleza está na {times.index("Fortaleza")+1}° posicão.')