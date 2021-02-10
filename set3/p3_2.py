# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 07/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 2 - Chave de dicionário

def swap(d, k1, k2):
    keep = d[k1]
    d[k1] = d[k2]
    d[k2] = keep
