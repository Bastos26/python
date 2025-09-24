print("olá eu sou a GPCeta.Se está aqui é porque quer ver se passou do limite de velocidade ou não ")
print("vale a pena lembrar que , caso tenha passado , a multa é 7 reais para cada km a mais de 80km/h")
velocidade = int(input("qual era a velocidade do veículo ?"))
if velocidade <=80:
    print("não se preocupe , estava dentro do limite de velocidade. Teha um bom dia , piranha!!")
else:
    multa=velocidade-80
    print(" você passou da velocidade permitida . A multa vai ser de {} reais".format(multa*7))
    print("só pra você ficar esperto , teu merda , pega a porra da visão e anda namoral ")
    print("tenha um bom dia ,tmj")
    #refinamento sucessivo é quando você está fazendo uma tarefa e vai resolvendo ele por partes
