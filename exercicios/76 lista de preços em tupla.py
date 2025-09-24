listagem = ('lapis',1,75,
            'borracha',2,
            'caderno',15.90,
            'estojo',25,
            'transferidor',4.20,
            'compaço',9.99,
            'mochila',120.32,
            'canetas',22.30,
            'livro',34.90)

print('-'*40)
print(f'{"LISTA ESCOLAR":^40}')#-> tá mostrando com 40 espaços centralizados
print('-'*40)
for pos in range(0,len(listagem)):#->for pos in listagem , são duas maneiras de se fazer a msm coisa
    if pos % 2 == 0 :
        print(f'{listagem[pos]:.<30}',end='')#-> o .<30 quer dizer que queremos por pontos alinhados a esquerda
    else:#-> isso aqui é porque o nome do produto está em uma posição par e o numero em posição impar
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
# esse desafio era mais a respeito de estética com pontos e afins para fazer com
# que manipulacemos o que iria retornar
