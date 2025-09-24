import math
a = float(input("digite um ângulo:"))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(" sobre o ângulo {} , o seno é {:.2f},o cosseno é {:.2f} e a tangente é {:.2f}.".format(a ,sen , cos, t))