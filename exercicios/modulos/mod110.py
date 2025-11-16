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