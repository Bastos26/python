import random
listatotal=[]
vezes=int(input('digite o numero de jogos que deseja sortear:'))
for c in range(0,vezes):
    n=sorted(random.sample(range(1 ,61),6))
    listatotal.append(n)
for p in listatotal:
    print(p)
