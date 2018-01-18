# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Mover import Mover

def setup():
    size(640, 360)
    global m, t
    m = Mover()
    t = 0.0
    
    
def draw():
    background(255)
    global m, t
    
    # Perlin noise wind
    wx = map(noise(t), 0, 1, -1, 1)
    wind = PVector(wx, 0)
    t += 0.01
    line(width/2, height/2, width/2+wind.x*100, height/2+wind.y*100)
    m.applyForce(wind)
    
    # Gravity
    gravity = PVector(0, 0.1)
    # m.applyForce(gravity)
    
    # Shake force
    # m.shake()
    
    # Boundary force
    if m.position.x > width - 50 :
        boundary = PVector(-1, 0)
        m.applyForce(boundary)
    elif m.position.x < 50 :
        boundary = PVector(1, 0)
        m.applyForce(boundary)
    
    m.update()
    m.display()
    m.checkEdges()
    
# Instant Force
def mousePressed():
    cannon = PVector.random2D()
    cannon.mult(5)
    m.applyForce(cannon)
