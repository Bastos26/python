"""
lista=[]
for numeros in range(0,4):
    n=(int(input('digite um valor:')))
    lista.append(n)
    if numeros == 0:
        maior=menor=n    # essa aqui tá certa mas falta uma coisa....
        maior_indice=menor_indice=0#tem que mostra os indices caso o numero se repita
    if n > maior:
        maior=n
        maior_indice=numeros
    elif n < menor:
        menor=n
        menor_indice=numeros
print(lista)
print(maior,maior_indice)
print(menor,menor_indice)#vamos de novo...."""
lista=[]
maior_ind=[]
menor_ind=[]
for num in range(0,5):
    n=int(input(f'digite o valor em que se deseja por na lista na posição {num}:'))
    lista.append(n)
    if num ==0:
        maior=menor=n

    if n > maior:
        maior=n        # aqui eu corrigi algo referente ao if e o elif
        maior_ind=[num]# o elif só vai ser ativado se o if for verdadeiro
    elif n == maior:   # é uma questão de camadas , se usasse o if duas vezes na condição da condição,
        maior_ind.append(num)# iria alterar o resultado e não iria ajudar
                            # elif só é ativado se o if for verdadeiro
    if n < menor :
        menor=n
        menor_ind=[num]
    elif n == menor:
        menor_ind.append(num)
print(f'o maior numero foi {maior} no indice {maior_ind}')
print(f'o menor numero foi {menor} no indice{menor_ind}')
"""resolução do guanabara
listanum=[]
mai=0
men=0
for c in range(0,5):
    listanum.append(int(input(f'digite um numero para a posição {c}
    if c == 0 :
        mai=men=listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
        men = listanum[c]
print('=-'*30)
print(f'você digitou os valores {listanum}')
print(f' o maior valor digitado foi {mai} nas posições ' end='')
for i,v in enumerate(listanum)
    if v == mai:
        prin(f'{i}...',end='')
print()
print(f' o menor valor digitado foi {men} nas posições ',end='')
for i,v in enumerate(listanum):
    if v == men :
        print(f'{i}...',end='')
print()
o professor usou o método enumerate onde ele vem a ser util justamente nesses casos
ele capita o valor e o indice no msm tempo , então na parte for i,v in enumerate(listanum)
ele está dizendo/atribuindo não só o indice no i (o que já é normal pois na estrutura de repetição
a primeira variavel que colocamos apos o for é referente ao "numero da repetição")mas 
tambem o valor que aquela vez que esta repetindo tambem , ficou mais facil do que a maneira que eu fiz que tambem funcionou        
"""
