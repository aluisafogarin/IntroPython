# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 02/02/2021
# a193948@dac.unicamp.br

# SET 0 - Problema 4 Algoritmo de Zeller

year = 2017
month = 1
day = 9

if month == 1 or month == 2:
    year1 = year - 1
    month1 = month + 12

elif month != 1 or month != 2:
    year1 = year
    month1 = month

year2 = year1 % 100
century = year1 / 100

out = round((day + (13 * (month1 + 1))//5 + year2 + year2//4 + century//4 - 2 * century) % 7)
print(out)
# Day = 1 -> domingo, 2 -> segunda ...

