# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(640, 360)
    global randomCounts
    randomCounts = [0] * 20 # An array to keep track of how often random numbers are picked

def draw():
    background(255)
    global randomCounts
    # Pick a random number and increase the count
    index = int(random(len(randomCounts)))
    randomCounts[index] += 1
    
    # Draw a rectangle to graph results
    stroke(0)
    strokeWeight(2)
    fill(127)
    
    w = width / len(randomCounts)
    
    for x in range(len(randomCounts)):
        rect(x * w, height - randomCounts[x], w - 1, randomCounts[x])