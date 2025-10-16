a = 4
b = 5
s = a+b
print(s)
a = 8
b = 9
s = a+b
print(s)
a = 2
b = 1
s = a+b
print(s)
#o código acima é algo que é nitidamente cansativo de se escrever
#aqui em baixo vemos um exemplo de como uma finção pode os ajudar
def soma(a,b):
    s = a + b       # os parâmetros formais são A e B
    print(s)        # os argumnetos são os valores que colocamos abaixo

soma(4,5)  # tambem pode ser soma(a=4, b=5) deixando explicito e poderia mudar de lugar tbm (soma(b=5,a=4)
soma(8,9)  #obs: se você for explicitar , tem que fazer com todos os argumentos
soma(2,1)

