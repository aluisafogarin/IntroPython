# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 08/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 8 - Compondo funções

def composite_result(f, g, x):
    return f(g(x))

def composite(f, g):
    def fog(x):
        return f(g(x))
    return fog

#print(composite_result(lambda x: 2*x + 2, lambda x: 5*x, 1))

#calcular = composite(lambda x: 2*x + 2, lambda x: 5*x)
#print(calcular(2))