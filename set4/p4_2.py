# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 10/02/2021
# a193948@dac.unicamp.br

# SET 4 - Problema 2 - Triângulos

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)

class Triangle:
    def __init__(self, point_a, point_b, point_c):
        '''
        Define os vértices do triângulo
        '''
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def side_lengths(self):
        '''
        Calcula e retorna uma tupla com o comprimento dos lados do triângulo
        '''
        return (self.point_a.euclidean_distance(self.point_b),
                self.point_a.euclidean_distance(self.point_c), 
                self.point_b.euclidean_distance(self.point_c)) 

    def angles(self):
        '''
        Retorna uma lista (ou tupla) com os ângulos em radiandos
        '''
        angle_a_b = self.point_a.angle_between(self.point_b)
        angle_a_c = self.point_a.angle_between(self.point_c)
        angle_c_b = self.point_c.angle_between(self.point_b)

        angle_one = abs(angle_a_b - angle_c_b)
        angle_two = abs(angle_a_c - angle_a_b)
        angle_three = math.pi - (angle_one + angle_two)

        return [angle_one, angle_two, angle_three]

    def side_classification(self):
        '''
        Classifica o triângulo em:
            - 'scalene' -> triângulo escaleno
            - 'isosceles' -> triângulo isosceles
            - 'equilateral' -> triângulo equilátero
        '''
        sides = self.side_lengths()
        
        if not math.isclose(sides[0], sides[1]) and not math.isclose(sides[0], sides[2]) and not math.isclose(sides[1], sides[2]):
            return 'scalene'
        elif math.isclose(sides[0], sides[1]) and math.isclose(sides[0], sides[2]) and math.isclose(sides[1], sides[2]):
            return 'equilateral'
        else:
            return 'isosceles'

    def angle_classification(self):
        '''
        'acute' -> acutângulo
        'right' -> retângulo
        'obtuse' -> obtusângulo
        'equitangular'
        '''
        angles = self.angles()
        count_acute = 0
        count_eq = 0
        if self.is_right():
            return 'right'
        
        if math.isclose(angles[0], math.pi/3) and math.isclose(angles[1], math.pi/3) and math.isclose(angles[2], math.pi/3):
            return 'equiangular'
        if angles[0] < (math.pi/2) and angles[1] < (math.pi/2) and angles[2] < (math.pi/2):
            return 'acute'
        if angles[0] > (math.pi/2) or angles[1] > (math.pi/2) or angles[2] > (math.pi/2):
            return 'obtuse'

    def is_right(self):
        '''
        True -> triângulo retângulo, False se não
        '''
        angles = self.angles()
        for angle in angles:
            if angle == (math.pi)/2:
                return True
        
        return False

    def area(self):
        '''
        Calcula e retorna a área do triângulo
        '''
        sides = self.side_lengths()
        semi_perimeter = self.perimeter() / 2
        area = (semi_perimeter 
        * (semi_perimeter - sides[0]) 
        * (semi_perimeter - sides[1]) 
        * (semi_perimeter - sides[2])) ** 0.5
        return area

    def perimeter(self):
        return sum(self.side_lengths())

    def __eq__(self, valueOne, valueTwo):
        return math.isclose(valueOne, valueTwo)
