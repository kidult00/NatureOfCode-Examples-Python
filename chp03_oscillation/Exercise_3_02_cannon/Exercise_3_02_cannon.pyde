# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

from CannonBall import CannonBall

def setup():
    size(640, 360)

    global angle, position, shot, ball
    angle = -PI/4
    position = PVector(50, 300)
    shot = False
    ball = CannonBall(position.x, position.y)
    

def draw():
    background(255)
    
    global position, shot, ball
    # Draw the canno
    pushMatrix()
    translate(position.x, position.y)
    rotate(angle)
    # noFill()
    rect(0, -5, 50, 10)
    popMatrix()
    
    if shot :
        gravity = PVector(0, 0.2)
        ball.applyForce(gravity)
        ball.update()
    
    ball.display() 
    
    if ball.position.y > height:
        ball = CannonBall(position.x, position.y)
        shot = False
       
    fill(0)
    text("SPACE : shot, RIGHT/LEFT : angle", 20, height-20)

def keyPressed():
    global angle, ball, shot
    if key ==CODED and keyCode == RIGHT : angle += 0.1
    elif key == CODED and keyCode == LEFT : angle -= 0.1
    elif key == ' ' :
        shot = True
        force = PVector.fromAngle(angle)
        force.mult(10)
        ball.applyForce(force)