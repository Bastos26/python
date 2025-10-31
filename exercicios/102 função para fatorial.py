def função(num):
    total = 1
    for c in range (num,0,-1):
        total = total * c
        print(f'{c} x',end=' ')
    print('=',total)


função(10)