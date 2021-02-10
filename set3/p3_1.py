# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 07/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 1 - Run Length

def is_flat(x):
    # Retorna True se a lista x é plana, do contrário False
    for i in x:
        if type(i) == list(i):
            return False
    return True

def flatten_list(x):
    out = []
    for e in x:
        if type(e) != list:
            out.append(e)
        else:
            f = flatten_list(e)
            for e2 in f:
                out.append(e2)
    return out

def run_length_encode_2d(array):
    compact_list = []
    frequency = 1
    prev_element = None

    flatten_array = flatten_list(array)

    for index in range(1, len(flatten_array)):
        if index < len(flatten_array):
            
            if flatten_array[index] == flatten_array[index - 1]:
                frequency += 1
            else:
                compact_list.append((frequency, flatten_array[index - 1]))
                frequency = 1
    compact_list.append((frequency, flatten_array[len(flatten_array) - 1]))

    return compact_list
