# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

class Box(object):
    """A rectangular box"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        
    def display(self):
        fill(127)
        stroke(0)
        strokeWeight(2)
        rectMode(CENTER)
        rect(self.x, self.y, self.w, self.h)