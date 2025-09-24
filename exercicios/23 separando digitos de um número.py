num = int(input("digite um numero de 0 até 9999:"))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000% 10
print("analisando o numero {} podemos dizer que :".format(num))
print(" a unidade é {}".format(u))
print("sua dezena é {}".format(d))
print("sua centena é {}".format(c))
print("e sua milhar é {}".format(m))
