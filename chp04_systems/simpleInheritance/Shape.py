# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Example 22-1: Inheritance

class Shape(object):
    def __init__(self, x_, y_, r_):
        self.x = x_
        self.y = y_
        self.r = r_
        
    def jiggle(self):
        self.x += random(-1, 1)
        self.y += random(-1, 1)
        
    # A generic shape does not really know how to be displayed. 
    # This will be overridden in the child classes.
    def display(self):
        point(self.x, self.y)