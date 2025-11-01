def função(num,show=False):
    """fatorial(n,show=false)
        -> Calcula o fatorial de um número.
         :param n: O número a ser calculado
         :param show: (opcional) Mostrar ou não a conta
         :return: O valor do fatorial de um número n"""
    total = 1
    for c in range (num,0,-1):
        total = total * c
        if show == True:
            if c > 1:
                print(f'{c} ',end='x ')
            else:
                print(f'{c} = ', end='')
    print(total)

função(5,True)
"""resolução do guanabara
def fatorial(n,show=False):
    f = 1
    for c in range(n, 0, -1):
        print(c,end='')
        if c > 1:
            print(' x ',end='')
        else:
            print(' = ',end='')
        f *= c
    return f
    
#programa principal
print(fatorial(5,show=True))"""
