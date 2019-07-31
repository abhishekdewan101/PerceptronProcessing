class Color(object):
    
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        
    def display(self):
        fill(self.red, self.green, self.blue)
