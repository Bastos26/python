lista1= list()
lista2=list()
maior=[]
menor=[]
contador=0
while True:

    nomes=str(input('nome:'))
    lista1.append(nomes)
    pesos=int(input('peso:'))
    lista1.append(pesos)
    lista2.append(lista1[:])
    lista1.clear()

    contador=contador+1
    if contador == 1:
        pesado=leve=pesos

    desejo=str(input('desejar continuar ? (S/N)')).strip().upper()
    if desejo == 'N':
        break

for c in lista2:
    if c[1] > pesado:
        pesado=c[1]
        maior.clear()
        maior.append(c[0])
    elif c[1] == pesado:
        maior.append(c[0])

    if c[1] < leve:
        leve=c[1]
        menor.clear()
        menor.append(c[0])
    elif c[1] == leve:
        menor.append(c[0])

print(f'foram {contador} nomes e pesos inseridos')
print(f'o maior peso registrado foi {pesado}KG de {maior}')
print(f'o menor peso registrado foi {leve}KG de {menor}')




# o problema desta parte era que , conforme
#fosse colocando os valores, ele não iria fazendo
#novas listas, apenas inserindo tudo em um
# através disso aqui , eu faço uma copia da lista 1 na lista 2 em cada ciclo
#e apago com o clear, assim , em cada ciclo,ele faz uma lista nova
#ex:se tirasse o clear e fiz fizesse o exemplo colocando a 1 , b 2 e c 3 (tres ciclos)
#iria ficar [['a ', 1], ['a ', 1, 'b ', 2], ['a ', 1, 'b ', 2, 'c ', 3]]
#porque no primeiro ciclo a lista 1 tinha a1, depois no segundo tinha a1 e b2 e no terceiro tinha a1,b2e c3
"""
e foi a mesma coisa das listas que eu usei para colocar os nomes das pessoas mais pesadas e leves 
eu atualizei as variaveis que usava como referencia , e se os numeros colocados fossem maiores eu atualizava a do peso
, apagava a lista dos nomes e introduzia o nome da pessoa nova que era mais pesada / leve 
e depois usei um elif para só colocar caso o peso maximo seja igual ao peso dessa pessoa
esse custou um pouco rs"""
