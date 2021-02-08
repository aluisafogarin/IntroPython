# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 05/02/2021
# a193948@dac.unicamp.br

# SET 2 - Problema 3 


def ndoors(num):
    doors = []
    open_doors = []

    for i in range(0, num):
        doors.append(False)
    
    for m in range(1, num + 1):
        for k in range(0, num):
            if (k + 1) % m == 0:
                if (doors[k]) == False:
                    doors[k] = True
                else:
                    doors[k] = False
    
    for k in range(0, num):
        if doors[k] == True:
            open_doors.append(k + 1)
    
    return open_doors