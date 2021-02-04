# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 03/02/2021
# a193948@dac.unicamp.br

# SET 1 - Problema 5 - Festa da Pizza
size = 'small'
toppings = ['presunto', 'abacaxi']

if size == 'small':
    base_value = 14
elif size == 'medium':
    base_value = 16
else:
    base_value = 18

for n, flavor in enumerate(toppings):
    m = len(flavor)
    porcent = (12 + n + m)/100# 12 + n + m (%)
    price_flavor = base_value * porcent
    base_value += price_flavor

if 'bacon' in toppings:
    base_value += 0.1 * base_value

if 'anchovas' in toppings:
    base_value += 0.1 * base_value

out = base_value
print(out)


