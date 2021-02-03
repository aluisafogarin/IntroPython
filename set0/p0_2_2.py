# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 02/02/2021
# a193948@dac.unicamp.br

# SET 0 - Problema 2 Parte 2 Raízes Quadrática
a = 1
b = 2
c = 3 

delta = (b * b) - (4 * a * c)

if delta == 0:
    out = (-b + delta ** 0.5) / (2 * a)

else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    out = x1, x2

print(out)