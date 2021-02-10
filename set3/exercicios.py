def is_flat(x):
    # Retorna True se a lista x é plana, do contrário False
    for i in x:
        if type(i) == list(i):
            return False
    return True

def flatten_list(x):
    # Caso recursivo
    out = []
    for e in x:
        if type(e) != list:
            out.append(e)
        else:
            f = flatten_list(e)
            for e2 in f:
                out.append(e2)
    return out

print(flatten_list([1,[2,3,[4]]]))