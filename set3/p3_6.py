# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 09/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 6 - Máximo de árvore

def binary_tree_max(tree):
    '''
    Cada nó tem 0 ou 2 filhos
    Recebe uma chave e encontra o valor máximo dela

    Caso base -> árvore não ter filhos -> retornar o value

    Caso recursivo -> chamar binary_tree_max recursivamente para encontra o máximo da primeira árvore filha
    Fazer outra chamada recursiva para o máximo da segunda árvore.
        - Possuirá: máximo da árvore, máximo da primeira árvore filha e da segunda
        - Ver qual é o maior 
    '''
    if tree['children'] == []:
        return tree['value']
        
    else:
        l = []
        for element in tree['children']:
            l.append(binary_tree_max(element))
        l.append(tree['value'])

    return max(l, key=int)

def tree_max(tree):
    return binary_tree_max(tree)

