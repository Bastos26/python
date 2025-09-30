ma1 = []
ma2 = []
ma3 = []
matrix = []
soma = par = 0

for c1 in range(0, 3):
    ma1.append(int(input(f'digite o valor :[1,{c1}]')))
for c2 in range(0, 3):
    ma2.append(int(input(f'digite o valor : [2,{c2}]')))
for c3 in range(0, 3):
    ma3.append(int(input(f'digite o valor : [3,{c3}]')))
matrix = [ma1[:], ma2[:], ma3[:]]

maior = matrix[0][0]

for c in matrix:
    soma = soma + c[2]

    for valores in c:
        if valores > maior:
            maior = valores

        if valores % 2 == 0:
            par = par + valores

print('=-'*50)
print(ma1)
print(ma2)
print(ma3)
print('=-'*50)
print(f'a soma dos valores pares é {par}')
print(f'o maior valor da segunda linha é {maior}')
print(f'a soma dos valores da terceira coluna é {soma}')
"""resolução do guanabara
matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for C in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}: '))
print('-='*30)
for l in range(0,3):
    for c in range(o,3):
        print(f'[{matriz[l][c]:^5}], end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in rage(0,3):
    if c ==0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')"""
