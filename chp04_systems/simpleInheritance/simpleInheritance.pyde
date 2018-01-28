# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Object oriented programming allows us to define classes in terms of other classes.
# A class can be a subclass (aka " child " ) of a super class (aka "parent").
# This is a simple example demonstrating this concept, known as "inheritance."

from Circle import Circle
from Square import Square

def setup():
    size(200, 200)
    global s, c
    s = Square(75, 75, 10)
    c = Circle(125, 125, 20, color(175))

def draw():
    background(255)
    c.jiggle()
    s.jiggle()
    c.changeColor()
    c.display()
    s.display()
