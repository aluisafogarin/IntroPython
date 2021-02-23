# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 12/02/2021
# a193948@dac.unicamp.br

# SET 5 - Problema 2 - Matrizes

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def size(self):
        # Retorna tupla (n_rows, n_cols)
        n_rows = 0
        for row in self.matrix:
            n_rows += 1

        return((n_rows, len(row)))
    
    def get(self, r, c):
        # Retorna o elemento da linha r coluna c
        return self.matrix[r][c]

    def set(self, r, c, val):
        # Define o elemento da linha r coluna c para val (modifica instância)
        self.matrix[r][c] = val

    def row(self, n):
        # Retorna todos os elementos da linha n
        return self.matrix[n]

    def col(self, n):
        # Retorna todos os elementos da coluna n
        new_list = []
        for row in self.matrix:
            for index, element in enumerate(row):
                if index == n:
                    new_list.append(element)
        return new_list

    def transpose(self):
        transpose = [list(line) for line in [*zip(*self.matrix)]]
        return Matrix(transpose)
    
    def __add__(self, other):
        n_rows, n_cols = self.size()
        new_matrix = []
        
        if isinstance(other, Matrix) and n_rows == other.size()[0] and n_cols == other.size()[1]:
            for i in range(n_rows):
                row = []
                for j in range(n_cols):
                    element = self.matrix[i][j] + other.matrix[i][j]
                    row.append(element)
                new_matrix.append(row)
            return Matrix(new_matrix)
        
        elif isinstance(other, int) or isinstance(other, float):
            for i in range(n_rows):
                row = []
                for j in range(n_cols):
                    element = self.matrix[i][j] + other
                    row.append(element)
                new_matrix.append(row)
            return Matrix(new_matrix)

        else:
            return None

    def __sub__(self, other):
        n_rows, n_cols = self.size()
        new_matrix = []
        
        if isinstance(other, Matrix) and n_rows == other.size()[0] and n_cols == other.size()[1]:
            for i in range(n_rows):
                row = []
                for j in range(n_cols):
                    element = self.matrix[i][j] - other.matrix[i][j]
                    row.append(element)
                new_matrix.append(row)
            print(new_matrix)
            return Matrix(new_matrix)
        
        elif isinstance(other, int) or isinstance(other, float):
            for i in range(n_rows):
                row = []
                for j in range(n_cols):
                    element = self.matrix[i][j] - other
                    row.append(element)
                new_matrix.append(row)
            print(new_matrix)
            return Matrix(new_matrix)

        else:
            return None

    def __mul__(self, other):
        n_rows, n_cols = self.size()

        if isinstance(other, Matrix) and n_cols == other.size()[0]:
            new_matrix = []

            for i in range(n_rows):
                new_matrix.append([])
                for j in range(other.size()[1]):
                    mult = [el_1 * el_2 for el_1, el_2 in zip(self.row(i), other.col(j))]
                    new_matrix[i].append(sum(mult))
            return Matrix(new_matrix)

        if isinstance(other, int) or isinstance(other, float):
            new_matrix = []
            for i in range(n_rows):
                row = []
                for j in range(n_cols):
                    element = self.matrix[i][j] * other
                    row.append(element)
                new_matrix.append(row)
            return Matrix(new_matrix)

        else:
            return None
