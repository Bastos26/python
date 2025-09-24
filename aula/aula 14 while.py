for c in range(1,10):
    print(c)  #versão antigo com a estrutura de repetição FOR
print('fim')
c=1
while c < 10 :# aqui diz , em outras palavras , enquanto o contador(c) não chegar a 10 :
    print(c)
    c=c+1 # ou c+=1
print('fim')

n = 1
while n != 0:
    n = int(input('digite um valor :'))#aqui eu digo para ele ir repetindo até o usuário inserir o numero 0, enquanto não acontecer, ele vai repetir
print('fim')

r = 'S'
while r =='S':
    n = int(input('digite um valor:'))
    r = str(input('deseja continuar?[S/N')).upper()
print('fim')  # aqui estou fazendo para que ele vá atribuindo um valor numero e , se quiser contiuar, ele continua mas se não , assim que ele colocar , , o programa para

n = 1
par=0 # ou pode ser tambem par=impar=0
impar=0
while n != 0 : # (enquanto for colocado numeros diferentes de 0 , ira continuar) é mais ou menos isso que o computador fala
    n = int(input('digite um valor:'))
    if n % 2 ==0:
        par=par+1#ou par+=1
    else:
        impar=impar+1 # ou impar+=1
print('em todas as vezes , teve {} numeros pares e {} numeros impares'.format(par,impar))
