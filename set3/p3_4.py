# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 09/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 4 - Põe na minha conta

def lend_money(debts, person, amount):
    '''
    Atualiza o dicionário
        - Adiciona novos devedores e suas quantias
        - Adiciona novos valores a devedores já existentes
    '''
    if person in debts.keys():
        debts[person].append(amount)
    else:
        debts[person] = []
        debts[person].append(amount)
    return None

def amount_owed_by(debts, person):
    '''
    Debts descreve as dívidas {pessoa} -> {valor}
    Recebe o nome de uma pessoa e retorna o quanto ela deve
    Se não estiver no dicionário -> retornar 0
    '''
    return consult_dict(debts, person)

def total_amount_owed(debts):
    '''
    Quantia total que lhe é devido, considerando todas as pessoas do dicionário
    '''
    return consult_dict(debts, 'all')

def consult_dict(debts, person): 
    '''
    Consulta a quantidade devida 
        - Se person = 'all' -> retorna a soma de todos os valores
        - Se person in dict -> retorna a soma do valor desta pessoa
        - Se person not in dict -> retorna 0
    '''
    total = 0
    if person == 'all':
        for value in debts.values():
            for money in value:
                total += money
        return total
    elif person in debts.keys():
        for money in debts[person]:
            total += money
        return total
    else:
        return 0





