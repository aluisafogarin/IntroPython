# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 02/02/2021
# a193948@dac.unicamp.br

# SET 1 - Problema 2.2- Média Geométrica

'''
    Se todos os números da lista tivessem o mesmo valor, 
    qual teria que ser esse valor para se obter o mesmo produto?

    media geometra entre a e b = c 
    distância(c, b) = distância(c, a)
    b / c = c / a 
'''

numbers = [2, 7, 3, 9, 13]

if numbers == []:
    out = None

else:
    count = 0
    for n in numbers:
        if count == 0:
            mult = n
            count += 1
        else:
            print(mult, '*', n)
            mult *= n
            print(mult)

    out = mult ** (1/len(numbers))
    print(out)