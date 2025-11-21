#funções
def resumo(n,p1,p2):
    #programas
    dobro=n*2
    metade=n/2
    aumento=n+((n*p1)/100)
    redução=n-((n*p2)/100)

    #apresentção
    print('-'*30)
    print(f'Resumo Do Valor:>.15f')
    print('-'*30)
    print(f'Preço Analisado:     R${n}'.replace('.',','))
    print(f'Dobro do preço:      R${dobro:.2f}'.replace('.',','))
    print(f'Metade do preço:     R${metade:.2f}'.replace('.',','))
    print(f'{p1}% de aumento:      R${aumento:.2f}'.replace('.',','))
    print(f'{p2}$ de redução:      R${redução:.2f}'.replace('.',','))
    print('-'*30)

    f"""resolução do guanabara
def diminuir(preço=0, taxa=0,formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)
    
def dobro(preço=0, fromat=False):
    res = preço * 2
    return res if not formato else moeda(res)
    
def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)
    
def moeda(preço=0, moeda=R$):
    return f'{moeda}{preço:>.ef}'.replace('.',',')
    
def resumo(preço=0,taxaa=10,taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro}(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(preço,taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preço, taxar, True)}')
    print('-' * 30)"""

#\t é referente a tabulação, para centralizar e por o espaçõ mais "bonitinho"
#center é referente a centralização do texto , (30) quer dizer que qeremos que ele centralize dentro de um espaço de 30