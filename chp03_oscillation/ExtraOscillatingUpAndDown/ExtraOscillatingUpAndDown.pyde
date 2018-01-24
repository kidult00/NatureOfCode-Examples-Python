# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(400, 400)
    global angle
    angle = 0
    

def draw():
    background(255)
    global angle
    y = 100 * sin(angle)
    angle += 0.02
    
    fill(127)
    translate(width/2, height/2)
    line(0, 0, 0 ,y)
    ellipse(0, y, 16, 16)