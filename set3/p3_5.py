# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 08/02/2021
# a193948@dac.unicamp.br

# SET 3 - Problema 5 - Cálculo numérico

def approx_derivative(f, x, delta = 1e-6):
    '''
        Retorna a derivada aproximada  de f em x (usando delta como o valor daquele simbolo)
    '''
    return (f(x+delta) - f(x-delta)) / (2 * delta)

def approx_derivative_2(f, delta = 1e-6):
    '''   
        Recebe função f e um número delta, porém deve retornar uma função que representa f'
        A saída deve ser a aproximação de f'(x) 
    '''
    def funcao(x):
        return (f(x+delta) - f(x-delta)) / (2 * delta)

    return funcao

def approx_integral(f, lo, hi, num_regions):
    '''
        Aproxima a integral da função f entre os limites lo e hi
        É preciso dividir a região em várias regiões (definida por num_regions) de tamanhos iguais (em x)
        Aproximar a área sob a curva em cada região usando a regra trapeizoidal e somar as áreas para 
        possuir a paroximação
        b -> max (hi)
        a -> min (lo)
        num_regions -> i 0...n
    '''


    h = (hi - lo) / num_regions

    for k in range(num_regions + 1):
        area = (lo + k * h)

    areas = [(lo + k * h) for k in range(num_regions + 1)]
    results = [f(area) for area in areas]
    return (h / 2) * (results[0] + 2 * sum(results[1:-1]) + results[-1])

print(approx_integral(lambda x: 3*x + 4, 0, 2, 2))