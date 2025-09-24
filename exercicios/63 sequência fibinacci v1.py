print('SEQUÊNCIA FIBONACCI')
termo=int(input('digite o numero de termos que deseja ver :'))
contador=1
t1=0
t2=1
while contador <=termo:
    contador=contador+1
    t3=t1+t2
    t1=t2
    t2=t3
    print(t1,t2,t3,end=' ')
