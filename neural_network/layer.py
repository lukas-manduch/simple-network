import random
import math

class Layer:
    """
    Represents one layer of neurons in network.
    """
    def __init__(self, layer_size, input_size):
        layer_size = int(layer_size)
        input_size = int(input_size)
        self.vec = list()
        rand_normalize = -1/(math.sqrt(input_size))
        for i in range(0, abs(num)):
            self.vec.append(random.random()*2*rand_normalize - rand_normalize)
