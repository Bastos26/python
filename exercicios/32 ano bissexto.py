import datetime
ano = int(input("digite um ano :"))
if ano==0:
    ano = datetime.date.today().year
if ano%4 ==0 and ano %100 !=0 or ano % 400 ==0:
    print("o ano é BISSEXTO")

else:
    print("o ano não é BISSEXTO")
    #quando estamos falando sobre condições , como o próprio nome diz,ele é uma condição que colocamos no programa ( tipo faça uma coisa se não der , faça outra)
    #na parte onde passamos as exigências dessas condições , parece que só podia passar uma exigência mas na verdade NÃO.
    #utilizando o "and" nós ACRECENTAMOS mais uma exigência nele .
    #e com o "or" colocamos mais ainda
    #obs= sinal de diferente é !=