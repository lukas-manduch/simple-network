from neural_network.network import Network

# First lets create network for xor
nn = Network([2, 4, 1])
print(nn.eval([1, 1]))
inputs = [[0,0], [0,1] , [1,0], [1, 1]]
outputs = [0, 1, 1, 0]

print("Hello Network!")