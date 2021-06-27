dados = dict()
gols = []
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for g in range(1, partidas + 1):
    gols.append(int(input(f'    Quantos gols na partida {g}? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {sum(dados["gols"])} gols.')
