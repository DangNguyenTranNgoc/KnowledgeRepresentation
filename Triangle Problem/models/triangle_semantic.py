from math import (
    asin, 
    sin, 
    sqrt, 
    pi, 
    radians, 
    degrees
)
from .network import Network
'''
Triangle Semantic Network
=====
Solution for Triangle problem using Semantic Network

Element of Triangle:
-----

- a, b, c: length of edges
- alpha, beta, delta: degrees of each vertex
- higth_c: altitude from vertex C
- square: square of triangle

Recipes:)
-----
(1) a/sin(alpha) = b/sin(beta)
(2) c/sin(delta) = b/sin(beta)
(3) square = sqrt(p(p-a)(p-b)(p-c))
(4) alpha + beta + delta = pi
(5) square = 1/2(hc * c)

Optional:
p = (a + b + c)/2

Semantic Network:
-----

       | (1) | (2) | (3) | (4) | (5)
a      | -1  |  0  | -1  |  0  |  0
b      | -1  | -1  | -1  |  0  |  0
c      |  0  | -1  | -1  |  0  | -1
alpha  | -1  |  0  |  0  | -1  |  0
beta   | -1  | -1  |  0  | -1  |  0
delta  |  0  | -1  |  0  | -1  |  0
hc     |  0  |  0  |  0  |  0  | -1
square |  0  |  0  | -1  |  0  | -1

Optimize for searching:

       | (1) | (2) | (3) | (4) | (5)
alpha  | -1  |  0  |  0  | -1  |  0
beta   | -1  | -1  |  0  | -1  |  0
delta  |  0  | -1  |  0  | -1  |  0
a      | -1  |  0  | -1  |  0  |  0
b      | -1  | -1  | -1  |  0  |  0
c      |  0  | -1  | -1  |  0  | -1
square |  0  |  0  | -1  |  0  | -1
hc     |  0  |  0  |  0  |  0  | -1

Pre-conditions:
-----

- Input of 'alpha', 'beta', 'delta' is degree and will be convert to radians.
'''
class TriangleSemanticException(Exception): 
    @classmethod
    def throw(cls, ex):
        raise ex

