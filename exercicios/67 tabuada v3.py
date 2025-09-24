cont=0
while True:
    tabuada=int(input('quer ver a tabuada de qual valor ?'))
    if tabuada<=0:
        break
    for c in range(1,10+1):
        print(tabuada * c)
print('acabou')
#antes eu estava comentendo um erro que era colocar o break depois do for , fazendo isso , quando digitava os numeros para parar o laço
#ele fazia a tabuada com o numero que era para ser o flag e depois saia do laço . A correção era colocar o break ANTES do for
#Colocar o break antes do for é como dizer: "Ei, antes de fazer qualquer coisa, vamos checar se ainda vale a pena continuar." Enquanto deixar o break depois é como: "Vamos fazer tudo isso... e só depois ver se deveríamos ter feito."