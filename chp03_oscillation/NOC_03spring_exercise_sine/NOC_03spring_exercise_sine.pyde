# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(640, 360)
    smooth()
    global angle, aVelocity
    angle = 0.0
    aVelocity = 0.05
    

def draw():
    background(255)
    global angle, aVelocity
    x = width/2
    y = map(sin(angle), -1, 1, 50, 250)
    angle += aVelocity
    
    ellipseMode(CENTER)
    fill(175)
    stroke(0)
    line(x, 0, x, y)
    ellipse(x, y, 20, 20)
    