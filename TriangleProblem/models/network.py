class NetWorkException(Exception):
    @classmethod
    def throw(cls, ex):
        raise ex
'''
       | (1) | (2) | (3) | (4) | (5) | (6) 
alpha  | -1  |  0  |  0  | -1  |  0  |  0 
beta   | -1  | -1  |  0  | -1  |  0  |  0 
delta  |  0  | -1  |  0  | -1  |  0  |  0 
a      | -1  |  0  | -1  |  0  |  0  | -1 
b      | -1  | -1  | -1  |  0  |  0  | -1 
c      |  0  | -1  | -1  |  0  | -1  | -1 
square |  0  |  0  | -1  |  0  | -1  |  0 
hc     |  0  |  0  |  0  |  0  | -1  |  0 
p      |  0  |  0  | -1  |  0  |  0  | -1 
'''
class Network:
    def __init__(self, network=None):
        if network:
            if Network.is_valid_network(network):
                self.__network = network
            else :
                raise NetWorkException("Invalid network!")
        network = [[0 for i in range(6)] for j in range(9)]
        network[0][0], network[1][0], network[3][0], network[4][0] = [-1] * 4
        network[1][1], network[2][1], network[4][1], network[5][1] = [-1] * 4
        network[3][2], network[4][2], network[5][2], network[6][2], network[8][2] = [-1] * 5
        network[0][3], network[1][3], network[2][3] = [-1] * 3
        network[5][4], network[6][4], network[7][4] = [-1] * 3
        network[3][5], network[4][5], network[5][5], network[8][5] = [-1] * 4
        self.__network = network
    
    @property
    def network(self):
        return self.__network
    
    @network.setter
    def network(self, network):
        self.__network = network.network
    @classmethod
    def is_valid_value(cls, value: int, is_element: bool = False) -> bool:
        '''
        Check if the value is valid for the network
        Parameters
        ----------
        value: int
            The value needed to check
        is_element: bool
            Flag for the element if it is realted to the expression
        '''
        if is_element:
            return value == -1 or value == 1
        return value == 0
    @classmethod
    def is_valid_network(cls, network: list) -> bool:
        '''
        Check if the list is valid for the network
        Parameters
        ----------
        network: list
            The list to be checked
        '''
        is_valid = (type(network) == list)
        if not is_valid:
            return False
        
        is_valid = (len(network) == 9 and len(network[0]) == 6)
        if not is_valid:
            return False
        e_x = [0, 1, 3, 4, 
               1, 2, 4, 5,
               3, 4, 5, 6, 8,
               0, 1, 2,
               5, 6, 7,
               3, 4, 5, 8]
        e_y = [0, 0, 0, 0,
               1, 1, 1, 1,
               2, 2, 2, 2, 2,
               3, 3, 3,
               4, 4, 4,
               5, 5, 5, 5]
        
        ne_x = [2, 5, 6, 7, 8,
                0, 3, 6, 7, 8,
                0, 1, 2, 7,
                3, 4, 5, 6, 7, 8,
                0, 1, 2, 3, 4, 8,
                0, 1, 2, 6, 7]
        
        ne_y = [0, 0, 0, 0, 0,
                1, 1, 1, 1, 1,
                2, 2, 2, 2,
                3, 3, 3, 3, 3, 3,
                4, 4, 4, 4, 4, 4,
                5, 5, 5, 5, 5]
        e_valid = sum([Network.is_valid_value(network[e_x[i]][e_y[i]], is_element=True) for i in range(23)])
        ne_valid = sum([Network.is_valid_value(network[ne_x[i]][ne_y[i]]) for i in range(31)])
        return e_valid == 18 and ne_valid == 22 and is_valid
    def __active_element(self, row: int, col: list):
        for i in range(len(col)):
            self.network[row][col[i]] = 1
    def activate_element(self, element: int):
        '''
        Activate element on network.
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
            9: p: semi-perimeter of triangle
        '''
        switcher = {
            1: lambda: self.__active_element(0, [0, 3]),
            2: lambda: self.__active_element(1, [0, 1, 3]),
            3: lambda: self.__active_element(2, [1, 3]),
            4: lambda: self.__active_element(3, [0, 2, 5]),
            5: lambda: self.__active_element(4, [0, 1, 2, 5]),
            6: lambda: self.__active_element(5, [1, 2, 4, 5]),
            7: lambda: self.__active_element(6, [2, 4]),
            8: lambda: self.__active_element(7, [4]),
            9: lambda: self.__active_element(8, [2, 5])
        }
        func = switcher.get(element, lambda: NetWorkException.throw(ValueError('Invalid argument')))
        
        return func()
    
    def get_unknown_element(self, expression: int) -> int:
        '''
        Get unknown element. If the elements greater than 1 (cannot calculated), return -1. 
        If the expression is calculated, return 0.
        Parameters
        ----------
        expression: int
            The index of each expression.
        
        Returns
        -------
        int:
            The index of the element (start from 1).
        '''
        pos = -1
        expression -= 1
        for i in range(9):
            if self.network[i][expression] == -1:
                if pos == -1:
                    pos = i
                else:
                    return -1
        
        return pos + 1
    def __str__(self) -> str:
        s = ''
        for line in self.network:
            s += '\t'.join(map(str, line))
        return s