ANGLE = 180.0
class TriangleSemantic:

    def __init__(self) -> None:
        '''
        - a, b, c: length of sides
        - alpha, beta, delta
        - hight_c: altitude from vertex C
        - square
        '''
        self.__a, self.__b, self.__c, self.__alpha, self.__beta, self.__delta, self.__hight_c, self.__square = [0.0] * 8
        self.__network = Network()

    @property
    def a(self) -> float:
        return self.__a
    
    @a.setter
    def a(self, value: float):
        self.__a = value
    
    @property
    def b(self) -> float:
        return self.__b
    
    @b.setter
    def b(self, value: float):
        self.__b = value

    @property
    def c(self) -> float:
        return self.__c
    
    @c.setter
    def c(self, value: float):
        self.__c = value

    @property
    def alpha(self) -> float:
        '''
        The value of 'alpha' angle in DEGREE
        '''
        return self.__alpha
    
    @alpha.setter
    def alpha(self, value: float):
        self.__alpha = value
    
    @property
    def beta(self) -> float:
        '''
        The value of 'beta' angle in DEGREE
        '''
        return self.__beta
    
    @beta.setter
    def beta(self, value: float):
        self.__beta = value
    
    @property
    def delta(self) -> float:
        '''
        The value of 'delta' angle in DEGREE
        '''
        return self.__delta
    
    @delta.setter
    def delta(self, value: float):
        self.__delta = value
    
    @property
    def hight_c(self) -> float:
        '''
        The altitude from vertex C
        '''
        return self.__hight_c
    
    @hight_c.setter
    def hight_c(self, value: float):
        self.__hight_c = value
    
    @property
    def square(self) -> float:
        '''
        The square of the triangle
        '''
        return self.__square
    
    @square.setter
    def square(self, value: float):
        self.__square = value
    
    @property
    def network(self) -> Network:
        '''
        The semantic network of the triangle problem.
        Default, the unknown elements have value -1; 
        the known elements have value 1; and not related elements have value 0. 
        '''
        return self.__network
    
    @network.setter
    def network(self, network: Network):
        _network = Network(network)
        self.__network = _network

    # For testing
    def __str__(self) -> str:
        network = ''
        for line in self.network.network:
            network += '\t'.join(map(str, line))
            network += '\n'
        return '''
The Triangle semantic network
Length              : a({a}), b({b}), c({c})
Angle               : alpha({alpha}), beta({beta}), delta({delta})
Altitude from c     : hight_c({hc})
The square          : square({s})
The semantic network:
{network}
'''.format(a=self.a, b=self.b, c=self.c, alpha=self.alpha, beta=self.beta, 
delta=self.delta, hc=self.hight_c, s=self.square, network=network)

    def __calculate_1(self, e_not_know: int) -> float:
        '''
        a: [3][j] alpha: [0][j] height_c: [7][j]
        b: [4][j] beta : [1][j] square  : [6][j]
        c: [5][j] delta: [2][j]
        '''
        switcher = {
            # Find alpha
            1: lambda: (asin((self.__b * sin(radians(self.__alpha))) / self.__a) * ANGLE) / pi,
            # Find beta
            2: lambda: (asin((self.__a * sin(radians(self.__beta))) / self.__b) * ANGLE) / pi,
            # Find a
            3: lambda: (self.__b * sin(radians(self.__alpha))) / sin(radians(self.__beta)),
            # Find b
            4: lambda: (self.__a * sin(radians(self.__beta))) / sin(radians(self.__alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()
    
    def __calculate_2(self, e_not_know: int) -> float:
        switcher = {
            # Find alpha
            1: lambda: (asin((self.__b * sin(radians(self.__alpha))) / self.__a) * ANGLE) / pi,
            # Find beta
            2: lambda: (asin((self.__a * sin(radians(self.__beta))) / self.__b) * ANGLE) / pi,
            # Find a
            3: lambda: (self.__b * sin(radians(self.__alpha))) / sin(radians(self.__beta)),
            # Find b
            4: lambda: (self.__a * sin(radians(self.__beta))) / sin(radians(self.__alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()
    
    def __calculate_3(self, e_not_know: int) -> float:
        switcher = {
            # Find alpha
            1: lambda: (asin((self.__b * sin(radians(self.__alpha))) / self.__a) * ANGLE) / pi,
            # Find beta
            2: lambda: (asin((self.__a * sin(radians(self.__beta))) / self.__b) * ANGLE) / pi,
            # Find a
            3: lambda: (self.__b * sin(radians(self.__alpha))) / sin(radians(self.__beta)),
            # Find b
            4: lambda: (self.__a * sin(radians(self.__beta))) / sin(radians(self.__alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()
    
    def __calculate_4(self, e_not_know: int) -> float:
        switcher = {
            # Find alpha
            1: lambda: (asin((self.__b * sin(radians(self.__alpha))) / self.__a) * ANGLE) / pi,
            # Find beta
            2: lambda: (asin((self.__a * sin(radians(self.__beta))) / self.__b) * ANGLE) / pi,
            # Find a
            3: lambda: (self.__b * sin(radians(self.__alpha))) / sin(radians(self.__beta)),
            # Find b
            4: lambda: (self.__a * sin(radians(self.__beta))) / sin(radians(self.__alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()

    def __calculate_5(self, e_not_know: int) -> float:
        switcher = {
            # Find alpha
            1: lambda: (asin((self.__b * sin(radians(self.__alpha))) / self.__a) * ANGLE) / pi,
            # Find beta
            2: lambda: (asin((self.__a * sin(radians(self.__beta))) / self.__b) * ANGLE) / pi,
            # Find a
            3: lambda: (self.__b * sin(radians(self.__alpha))) / sin(radians(self.__beta)),
            # Find b
            4: lambda: (self.__a * sin(radians(self.__beta))) / sin(radians(self.__alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()

    def __calculate_6(self, e_not_know: int) -> float:
        switcher = {
            # Find alpha
            1: lambda: (asin((self.__b * sin(radians(self.__alpha))) / self.__a) * ANGLE) / pi,
            # Find beta
            2: lambda: (asin((self.__a * sin(radians(self.__beta))) / self.__b) * ANGLE) / pi,
            # Find a
            3: lambda: (self.__b * sin(radians(self.__alpha))) / sin(radians(self.__beta)),
            # Find b
            4: lambda: (self.__a * sin(radians(self.__beta))) / sin(radians(self.__alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()

    def __calculate_7(self, e_not_know: int) -> float:
        switcher = {
            # Find alpha
            1: lambda: (asin((self.__b * sin(radians(self.__alpha))) / self.__a) * ANGLE) / pi,
            # Find beta
            2: lambda: (asin((self.__a * sin(radians(self.__beta))) / self.__b) * ANGLE) / pi,
            # Find a
            3: lambda: (self.__b * sin(radians(self.__alpha))) / sin(radians(self.__beta)),
            # Find b
            4: lambda: (self.__a * sin(radians(self.__beta))) / sin(radians(self.__alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()

    def __calculate_8(self, e_not_know: int) -> float:
        switcher = {
            # Find alpha
            1: lambda: (asin((self.__b * sin(radians(self.__alpha))) / self.__a) * ANGLE) / pi,
            # Find beta
            2: lambda: (asin((self.__a * sin(radians(self.__beta))) / self.__b) * ANGLE) / pi,
            # Find a
            3: lambda: (self.__b * sin(radians(self.__alpha))) / sin(radians(self.__beta)),
            # Find b
            4: lambda: (self.__a * sin(radians(self.__beta))) / sin(radians(self.__alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()
    
    def get_unknow(self, expression: int) -> int:
        pos = 0
        for i in range(8):
            if self.network[i][expression] == -1:
                if pos == 0:
                    pos = i
                else:
                    return 0
        return pos

