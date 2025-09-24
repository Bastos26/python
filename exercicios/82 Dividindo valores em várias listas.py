lista=[]
impar=[]
par=[]
while True:
    n=int(input('digite um valor'))
    lista.append(n)
    desejo=str(input('deseja continuar? (S/N')).strip().upper()
    if n % 2 ==0:
        par.append(n)
        print(par)
    else:
        impar.append(n)
        print(impar)
    if desejo == 'N':
        break
print(f'a lista inteira é {lista}')
print(f'a lista com is numeros pares é {par}')
print(f'a lista com os umeros impares é {impar}')


