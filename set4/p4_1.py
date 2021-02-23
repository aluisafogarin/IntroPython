# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 10/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 1 Armazem

'''
    Sistema de contabilidade de armazém
        - Estoque para um conjunto de mercadorias 
        - Transações de recebimento / envio de mercadoria 

'''

class Warehouse:
    def __init__(self):
        self.stock = {}

    def process(self, transaction):
        '''
        Realiza as operações de recebimento e envio de produtos
        '''
        warehouse_process(self.stock, transaction)
    
    def lookup(self, item):
        '''
        Retorna o suprimento total atual para uma determinada mercadoria
        '''
        if item in self.stock.keys():
            return self.stock[item]
        else:
            return 0

def warehouse_process(stock, transaction):
    '''
    Modifica o dicionário de acordo com a transação envio / recebimento
    - Recieve:
        - Se mercadoria não está no estoque (stock), adicioná-la
        - Se estiver, adicionar a quantidade à quantidade já existente
    - Ship:
        - Se não houver quantidade suficiente, enviar todas as disponíveis e imprimir 'not enough'
    '''
    if transaction[0] == 'receive':
        if transaction[1] in stock.keys():
            stock[transaction[1]] += transaction[2]
        else:
            stock[transaction[1]] = transaction[2]

    elif transaction[0] == 'ship':
        if transaction[1] in stock.keys():
            if transaction[2] > stock[transaction[1]]:
                stock[transaction[1]] = 0
                print("not enough")
            else:
                stock[transaction[1]] -= transaction[2]
        else:
            print("product not found")
    else:
        print("invalid transaction")