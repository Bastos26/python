cont=1
while cont <= 10 : # enquanto cont for menor que 10 , o laço vai continuar
    cont=cont+1    # se fosse com while True, o laço seria infinito e a única maneira de fazer parar é utilizando o break
    print(cont)
print('acabou')



n = cont1 = s =0
while cont != 999: # aqui é a ideia de controle de loop, onde colocamos uma restrição (flag) para ser o ponto de parada
    n = int(input('digite um numero:'))
    cont+=1
    s=s+n # normalmente o flag 999 seria contado aqui, e ele é para ser um flag e não um valor
    print(s)

while True: #aqui é um loop infinito
    n=int(input('digite um numero:'))
    if n == 999:# aqui o 999 não vai ser somada , aqui ela está sendo uma flag e não um valor em si
        break
    s = s+n
print(f'a smoa é {s}')