# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(640, 360)
    global angle1, aVelocity1, amplitude1, angle2, aVelocity2, amplitude2
    angle1 = 0
    aVelocity1 = 0.01
    amplitude1 = 300
    angle2 = 0
    aVelocity2 = 0.3
    amplitude2 = 10

def draw():
    background(255)
    global angle1, aVelocity1, amplitude1, angle2, aVelocity2, amplitude2
    
    x = 0
    x += amplitude1 * cos(angle1)
    x += amplitude2 * cos(angle2)
    
    angle1 += aVelocity1
    angle2 += aVelocity2

    ellipseMode(CENTER)
    stroke(0)
    fill(175)
    translate(width/2, height/2)
    line(0, 0, x, 0)
    ellipse(x, 0, 20, 20)