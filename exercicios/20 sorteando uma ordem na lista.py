import random
a = str (input("digite o nome do candidato 1:"))
b = str (input("digite o nome do candidato 2:"))
c = str (input("digite o nome do candidato 3:"))
d = str (input("digite o nome do candidato 4:"))
lista = [a,b,c,d]
random.shuffle(lista)
print(lista)
