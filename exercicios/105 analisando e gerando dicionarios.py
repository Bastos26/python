def notas(*valores,sit = False):
    """notas(*valores, sit=False)
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos(aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma"""
    dicionário={}
    dicionário['total'] = len(valores)
    dicionário['maior'] = max(valores)
    dicionário['menor'] = min(valores)
    #para a média
    total = 0
    for c in valores:
        total = total + c
        dicionário ['média'] = total / dicionário['total']
    if sit == True:
        if dicionário['média'] > 0 and dicionário['média'] <= 5 :
            dicionário['situação'] = 'RUIM'
        if 5 < dicionário['média'] >= 7  :
            dicionário['situação'] = 'REGULAR'
        if 7 < dicionário['média'] >= 10 :
            dicionário['situação'] = 'MUITO BOM'
        print(dicionário)
    else:
        print(dicionário)

notas(10,5,10,10,sit=True)
"""resolução do guanabara
def notas(*n,sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
    
#programa pricipal
resp = notas(5.5,2.5,1.5,sit=True)
print(resp)
help(notas)"""
