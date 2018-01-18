# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(400, 200)
    smooth()
    # frameRate(60)
    global t
    t = 0.0

def draw():
    background(255)
    global t
    xoff = t  
       
    noFill()
    stroke(0)
    strokeWeight(2)
    beginShape()
    for i in range(width):
        y = noise(xoff) * height
        xoff += 0.01
        vertex(i, y)
    endShape()
    
    t += 0.01