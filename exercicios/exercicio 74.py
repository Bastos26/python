import random
tupla = (1,2,3,4,5,6,7,8,9,10)
numeros = random.sample(tupla,k=5)
numeros = sorted(numeros)
print(numeros)
print(f'o menor numero da lista é {numeros[0]} e o maior é o numero {numeros[4]}')

""" resolução do guanabara:
from random import randint
n = randint(1,10) ->  aqui ele não precisou colocar todos os numeros , bastou colocar 1 e 10 que já se entendeu

obs: randint é o que sorteia o numero do random

numeros = ( randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)) -> aqui ele diz que a tupla é 
composta por 5 numeros aleatorios de 1 a 10(radint(1,10)) 
->se colocar tudo dentro de um parenteses , ele vai passar a receber todos os valores ,logo ,
 ele vai passar a ser uma TUPLA
  
print(f'eu sorteei os numeros :', end = '')
if n in numeros:
    print(f'{n}', end = ''
print(f' \no maior valor sorteado foi {max(numeros)}')
print(f'o menor valor sorteado foi {min(numeros}
obs: max e min são métodos que se estão disponiveis quando se utilizam tuplas,onde sua função é achar o maior valor int e o menor valor int
    """
