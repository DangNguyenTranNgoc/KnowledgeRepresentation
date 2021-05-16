'''
Tritangle Semantic Network
=====
Solution for Tritangle problem using Semantic Network

Element of Tritangle:
-----

- a, b, c: length of edges
- alpha, beta, delta: degrees of each vertex
- higth_c: altitude from vertex C
- square: square of tritangle

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

'''
class TriangleSemanticException(Exception):
    pass

class TriangleSemantic():
    
    def __init__(self) -> None:
        '''
        - a, b, c: length of sides
        - alpha, beta, delta
        - hight_c: altitude from vertex C
        - square
        '''
        self.__a, self.__b, self.__c, self.__alpha, self.__beta, self.__delta, self.__hight_c, self.__square = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

