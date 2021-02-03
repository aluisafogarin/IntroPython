# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 02/02/2021
# a193948@dac.unicamp.br

# SET 0 - Problema 3 - Conta de Energia

# 0 - 500 kWh = 0.45
# 500 - 1500 kWh = 0.74
# 1500 - 2500 kWh = 1.25
# > 2500 = 2.00

# Taxa adicional 20%

kwh_used = 1700

tax1 = 0.45
tax2 = 0.74
tax3 = 1.25
tax4 = 2
addTax = 0.2

kwhValue = kwh_used
energyBill = 0

if kwhValue > 2500:
    kwhCalculated = kwhValue
    kwhCalculated -= 2500
    energyBill += kwhCalculated * tax4
    kwhValue = 2500

if kwhValue > 1500 and kwhValue <= 2500:
    kwhCalculated = kwhValue
    kwhCalculated -= 1500
    energyBill += kwhCalculated * tax3
    kwhValue = 1500

if kwhValue > 500 and kwhValue <= 1500:
    kwhCalculated = kwhValue
    kwhCalculated -= 500
    energyBill += kwhCalculated * tax2
    kwhValue = 500

if kwhValue <= 500:
    energyBill += kwhValue * tax1

energyBill += energyBill * addTax
out = energyBill
print(out)