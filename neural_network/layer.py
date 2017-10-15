import random
import math
from numpy import random
from numpy import dot
from numpy import exp
from numpy import array
from numpy import transpose

def _sigmoid(val):
    return 1 / (1 + exp(-val))

class Layer:
    """
    Represents one layer of neurons in network.
    self.matrix - contains values theta, used for evaluation,
    """
    layer_size = 0
    input_size = 0
    matrix = array(list())
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

    def train(self, inputs_array :list, errors_array :list) -> list():
        """Sets new values in layer based on error_array

        errors_array: array of error values calculated like
                      layerOutput-desiredOutput

        returns: array of errors which can be used for next layer
                 training

        """
        inputs_array = array(inputs_array)
        errors_array = array(errors_array)
        if len(errors_array) != len(self.matrix):
            raise Exception("Invalid size array passed exp: "
                            + str(len(self.matrix)) + " got " + str(len(errors_array)))
        my_out = self.eval(inputs_array)
        aa = transpose([errors_array]) * transpose([my_out]) * (1 - transpose([ my_out]) )
        self.matrix += 0.1 * dot(aa , array([inputs_array]))
        backprop_errors = dot(errors_array, self.matrix)

        return backprop_errors


    @classmethod
    def __len__(cls):
        return cls.layer_size

if __name__ == "__main__":
    pass
