contador1=1
contador2=0
primeiro=int(input('digite o primeiro termo:'))
razão=int(input('digite a razão:'))
termo=primeiro
while contador1<=10:
    contador1=contador1+1
    termo=termo+razão
    print('{} ->'.format(termo),end=' ')
print('pausa')
quantidade=int(input('quantos termos você quer mostrar a mais?'))
while quantidade!=0:
    for c in range(0,quantidade):
        termo=termo+razão
        print('{} ->'.format(termo),end=' ')
    contador2 = contador2 + quantidade
    print('pausa')
    quantidade = int(input('quantos termos você quer mostrar a mais?'))
print('fim {}'.format(contador2+10))