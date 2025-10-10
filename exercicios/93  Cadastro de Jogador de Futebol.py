jogador = {}
partidas = []
tot = 0
jogador['nome'] = str(input('Qual é o nome do jogador ?'))
for c in range (0,5):
    gol=int(input(f'Quantos gols o jogador {jogador["nome"]} fez na partida {c+1}: '))
    partidas.append(gol)
    tot = tot + gol
jogador['gols'] = partidas
jogador['total'] = tot
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f' O jogador {jogador["nome"]} jogou 5 partidas.')
for c , v in enumerate(partidas):
    print(f' => Na partida {c}, fez {v} gols')
print(f' Foi um total de {tot} gols')
"""resolução do guanabara
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantos partidas {jogador["nome"]} jogou ? '))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c} ?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k , v in jogador.items():
    print(f' O campo {k} tem o valor {v}')
print('-='*30)
print(f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i,v i enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total]} gols.')"""