import random
contador=0
while True:
    n = int(input('escolha um numero de 1 a 10:'))
    escolha= str(input('escolha PAR ou IMPAR(P/I)')).strip().upper()
    comp=random.randint(1,10)
    soma=n+comp
    if escolha == 'I':
        comp_escolha = 'P'
    elif escolha == 'P':
        comp_escolha = 'I'
    if soma % 2 == 0:
        resultado =  'P'
        print(f'você jogou {n} e o computador jogou {comp} e escolheu {comp_escolha}, o resultado é {soma} e é um numero PAR')
        if escolha == resultado:
            contador = contador + 1
            print('você ganhou')
        if comp_escolha == resultado:
            print('você perdeu, GAME OVER')
            break
    else:
        resultado = 'I'
        print(f'você jogou {n} e o computador jogou {comp} e escolheu {comp_escolha}, o resultado é {soma} e é um numero IMPAR')
        if escolha == resultado:
            contador = contador + 1
            print('você ganhou')
        if comp_escolha == resultado:
            print('você perdeu,GAME OVER')
            break
print(f'numero de rodadas: {contador} ')