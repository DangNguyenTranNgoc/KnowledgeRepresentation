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

Optimized:

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
        - height_c: altitude from vertex C
        - square
        '''
        self.__a, self.__b, self.__c, self.__alpha, self.__beta, self.__delta, self.__height_c, self.__square = [-1] * 8
        self.__network = Network()

    @property
    def a(self) -> float:
        return self.__a
    
    @a.setter
    def a(self, value: float):
        self._a = value
        self.network.activate_element(4)
        self.spreading_activation(1)
    
    def set_a(self, value: float):
        self._a = value

    @property
    def b(self) -> float:
        return self.__b
    
    @b.setter
    def b(self, value: float):
        self._b = value
        self.network.activate_element(5)
        self.spreading_activation(1)
    
    def set_b(self, value: float):
        self._b = value

    @property
    def c(self) -> float:
        return self.__c
    
    @c.setter
    def c(self, value: float):
        self._c = value
        self.network.activate_element(6)
        self.spreading_activation(2)

    def set_c(self, value: float):
        self._c = value

    @property
    def alpha(self) -> float:
        '''
        The value of 'alpha' angle in DEGREE
        '''
        return self.__alpha
    
    @alpha.setter
    def alpha(self, value: float):
        self._alpha = value
        self.network.activate_element(1)
        self.spreading_activation(1)
    
    def set_alpha(self, value: float):
        self._alpha = value
    
    @property
    def beta(self) -> float:
        '''
        The value of 'beta' angle in DEGREE
        '''
        return self.__beta
    
    @beta.setter
    def beta(self, value: float):
        self._beta = value
        self.network.activate_element(2)
        self.spreading_activation(1)
    
    def set_beta(self, value: float):
        self._beta = value
    
    @property
    def delta(self) -> float:
        '''
        The value of 'delta' angle in DEGREE
        '''
        return self.__delta
    
    @delta.setter
    def delta(self, value: float):
        self._delta = value
        self.network.activate_element(3)
        self.spreading_activation(2)
    
    def set_delta(self, value: float):
        self._delta = value
    
    @property
    def height_c(self) -> float:
        '''
        The altitude from vertex C
        '''
        return self.__height_c
    
    @height_c.setter
    def height_c(self, value: float):
        self._height_c = value
        self.network.activate_element(8)
        self.spreading_activation(5)
    
    def set_height_c(self, value: float):
        self._height_c = value
    
    @property
    def square(self) -> float:
        '''
        The square of the triangle
        '''
        return self.__square
    
    @square.setter
    def square(self, value: float):
        self._square = value
        self.network.activate_element(6)
        self.spreading_activation(3)
    
    def set_square(self, value: float):
        self._square = value
    
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
        self._network = _network
    
    def set_network(self, network: Network):
        _network = Network(network)
        self._network = _network

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
Altitude from c     : height_c({hc})
The square          : square({s})
The semantic network:
{network}
'''.format(a=self.a, b=self.b, c=self.c, alpha=self.alpha, beta=self.beta, 
delta=self.delta, hc=self.height_c, s=self.square, network=network)

    def __calculate_1(self, e_not_know: int) -> float:
        '''
        (1) a/sin(alpha) = b/sin(beta)
        Calculate:
            - a: (b*sin(alpha))/sin(beta)
            - b: (a*sin(beta))/sin(alpha)
            - alpha: (asin((a*sin(beta))/b)*180)/pi
            - beta: (asin((b*sin(alpha)/a)*180)/pi
        
        Parameters
        ----------
        e_unknow: int
            Element not known and need to be calculated
            Input should within:
            1: Calculate a
            2: Calculate b
            3: Calculate alpha (in degree)
            4: Calculate beta (in degree)
        Returns
        -------
        float: 
            Value of c, b delta or beta
        '''
        switcher = {
            1: lambda: (self.a * sin(radians(self.beta))) / sin(radians(self.alpha)),
            2: lambda: (self.b * sin(radians(self.alpha))) / sin(radians(self.beta)),
            3: lambda: (self.b * sin(radians(self.alpha))) / sin(radians(self.beta)),
            4: lambda: (self.a * sin(radians(self.beta))) / sin(radians(self.alpha))
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))
        return func()
    
    def __calculate_2(self, e_unknown: int) -> float:
        '''
        (2) c/sin(delta) = b/sin(beta)
        Calculate:
            - c: (b*sin(delta))/sin(beta)
            - b: (c*sin(beta))/sin(delta)
            - delta: (asin((c*sin(beta))/b)*180)/pi
            - beta: (asin((b*sin(delta)/c)*180)/pi
        
        Parameters
        ----------
        e_unknow: int
            Element not known and need to be calculated
            Input should within:
            1: Calculate c
            2: Calculate b
            3: Calculate delta (in degree)
            4: Calculate beta (in degree)
        Returns
        -------
        float: 
            Value of c, b delta or beta
        '''
        switcher = {
            1: lambda: (asin((self.b * sin(radians(self.alpha))) / self.a) * ANGLE) / pi,
            2: lambda: (asin((self.a * sin(radians(self.beta))) / self.b) * ANGLE) / pi,
            3: lambda: (self.b * sin(radians(self.alpha))) / sin(radians(self.beta)),
            4: lambda: (self.a * sin(radians(self.beta))) / sin(radians(self.alpha))
        }

        func = switcher.get(e_unknown, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))
        return func()
    
    def __calculate_p(self) -> float:
        return (self.a + self.b + self.c) / 2
    
    def __calculate_3(self, e_not_know: int) -> float:
        '''
        (3) square = sqrt(p(p-a)(p-b)(p-c))
        Calculate:
            - a: sqrt((b^2 + c^2) + sqrt((b^2 * c^2) - (4*s^2)))
            - b: sqrt((a^2 + c^2) + sqrt((a^2 * c^2) - (4*s^2)))
            - c: sqrt((b^2 + a^2) + sqrt((b^2 * a^22) - (4*s^2)))
            - square: sqrt(p(p-a)(p-b)(p-c))
        In which: 
            p=(a + b + c)/2
        
        Parameters
        ----------
        e_unknow: int
            Element not known and need to be calculated
            Input should within:
            1: Calculate a
            2: Calculate b
            3: Calculate c
            4: Calculate square
        Returns
        -------
        float: 
            Value of a, b, c or square
        '''
        switcher = {
            1: lambda: 0,
            2: lambda: 0,
            3: lambda: 0,
            4: lambda: sqrt(self.__calculate_p()*(self.__calculate_p()-self.a)*(self.__calculate_p()-self.b)*(self.__calculate_p()-self.__c))/2
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))
        
        return func()
    
    def __calculate_4(self, e_not_know: int) -> float:
        '''
        (3) alpha + beta + delta = pi
        Calculate:
            - alpha: ((pi - beta - delta)*180)/pi
            - beta: ((pi - alpha - delta))*180)/pi
            - delta: ((pi - alpha - beta)*180)/pi
        
        Parameters
        ----------
        e_unknow: int
            Element not known and need to be calculated
            Input should within:
            1: Calculate alpha (in degree)
            2: Calculate beta (in degree)
            3: Calculate delta (in degree)
        Returns
        -------
        float: 
            Value of alpha, beta or delta
        '''
        switcher = {
            1: lambda: ((pi - self.beta - self.delta) * ANGLE) / pi,
            2: lambda: ((pi - self.alpha - self.delta) * ANGLE) / pi,
            3: lambda: ((pi - self.alpha - self.beta) * ANGLE) / pi
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()

    def __calculate_5(self, e_not_know: int) -> float:
        '''
        (4) square = 1/2(hc * c)
        Calculate:
            - square: 0.5*(height_c * c)
            - height_c: (2 * square)/c
            - c: (2 * square)/height_c
        
        Parameters
        ----------
        e_unknow: int
            Element not known and need to be calculated
            Input should within:
            1: Calculate square
            2: Calculate height_c
            3: Calculate c
        Returns
        -------
        float: 
            Value of square, height or c
        '''
        switcher = {
            1: lambda: 0.5*(self.height_c * self.c),
            2: lambda: (2 * self.square)/self.c,
            3: lambda: (2 * self.square)/self.height_c
        }

        func = switcher.get(e_not_know, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))

        return func()

    def get_element_by_index(self, index: int) -> float:
        '''
        Get the value of an element throught index.

        Parameters
        ----------
        element: int
            Index of each element
            1: alpha
            2: beta
            3: delta
            4: a
            5: b
            6: c
            7: square            
            8: height from c vertex
        '''
        switcher = {
            1: self.alpha,
            2: self.beta,
            3: self.delta,
            4: self.a,
            5: self.b,
            6: self.c,
            7: self.square,
            8: self.height_c,
        }

        func = switcher.get(index, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))
        return func()

    def set_e_value_by_index(self, index: int, value: float):
        '''
        Set the value of an element throught index.

        Parameters
        ----------
        element: int
            Index of each element
            1: alpha
            2: beta
            3: delta
            4: a
            5: b
            6: c
            7: square            
            8: height from c vertex
        value: float
            Value of the element
        '''
        switcher = {
            1: lambda: self.set_alpha(value),
            2: lambda: self.set_beta(value),
            3: lambda: self.set_delta(value),
            4: lambda: self.set_a(value),
            5: lambda: self.set_b(value),
            6: lambda: self.set_c(value),
            7: lambda: self.set_square(value),
            8: lambda: self.set_height_c(value)
        }

        func = switcher.get(index, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))
        return func()
    
    def calculate_expression_controller(self, expression: int, element_unknown: int):
        '''
        Calculate an expression and update an unknown element.
        Loop:
            1> Begin from 1.
            2> Find unknown element.
            3> If has, calculate the expression. Go back 1.
            4> Can't calculate the expression (or it is calculated). Go to next expression.

        Parameters
        ----------
        expression: int
            The index of each expression
            1: a/sin(alpha) = b/sin(beta)
            2: c/sin(delta) = b/sin(beta)
            3: square = sqrt(p(p-a)(p-b)(p-c))
            4: alpha + beta + delta = pi
            5: square = 1/2(hc * c)
        element_unk
        '''
        switcher = {
            1: lambda: self.__calculate_1(element_unknown),
            2: lambda: self.__calculate_2(element_unknown),
            3: lambda: self.__calculate_3(element_unknown),
            4: lambda: self.__calculate_4(element_unknown),
            5: lambda: self.__calculate_5(element_unknown)
        }

        func = switcher.get(expression, lambda: TriangleSemanticException.throw(ValueError('Invalid argument')))
        return func()
    
    def spreading_activation(self, expression: int):
        '''
        Calculate an expression and update an unknown element.
        Loop:
            1> Begin from 1.
            2> Find unknown element.
            3> If has, calculate the expression. Go back 1.
            4> Can't calculate the expression (or it is calculated). Go to next expression.

        Parameters
        ----------
        expression: int
            The index of each expression
            1: a/sin(alpha) = b/sin(beta)
            2: c/sin(delta) = b/sin(beta)
            3: square = sqrt(p(p-a)(p-b)(p-c))
            4: alpha + beta + delta = pi
            5: square = 1/2(hc * c)
        '''
        print('Calculated expression: {}'.format(expression))
        unknown_element = self.network.get_unknown_element(expression)
        if unknown_element == -1 or unknown_element == 0:
            return
        
        value = self.calculate_expression_controller(expression, unknown_element)
        if value <= 0:
            return
        self.set_e_value_by_index(unknown_element, value)
        self.network.activate_element(unknown_element)
        print('Calculated element: {}'.format(unknown_element))

        index = 1
        while index <= 5:
            unknown_element = self.network.get_unknown_element(expression)
            if unknown_element == -1 or unknown_element == 0:
                index += 1
                continue

            value = self.calculate_expression_controller(expression, unknown_element)
            if value <= 0:
                return
            self.set_e_value_by_index(unknown_element, value)
            self.network.activate_element(unknown_element)
            print('Calculated element: {}'.format(unknown_element))
     
    def calculate_element(self, element: int) -> float:
        '''
        Return or calculate an elemnt (if not existed).

        Parameters
        ----------
        element: int
            1: alpha
            2: beta
            3: delta
            4: a
            5: b
            6: c
            7: square            
            8: height from c vertex

        Returns
        -------
        float: 
            Value of a, b, c, alpha, beta, delta, height, square or -1 if not calculed
        '''
        value = self.get_element(element)
        if value > 0.0:
            return value
        
        

        return value

