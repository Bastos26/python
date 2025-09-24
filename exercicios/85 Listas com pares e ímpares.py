lista1=[]
impar=[]
par=[]
for c in range(0,8):
    n=int(input(f' digite o {c}º numero'))
    lista1.append(n)
for n in lista1:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(sorted(par))
print(sorted(impar))