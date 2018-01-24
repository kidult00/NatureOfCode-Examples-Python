# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Sine Wave

from Wave import Wave

def setup():
    size(640, 360)
    # Initialize a wave with starting point, width, amplitude, and period
    global wave0, wave1
    wave0 = Wave(PVector(200, 75), 100, 20, 500)
    wave1 = Wave(PVector(150, 250), 300, 40, 220)
    
def draw():
    background(255)

    # Update and display waves
    wave0.calculate()
    wave0.display()
    wave1.calculate()
    wave1.display()