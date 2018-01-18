# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Forces (Gravity and Fluid Resistence) with Vectors 

# Demonstration of multiple force acting on bodies (Mover class)
# Bodies experience gravity continuously
# Bodies experience fluid resistance when in "water"

from Mover import Mover
from Liquid import Liquid

def setup():
    size(450, 450)
    randomSeed(1)
    reset()
    global liquid
    # Create liquid object
    liquid = Liquid(0.0, height/2, width, height/2, 0.1)
    
    
def draw():
    background(255)
    
    global movers, liquid
    liquid.display() # Draw water
    
    wind = PVector(0.01, 0)
    
    for each in movers :
        # Is the Mover in the liquid?
        if liquid.contains(each):
            # Calculate drag force
            dragForce = liquid.drag(each)
            # Apply drag force to Mover
            each.applyForce(dragForce)

        # Gravity is scaled by mass here!
        gravity = PVector(0, 0.1 * each.mass)
        each.applyForce(gravity) # Apply gravity
        
        # Update and display
        each.update()
        each.display()
        each.checkEdges()
        
    fill(0)
    # text("click mouse to reset", 10, 30)
    
    if (frameCount % 20 == 0) : saveFrame("ch2_05_####.png")

def mousePressed():
    reset()
    
def reset():
    global movers
    movers = [Mover(random(0.5*2.25, 3*2.25), 20*2.25 + i*40*2.25, 0) for i in range(5)]
    
    # for (idx,each) in enumerate(movers):
    #     # movers = [Mover(random(0.5, 3), 40+idx*70, 0)]
    #     print(idx, each)
    #     each = Mover(random(0.5, 3), 40+idx*70, 0)
    