# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 04/03/2021
# a193948@dac.unicamp.br

# SET 1 - Problema 6
import math
p_d = 5

def square_coordinates(p_d):
    coordinates = []
    for x in range(-int(p_d/2), int(p_d/2) + 1):
        for y in range(-int(p_d/2), int(p_d/2) + 1):
            coordinates.append([x,y])

    return coordinates

def square_isin_circle(square, p_d):
    distance = math.sqrt(square[0]**2 + square[1]**2)

    if distance < (p_d/2):
        return True
    else:
        return False

def find_pi(num_cells_circle, num_cells):
    ratio = num_cells_circle / num_cells
    print("Estimate of Ac / As ", ratio)
    return 4 * ratio

coordinates = square_coordinates(p_d)
num_cells_circle = 0

for square in coordinates:
    cells_circle = square_isin_circle(square, p_d)
    if cells_circle == True:
        num_cells_circle += 1

print("Total cells in square", len(coordinates))
print("Cells in circle", num_cells_circle)

out = find_pi(num_cells_circle, len(coordinates))
print("Estimate of pi:", out)
