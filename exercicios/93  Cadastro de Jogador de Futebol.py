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