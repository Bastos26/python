def area(largura,comprimento):
    total = largura*comprimento
    print(f' a largura {largura} x o comprimento {comprimento} faz com que o terreno tenha {total} metros quadrados')

print('CONTROLE DE TERRENO')
print('-'*30)
l = float(input('Digite a largura (M): '))
c = float(input('Digite o comprimento (M): '))
area(l,c)
#eu estava tentando fazer esse exercicio no meu trabalho e não consegui de imediato
# estava fazendo tudo com se fosse em um laço e estava tendo problemas em como fazer para introduzir os valorer do usuario no programa
#mas ai eu entendi que quando se trata de função , você deve pensar em que , na verdade, está fazendo uma nova função/ferramenta
#então o correto é pensar em programar a ferramenta e depois introduzir ela no código principal
"""resolução do guanabara
def área(larg, comp):
    a = larg * comp
    print(f' A área de um terreno {larg}x{comp} é de {a} metros quadrados.')
    
#programa principal
print('Controle de Terreno')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l,c)"""