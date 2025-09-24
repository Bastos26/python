while True:
    expressão=str(input('digite a expressão:'))
    abertura = expressão.count('(')
    fechamento = expressão.count(')')
    if abertura == fechamento :
        print(' a expressão é aceitável')
    else:
        print('a expressão não é aceitavel')
    desejo = str(input('deseja continuar? (S/N)')).upper().strip()
    if desejo == 'N':
        break
"""
resolução do guanabara 
exp = str(input('digite a expressão:')
pilha=[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão está válida')
else:
    print('sua expressão está errada')"""