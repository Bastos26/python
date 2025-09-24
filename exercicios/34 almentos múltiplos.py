valor=float(input("digite o seu salário:"))
maior=(valor*15)/100
menor=((valor)*10/100)
if valor<1250 or valor == 1250:
    print("você recebe {} e irá passar a receber {:.2f}R$".format(valor,valor+maior))
else:
    print("você recebe {} e irá passar a receber {:.2f}R$".format(valor,valor+menor))
