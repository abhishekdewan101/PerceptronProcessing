from Point import Point
from Colors import Color
from Perceptron import Perceptron
from Utils import initialize1DArray,initializeRandomPoint

numberOfPoints = 1000
numberOfInputs = 2;
width = numberOfPoints
height = numberOfPoints

perceptron = Perceptron(numberOfInputs)

trainingData = []
for i in range(numberOfPoints - 1):
    trainingData.append(initializeRandomPoint(width, height))
    
for points in trainingData:
    perceptron.train([points.xPos, points.yPos], points.label)

testingData = []
for i in range(numberOfPoints - 1):
    testingData.append(initializeRandomPoint(width, height))

numberOfCorrect = 0
for points in testingData:
    guess = perceptron.guess([points.xPos, points.yPos])
    if (points.label == guess):
        points.setFillColor(Color(0,255,0))
    else:
        points.setFillColor(Color(255,0,0))
        
print(numberOfCorrect)
                                
def setup():
    size(width, height)

def draw():
    for data in testingData:
        data.display() 
