import random
a = input("digite o nome do aluno 1 para o sorteio :")
b = input("digite o nome do aluno 2 para o sorteio:")
c = input("digite o nome do aluno 3 para o sorteio:")
d = input("digite o nome do aluno 4 para o sorteio:")
lista = [a, b, c, d]
r = random.choice(lista)
print(" o aluno escolhido foi {}".format(r))