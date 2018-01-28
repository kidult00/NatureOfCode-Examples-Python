# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Shape import Shape

class Circle(Shape):

    def __init__(self, x, y, r, c):
        # super(Circle, self).__init__(x, y, r) # Call the parent constructor
        Shape.__init__(self, x, y, r)
        self.c = c  # Also deal with this new instance variable

    # Call the parent jiggle, but do some more stuff too
    def jiggle(self):
        super(Circle, self).jiggle()
        # The Circle jiggles its size as well as its x,y position.
        self.r += random(-1, 1)
        self.r = constrain(self.r, 0, 100)

    # The changeColor() function is unique to the Circle class.
    def changeColor(self):
        self.c = color(random(255), random(255), random(255))
        
    def display(self):
        ellipseMode(CENTER)
        fill(self.c)
        stroke(0)
        ellipse(self.x, self.y, self.r, self.r)