times = ('Fortaleza', 'Athletico', 'Atlético-GO', 'Bragantino',
          'Bahia', 'Fluminense', 'Palmeiras', 'Flamengo', 'Atlético-MG',
          'Corinthians', 'Ceará', 'Santos', 'Cuiabá', 'Sport', 'São Paulo',
          'Juventude', 'Internacional', 'Grêmio', 'América-MG', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')
