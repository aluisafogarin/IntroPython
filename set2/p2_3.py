# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 05/02/2021
# a193948@dac.unicamp.br

# SET 2 - Problema 3 


def ndoors(num):
    count = 0
    doors = []
    open_doors = []

    for i in range(0, num):
        doors.append([i+1, False])
        
    for m in range(1, num + 1):
        for k in range(0, num):
            if doors[k][0] % m == 0:
                if doors[k][1] == True:
                    doors[k][1] = False
                else:
                    doors[k][1] = True
    
    for k in range(0, num):
        if doors[k][1] == True:
            open_doors.append(doors[k][0])
    
    return open_doors
