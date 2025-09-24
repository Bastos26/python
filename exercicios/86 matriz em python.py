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

print('=-'*50)
print(ma1)
print(ma2)
print(ma3)
print('=-'*50)