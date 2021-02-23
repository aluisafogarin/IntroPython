# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 12/02/2021
# a193948@dac.unicamp.br

# SET 5 - Problema 1 - Langton Ant

'''
    1. Mude a cor da célula atual (branco -> preto, preto -> branco)
    2. Avançe uma célula na direção em que está voltada
    3. Mude de direção de acordo com a regra
        - Regra: 'RL'
        - 0 (preto) -> R
        - 1 (branco) -> L

        - Regra: 'RLRR'
        - 0, 2, 3  -> R
        - 1 -> L

    INÍCIO 
    - Comece voltada para norte e na célula central do grid
    - Grid bidmensional tamanho size -> todas células 0

    DICA
    - Será preciso representar a posição da formiga, incluindo o ângulo, para saber como movimentá-la

'''

class Ant:
    def __init__(self, middle):
        self.position = [middle, middle]
        self.orientation = 90 # 0, 90, 180, 270
    
    def rotate(self, direction):
        if direction == 'R':
            self.orientation -= 90
            if self.orientation < 0 and self.orientation >= -360:
                self.orientation = 360 + self.orientation
        
        elif direction == 'L':
            self.orientation += 90
            if self.orientation >= 360:
                self.orientation = 360 - self.orientation

    def walk(self):
        if self.orientation == 0: # Direita
            self.position[1] += 1
        elif self.orientation == 90: # Cima
            self.position[0] -= 1
        elif self.orientation == 180: # Esquerda
            self.position[1] -= 1
        elif self.orientation == 270: # Baixo
            self.position[0] += 1

class Grid:
    
    def __init__(self, rules, size):
        self.grid = []
        self.rules = rules
        self.num_colors = len(self.rules)
        self.rules_color = dict(zip(range(self.num_colors), rules))
        self.size = size
        for cel in range(size):
            self.grid.append([0 for i in range(size)])
    
    def middle_grid(self):
        middle = int((self.size - 1) / 2)
        return middle

# RL -> 0, 1 
    def change_color(self, x, y):
        self.grid[x][y] = (self.grid[x][y] + 1) % self.num_colors
"""         if self.grid[x][y] < self.num_colors - 1:
            self.grid[x][y]+= 1
        else:
            self.grid[x][y] = 0 """

def run_langton(rules, size):
    '''
    Retornar uma tupla (count, grid)
        count: número de passos até a formiga sair da grade
        grid: lista de inteiros representando a coloração final da grade
    '''
    g = Grid(rules, size)
    ant = Ant(g.middle_grid())
    count = 0
    while True:
        g.change_color(ant.position[0], ant.position[1])
        ant.walk()
        count += 1

        if ant.position[0] >= g.size or ant.position[0] < 0:
            break
        if ant.position[1] >= g.size or ant.position[1] < 0:
            break

        direction = g.rules_color[g.grid[ant.position[0]][ant.position[1]]]
        ant.rotate(direction)

    return count, g.grid