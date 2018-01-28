# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Shape import Shape

class Square(Shape):
    """
    Variables are inherited from the parent.
    We could also add variables unique to the Square class if we so desire
    """
        
    def display(self):
        rectMode(CENTER)
        fill(175)
        stroke(0)
        rect(self.x, self.y, self.r, self.r)
        