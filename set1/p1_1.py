# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 04/03/2021
# a193948@dac.unicamp.br

# SET 1 - Problema 1 - Juros Compostos
import math

interest_rate = 0.2 # Taxa de juros composto (de 0 a 1) 

def yearsDoubleValue(interest_rate):
    if interest_rate == 0.0:
        out = "NEVER" # Número mínimo de anos até o dinheiro dobrar 

    else:
        years = (72 / (interest_rate * 100)) # 72 / % juros
    return years

out = yearsDoubleValue(interest_rate)
out = round(out)
print(out)
