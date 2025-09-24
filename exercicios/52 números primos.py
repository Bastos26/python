contador1=0
contador2=0
numero = int(input('digite um numero:'))
for n in range(1,numero+1):
    print(n,end=' ')
    if numero%n==0:
        contador2 = contador2 + 1
    else:
        contador1 = contador1 + 1
if contador2>2:
        print('\nO numero não é primo porque é divisível por {} numeros'.format(contador2))
else:
        print('\nÉ PRIMOOOO!!!')

# quando o exemplo é 10 , o contador conta 6 por o contador esta "dentro"
 # do else e o else está contando os numeros que não tem o resto da divisão 0
#a adentação e o momento onde você vai aplicar a função é importante, o contador vai contar onde ele está sendo aplicado em relação a adentação,se colocar onde tem um if, ele vai contar o numero de vezes que aquele if acontecer