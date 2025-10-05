import random
jogadores = {}
jogadores['jogador1']= random.randint(1,6)
jogadores['jogador2']= random.randint(1,6)
jogadores['jogador3']= random.randint(1,6)
jogadores['jogador4']= random.randint(1,6)
for k,v in jogadores.items():
    print(f'{k} = {v}')