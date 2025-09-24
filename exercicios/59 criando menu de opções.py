n1=int(input('digite um valor:'))
n2=int(input('digite o segundo valor:'))
ação=''
while ação != 'E':
    ação = str(input(
        'selecione o que gostaria de executar:\n[A]somar\n[B]multiplicar\n[C]maior\n[D]novos numeros\n[E]sair do programa')).strip().upper()
    if ação== 'A':
        soma=n1+n2
        print(' a soma dos numeros é {}'.format(soma))
    elif ação == 'B':
        multiplicação=n1*n2
        print('a multiplicação dos valores é {}'.format(multiplicação))
    elif ação == 'C':
        if n1>n2:
            print('o maior numero é {}'.format(n1))
        else: print('o maior numero é {}'.format(n2))
    elif ação == 'D':
        n1=int(input('digite o primeiro valor:'))
        n2=int(input('digite o segundo valor:'))
    elif ação == 'E':
            print('fim')