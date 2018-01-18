# The Nature of Code - Python Version
# [kidult00](https://github.com/kidult00)

size(640, 360)
background(255)
noFill()
stroke(0)
strokeWeight(2)

angle = 0.0
angleVel = 0.1

beginShape()
for x in range(0, width+1, 5):
    y = map(sin(angle), -1, 1, 0, height)
    vertex(x, y)
    angle += angleVel
endShape()
