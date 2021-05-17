from math import (
    asin, 
    sin, 
    sqrt, 
    pi, 
    radians, 
    degrees
)

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

class TriangleSemantic():
    
    def __init__(self) -> None:
        '''
        a: [3][j] alpha: [0][j] height_c: [7][j]
        b: [4][j] beta : [1][j] square  : [6][j]
        c: [5][j] delta: [2][j]
        '''
        self.__a, self.__b, self.__c, self.__alpha, self.__beta, self.__delta, self.__hight_c, self.__square = [0.0] * 8
        self.network = self.__init_network()
    
    def __init_network(self):
        network = [[0.0 for i in range(5)] for j in range(8)]
        network[0][0], network[1][0], network[3][0], network[4][0] = [-1] * 4
        network[1][1], network[2][1], network[4][1], network[5][1] = [-1] * 4
        network[3][2], network[4][2], network[5][2], network[6][2] = [-1] * 4
        network[0][3], network[1][3], network[2][3] = [-1] * 3
        network[5][4], network[6][4], network[7][4] = [-1] * 3

        return network

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

