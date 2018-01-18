# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

# Example 1-2: Bouncing Ball, with PVector!
def setup():
    size(200, 200)
    background(255)

    global position, velocity
    position = PVector(100, 100)
    velocity = PVector(2.5, 5)
    
def draw():
    noStroke()
    fill(255, 10)
    rect(0, 0, width, height)
    
    global position, velocity
    # Add the current speed to the position
    position.add(velocity)
    
    if position.x > width or position.x < 0 :
        velocity.x *= -1
    if position.y > height or position.y < 0 :
        velocity.y *= -1
    
    # Display circle at x position
    stroke(0)
    fill(175)
    ellipse(position.x, position.y, 16, 16)