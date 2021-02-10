# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 08/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 7 - Hailstones

def hailstone_sequence(a_0):
    A = []
    A.append(a_0) 
    a = a_0

    while a > 1:
        a = num(a)
        A.append(a) 

    return A

def num(a):
    if a % 2 == 0: # par
        return a/2

    else: # impar
        return (a * 3 + 1)
