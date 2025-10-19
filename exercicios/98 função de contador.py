def contador(i, f, p):
    while i != f:
        i = i + p
        print(i)


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
inicio = float(input('Início: '))
fim = float(input('Fim: '))
passo = float(input('Passo: '))
contador(inicio, fim, passo)
for c in range(0,10,2):
    print(c,end='')
#no exercicio eu estou tendo dificuldades em fazer o sistema de contagem , acredito que o programa principal esteja ok
#a primeira duvida era se poderiamos colocar parâmetros formais, mais que um , e pelo visto sim , então acredito que sempre sera três
#tentei utilizar o if para contar mas acredito que devo usar o for para fazer a contagem
#não lembro onde eu vi para fazer contagens regressivas , tenho que ver onde , acredito que n falta muito para terminar o exercicio
