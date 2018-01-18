# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from Walker import Walker

def setup():
    size(600, 400)
    
    global w, total
    total = 0
    # Creat a set of walker object
    w = [Walker() for i in range(10)]

def draw():
    background(255)
    o = int(map(mouseX, 0, width, 1, 8))
    noiseDetail(o, 0.3)
    global total
    if frameCount % 30 == 0:
        total += 1
        if total > len(w) - 1 :
            total = len(w) - 1
    
    for each in w:
        each.walk()
        each.display()