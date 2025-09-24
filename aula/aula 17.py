teste1 = list()
teste1.append('gustavo')
teste1.append(40)
galera = list()
galera.append(teste1) #fazendo sem o [:]
teste1[0]='maria'
teste1[1]=22
galera.append(teste1)
print(galera)

teste2=list()
teste2.append('gustavo')
teste2.append(40)
print(teste2)
galera = list()
galera.append(teste2[:])#fazendo com [:]
teste2[0]='maria'
teste2[1]=22
galera.append(teste2[:])
print(teste2)
print(galera)
"""as listas são mutaveis ao contrario das tuplas então vemos esses cenários algumas vezes e devemos ter atenção
   quando queremos fazer copias de listas apenas copiamos "normalmente mas esquecemos de que criamos um elo 
   igual o que aconteceu com o teste1 em cima 
   para contornar isso , o uso do sinal [:] é importante, pois como esta no exemplo do teste2,o valor antigo e o valor novo 
    se encontram na lista sendo duas listas
    a cada vez que fazemos uma copia da uma determinada lista , fazemos uma especie de registro de todos os valores que ele
    já veio a ter 
    no exemplo do teste2, um momento a lista 2 é composta por guanabara 40 e depois por somente maria 22
    mas como foi feito a copia em dois momentos , ele registrou o guanabara 40 e a maria 22
    assim como tá no exemplo """

exemplo = [['maria',22],['yuri',29],['ana',11],]
print(exemplo[0])
print(exemplo[1][0])
"""
como vimos na aula , este meio de fatiamneto faz com que venhamos a conseguir
navegar nas listas dentro da lista"""
for p in exemplo:
    print(p)
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade')
"""o for é muito util e no quesito de listas compostas tambem
no primeiro pedimos para retornar todos os valores da lista principal
no caso só apareceu as listas que estava na lista principal
e o print(p[0]) estamos pedido para ele mostrar somente os 
 nomes das listas , no caso todos os indices 0 das listas secundarias
 talvez essa questão de lista principal e secundaria ajude """
"""
galera=list()
dado=list()
totmai=totmen=0
for c in range(0,3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade:')))
    galera.append(dado[:])
    dado.clear
    
for p i galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen+=1

print(f' temos {totmai} maiores e {totmen} menores de idade.')

a importancia do clear novamente , a cada ciclo , é como se ele fizesse uma copia
e a colocasse na outra lista, os valores ficam duplicados se não 
utilizar o clear no momento certo"""