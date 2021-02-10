# Thays Rodrigues 
# SET 3 - Problema 3_1
def is_flat(lista):
    for element in lista:
        if type(element) == list(element): 
            return False
    return True

def flatten_list(lista):
    out = []
    for element in lista:
        if type(element) != list:
            out.append(element)
        else:
            flat = flatten_list(element)
            for element_2 in flat:
                out.append(element_2)
    return out

def run_length_encode_2d(array):
    out = []
    count = 1

    lista = flatten_list(array)

    for indice in range(1, len(lista)):
        if indice < len(lista):
            if lista[indice] == lista[indice - 1]:
                count += 1
            else:
                out.append((count, lista[indice - 1]))
                count = 1
    
    out.append((count, lista[len(lista) - 1]))
    return out