# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 04/03/2021
# a193948@dac.unicamp.br

# SET 1 - Problema 3- divmod
dividend = 7
divisor = 2

def devision_op(dividend, divisor):
    results = []

    if dividend > 0 and divisor > 0:
        quot = 0
        rest = dividend
        while True:
            rest -= divisor 
            quot += 1
            if rest < divisor:
                break
        return quot, rest

out = devision_op(dividend, divisor)
print(out)