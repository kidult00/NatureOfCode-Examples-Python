# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(200, 200)
    background(0)
    smooth()
    global x, y
    x = 0
    y = 0

def draw():
    # create an alpha blended background
    fill(0,1);
    rect(0, 0, width, height)
    global x, y
    # probabilities for 3 different cases (these need to add up to 100% since something always occurs here!)
    p1 = 0.05     # 5% chance of pure white occurring
    p2 = 0.8 + p1 # 80% chance of gray occuring
    
    num = random(1)
    if num < p1 :
        fill(255)
    elif num < p2:
        fill(150)
    else:
        fill(0)
    
    stroke(200)
    rect(x, y, 10, 10)
    
    # X and Y walk through a grid
    x = (x + 10) % width
    if x == 0: y = (y + 10) % width 