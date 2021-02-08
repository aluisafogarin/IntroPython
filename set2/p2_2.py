# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 05/02/2021
# a193948@dac.unicamp.br

# SET 2 - Problema 2

def prime(num):
    count = 0
    if num == 1 or num == 0 or num < 0:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False
    
    else:
        for mult in range(2,num):
            if num % mult == 0:
                count += 1
        if count == 0:
            return True
        else:
            return False
