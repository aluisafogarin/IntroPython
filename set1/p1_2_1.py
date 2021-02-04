# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 02/02/2021
# a193948@dac.unicamp.br

# SET 1 - Problema 2.1 - Média aritimética

'''
A média aritimética entre dois números a e b é c. 
    distancia(c,b) = distância(c,a) 
    b - c = c - a
'''

numbers = [2, 7, 3, 9, 13]

if numbers == []: 
    out = None

else: 
    sum = sum(numbers) # Pega a soma dos valores da lista

    out = sum(numbers) / len(numbers)
    print(out)