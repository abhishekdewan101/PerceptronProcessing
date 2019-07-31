from Colors import Color

class Point(object):
    
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.label = self.calculateLabel()
    
    def calculateLabel(self):
        if (self.xPos > self.yPos):
            self.setFillColor(Color(255,0,0))
            return 1
        else:
            self.setFillColor(Color(0,255,0))
            return -1
    
    def setFillColor(self, fillColor):
        self.fillColor = fillColor;
        
    def display(self):
        self.fillColor.display()
        ellipse(self.xPos, self.yPos, 20, 20);
