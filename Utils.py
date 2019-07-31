from Point import Point

def initialize1DArray(numberOfInputs):
    array = []
    for x in xrange(numberOfInputs):
        array.append(0)
    return array

def initialize1DArrayRandom(numberOfInputs, low, high):
    array = []
    for x in xrange(numberOfInputs):
        array.append(random(low, high))
    return array

def initializeRandomPoint(highX, highY):
    return Point(random(0, highX), random(0, highY))

def sign(input):
    if (input >= 0):
        return 1
    else:
        return -1
