import random
import math
from numpy import random

class Layer:
    """
    Represents one layer of neurons in network.
    """
    def __init__(self, input_size,layer_size):
        layer_size = int(layer_size)
        input_size = int(input_size)
        self.vec = list()
        self.matrix = random.rand(layer_size, input_size)
#        rand_normalize = -1/(math.sqrt(input_size))
#        for i in range(0, abs(num)):
#            self.vec.append(random.random()*2*rand_normalize - rand_normalize)

    def eval(self, input_values :list) -> list:
        return list()