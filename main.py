from neural_network.network import Network

# First lets create network for xor
nn = Network([3, 4,  1])
#print(nn.eval([1, 1]))

nn = Network([2, 4, 1])
print(nn.eval([1, 1]))
inputs = [[0,0], [0,1] , [1,0], [1, 1]]
outputs = [0, 1, 1, 1]

for i in range(0, 8000):
    nn.train(inputs, outputs)

print(nn.eval([1,1]))
print(nn.eval([0,0]))

print(nn.eval([ 1,0]))
print(nn.eval([ 0,1]))
