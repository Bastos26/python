
# OU....
import random
from time import sleep
print("-=-"*50)#isso é só uma maneira de deixar mais estético
print("vamos brincar ..... ")
n1 = int(input("adivinha em que numero , de 1 a 5, eu estou pensando ."))
print("-=-"*50)
print("processando ...")
sleep(2)#isso aqui é só para fazer uma graça , essa biblioteca time e a operação sleep faz com que o computador espero um pouco antes de continuar o código
n2 = random.randint(1,5)
if n1 == n2 :
    print("tu é muito brabo , menó")
else:
    print("burrão, estuda mais ai , man...")
print(" eu pensei no numero {}".format(n2))
print("-=-"*50)

