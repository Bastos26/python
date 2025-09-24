"""num = [2,5,9,1]
num[2]=3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)#primero é o valor(2) e depois da virgula a posição que desejamos(no caso do exemplo o 0)
#num.pop()
num.remove(2) # a key ficaria com dois numeros 2 , o remove retira apenas o primerio numero que ele encontrar na ordem
print(num)
print(f'essa lista tem {len(num)} elementos')

"""
valores=[]
"""valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}....')
for c in range:
    valores.append(int(input('digite um numero:')))
    
for c,v in enumerate(valores):
    print(f' na posição {c} encontrei o valor {v}')
print(f'chegeui no final da lista')"""

a = [1,2,3,4,5]
b = a
print(a)#aqui fizemos uma cópia de uma lista
print(b)# em python existe algo peculiar

b[2]=8#pela lógica, só iria mudar a lista b mas ,na verdade vai se
print(a)#alterar a lista a tambem
print(b)#porque em python , as listas estão ligadas, altera um e a outra vai sofrer tambem

c = a[:] # através dessa maneira que fazemos uma cópia de fato e não uma ligação
c[2]=9 #aqui a unica lista que vai ser alterada vai ser o c
print(a)
print(c)