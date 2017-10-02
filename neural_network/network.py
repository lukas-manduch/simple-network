from .layer import Layer

class Network:
    def __init__(self, layers):
        """
        Constructs neural network, with random weights
        Network size is specified by argument
        :param layers: list of counts nodes for each layer
        """
        self.layers = list()
        for i in range(1, len(layers)):
            self.layers.append(Layer(layers[i-1], layers[i]))

    def train(self, input_values :list, output_values :list):
        pass

    def eval(self, input_values :list) -> list:
        input_values = list(input_values)
        for layer in self.layers:
            input_values = layer.eval(input_values)
        return input_list

if __name__ == "__main__":
    # run unit tests
    pass
