# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Sine Wave

from Wave import Wave

def setup():
    size(750, 200)
    # Initialize a wave with starting point, width, amplitude, and period
    global wave0, wave1
    wave0 = Wave(PVector(50, 70), 100, 20, 500)
    wave1 = Wave(PVector(300, 100), 300, 40, 220)
    
def draw():
    background(255)
    # global mover
    # Update and display waves
    wave0.calculate()
    wave0.display()
    wave1.calculate()
    wave1.display()