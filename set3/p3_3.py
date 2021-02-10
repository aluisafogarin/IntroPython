# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 09/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 3

def dictmap(d, f):
    for key in d:
        d[key] = f(d[key])
