# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 11/02/2021
# a193948@dac.unicamp.br

# SET 4 - Problema 4 - Vetor

class Vector():
    def __init__(self, values):
        self.vector = values 

    def as_list(self):
        return self.vector
    
    def size(self):
        return len(self.vector)

    def magnitude(self):
        mag = 0
        for value in self.vector:
            mag += value ** 2
        return mag ** 0.5
    
    def euclidean_distance(self, other):
        distance = 0
        for element in range(len(self.vector)):
            distance += (self.vector[element] - other.vector[element]) ** 2
        return distance ** 0.5
    
    def normalized(self):
        normalized = []
        for value in self.vector:
            normalized.append(value/self.magnitude())
        return Vector(normalized)

    def cosine_similarity(self, other):
        num = 0
        den = 0
        for element in range(len(self.vector)):
            num += self.vector[element] * other.vector[element]
        den += self.magnitude() * other.magnitude()
        return num/den
    
    def __add__(self, other):
        vector_sum = []
        if isinstance(other, Vector) and len(self.vector) == len(other.vector):
            for element in range(0, (len(self.vector))):
                vector_sum.append(self.vector[element] + other.vector[element])
            return Vector(vector_sum)
        
        if isinstance(other, int):
            return self.vector + other.vector

        else:
            return None
    
    def __sub__(self, other):
        vector_sub = []
    
        if isinstance(other, Vector) and len(self.vector) == len(other.vector):
            for element in range(0, len(self.vector)):
               vector_sub.append(self.vector[element] - other.vector[element])
            return Vector(vector_sub)

        elif isinstance(other, int):
            return self.vector - other.vector

        else:
            return None 
    
    def __mul__(self, other):
        escalar_product = 0

        if isinstance(other, Vector) and len(self.vector) == len(other.vector):
            for element in range(len(self.vector)):
                escalar_product += self.vector[element] * other.vector[element]
            return escalar_product
        
        elif isinstance(other, int) or isinstance(other, float):
            mult_vector = []
            for element in range(len(self.vector)):
                mult_vector.append(self.vector[element] * other)
            return Vector(mult_vector)

        else:
            return None
    
    def __truediv__(self, other):
        div_vector = []
        if isinstance(other, float) or isinstance(other, int):
            for element in range(len(self.vector)):
                div_vector.append(self.vector[element] / other)
            return Vector(div_vector)
        else:
            return None

v = Vector([-3, 3])
print(v.normalized().as_list())