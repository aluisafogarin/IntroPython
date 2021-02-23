# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 11/02/2021
# a193948@dac.unicamp.br

# SET 4 - Problema 3 - Fração

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator
    
    def to_float(self):
        return self.numerator/self.denominator
    
    def reciprocal(self):
        '''
        Retorna o recíproco desse número como uma instância de Rational
        '''
        return Rational(self.denominator,self.numerator)

    def reduce(self):
        '''
        Retorna o número Rational equivalente, mas reduzido aos termos mais baixos
        Encontrar o máximo divisor comum dos dois números 
        '''
        maximum_divisor = mdc(self.numerator, self.denominator)
        return Rational(self.numerator/maximum_divisor, self.denominator/maximum_divisor)
    
    def __add__(self, other):
        '''
        Retorna a soma da instância original e other
            - Se other for uma instancia de Rational ou Int -> retorna nova instância de Rational
            - Se other foi uma instância de float -> retornar um float
            - Se nao, retornar None
        '''
        if isinstance(other, Rational):
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator).reduce()
        
        if isinstance(other, int):
            new_numerator = self.numerator + (other.numerator * self.denominator)
            return Rational(new_numerator, self.denominator).reduce()
        
        if isinstance(other, float):
            return ((self.numerator/self.denominator) + other)
        
        return None

    def __mul__(self, other):
        '''
        Retorna a multiplicação da instância original e other, mesmas regras do add
        '''
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        
        elif isinstance(other, int):
            return Rational(self.numerator * other, self.denominator)
        
        elif isinstance(other, float):
            return ((self.numerator * other)/self.denominator) 
        
        return None

    def __truediv__(self, other):
        '''
        Retorna o resultado da divisão da instancia original por other, mesma regras de add
        '''
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        
        elif isinstance(other, int):
            return Rational(self.numerator, self.denominator * other)
        
        elif isinstance(other, float):
            return ((self.numerator / self.denominator) / other)  
        
        return None

    def __sub__(self, other):
        '''
        Subtração instancia original e other
        '''
        if isinstance(other, Rational):
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator).reduce()
        
        elif isinstance(other, int):
            return Rational(self.numerator - (other * self.denominator), self.denominator).reduce()
        
        elif isinstance(other, float):
            return ((self.numerator/self.denominator) - other)
        
        return None

def mdc(num1, num2):
    '''
    Calcula o máximo divisor comum entre os números
    '''
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

fracao = Rational(1, 2)
fracao2 = Rational(3, 4)
soma = fracao + fracao2
print(soma.get_numerator(), soma.get_denominator())