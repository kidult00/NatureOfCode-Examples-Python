# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Oscillator import Oscillator

# An array of objects

def setup():
    size(640, 360)
    smooth()
    global oscillators
    # Initialize all objects
    oscillators = [Oscillator() for i in range(10)]

def draw():
    background(255)
    global oscillators
    
    for each in oscillators :
        each.oscillate()
        each.display()