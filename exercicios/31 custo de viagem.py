distancia = float(input("digite a distância da viagem:"))
if distancia <=150:
    print(" na sua viagem de {}KM ,o valor pendente é {:.2f}R$".format(distancia,distancia*0.5))
else:
    print("na sua vagem de {}KM,o valor pendente é {:.2f}R$".format(distancia,distancia*0.45))