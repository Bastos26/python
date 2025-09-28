lista1=[]
impar=[]
par=[]
for c in range(0,8):
    n=int(input(f' digite o {c}º numero'))
    lista1.append(n)
for n in lista1:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(sorted(par))
print(sorted(impar))
"""resolução do guanabara
núm = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'digite o {c}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
"""

#Na parte de cima ele criou logo uma lista detro da outra
#normalmente criariamos separadamente mas assim parece ser mais rápido
#a parte onde ele colocanúm[0].append(valor), ele quer dizer que
#na primeira lista da lista núm vai receber o valor , ou seja,
#ele está falando em qual das listas internas vai entrar o valor