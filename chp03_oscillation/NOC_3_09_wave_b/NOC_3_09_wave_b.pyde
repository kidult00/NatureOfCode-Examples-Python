# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(250, 200)
    smooth()
    global startAngle, angleVel
    startAngle = 0.0
    angleVel = 0.2

def draw():
    background(255)
    stroke(0)
    fill(0, 50)
    strokeWeight(2)
    
    global startAngle, angleVel
    startAngle += 0.015
    angle = startAngle
    
    for x in range(0, width+1, 24):
        y = map(sin(angle), -1, 1, 0, height)
        ellipse(x, y, 48, 48)
        angle += angleVel