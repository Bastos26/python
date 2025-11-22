#funções
def validação(n):
    while True:
        if n == '':
            n = input('ERRO! tente novamente: R$ ')
        try:
            n = float(n)
            break
        except ValueError:
            if ',' in n :
                n = float(n.replace(',','.'))
                break
            else:
                n = input('ERRO! tente novamente: (Não pode conter caracteres) R$')
    return n

def resumo(n,p1,p2):
    #programas
    dobro=n*2
    metade=n/2
    aumento=n+((n*p1)/100)
    redução=n-((n*p2)/100)

    #apresentção
    print('-'*30)
    print('               Resumo Do Valor')
    print('-'*30)
    print(f'Preço Analisado:     R${n}'.replace('.',','))
    print(f'Dobro do preço:      R${dobro:.2f}'.replace('.',','))
    print(f'Metade do preço:     R${metade:.2f}'.replace('.',','))
    print(f'{p1}% de aumento:      R${aumento:.2f}'.replace('.',','))
    print(f'{p2}$ de redução:      R${redução:.2f}'.replace('.',','))
    print('-'*30)
    #obs toda vez que se utiliza o replace , deve se ter cuidado caso esteja envolvendo numeros na situação porque o replace transforma
    # em string

"""resolução do guanabara
def LeiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido! \033[m')
        else:
            válido = True
            return float(entrada)"""