print('Vamos formar triângulos')
print('Para formar um trângulo , a soma dos dois lados não pode ser menor q o terceiro lado')
print('Os triânglulos podem ser:\nequiláteros(todos os lados iguais)\nisósceles(dois lados iguais) \nescaleno(todos os lados diferentes)')
print('Vamos formar um triângulo e identifica-lo')
n1 = int(input('Digite o primeiro ângulo:'))
n2 = int(input('Digite o segundo ângulo:'))
n3 = int(input('Digite o terceiro ângulo:'))
if n1+n2>n3 and n2+n3>n1 and n1+n3>n2 :
    print('Os ângulos apresentados formam um triângulo. ')#eu poderia colocar o end='' para colocar o print de baixo na mesma linha
    if n1==n2==n3:
        print('O triângulo é equilatero')
    elif n1!=n2!=n3!=n1:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Os ângulos apresentados não forma um triângulo.')
#se é possivel fazer um if dentro de um if , basta colocar a adentação
#correta . É como se colocasse uma condição dentro de uma condição,
#eu estava tendo dificuldade porque estava aparecendo o tipo de triângulo
#mesmo quando os ângulos não formavam um triângulo, mas desse jeito resolveu.
#primeiro ele analisa se é um triângulo e , se for , ele vai ler qual tipo é.