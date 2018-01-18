# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Ball(object):
    def __init__(self):
        self.position = PVector(100, 100)
        self.velocity = PVector(2.5, 5)
    
    def update(self):
        # Add the current speed to the position
        self.position.add(self.velocity)
    
        if self.position.x > width or self.position.x < 0 :
            self.velocity.x *= -1
        if self.position.y > height or self.position.y < 0 :
            self.velocity.y *= -1
    
    def display(self):
        # Display circle at x position
        stroke(0)
        fill(175)
        ellipse(self.position.x, self.position.y, 16, 16)