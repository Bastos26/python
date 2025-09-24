for c in range(1,6):#por mais que tenha colocado de 1 a 6 , ele não considera o último numero , por isso que só tem 5 oi
    print('oi')
print('fim')
# a adentação é algo muito importate, é através dele que sabemos se alguma coisa tá intrelaçada(aninhada) a outra ou não , igual o que vimos no html
for c in range(0,6):
    print(c)# aqui ele vai começar a contar
print('fim')
for c in range(6,0):
    print(c)# aqui é o que se faria supostamente caso quisesse fazer uma contagem decrescente mas isso não iria funcionar
print('fim')
for c in range (6,0,-1):
    print(c)# agora sim ele vai contar do 6 até o 0
print('fim')
for c in range(0,7,2):
    print(c)# com a mesma dinâmica do fatiamento na manipulação de texto, aqui, graças a esse 2, ele vai retornar numeros de 2 em 2
print('fim')
n = int(input('digite um número:'))
for c in range (0,n+1):#fiz isso pq , como disse antes, ele não conta o último numero , então com esse +1 ele vai contar de fato até o número q você desejar
    print(c)
print('fim')

for c in range (0,3):
    n = int(input('digite um número:'))
print('fim')
s=0
for c in range (0,3):
    n = int(input('digite um número:'))
    s = s + n # ou s += n , o pycharm tbm pode ler assim
print(s)








i = int(input('digite o número de início:'))
f = int(input('digite o fim :'))
pulo =str(input('gostario de que ele pulasse ?(sim ou não'))
if pulo == 'sim' :
    p=int(input('digite o número de intevalos que deseja: '))
    for c in range (i,f+1,p):
        print(c)
else:
    for c in range (i,f):
        print(c)
