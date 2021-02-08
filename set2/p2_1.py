# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 05/02/2021
# a193948@dac.unicamp.br

# SET 2 - Problema 1

def square(num):
    return num**2 

def fourth_power(num):
    return square(square(num))
    
def perfect_square(num):
    root = (num ** 0.5)
    root = int(root)

    if root ** 2 == num:
        return True
    else:
        return False

print(square(1))
print(fourth_power(3))
print(perfect_square(0))