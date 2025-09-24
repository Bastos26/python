"""lista=[]

n1=int(input('digite um valor:'))
lista.append(n1)

n2=int(input('digite um valor:'))
if n2 > lista[0]:
    lista.append(n2)
else:
    lista.insert(0,n2)
print(lista)

n3=int(input('digite um valor:'))
if n3 < lista[0]:
    lista.insert(0,n3)
elif n3 > lista[0] and n3 < lista[1]:
    lista.insert(1,n3)
else:
    lista.append(n3)
print(lista)

n4=int(input('digite um valor:'))
if n4 < lista[0]:
    lista.insert(0,n4)
elif n4 > lista[0] and n4 < lista[1]:
    lista.insert(1,n4)
elif n4 > lista[1] and n4 < lista[2]:
    lista.insert(2,n4)
elif n4 > lista[2] and n4 < lista[3]:
    lista.insert(3,n4)
else:
    lista.append(n4)
print(lista)

n5=int(input('digite um valor:'))
if n5 < lista[0]:
    lista.insert(0,n5)
elif n5 > lista[0] and n5 < lista[1] :
    lista.insert(1,n5)
elif n5 > lista[1] and n5 < lista[2]:
    lista.insert(2,n5)
elif n5 > lista[2] and n5 < lista[3]:
    lista.insert(3,n5)
else:
    lista.append(n5)
    print('valor adicionado no final da lista')
print(lista)


lista=[]
for c in range (5):
    n=int(input(f'digite o {c+1}º valor :'))
    pos=0
    while pos < len(lista) and n > lista[pos]:
        pos+=1
    lista.insert(pos,n)
    print(len(lista))
print(lista)"""
lista=[]
for c in range(0,5):
    n =int(input('digite um valor:'))
    if c == 0 :
        lista.append(n)


