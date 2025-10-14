jogador={}
jogadores=[]
gols=[]
tot=0
while True :
    jogador['nome'] = str(input('Nome do Jogador:'))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
    for c in range(0,jogador['partidas']):
        gol = int(input(f'Quantos gols o jogador {jogador["nome"]} marcou na {c+1}º partida ?'))
        tot = tot + gol
        jogador['total'] = tot
        gols.append(gol)
    tot = 0
    jogador['gols'] = gols[:]
    gols.clear()
    jogadores.append(jogador.copy())
    while True:
        desejo = str(input('Deseja continuar ? [S/N]')).upper()[0]
        if desejo == 'S':
            break
        if desejo != 'N':
            print('ERRO! Tente novamente:')
        if desejo == 'N':
            break
    if desejo == 'N':
        break
for c in jogadores:
    print(c)
print('=-'*30)
print('cod nome          gols          total')
print('-'*50)
for c in range(0,len(jogadores)):
    print(f'{c} {jogadores[c]["nome"]}             {jogadores[c]["gols"]}             {jogadores[c]["total"]}')
print('-'*50)
while True:
    escolha = int(input('Mostrar dados de qual jogador ? (999 para parar)'))
    if escolha <= len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolha]['nome']}')
        for c in range(0,jogadores[escolha]['partidas']):
            print(f' No jogo {c+1} fez {jogadores[escolha]["gols"][c]}')
    if escolha == 999:
        print('<<< ADEUS >>>')
        break
    if escolha > len(jogadores) and escolha < 999 :
        print('ERRO!!!')
#com a lista , fazemos a copia da lista e apagamos a antiga , para que sempre vá atualizando a outra variavel composta
#com os dicionarios , basta fazer o copy que já efetua este procedimento"""
"""resolução do guanabara
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = in(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'   Quantos gols a partida {c} ?')))
    jogador['gol'] = partidas[:]
    jogador['total] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'SN':
            break
        print('ERRO !   Responda apenas com S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k,v in enumerate(time)
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca = inpu(input(('Mostrar dados de qual jogador ? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO ! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')"""
