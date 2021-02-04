# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 03/02/2021
# a193948@dac.unicamp.br

# SET 1 - Problema 4.2 - Cálculo Polinomial, Integrais

poly = [0, 0, 1/2] # polinômio 1x²/2
out = []
new_out = []
const = 'c'

for index, number in enumerate(poly):
    
    if index == 0:
        out.append(const)

    num_inte = number / (index + 1)
    index_inte = index + 1 
    #print("number ", number, "->", num_inte, "exp", index_inte)
    out.append(num_inte)
    print(out)