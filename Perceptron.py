from Utils import initialize1DArrayRandom,sign

class Perceptron(object):
    
    def __init__(self, numberOfInputs):
        self.weights = initialize1DArrayRandom(numberOfInputs, -1, 1)
        print(self.weights)
        
    def guess(self, inputs):
        weightSum = 0
        for i in range(0,len(self.weights)):
            weightSum += inputs[i] * self.weights[i]
        return sign(weightSum);
    
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        for x in range(0,len(self.weights)):
            self.weights[x] += error * inputs[x]
