def metade(n):
    met = n / 2
    print(f'A metade de R${n} é de R${met:.2f}'.replace(".",","))
def dobro(n):
    dob = n * 2
    print(f' O dobro de R${n} é de R${dob:.2f}'.replace(".",","))
def porcentagem(n):
    p = float(input('Digite a porcentagem desejada: '))
    por = (n * p) /100
    print(f'Aumentando em {p}%, temos R${n+por:.2f}'.replace(".","."))

#👉 Então: replace não é uma função isolada, mas sim um método da classe str. Ele só funciona em strings, e é por isso que usamos f"{valor:.2f}" (que gera uma string) antes de aplicar .replace(".", ",").
#como o exercicio pede uma nova função , meio que esse não é a resposta adequada

"""resolução do guanabra
def aumentar(preço=0,taxa=0):
    res = preço + (preço * taxa/100)
    return res

def diminuir(preço=0,taxa=0):
    res = preço - (preço * taxa/100)
    return res

def dobro(preço=0):
    res = preço * 2
    return = res

def metade(preço=0):
    res = preço / 2
    return res

def moeda(preço=0, moeda=R$):
    return f'{moeda}{preço:>.2f}'.replace('.',',')"""