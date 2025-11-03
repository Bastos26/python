def registro(jog='<desconhecido>',g=0):
    if jog == '':
        jog = '<desconhecido>'

    while True:
        if g == '':
            g = 0
            break
        try:
            g = int(g)
            break
        except ValueError:
            g = input('Tente novamente: ')
    print(f'o jogador {jog} fez {g} gol(s)')

#programa principal
nome=str(input('Digite o nome do jogador: '))
gol=input('Digite o número de gol(s): ')
registro(nome,gol)

#o meu grande problema na questão foi o tratamento dos tipos de variáveis errados
#para ser mais preciso , quando apertamos enter no gol
#tirei o int porque assim não dava o erro 10 e o programa poderia continuar para eu o tratar

"""
resolução do guanabara
def ficha (jog='<desconhecido>',gol=0):
    print(f' O jogador{jog} fez {gol} gol(s) no campeonato.')
    
#programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if ,strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)"""



