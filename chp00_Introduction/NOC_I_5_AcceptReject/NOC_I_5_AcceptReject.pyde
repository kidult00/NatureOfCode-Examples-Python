# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

def setup():
    size(800, 200)
    global randomCounts
    randomCounts = [0] * 20 # An array to keep track of how often random numbers are picked

def draw():
    background(255)
    global randomCounts
    # Pick a random number and increase the count
    index = int(acceptreject() * len(randomCounts))
    randomCounts[index] += 1
    
    # Draw a rectangle to graph results
    stroke(0)
    strokeWeight(2)
    fill(127)
    
    w = width / len(randomCounts)
    
    for x in range(len(randomCounts)):
        rect(x * w, height - randomCounts[x], w - 1, randomCounts[x])

def acceptreject():
    """
    An algorithm for picking a random number based on monte carlo method
    Here probability is determined by formula y = x
    """
    foundone = False # Have we found one yet
    hack = 0 # let's count just so we don't get stuck in an infinite loop by accident

    while(not foundone and hack < 10000):
        r1 = random(1)
        r2 = random(1)
        y = r1 * r1
        
        if r2 < y:
            foundone = True
            return r1
        hack += 1
    # Hack in case we run into a problem (need to improve this)
    return 0