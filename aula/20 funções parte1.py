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

def contador(*num): # empacotamento de parâmetros
    for valor in num:
        print(f'{valor} ',end='')
    print('fim')
    tam = len(num)
    print(f'recebi os valores {num} e são ao todo {tam}')
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos=pos + 1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)

def soma(*valores):
    s = 0
    for c in valores:
        s = s + c
    print(f' somando os valores {c} , temos {s}')

soma(5,2)
soma(2,9,4)