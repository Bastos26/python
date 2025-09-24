print("aqui iremos entender um pouco sobre os triângulos")
print("Para formar um triângulo, a soma de quaisquer lado deve sempre ser maior que o terceiro ")
a1=float(input("digite o primeiro ângulo:"))
a2=float(input("digite o segundo ângulo:"))
a3=float(input("digite o terceiro ângulo:"))
if a1 + a2 > a3 and a2 + a3 > a1 and a1 + a3 > a2:
    print("acertou")
else:
    print("erro")
