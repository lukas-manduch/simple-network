import random
import math
from numpy import random
from numpy import dot
from numpy import exp

def _sigmoid(val):
    return 1 / (1 + exp(-val))

class Layer:
    """
    Represents one layer of neurons in network.

    self.matrix - contains values theta, used for evaluation,
    """
    def __init__(self, input_size,layer_size):
        self.layer_size = int(layer_size)
        self.input_size = int(input_size)
        self.matrix = random.rand(self.layer_size, self.input_size)
        # TODO: Instead of "plain" random values initialize it properly
#        rand_normalize = -1/(math.sqrt(input_size))
#        for i in range(0, abs(num)):
#            self.vec.append(random.random()*2*rand_normalize - rand_normalize)

    def eval(self, input_values :list) -> list:
        if len(input_values) != self.input_size:
            raise Exception("Bad input size for layer")
        ret = _sigmoid(dot(self.matrix, input_values))
        return ret

if __name__ == "__main__":
    pass