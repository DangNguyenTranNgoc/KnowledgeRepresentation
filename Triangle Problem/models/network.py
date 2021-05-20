class NetWorkException(Exception):
    @classmethod
    def throw(cls, ex):
        raise ex

class Network:
    def __init__(self, network=None):
        if network:
            if Network.is_valid_network(network):
                self.__network = network
            else :
                raise NetWorkException("Invalid network!")

        network = [[0.0 for i in range(5)] for j in range(8)]
        network[0][0], network[1][0], network[3][0], network[4][0] = [-1] * 4
        network[1][1], network[2][1], network[4][1], network[5][1] = [-1] * 4
        network[3][2], network[4][2], network[5][2], network[6][2] = [-1] * 4
        network[0][3], network[1][3], network[2][3] = [-1] * 3
        network[5][4], network[6][4], network[7][4] = [-1] * 3

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
        is_valid = (len(network) == 8 and len(network[0]) == 5)

        e_x = [0, 1, 3, 4, 
               1, 2, 4, 5,
               3, 4, 5, 6,
               0, 1, 2,
               5, 6, 7]
        e_y = [0, 0, 0, 0,
               1, 1, 1, 1,
               2, 2, 2, 2,
               3, 3, 3,
               4, 4, 4,]
        
        ne_x = [7, 7, 7, 7,
                0, 0, 0,
                2, 2, 2,
                3, 3, 3,
                6, 6, 6,
                1, 1, 
                4, 4, 
                5, 5]
        ne_y = [0, 1, 2, 3,
                1, 2, 4, 
                0, 2, 4, 
                1, 3, 4, 
                0, 1, 3, 
                2, 4, 
                3, 4, 
                0, 3]

        e_valid = sum([Network.is_valid_value(network[e_x[i]][e_y[i]], is_element=True) for i in range(18)])
        ne_valid = sum([Network.is_valid_value(network[ne_x[i]][ne_y[i]]) for i in range(22)])
        return e_valid == 18 and ne_valid == 22 and is_valid

    def __str__(self) -> str:
        s = ''
        for line in self.network:
            s += '\t'.join(map(str, line))
        return s
        