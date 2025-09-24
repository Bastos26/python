cont=cont2=0
numeros=[]
for c in range(4):
    n = int (input('digite um numero'))

    if n % 2 == 0 :
        cont2=cont2+1

    numeros.append(n) # essa função pega o valor e armazena na lista

tuplas=tuple(numeros) # aqui transformamos a lista em tuplas
print(tuplas)

for n in tuplas:
    if n == 9 :
        cont=cont+1
print(f'o numero 9 aparece {cont} vezes na tupla')

if 3 in tuplas:
    print(f'o numero 3 está na posição {tuplas.index(3)}')
else:
    print('o numero 3 não foi digitado')
print(f'existe {cont2} numeros pares')

"""
uma das maneiras de se contar um valor em uma dupla:
count é um método que se está na tupla que conta as vezes em que está presente na variavel composta
ex:
nove = tuplas.count(9)
print(f'o numero 9 aparece {nove} vezes na tupla')"""

"""resolução do guanabara:
num = (int(input('digite um numero interio :')),    -> aqui vemos novamente a formação das tuplas ,
       int(input('digite outro numero interio :'))  ,sem precisar usar append para por na lista
       int(input('digite mais numero interio :')),  e depois usar  tuple para transformar em tuplas. 
       int(input('digite e mais numero interio :'))) ->basta colocar tudo dentro de um parenteses unico e ir  
print(f' você digitou os valores{num}')                separando cada valor com parenteses e virgula.
print(f' o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu na posição {num.index(3)+1}')
else:
    print('o valor 3 não foi digitado')
for n in num:
    if n % 2 == 0 :
    print(n, end=' ')
  
"""