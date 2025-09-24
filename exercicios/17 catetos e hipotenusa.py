import math
co = float(input(" digite o cateto oposto: "))
ca = float(input("digite o cateto adjacente:"))
h = math.hypot(co,ca)
print(" com base nos ângulos digitados , a hipotenusa deste triângulo retângulo é {:.2f}".format(h))