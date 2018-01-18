# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(640, 360)
    smooth()
    global angle, aVelocity
    angle = 0.0
    aVelocity = 0.03

def draw():
    background(255)
    global angle, aVelocity
    amplitude = 300
    x = amplitude * sin(angle)
    angle += aVelocity

    fill(127)
    stroke(0)

    translate(width/2, height/2)
    line(0, 0, x, 0)
    ellipse(x, 0, 20, 20)