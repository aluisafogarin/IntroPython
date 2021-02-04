# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 03/02/2021
# a193948@dac.unicamp.br

# SET 1 - Problema 4.1 - Cálculo Polinomial, Derivadas

'''
Calcular a derivada do polinômio fornecido
'''

poly = [0, 0, 1/2] # polinômio 1/2 x² 
out = []

for index, number in enumerate(poly):
    if index == 0:
        pass
    else:
        if index == 1:
            der = number 
        elif index > 1:
            der = number * index
        out.append(der)