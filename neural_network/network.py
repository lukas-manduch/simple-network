from .layer import Layer
import numpy
from numpy import array

class Network:
    def __init__(self, layers):
        """Constructs neural network, with random weights

        Network size is specified by argument
        :param layers: list of counts nodes for each layer

        """
        self.layers = list()
        for i in range(1, len(layers)):
            self.layers.append(Layer(layers[i-1], layers[i]))

    def train(self, input_values :list, output_values :list):
        if len(input_values) != len(output_values):
            raise Exception("Network train, length of arguments mismatch")

        for i in range(0, len(input_values)): # For each example
            # Evaluate layers values
            values = list() # Outputs
            inputs = input_values[i]
            values.append(inputs)
            for layer in self.layers:
                inputs = layer.eval(inputs)
                values.append(inputs)
            # current_results = array(inputs)
            correct = output_values[i]
            for i in range(len(self.layers) - 1, -1, -1):
                correct  = self.layers[i].train(values[i], values[i+1] - correct)
        ########################################################


    def eval(self, input_values :list) -> list:
        input_values = list(input_values)
        for layer in self.layers:
            input_values = layer.eval(input_values)
        return input_values

if __name__ == "__main__":
    # run unit tests
    pass
