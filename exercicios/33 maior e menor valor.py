v1=float(input("digite o primeiro valor:"))
v2=float(input("digite o segundo valor:"))
v3=float(input("digite o terceiro valor:"))
"""if v1>=v2 and v1>=v3:
    print("o maior valor é ",v1)
if v2>=v1 and v2>=v3:
    print("o maior valor é" ,v2)
if v3>=v1 and v3>=v2:
    print("o maior valor é ",v3)
                                  # essa foi a solução que eu criei
    print("o menor é" ,v1)
if v2<=v1 and v2<=v3:
    print("o menor valor é" ,v2)
else :
    print("o menor valor é ",v3)

if v1<=v2 and v1<=v3:
    print("o menor valor é" ,v1)
if v2<=v1 and v2<=v3:
    print("o menor valor é" ,v2)
if v3<=v1 and v3<=v2 :
    print("o menor valor é ",v3)"""

menor = v1
if v2<v1 and v2<v3:
 menor=v2
if v3<v1 and v3<v2:
 menor=v3
print(menor)
                #resolução do professor
                #A utilidade das condições simples e compostas que vimos na aula
                #tambem pode ser aplicado no sentido do PORÉM , como visto aqui
                #eu digo que , se determinado cenário acontecer, é para dar preferência
                #a determinado modus operante.Consegue entender?
maior = v1
if v2>v1 and v2>v3:
 maior =v2
if v3>v1 and v3>v2:
 maior =v3
print(maior)
