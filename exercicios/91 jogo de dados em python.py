import random
jogadores = {}
jogadores['jogador1']= random.randint(1,6)
jogadores['jogador2']= random.randint(1,6)
jogadores['jogador3']= random.randint(1,6)
jogadores['jogador4']= random.randint(1,6)
for k,v in jogadores.items():
    print(f'{k} tirou o valor {v}')
ordem=sorted(jogadores.items(),key=lambda item:item[1])
print('-='*30)
print(' << RANKING DOS JOGADORES  >> ')
for i,v in enumerate(ordem):
    print(f'{i+1}º lugar:{v[0]} com {v[1]}')


    """resolução do guanabara
from random import radint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}
print('Valores Sorteados')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)"""
#ele utiliza o import operator com a funcionalidade itemgetter
#pelo visto ele faz a mesma coisa, quando o sorted tá trabalhando, diz para se basear no values e não nas keys



